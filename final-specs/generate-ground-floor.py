#!/usr/bin/env python3
"""
Generate a Collada (.dae) 3D model of the full building (GF + 1F).
All dimensions defined in feet, converted to meters for the DAE file.

Coordinate system:
  x-axis: width (0 = left wall inside face, 20 = right wall inside face)
  y-axis: depth (0 = front wall inside face, 25 = back wall inside face)
  z-axis: height (0 = natural ground, 3 = plinth top / GF floor, 15 = slab soffit,
          15.5 = 1F floor level, 27.5 = 1F roof slab soffit)

Internal clear space: 20ft x 25ft x 12ft (room height per floor)
External wall thickness: 9" (0.75ft)
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

FT_TO_M = 0.3048
IN_TO_M = 0.0254

# Colors (RGBA 0-1)
COLORS = {
    'plinth': (0.72, 0.53, 0.26, 1.0),
    'wall': (0.96, 0.93, 0.85, 1.0),
    'column': (0.35, 0.38, 0.42, 1.0),
    'beam': (0.42, 0.44, 0.48, 1.0),
    'slab': (0.55, 0.58, 0.62, 1.0),
    'floor': (0.78, 0.75, 0.70, 1.0),
    'staircase': (0.85, 0.72, 0.55, 1.0),
    'ramp': (0.78, 0.68, 0.52, 1.0),
    'shutter': (0.18, 0.22, 0.28, 1.0),
    'gate': (0.45, 0.25, 0.12, 1.0),
    'toilet': (0.55, 0.82, 0.78, 1.0),
    'septic': (0.45, 0.27, 0.14, 1.0),
    'ground': (0.28, 0.45, 0.22, 1.0),
    'pipe': (0.85, 0.45, 0.15, 1.0),
    'kitchen': (0.30, 0.55, 0.25, 1.0),
    'railing': (0.50, 0.50, 0.55, 1.0),
    'fixture': (0.90, 0.90, 0.92, 1.0),
    'water_tank': (0.20, 0.55, 0.82, 1.0),
}


def ft(val):
    """Convert feet to meters."""
    return val * FT_TO_M


def inch(val):
    """Convert inches to meters."""
    return val * IN_TO_M


def box_mesh(x, y, z, w, d, h):
    """Generate vertices and triangles for a box at (x,y,z) with dimensions (w,d,h)."""
    verts = [
        (x, y, z), (x+w, y, z), (x+w, y+d, z), (x, y+d, z),
        (x, y, z+h), (x+w, y, z+h), (x+w, y+d, z+h), (x, y+d, z+h),
    ]
    tris = [
        (0,1,2), (0,2,3),
        (4,6,5), (4,7,6),
        (0,1,5), (0,5,4),
        (2,3,7), (2,7,6),
        (0,3,7), (0,7,4),
        (1,2,6), (1,6,5),
    ]
    return verts, tris


def ramp_mesh(x, y, z_bottom, z_top, w, length):
    """Generate a ramp from (x, y, z_bottom) rising to (x, y+length, z_top)."""
    thickness = ft(0.5)
    verts = [
        (x, y, z_bottom), (x+w, y, z_bottom),
        (x+w, y+length, z_top), (x, y+length, z_top),
        (x, y, z_bottom - thickness), (x+w, y, z_bottom - thickness),
        (x+w, y+length, z_top - thickness), (x, y+length, z_top - thickness),
    ]
    tris = [
        (0,1,2), (0,2,3),
        (4,6,5), (4,7,6),
        (0,1,5), (0,5,4),
        (2,3,7), (2,7,6),
        (0,3,7), (0,7,4),
        (1,2,6), (1,6,5),
    ]
    return verts, tris


def stair_mesh(x, y, z_start, num_risers, riser_h, tread_d, width, going_y=True):
    """Generate staircase steps as individual boxes."""
    verts = []
    tris = []
    offset = 0
    for i in range(num_risers):
        z = z_start + i * riser_h
        if going_y:
            sy = y + i * tread_d
            bv, bt = box_mesh(x, sy, z, width, tread_d, riser_h)
        else:
            sy = y - i * tread_d
            bv, bt = box_mesh(x, sy - tread_d, z, width, tread_d, riser_h)
        bt_offset = [(a+offset, b+offset, c+offset) for a, b, c in bt]
        verts.extend(bv)
        tris.extend(bt_offset)
        offset += len(bv)
    return verts, tris


class ColladaBuilder:
    def __init__(self):
        self.geometries = []
        self.materials = []
        self.scene_nodes = []
        self.mat_ids = set()

    def add_material(self, name, color):
        if name in self.mat_ids:
            return
        self.mat_ids.add(name)
        self.materials.append((name, color))

    def add_geometry(self, name, verts, tris, material_name):
        self.geometries.append((name, verts, tris, material_name))
        self.scene_nodes.append((name, material_name))

    def build_xml(self):
        root = ET.Element('COLLADA', {
            'xmlns': 'http://www.collada.org/2005/11/COLLADASchema',
            'version': '1.4.1'
        })

        asset = ET.SubElement(root, 'asset')
        ET.SubElement(asset, 'unit', {'name': 'meter', 'meter': '1'})
        up = ET.SubElement(asset, 'up_axis')
        up.text = 'Z_UP'

        lib_effects = ET.SubElement(root, 'library_effects')
        for mat_name, color in self.materials:
            effect = ET.SubElement(lib_effects, 'effect', {'id': f'{mat_name}-effect'})
            profile = ET.SubElement(effect, 'profile_COMMON')
            technique = ET.SubElement(profile, 'technique', {'sid': 'common'})
            phong = ET.SubElement(technique, 'phong')
            diffuse = ET.SubElement(phong, 'diffuse')
            c = ET.SubElement(diffuse, 'color')
            c.text = f'{color[0]} {color[1]} {color[2]} {color[3]}'

        lib_materials = ET.SubElement(root, 'library_materials')
        for mat_name, _ in self.materials:
            mat = ET.SubElement(lib_materials, 'material', {'id': f'{mat_name}-mat', 'name': mat_name})
            ET.SubElement(mat, 'instance_effect', {'url': f'#{mat_name}-effect'})

        lib_geom = ET.SubElement(root, 'library_geometries')
        for name, verts, tris, _ in self.geometries:
            geom = ET.SubElement(lib_geom, 'geometry', {'id': f'{name}-geom', 'name': name})
            mesh = ET.SubElement(geom, 'mesh')

            src = ET.SubElement(mesh, 'source', {'id': f'{name}-positions'})
            farr = ET.SubElement(src, 'float_array', {
                'id': f'{name}-positions-array',
                'count': str(len(verts) * 3)
            })
            farr.text = ' '.join(f'{v[0]:.4f} {v[1]:.4f} {v[2]:.4f}' for v in verts)

            technique = ET.SubElement(src, 'technique_common')
            accessor = ET.SubElement(technique, 'accessor', {
                'source': f'#{name}-positions-array',
                'count': str(len(verts)),
                'stride': '3'
            })
            ET.SubElement(accessor, 'param', {'name': 'X', 'type': 'float'})
            ET.SubElement(accessor, 'param', {'name': 'Y', 'type': 'float'})
            ET.SubElement(accessor, 'param', {'name': 'Z', 'type': 'float'})

            vertices = ET.SubElement(mesh, 'vertices', {'id': f'{name}-vertices'})
            ET.SubElement(vertices, 'input', {'semantic': 'POSITION', 'source': f'#{name}-positions'})

            triangles = ET.SubElement(mesh, 'triangles', {'count': str(len(tris))})
            ET.SubElement(triangles, 'input', {'semantic': 'VERTEX', 'source': f'#{name}-vertices', 'offset': '0'})
            p = ET.SubElement(triangles, 'p')
            p.text = ' '.join(str(idx) for tri in tris for idx in tri)

        lib_scenes = ET.SubElement(root, 'library_visual_scenes')
        vscene = ET.SubElement(lib_scenes, 'visual_scene', {'id': 'Scene', 'name': 'FullBuilding'})

        for name, mat_name in self.scene_nodes:
            node = ET.SubElement(vscene, 'node', {'id': f'{name}-node', 'name': name, 'type': 'NODE'})
            inst_geom = ET.SubElement(node, 'instance_geometry', {'url': f'#{name}-geom'})
            bind_mat = ET.SubElement(inst_geom, 'bind_material')
            tc = ET.SubElement(bind_mat, 'technique_common')
            ET.SubElement(tc, 'instance_material', {
                'symbol': mat_name,
                'target': f'#{mat_name}-mat'
            })

        scene = ET.SubElement(root, 'scene')
        ET.SubElement(scene, 'instance_visual_scene', {'url': '#Scene'})

        return root

    def save(self, filepath):
        root = self.build_xml()
        xml_str = ET.tostring(root, encoding='unicode')
        dom = minidom.parseString(xml_str)
        pretty = dom.toprettyxml(indent='  ')
        lines = pretty.split('\n')
        lines = [l for l in lines if not l.startswith('<?xml')]
        final = '<?xml version="1.0" encoding="utf-8"?>\n' + '\n'.join(lines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final)


def build_ground_floor():
    cb = ColladaBuilder()

    for name, color in COLORS.items():
        cb.add_material(name, color)

    # Key dimensions in feet (converted to meters via ft())
    WALL_T = 0.75       # 9 inches = 0.75ft
    INT_W = 20.0        # internal width
    INT_D = 25.0        # internal depth
    PLINTH_H = 3.0      # plinth height
    ROOM_H = 12.0       # GF room height (plinth top to slab soffit)
    SLAB_T_FT = 0.5     # 6 inches slab thickness
    FLOOR_T = 0.33      # 4 inches floor slab

    # Z levels
    Z_GROUND = 0.0
    Z_PLINTH = PLINTH_H          # 3ft - plinth top / GF floor level
    Z_SLAB_SOFFIT = Z_PLINTH + ROOM_H  # 15ft - slab soffit
    Z_SLAB_TOP = Z_SLAB_SOFFIT + SLAB_T_FT  # 15.5ft - slab top

    # ============ 1. PLINTH ============
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_GROUND),
                    ft(INT_W + 2*WALL_T), ft(INT_D + 2*WALL_T), ft(PLINTH_H))
    cb.add_geometry('plinth', v, t, 'plinth')

    # ============ 2. FLOOR SLAB ============
    v, t = box_mesh(ft(0), ft(0), ft(Z_PLINTH),
                    ft(INT_W), ft(INT_D), ft(FLOOR_T))
    cb.add_geometry('floor_slab', v, t, 'floor')

    # ============ 3. EXTERNAL WALLS ============
    # Wall base z (on top of floor slab)
    WALL_Z = Z_PLINTH + FLOOR_T
    WALL_H = ROOM_H - FLOOR_T

    # Back wall: full width including wall thickness on sides
    v, t = box_mesh(ft(-WALL_T), ft(INT_D), ft(WALL_Z),
                    ft(INT_W + 2*WALL_T), ft(WALL_T), ft(WALL_H))
    cb.add_geometry('wall_back', v, t, 'wall')

    # Left wall: full depth including wall thickness
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(WALL_Z),
                    ft(WALL_T), ft(INT_D + 2*WALL_T), ft(WALL_H))
    cb.add_geometry('wall_left', v, t, 'wall')

    # Right wall: full depth including wall thickness
    v, t = box_mesh(ft(INT_W), ft(-WALL_T), ft(WALL_Z),
                    ft(WALL_T), ft(INT_D + 2*WALL_T), ft(WALL_H))
    cb.add_geometry('wall_right', v, t, 'wall')

    # Front wall segments (at y=0, going from y=0 to y=-0.75)
    # Layout left to right:
    #   x=0 to x=2: toilet door opening (2ft wide, 7ft high)
    #   x=2 to x=3.25: partition wall (1.25ft, full height)
    #   x=3.25 to x=6: stair gate opening (2.75ft wide, 7ft high)
    #   x=6 to x=7: C6 column zone (1ft, handled by column)
    #   x=7 to x=17: shutter opening (10ft wide, 10ft high)
    #   x=17 to x=18: C7 column zone (1ft, handled by column)
    #   x=18 to x=20: solid wall (2ft wide, full height)

    DOOR_H = 7.0  # toilet door and stair gate height

    # Wall above toilet door (x=0 to x=2, above 7ft)
    v, t = box_mesh(ft(0), ft(-WALL_T), ft(WALL_Z + DOOR_H),
                    ft(2.0), ft(WALL_T), ft(WALL_H - DOOR_H))
    cb.add_geometry('wall_above_toilet_door', v, t, 'wall')

    # Partition between toilet door and stair gate (x=2 to x=3.25, full height)
    v, t = box_mesh(ft(2.0), ft(-WALL_T), ft(WALL_Z),
                    ft(1.25), ft(WALL_T), ft(WALL_H))
    cb.add_geometry('wall_front_partition', v, t, 'wall')

    # Wall above stair gate (x=3.25 to x=6, above 7ft)
    v, t = box_mesh(ft(3.25), ft(-WALL_T), ft(WALL_Z + DOOR_H),
                    ft(2.75), ft(WALL_T), ft(WALL_H - DOOR_H))
    cb.add_geometry('wall_above_stair_gate', v, t, 'wall')

    # Wall above shutter (x=7 to x=17, above 10ft, 2ft high)
    SHUTTER_H = 10.0
    v, t = box_mesh(ft(7.0), ft(-WALL_T), ft(WALL_Z + SHUTTER_H),
                    ft(10.0), ft(WALL_T), ft(WALL_H - SHUTTER_H))
    cb.add_geometry('wall_above_shutter', v, t, 'wall')

    # Solid wall right of C7 (x=18 to x=20, full height)
    v, t = box_mesh(ft(18.0), ft(-WALL_T), ft(WALL_Z),
                    ft(2.0), ft(WALL_T), ft(WALL_H))
    cb.add_geometry('wall_front_right', v, t, 'wall')

    # ============ 4. COLUMNS ============
    # All 9"x12" RCC. 12" ALONG the wall, 9" ACROSS (= wall thickness = flush/hidden).
    # Columns positioned WITHIN the walls (overlapping wall geometry).
    # Visible as different color; when walls hidden, columns show structural positions.
    COL_9 = 0.75   # 9 inches in feet
    COL_12 = 1.0   # 12 inches in feet
    COL_H = ROOM_H  # 12ft

    # LEFT WALL columns (wall at x=-0.75 to x=0): 9" across x (inside wall), 12" along y
    # C1: back-left corner
    v, t = box_mesh(ft(-WALL_T), ft(INT_D - COL_12), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C1', v, t, 'column')

    # C3: left wall at y=9 (9ft from front)
    v, t = box_mesh(ft(-WALL_T), ft(9.0 - COL_12/2), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C3', v, t, 'column')

    # C5: front-left corner
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C5', v, t, 'column')

    # RIGHT WALL columns (wall at x=20 to x=20.75): 9" across x, 12" along y
    # C2: back-right corner
    v, t = box_mesh(ft(INT_W), ft(INT_D - COL_12), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C2', v, t, 'column')

    # C4: right wall at y=9
    v, t = box_mesh(ft(INT_W), ft(9.0 - COL_12/2), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C4', v, t, 'column')

    # C8: front-right corner
    v, t = box_mesh(ft(INT_W), ft(-WALL_T), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C8', v, t, 'column')

    # FRONT WALL columns: C6 and C7 are 9"×9" (square columns, smaller than others)
    # C6: at x=6 on front wall
    v, t = box_mesh(ft(6.0), ft(-WALL_T), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_9), ft(COL_H))
    cb.add_geometry('col_C6', v, t, 'column')

    # C7: at x=17 on front wall
    v, t = box_mesh(ft(17.0), ft(-WALL_T), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_9), ft(COL_H))
    cb.add_geometry('col_C7', v, t, 'column')

    # ============ 5. STAIRCASE ============
    # REVISED: Landing 2.5ft deep (comfortable turn), flight run 6ft each
    # Flight 1 (RIGHT side of stair zone, toward C6):
    #   x=3.25 to x=6 (2.75ft wide), y=0 to y=6 (6ft run)
    #   9 risers, 8" riser, 9" tread (8 treads × 9" = 6ft)
    #   Rises from z=3 to z=3+9*(8/12)=3+6=9

    RISER_H_FT = 8.0 / 12.0     # 8 inches = 0.667ft
    TREAD_D_FT = 9.0 / 12.0     # 9 inches = 0.75ft (revised from 10.5")
    FLIGHT_W = 2.75
    RISERS_PER_FLIGHT = 9
    TREADS_PER_FLIGHT = 8        # one less than risers

    # Flight 1: x=3.25 to x=6, y=0 to y=6, rising from z=3 to z=9
    v, t = stair_mesh(ft(3.25), ft(0), ft(Z_PLINTH),
                      RISERS_PER_FLIGHT, ft(RISER_H_FT), ft(TREAD_D_FT), ft(FLIGHT_W), going_y=True)
    cb.add_geometry('stair_flight1', v, t, 'staircase')

    # Landing: x=0 to x=6 (full width), y=6 to y=8.5 (2.5ft deep!), at z=9
    LANDING_Z = Z_PLINTH + RISERS_PER_FLIGHT * RISER_H_FT  # 3 + 6 = 9ft
    v, t = box_mesh(ft(0), ft(6.0), ft(LANDING_Z),
                    ft(6.0), ft(2.5), ft(RISER_H_FT))
    cb.add_geometry('stair_landing', v, t, 'staircase')

    # Flight 2 (LEFT side, from landing going back toward front):
    #   x=0 to x=2.75, starting at y=8.25 going back to y=2.25
    #   (0.25ft offset from landing edge = small rest/turning zone before steps begin)
    #   9 risers, rising from z=9 to z=15
    v, t = stair_mesh(ft(0), ft(8.25), ft(LANDING_Z),
                      RISERS_PER_FLIGHT, ft(RISER_H_FT), ft(TREAD_D_FT), ft(FLIGHT_W), going_y=False)
    cb.add_geometry('stair_flight2', v, t, 'staircase')

    # Partition wall between flights:
    #   x=2.75 to x=3.25 (0.5ft), y=0 to y=8.5, z=3 to z=9 (up to landing height)
    v, t = box_mesh(ft(2.75), ft(0), ft(Z_PLINTH),
                    ft(0.5), ft(8.5), ft(LANDING_Z - Z_PLINTH))
    cb.add_geometry('stair_partition', v, t, 'wall')

    # ============ 6. TOILET ============
    # Under Flight 2, LEFT side: x=0 to x=2.75, y=0 to y=5
    # Back wall at y=5 (4.5" thick = 0.375ft)
    TOILET_WALL_T = 0.375  # 4.5 inches

    v, t = box_mesh(ft(0), ft(5.0 - TOILET_WALL_T), ft(Z_PLINTH),
                    ft(2.75), ft(TOILET_WALL_T), ft(LANDING_Z - Z_PLINTH))
    cb.add_geometry('toilet_back_wall', v, t, 'toilet')

    # Right wall of toilet at x=2.75 (shared with partition)
    # Already covered by stair_partition

    # ============ 7. SHUTTER ============
    # Thin panel at y=0 (front wall line), x=7 to x=17, z=3 to z=13 (10ft high)
    v, t = box_mesh(ft(7.0), ft(-0.1), ft(Z_PLINTH),
                    ft(10.0), ft(0.1), ft(SHUTTER_H))
    cb.add_geometry('shutter', v, t, 'shutter')

    # ============ 8. GATES ============
    # Stair gate: at y=0, x=3.25 to x=6 (2.75ft wide), z=3 to z=10 (7ft high)
    v, t = box_mesh(ft(3.25), ft(-0.1), ft(Z_PLINTH),
                    ft(2.75), ft(0.1), ft(DOOR_H))
    cb.add_geometry('stair_gate', v, t, 'gate')

    # Toilet door: at y=0, x=0 to x=2 (2ft wide), z=3 to z=10 (7ft high)
    v, t = box_mesh(ft(0), ft(-0.1), ft(Z_PLINTH),
                    ft(2.0), ft(0.1), ft(DOOR_H))
    cb.add_geometry('toilet_door', v, t, 'gate')

    # ============ 9. RAMP ============
    # In front of shutter, from z=0 (ground) up to z=3 (plinth level)
    # Width: 12ft, centered on shutter (shutter x=7 to x=17, center=12)
    # So ramp from x=6 to x=18? No, centered: x = 12 - 6 = 6, so x=6 to x=18...
    # Actually "centered on shutter": shutter center = (7+17)/2 = 12. Ramp width=12ft.
    # Ramp x = 12 - 6 = 6 to 12 + 6 = 18. But spec says x=4 to x=16.
    # Using spec: x=4 to x=16 (12ft wide)
    # Length: 8ft, from y=0 going to y=-8
    # Rises from z=0 at y=-8 to z=3 at y=0
    RAMP_X = 4.0
    RAMP_W_FT = 12.0
    RAMP_L_FT = 8.0
    v, t = ramp_mesh(ft(RAMP_X), ft(-RAMP_L_FT), ft(Z_GROUND), ft(Z_PLINTH),
                     ft(RAMP_W_FT), ft(RAMP_L_FT))
    cb.add_geometry('ramp', v, t, 'ramp')

    # ============ 10. GATE STEPS ============
    # Width: 6ft (x=0 to x=6), going from z=3 down to z=0
    # 5 steps, each ~7.2" riser, ~10" tread, going in -y direction
    STEP_RISER = 3.0 / 5.0  # 3ft plinth / 5 steps = 0.6ft per riser
    STEP_TREAD = 10.0 / 12.0  # 10 inches
    STEP_W = 6.0

    for i in range(5):
        step_z = Z_GROUND + i * STEP_RISER
        step_y = -(5 - i) * STEP_TREAD
        v, t = box_mesh(ft(0), ft(step_y), ft(step_z),
                        ft(STEP_W), ft(STEP_TREAD), ft(STEP_RISER))
        cb.add_geometry(f'gate_step_{i}', v, t, 'staircase')

    # ============ 11. BEAMS ============
    BEAM_9 = COL_9         # 9 inches = 0.75ft
    BEAM_20 = 20.0 / 12.0  # 20 inches = 1.67ft (deep beams: back + middle + front)
    BEAM_24 = 24.0 / 12.0  # 24 inches = 2.0ft (SIDE beams: left + right — increased per structural calc)

    # Back beam (9"x20"): spans x=0-20, at y=25
    v, t = box_mesh(ft(0), ft(INT_D - BEAM_9), ft(Z_SLAB_SOFFIT - BEAM_20),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_20))
    cb.add_geometry('beam_back', v, t, 'beam')

    # Middle beam (9"x20"): spans x=0-20, at y=9
    v, t = box_mesh(ft(0), ft(9.0), ft(Z_SLAB_SOFFIT - BEAM_20),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_20))
    cb.add_geometry('beam_middle', v, t, 'beam')

    # Front beam (9"x20"): spans x=0-20, at y=0 (INCREASED from 15" per structural calc)
    v, t = box_mesh(ft(0), ft(0), ft(Z_SLAB_SOFFIT - BEAM_20),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_20))
    cb.add_geometry('beam_front', v, t, 'beam')

    # Left beam (9"x24"): spans y=0-25, at x=0 (INCREASED from 15" — 7.62m span needs deeper beam)
    v, t = box_mesh(ft(0), ft(0), ft(Z_SLAB_SOFFIT - BEAM_24),
                    ft(BEAM_9), ft(INT_D), ft(BEAM_24))
    cb.add_geometry('beam_left', v, t, 'beam')

    # Right beam (9"x24"): spans y=0-25, at x=20 (INCREASED from 15")
    v, t = box_mesh(ft(INT_W - BEAM_9), ft(0), ft(Z_SLAB_SOFFIT - BEAM_24),
                    ft(BEAM_9), ft(INT_D), ft(BEAM_24))
    cb.add_geometry('beam_right', v, t, 'beam')

    # ============ 12. ROOF SLAB (with STAIR WELL OPENING) ============
    # The slab covers full building + 6ft cantilever at front
    # Cantilever: y=0 to y=-6 (6ft in front of building — PURE CANTILEVER, no supports)
    # Stair well opening: x=0 to x=3, y=0 to y=8.5 (INSIDE building only)
    # The cantilever DOES extend in front of the stair well area (covers toilet door + gate from rain)
    CANTILEVER = 6.0  # 6ft cantilever (updated from 5ft)

    # Piece 1: BACK portion (y=8.5 to y=25.75) — full width
    v, t = box_mesh(ft(-WALL_T), ft(8.5), ft(Z_SLAB_SOFFIT),
                    ft(INT_W + 2*WALL_T), ft(INT_D - 8.5 + WALL_T), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_back', v, t, 'slab')

    # Piece 2: FRONT-RIGHT portion (x=3 to x=20.75, y=-6 to y=8.5) — includes cantilever
    v, t = box_mesh(ft(3.0), ft(-CANTILEVER), ft(Z_SLAB_SOFFIT),
                    ft(INT_W - 3.0 + WALL_T), ft(8.5 + CANTILEVER), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_front_right', v, t, 'slab')

    # Piece 3: FRONT-LEFT edge (x=-0.75 to x=0, y=-6 to y=8.5) — left wall thickness strip
    v, t = box_mesh(ft(-WALL_T), ft(-CANTILEVER), ft(Z_SLAB_SOFFIT),
                    ft(WALL_T), ft(8.5 + CANTILEVER), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_front_left_edge', v, t, 'slab')

    # Piece 4: CANTILEVER in front of stair well (x=0 to x=3, y=-6 to y=0)
    # This IS the cantilever that covers the toilet door + stair gate from rain!
    # The stair well opening is at y=0 to y=8.5 (INSIDE). This piece is at y=-6 to y=0 (OUTSIDE). No conflict.
    v, t = box_mesh(ft(0), ft(-CANTILEVER), ft(Z_SLAB_SOFFIT),
                    ft(3.0), ft(CANTILEVER), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_cantilever_stairzone', v, t, 'slab')

    # The STAIR WELL OPENING: x=0 to x=3, y=0 to y=8.5 (no slab here — visible as gap in slab pieces)

    # ============ 13. SHADE — PURE CANTILEVER (no walls, no pillars!) ============
    # The roof slab extends 5ft in front (y=0 to y=-5) as a pure cantilever.
    # NO shade walls, NO front pillars. The slab hangs from the front beam.
    # Side walls STOP at y=0 (front wall line) — they do NOT extend forward.
    # (The slab extension is already part of the roof_slab geometry above.)
    # Nothing else to add here — the shade area below is completely open.

    # ============ 14. SEPTIC TANK + SOAK PIT (Black Water System) ============
    # Septic tank: 5ft x 2.5ft x 4.5ft (per architect, toilet-only, 3-5 users)
    SEPTIC_X = 3.0
    SEPTIC_Y = -7.0
    SEPTIC_W = 5.0
    SEPTIC_D = 2.5
    SEPTIC_H = 4.5
    v, t = box_mesh(ft(SEPTIC_X - SEPTIC_W/2), ft(SEPTIC_Y - SEPTIC_D/2), ft(-SEPTIC_H),
                    ft(SEPTIC_W), ft(SEPTIC_D), ft(SEPTIC_H))
    cb.add_geometry('septic_tank', v, t, 'septic')

    # Black Water Soak pit: 5ft dia x 7ft deep (approximated as box)
    SOAK_Y = -14.0
    SOAK_DIA = 5.0
    SOAK_H = 7.0
    v, t = box_mesh(ft(SEPTIC_X - SOAK_DIA/2), ft(SOAK_Y - SOAK_DIA/2), ft(-SOAK_H),
                    ft(SOAK_DIA), ft(SOAK_DIA), ft(SOAK_H))
    cb.add_geometry('bw_soak_pit', v, t, 'septic')

    # Grey Water Soak pit (SEPARATE, on the RIGHT side of building)
    GW_SOAK_X = 17.0  # right side
    GW_SOAK_Y = -10.0
    v, t = box_mesh(ft(GW_SOAK_X - 2.0), ft(GW_SOAK_Y - 2.0), ft(-6.0),
                    ft(4.0), ft(4.0), ft(6.0))
    cb.add_geometry('gw_soak_pit', v, t, 'septic')

    # Wash Water Soak pit (SEPARATE, near the ramp/front)
    WW_SOAK_X = 10.0  # center front
    WW_SOAK_Y = -12.0
    v, t = box_mesh(ft(WW_SOAK_X - 2.5), ft(WW_SOAK_Y - 2.5), ft(-6.5),
                    ft(5.0), ft(5.0), ft(6.5))
    cb.add_geometry('ww_soak_pit', v, t, 'septic')

    # Connecting pipe (thin orange box from septic to soak pit)
    PIPE_SIZE = 0.33  # ~4 inches
    pipe_length = abs(SOAK_Y - SEPTIC_Y) - SEPTIC_D/2 - SOAK_DIA/2
    v, t = box_mesh(ft(SEPTIC_X - PIPE_SIZE/2), ft(SEPTIC_Y - SEPTIC_D/2 - pipe_length), ft(-3.0),
                    ft(PIPE_SIZE), ft(pipe_length), ft(PIPE_SIZE))
    cb.add_geometry('septic_pipe', v, t, 'pipe')

    # ============ GROUND PLANE ============
    ground_extent = 20.0
    v, t = box_mesh(ft(-ground_extent), ft(-ground_extent), ft(-0.1),
                    ft(INT_W + 2*ground_extent), ft(INT_D + 2*ground_extent), ft(0.1))
    cb.add_geometry('ground_plane', v, t, 'ground')

    # ================================================================
    # ============ FIRST FLOOR (1F) ============
    # ================================================================
    # 1F floor level: z=15.5 (top of GF ceiling slab)
    # 1F height: 12ft (z=15.5 to z=27.5)
    # 1F roof slab: at z=27.5

    Z_1F_FLOOR = Z_SLAB_TOP        # 15.5ft
    Z_1F_ROOF = Z_1F_FLOOR + 12.0  # 27.5ft
    WALL_1F_H = 12.0               # 1F wall height

    # ============ 1F.1 EXTERNAL WALLS ============
    # Left wall: x=-0.75 to x=0, y=0 to y=25.75, z=15.5 to z=27.5
    v, t = box_mesh(ft(-WALL_T), ft(0), ft(Z_1F_FLOOR),
                    ft(WALL_T), ft(INT_D + WALL_T), ft(WALL_1F_H))
    cb.add_geometry('wall_1f_left', v, t, 'wall')

    # Right wall: x=20 to x=20.75, y=0 to y=25.75, z=15.5 to z=27.5
    v, t = box_mesh(ft(INT_W), ft(0), ft(Z_1F_FLOOR),
                    ft(WALL_T), ft(INT_D + WALL_T), ft(WALL_1F_H))
    cb.add_geometry('wall_1f_right', v, t, 'wall')

    # Back wall: x=-0.75 to x=20.75, y=25 to y=25.75, z=15.5 to z=27.5
    v, t = box_mesh(ft(-WALL_T), ft(INT_D), ft(Z_1F_FLOOR),
                    ft(INT_W + 2*WALL_T), ft(WALL_T), ft(WALL_1F_H))
    cb.add_geometry('wall_1f_back', v, t, 'wall')

    # NO FRONT WALL on 1F — the balcony zone (y=0 to y=9) is OPEN AIR
    # (roof overhead, no wall at y=0). The partition at y=9 is where the room starts.
    # The open terrace (y=-6 to y=0) has railings only.

    # ============ 1F.1b COLUMNS (extending from GF to 1F, z=15.5 to z=27.5) ============
    # Same positions as GF, INSIDE the walls (overlapping), continuing upward.
    # LEFT WALL columns: x=-WALL_T to x=0, 12" along y
    v, t = box_mesh(ft(-WALL_T), ft(INT_D - COL_12), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C1', v, t, 'column')

    v, t = box_mesh(ft(-WALL_T), ft(9.0 - COL_12/2), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C3', v, t, 'column')

    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C5', v, t, 'column')

    # RIGHT WALL columns: x=INT_W to x=INT_W+COL_9, 12" along y
    v, t = box_mesh(ft(INT_W), ft(INT_D - COL_12), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C2', v, t, 'column')

    v, t = box_mesh(ft(INT_W), ft(9.0 - COL_12/2), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C4', v, t, 'column')

    v, t = box_mesh(ft(INT_W), ft(-WALL_T), ft(Z_1F_FLOOR),
                    ft(COL_9), ft(COL_12), ft(WALL_1F_H))
    cb.add_geometry('col_1f_C8', v, t, 'column')

    # FRONT WALL columns: C6 and C7 do NOT extend to 1F (front wall doesn't exist at 1F!)
    # Only side wall columns (C1-C5, C2-C4-C8) continue up.

    # ============ 1F.2 ROOM PARTITION WALL (y=9) ============
    # Layout at y=9 (from x=0 to x=14, stops before bathroom at x=14):
    # x=0-3: GATE (roof stair access from room)
    # x=3-6: SOLID wall
    # x=6-9: GATE (main room entry from balcony)
    # x=9-14: SOLID wall

    # Gate 1 (x=0-3): roof stair access — above gate lintel only
    v, t = box_mesh(ft(0), ft(9.0), ft(Z_1F_FLOOR + 7.0),
                    ft(3.0), ft(WALL_T), ft(WALL_1F_H - 7.0))
    cb.add_geometry('wall_1f_partition_above_roof_gate', v, t, 'wall')
    # Gate panel (roof stair gate)
    v, t = box_mesh(ft(0), ft(9.0 + WALL_T), ft(Z_1F_FLOOR),
                    ft(3.0), ft(0.1), ft(7.0))
    cb.add_geometry('roof_stair_gate', v, t, 'gate')

    # Solid segment: x=3 to x=6
    v, t = box_mesh(ft(3.0), ft(9.0), ft(Z_1F_FLOOR),
                    ft(3.0), ft(WALL_T), ft(WALL_1F_H))
    cb.add_geometry('wall_1f_partition_solid1', v, t, 'wall')

    # Gate 2 (x=6-9): main room entry from balcony — above gate lintel only
    v, t = box_mesh(ft(6.0), ft(9.0), ft(Z_1F_FLOOR + 7.0),
                    ft(3.0), ft(WALL_T), ft(WALL_1F_H - 7.0))
    cb.add_geometry('wall_1f_partition_above_room_gate', v, t, 'wall')

    # Solid segment: x=9 to x=14 (stops at bathroom)
    v, t = box_mesh(ft(9.0), ft(9.0), ft(Z_1F_FLOOR),
                    ft(5.0), ft(WALL_T), ft(WALL_1F_H))
    cb.add_geometry('wall_1f_partition_solid2', v, t, 'wall')

    # ============ 1F.3 KITCHEN (6ft × 6ft, back-right corner of room) ============
    # Simple 6ft × 6ft zone in the back-right corner (y=19-25, x=14-20)
    # Semi-open: half-walls (3.5ft high) on the two OPEN sides (y=19 and x=14)
    # 6ft × 6ft EMPTY space between kitchen (y=19) and bathroom (y=13) on right side

    # Half-wall at y=19 (front of kitchen, facing empty/living zone)
    v, t = box_mesh(ft(14.0), ft(19.0), ft(Z_1F_FLOOR),
                    ft(6.0), ft(0.375), ft(3.5))
    cb.add_geometry('kitchen_halfwall_front', v, t, 'kitchen')

    # Half-wall at x=14 (left edge of kitchen, facing living area)
    v, t = box_mesh(ft(14.0 - 0.375), ft(19.0), ft(Z_1F_FLOOR),
                    ft(0.375), ft(6.0), ft(3.5))
    cb.add_geometry('kitchen_halfwall_left', v, t, 'kitchen')

    # Kitchen floor indicator: 6ft × 6ft
    v, t = box_mesh(ft(14.0), ft(19.0), ft(Z_1F_FLOOR + 0.02),
                    ft(6.0), ft(6.0), ft(0.02))
    cb.add_geometry('kitchen_floor', v, t, 'kitchen')

    # ============ 1F.4 BATHROOM (6ft x 8ft, CONTINUOUS, RIGHT side) ============
    # x=14 to x=20, y=5 to y=13 — ONE continuous room (NO wall in the middle!)
    # The partition wall at y=9 STOPS at x=14 — bathroom spans freely across y=9.

    # Left wall (bathroom partition): x=14, y=5 to y=13
    # DOOR is on this wall at y=10 to y=12.5 (in the 4ft inside-room portion, y=9-13)
    # Segment: y=5 to y=10
    v, t = box_mesh(ft(14.0 - 0.375), ft(5.0), ft(Z_1F_FLOOR),
                    ft(0.375), ft(5.0), ft(WALL_1F_H))
    cb.add_geometry('bath_wall_left_1', v, t, 'toilet')
    # Segment: y=12.5 to y=13
    v, t = box_mesh(ft(14.0 - 0.375), ft(12.5), ft(Z_1F_FLOOR),
                    ft(0.375), ft(0.5), ft(WALL_1F_H))
    cb.add_geometry('bath_wall_left_2', v, t, 'toilet')
    # Above door: y=10 to y=12.5
    v, t = box_mesh(ft(14.0 - 0.375), ft(10.0), ft(Z_1F_FLOOR + 7.0),
                    ft(0.375), ft(2.5), ft(WALL_1F_H - 7.0))
    cb.add_geometry('bath_wall_left_above_door', v, t, 'toilet')

    # Back wall of bathroom: y=13, x=14 to x=20, SOLID (no door here — door is on left wall)
    v, t = box_mesh(ft(14.0), ft(13.0 - 0.375), ft(Z_1F_FLOOR),
                    ft(6.0), ft(0.375), ft(WALL_1F_H))
    cb.add_geometry('bath_wall_back', v, t, 'toilet')

    # Front wall of bathroom: y=5, x=14 to x=20, full height
    v, t = box_mesh(ft(14.0), ft(5.0), ft(Z_1F_FLOOR),
                    ft(6.0), ft(0.375), ft(WALL_1F_H))
    cb.add_geometry('bath_wall_front', v, t, 'toilet')

    # NOTE: NO wall at y=9 inside the bathroom! It's one continuous 8ft room.
    # The partition wall stops at x=14 — bathroom is uninterrupted.

    # Bathroom fixtures (all on RIGHT side, x=14-20, y=5-13)
    # Commode (WC): against right wall, near front
    v, t = box_mesh(ft(18.0), ft(6.0), ft(Z_1F_FLOOR),
                    ft(1.5), ft(2.0), ft(1.5))
    cb.add_geometry('bath_commode', v, t, 'fixture')

    # Shower tray: near the back of bathroom (room-side)
    v, t = box_mesh(ft(14.5), ft(10.0), ft(Z_1F_FLOOR),
                    ft(3.0), ft(3.0), ft(0.2))
    cb.add_geometry('bath_shower', v, t, 'fixture')

    # Wash basin: against right wall, middle area
    v, t = box_mesh(ft(18.5), ft(9.0), ft(Z_1F_FLOOR + 2.5),
                    ft(1.5), ft(1.0), ft(0.5))
    cb.add_geometry('bath_basin', v, t, 'fixture')

    # Geyser: REMOVED (not shown in model)

    # Geyser: REMOVED (not shown in model)

    # ============ 1F.5 STAIR WELL ENCLOSURE (full walls + gate) ============
    # The stair well (x=0-3, y=0-8.5) is enclosed by WALLS (not railings!)
    # Gate is at the FRONT of the x=3 wall — where Flight 2 arrives at the top.
    # Flight 2 arrives at approximately y=2.25 facing forward. Gate is right there.

    # Small LANDING PLATFORM at the top of stair well (fills gap between beam and Flight 2)
    # This is where you stand after reaching the top of Flight 2, before going through gate.
    v, t = box_mesh(ft(0), ft(0), ft(Z_1F_FLOOR - 0.5),
                    ft(3.0), ft(2.5), ft(0.5))
    cb.add_geometry('stairwell_top_landing', v, t, 'staircase')

    # FRONT WALL of stair well enclosure (CLOSES the front above the front beam)
    # At y=0 (front wall line), x=0 to x=3, full height.
    # This ensures the ONLY way out of the stair well is through the GATE at x=3.
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_1F_FLOOR),
                    ft(3.0 + WALL_T), ft(WALL_T), ft(WALL_1F_H))
    cb.add_geometry('stairwell_wall_front', v, t, 'wall')

    # Right wall: x=3, y=0 to y=9 (extends to partition line — NO gap!)
    # Gate opening (3ft wide × 7ft high) at y=0 to y=3 (front, where Flight 2 exits)
    # Segment: y=3 to y=9 (SOLID wall)
    v, t = box_mesh(ft(3.0), ft(3.0), ft(Z_1F_FLOOR),
                    ft(0.375), ft(6.0), ft(WALL_1F_H))
    cb.add_geometry('stairwell_wall_r1', v, t, 'wall')

    # Above gate: y=0 to y=3, z above 7ft only
    v, t = box_mesh(ft(3.0), ft(0), ft(Z_1F_FLOOR + 7.0),
                    ft(0.375), ft(3.0), ft(WALL_1F_H - 7.0))
    cb.add_geometry('stairwell_wall_above_gate', v, t, 'wall')

    # Gate panel (dark, at x=3, y=0-3, 3ft × 7ft)
    v, t = box_mesh(ft(3.05), ft(0), ft(Z_1F_FLOOR),
                    ft(0.1), ft(3.0), ft(7.0))
    cb.add_geometry('stairwell_gate', v, t, 'gate')

    # Back of enclosure: OPEN at y=9 — sloped stair starts here.
    # The partition wall at x=0-3 is NOT built (enclosure merges into the sloped stair zone).

    # ============ 1F.6 SLOPED STAIR-SLAB (to roof) ============
    # x=0 to x=3, from y=9 (partition line, back of enclosure) at z=15.5
    # rising to y=0 at z=27.5. Accessed from inside the enclosure (back is open to y=9).
    thickness = 0.3
    SLOPE_START_Y = 9.0  # starts at partition line
    stair_slope_verts = [
        # Top surface
        (ft(0), ft(SLOPE_START_Y), ft(Z_1F_FLOOR)),
        (ft(3), ft(SLOPE_START_Y), ft(Z_1F_FLOOR)),
        (ft(3), ft(0), ft(Z_1F_ROOF)),
        (ft(0), ft(0), ft(Z_1F_ROOF)),
        # Bottom surface
        (ft(0), ft(SLOPE_START_Y), ft(Z_1F_FLOOR - thickness)),
        (ft(3), ft(SLOPE_START_Y), ft(Z_1F_FLOOR - thickness)),
        (ft(3), ft(0), ft(Z_1F_ROOF - thickness)),
        (ft(0), ft(0), ft(Z_1F_ROOF - thickness)),
    ]
    stair_slope_tris = [
        (0, 1, 2), (0, 2, 3),   # top face
        (4, 6, 5), (4, 7, 6),   # bottom face
        (0, 1, 5), (0, 5, 4),   # front edge (y=9)
        (2, 3, 7), (2, 7, 6),   # back edge (y=0)
        (0, 3, 7), (0, 7, 4),   # left side
        (1, 2, 6), (1, 6, 5),   # right side
    ]
    cb.add_geometry('stair_slope_1f', stair_slope_verts, stair_slope_tris, 'staircase')

    # Step indicators on the slope (12 steps over 8.5ft run, 12ft rise)
    step_run = SLOPE_START_Y / 12.0     # per step in y
    step_rise = 12.0 / 12.0   # 1.0ft per step in z
    for i in range(12):
        step_y = 9.0 - i * step_run
        step_z = Z_1F_FLOOR + i * step_rise
        v, t = box_mesh(ft(0), ft(step_y - step_run), ft(step_z),
                        ft(3.0), ft(step_run), ft(step_rise))
        cb.add_geometry(f'stair_1f_step_{i}', v, t, 'staircase')

    # ============ 1F.7a WINDOWS (symmetrical, aligned sills, no columns, no kitchen) ============
    # All room windows: 4ft W × 4ft H, sill at 3ft from 1F floor
    # Bathroom: 3ft W × 2ft H, sill at 5ft (frosted)
    # NO window in kitchen zone (chimney goes there)
    # NO window crossing column positions
    WIN_COLOR = 'railing'
    WIN_SILL = 3.0
    WIN_H = 4.0
    WIN_W = 4.0

    # BACK WALL (y=25): 2 windows in LIVING zone only (x=0-14, NOT kitchen x=14-20)
    # Evenly spaced in 14ft living portion: centers at x=4 and x=10
    v, t = box_mesh(ft(2.0), ft(INT_D + WALL_T - 0.1), ft(Z_1F_FLOOR + WIN_SILL),
                    ft(WIN_W), ft(0.1), ft(WIN_H))
    cb.add_geometry('window_back_1', v, t, WIN_COLOR)

    v, t = box_mesh(ft(8.0), ft(INT_D + WALL_T - 0.1), ft(Z_1F_FLOOR + WIN_SILL),
                    ft(WIN_W), ft(0.1), ft(WIN_H))
    cb.add_geometry('window_back_2', v, t, WIN_COLOR)

    # LEFT WALL (x=0, room y=9-25): 2 windows evenly spaced
    # Avoid C3 (y=8.5-9.5) and C1 (y=24-25). Available: y=10-24 (14ft)
    # Centers at y=14 and y=20
    v, t = box_mesh(ft(-WALL_T), ft(12.0), ft(Z_1F_FLOOR + WIN_SILL),
                    ft(0.1), ft(WIN_W), ft(WIN_H))
    cb.add_geometry('window_left_1', v, t, WIN_COLOR)

    v, t = box_mesh(ft(-WALL_T), ft(18.0), ft(Z_1F_FLOOR + WIN_SILL),
                    ft(0.1), ft(WIN_W), ft(WIN_H))
    cb.add_geometry('window_left_2', v, t, WIN_COLOR)

    # RIGHT WALL (x=20, room y=13-25): ONLY 1 window — in UTILITY area (y=13-19)
    # Kitchen (y=19-25) has NO window (chimney). Only utility zone gets a window.
    # Center at y=16 (middle of utility zone y=13-19)
    v, t = box_mesh(ft(INT_W + WALL_T - 0.1), ft(14.0), ft(Z_1F_FLOOR + WIN_SILL),
                    ft(0.1), ft(WIN_W), ft(WIN_H))
    cb.add_geometry('window_right_utility', v, t, WIN_COLOR)

    # RIGHT WALL — BATHROOM window (BELOW C4 at y=8.5-9.5)
    # Position: y=5.5-8.5 (3ft wide), sill at 5ft, frosted, avoids C4
    v, t = box_mesh(ft(INT_W + WALL_T - 0.1), ft(5.5), ft(Z_1F_FLOOR + 5.0),
                    ft(0.1), ft(3.0), ft(2.0))
    cb.add_geometry('window_bathroom', v, t, WIN_COLOR)

    # ============ 1F.7a2 GF PROVISIONAL LINTELS (for future windows) ============
    # RCC lintels cast NOW in GF walls at future window positions.
    # Bricks below can be knocked out later to create windows.
    # Lintel size: 9" deep × 9" wide (same as wall thickness) × 5ft long (4ft window + 6" bearing each side)
    # Position: lintel TOP at 7ft from GF floor (z=3+7=10). Future window: 3ft sill, 4ft high.
    # Aligned with 1F windows above for symmetry.
    LINTEL_DEPTH = 0.75  # 9" deep
    LINTEL_W = 5.0       # 5ft long (4ft opening + 6" bearing each side)
    LINTEL_Z = Z_PLINTH + 7.0  # top of future window = 7ft from GF floor = z=10

    # LEFT WALL: 2 lintels (aligned with 1F windows at y=14, y=20)
    for ly in [14.0, 20.0]:
        v, t = box_mesh(ft(-WALL_T), ft(ly - LINTEL_W/2), ft(LINTEL_Z),
                        ft(WALL_T), ft(LINTEL_W), ft(LINTEL_DEPTH))
        cb.add_geometry(f'lintel_gf_left_{ly:.0f}', v, t, 'beam')

    # RIGHT WALL: 2 lintels (utility at y=16, bathroom area at y=7)
    for ly in [16.0, 7.0]:
        v, t = box_mesh(ft(INT_W), ft(ly - LINTEL_W/2), ft(LINTEL_Z),
                        ft(WALL_T), ft(LINTEL_W), ft(LINTEL_DEPTH))
        cb.add_geometry(f'lintel_gf_right_{ly:.0f}', v, t, 'beam')

    # BACK WALL: 2 lintels (aligned with 1F windows at x=4, x=10)
    for lx in [4.0, 10.0]:
        v, t = box_mesh(ft(lx - LINTEL_W/2), ft(INT_D), ft(LINTEL_Z),
                        ft(LINTEL_W), ft(WALL_T), ft(LINTEL_DEPTH))
        cb.add_geometry(f'lintel_gf_back_{lx:.0f}', v, t, 'beam')
    VENT_W = 3.0
    VENT_H = 1.5
    # Side walls: beam is 9"×24" (2.0ft deep), bottom at z=15-2.0=13.0
    # Vent top touches beam bottom: vent at z=13.0-1.5=11.5 to z=13.0
    VENT_Z_SIDE = 15.0 - 2.0 - VENT_H  # = 11.5 (8.5ft above GF floor)

    # Back wall: beam is 9"×20" (1.67ft deep), bottom at z=15-1.67=13.33
    # Vent top touches beam bottom: vent at z=13.33-1.5=11.83 to z=13.33
    VENT_Z_BACK = 15.0 - 1.67 - VENT_H  # = 11.83 (8.83ft above GF floor)

    # LEFT WALL: 3 vents just below side beam
    for vy in [5.0, 14.0, 20.0]:
        v, t = box_mesh(ft(-WALL_T), ft(vy - VENT_W/2), ft(VENT_Z_SIDE),
                        ft(0.1), ft(VENT_W), ft(VENT_H))
        cb.add_geometry(f'vent_left_{vy:.0f}', v, t, WIN_COLOR)

    # RIGHT WALL: 3 vents just below side beam
    for vy in [7.0, 16.0, 22.0]:
        v, t = box_mesh(ft(INT_W + WALL_T - 0.1), ft(vy - VENT_W/2), ft(VENT_Z_SIDE),
                        ft(0.1), ft(VENT_W), ft(VENT_H))
        cb.add_geometry(f'vent_right_{vy:.0f}', v, t, WIN_COLOR)

    # BACK WALL: 2 vents just below back beam (deeper beam = slightly lower)
    for vx in [4.0, 10.0]:
        v, t = box_mesh(ft(vx - VENT_W/2), ft(INT_D + WALL_T - 0.1), ft(VENT_Z_BACK),
                        ft(VENT_W), ft(0.1), ft(VENT_H))
        cb.add_geometry(f'vent_back_{vx:.0f}', v, t, WIN_COLOR)

    # ============ 1F.7c OPEN TERRACE RAILINGS (y=-6 to y=0, z=15.5) ============
    # Front railing: y=-6, x=-0.75 to x=20.75, z=15.5 to z=19
    v, t = box_mesh(ft(-WALL_T), ft(-CANTILEVER), ft(Z_1F_FLOOR),
                    ft(INT_W + 2*WALL_T), ft(0.05), ft(3.5))
    cb.add_geometry('railing_terrace_front', v, t, 'railing')

    # Left railing: x=-0.75, y=-6 to y=0, z=15.5 to z=19
    v, t = box_mesh(ft(-WALL_T), ft(-CANTILEVER), ft(Z_1F_FLOOR),
                    ft(0.05), ft(CANTILEVER), ft(3.5))
    cb.add_geometry('railing_terrace_left', v, t, 'railing')

    # Right railing: x=20.75, y=-6 to y=0, z=15.5 to z=19
    v, t = box_mesh(ft(INT_W + WALL_T - 0.05), ft(-CANTILEVER), ft(Z_1F_FLOOR),
                    ft(0.05), ft(CANTILEVER), ft(3.5))
    cb.add_geometry('railing_terrace_right', v, t, 'railing')

    # ============ 1F.8 ROOF SLAB (with 6ft × 3ft stair well opening) ============
    # Covers building footprint: x=-0.75 to x=20.75, y=-0.75 to y=25.75
    # z=27.5 to z=28.0 (0.5ft thick)
    # STAIR WELL OPENING: x=0 to x=3, y=0 to y=6 (above where sloped stair arrives)
    # Split into pieces around the opening:

    # Piece 1: BACK portion (y=6 to y=25.75) — full width
    v, t = box_mesh(ft(-WALL_T), ft(6.0), ft(Z_1F_ROOF),
                    ft(INT_W + 2*WALL_T), ft(INT_D - 6.0 + WALL_T), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_1f_back', v, t, 'slab')

    # Piece 2: FRONT-RIGHT (x=3 to x=20.75, y=-0.75 to y=6)
    v, t = box_mesh(ft(3.0), ft(-WALL_T), ft(Z_1F_ROOF),
                    ft(INT_W - 3.0 + WALL_T), ft(6.0 + WALL_T), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_1f_front_right', v, t, 'slab')

    # Piece 3: FRONT-LEFT edge (x=-0.75 to x=0, y=-0.75 to y=6) — left wall strip
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_1F_ROOF),
                    ft(WALL_T), ft(6.0 + WALL_T), ft(SLAB_T_FT))
    cb.add_geometry('roof_slab_1f_left_edge', v, t, 'slab')

    # STAIR WELL (6ft × 3ft): x=0 to x=3, y=0 to y=6 — OPEN (no slab here)

    # ============ 1F.9 PARAPET WALLS (3ft high on roof edges) ============
    Z_PARAPET = Z_1F_ROOF + SLAB_T_FT  # 28.0
    PARAPET_H = 3.0

    # Back parapet
    v, t = box_mesh(ft(-WALL_T), ft(INT_D), ft(Z_PARAPET),
                    ft(INT_W + 2*WALL_T), ft(WALL_T), ft(PARAPET_H))
    cb.add_geometry('parapet_back', v, t, 'wall')

    # Left parapet
    v, t = box_mesh(ft(-WALL_T), ft(0), ft(Z_PARAPET),
                    ft(WALL_T), ft(INT_D + WALL_T), ft(PARAPET_H))
    cb.add_geometry('parapet_left', v, t, 'wall')

    # Right parapet
    v, t = box_mesh(ft(INT_W), ft(0), ft(Z_PARAPET),
                    ft(WALL_T), ft(INT_D + WALL_T), ft(PARAPET_H))
    cb.add_geometry('parapet_right', v, t, 'wall')

    # Front parapet
    v, t = box_mesh(ft(-WALL_T), ft(-WALL_T), ft(Z_PARAPET),
                    ft(INT_W + 2*WALL_T), ft(WALL_T), ft(PARAPET_H))
    cb.add_geometry('parapet_front', v, t, 'wall')

    # ============ 1F.10 WATER TANK (on roof, away from stair well zone) ============
    # Positioned on clear roof area (NOT above stair well/sloped stair)
    TANK_X = 8.0   # center-right area of roof (away from x=0-3 stair zone)
    TANK_Y = 2.0
    TANK_W = 3.0
    TANK_D = 2.5
    TANK_H = 2.5
    STAND_H = 2.0
    LEG_SIZE = 0.2
    Z_ROOF_TOP = Z_PARAPET  # 28.0 (top of roof slab)

    # Legs at 4 corners
    for lx, ly in [(TANK_X, TANK_Y), (TANK_X + TANK_W - LEG_SIZE, TANK_Y),
                   (TANK_X, TANK_Y + TANK_D - LEG_SIZE), (TANK_X + TANK_W - LEG_SIZE, TANK_Y + TANK_D - LEG_SIZE)]:
        v, t = box_mesh(ft(lx), ft(ly), ft(Z_ROOF_TOP),
                        ft(LEG_SIZE), ft(LEG_SIZE), ft(STAND_H))
        cb.add_geometry(f'tank_leg_{lx:.0f}_{ly:.0f}', v, t, 'railing')

    # Tank body
    v, t = box_mesh(ft(TANK_X), ft(TANK_Y), ft(Z_ROOF_TOP + STAND_H),
                    ft(TANK_W), ft(TANK_D), ft(TANK_H))
    cb.add_geometry('water_tank', v, t, 'water_tank')

    return cb


def main():
    print("Generating full building (GF + 1F) 3D model...")
    cb = build_ground_floor()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dae = os.path.join(script_dir, 'ground-floor.dae')
    cb.save(output_dae)

    size_kb = os.path.getsize(output_dae) / 1024
    print(f"Collada model saved: {output_dae}")
    print(f"  Size: {size_kb:.0f} KB")

    # Try to generate GLB for better color support
    try:
        import trimesh
        import numpy as np

        scene = trimesh.Scene()

        for name, color in COLORS.items():
            pass  # materials handled per-mesh

        for geom_name, verts, tris, mat_name in cb.geometries:
            vertices = np.array(verts, dtype=np.float64)
            faces = np.array(tris, dtype=np.int64)
            color_rgba = COLORS[mat_name]
            color_uint8 = [int(c * 255) for c in color_rgba]

            mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
            mesh.visual.face_colors = color_uint8
            scene.add_geometry(mesh, node_name=geom_name)

        output_glb = os.path.join(script_dir, 'ground-floor.glb')
        scene.export(output_glb)
        size_glb = os.path.getsize(output_glb) / 1024
        print(f"GLB model saved: {output_glb}")
        print(f"  Size: {size_glb:.0f} KB")
    except ImportError:
        print("trimesh not available, skipping GLB generation")
    except Exception as e:
        print(f"GLB generation failed: {e}")

    print("\nElements included:")
    print("  GROUND FLOOR:")
    print("  - Plinth (raised platform)")
    print("  - Floor slab")
    print("  - External walls (back, left, right, front segments)")
    print("  - Columns C1-C8 (inside walls, overlapping — different color for visibility)")
    print("  - Staircase (Flight 1, Landing, Flight 2, partition)")
    print("  - Toilet enclosure")
    print("  - Shutter (rolling)")
    print("  - Gates (stair gate + toilet door)")
    print("  - Ramp (front)")
    print("  - Gate steps")
    print("  - Beams (back, middle, front, left, right)")
    print("  - Roof slab (with 6ft front cantilever)")
    print("  - Shade: PURE CANTILEVER (no walls, no pillars)")
    print("  - Septic tank + soak pits (underground)")
    print("  - Ground plane")
    print("  FIRST FLOOR:")
    print("  - 1F External walls (left, right, back, front)")
    print("  - 1F Room partition wall (y=9, with door opening)")
    print("  - 1F Kitchen (L-shaped half-walls + floor indicator)")
    print("  - 1F Bathroom (walls + fixtures: commode, shower, basin, geyser)")
    print("  - 1F Stair well railing")
    print("  - 1F Sloped stair-slab to roof (with step indicators)")
    print("  - 1F Open terrace railings")
    print("  - 1F Roof slab (building footprint only)")
    print("  - 1F Parapet walls (3ft high)")
    print("  - Water tank on roof (with stand)")


if __name__ == "__main__":
    main()
