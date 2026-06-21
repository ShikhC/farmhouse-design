#!/usr/bin/env python3
"""
Generate a Collada (.dae) 3D model of the ground floor structure.
All dimensions defined in feet, converted to meters for the DAE file.

Coordinate system:
  x-axis: width (0 = left wall inside face, 20 = right wall inside face)
  y-axis: depth (0 = front wall inside face, 25 = back wall inside face)
  z-axis: height (0 = natural ground, 3 = plinth top / GF floor, 15 = slab soffit)

Internal clear space: 20ft x 25ft x 12ft (room height)
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
        vscene = ET.SubElement(lib_scenes, 'visual_scene', {'id': 'Scene', 'name': 'GroundFloor'})

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
    # All 9"x12" (0.75ft x 1ft), 12ft high from z=3 to z=15
    COL_9 = 0.75   # 9 inches in feet
    COL_12 = 1.0   # 12 inches in feet
    COL_H = ROOM_H  # 12ft

    # C1: back-left corner (inside the wall intersection)
    v, t = box_mesh(ft(0), ft(INT_D - COL_12), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C1', v, t, 'column')

    # C2: back-right corner
    v, t = box_mesh(ft(INT_W - COL_9), ft(INT_D - COL_12), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C2', v, t, 'column')

    # C3: left wall, 9ft from front
    v, t = box_mesh(ft(0), ft(9.0), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C3', v, t, 'column')

    # C4: right wall, 9ft from front
    v, t = box_mesh(ft(INT_W - COL_9), ft(9.0), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C4', v, t, 'column')

    # C5: front-left corner
    v, t = box_mesh(ft(0), ft(0), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C5', v, t, 'column')

    # C6: front wall at x=6, 9" along x-axis, 12" along y-axis (into building)
    # C6: front wall column, 9"x12" with 12" ALONG the wall (x-axis), 9" ACROSS (y-axis = flush with 9" wall)
    # C5-to-C6 clear = 6ft. C6 starts at x=6, extends 12" (1ft) along x = x=6 to x=7.
    # Depth: 9" (0.75ft) along y = same as wall thickness = HIDDEN in wall.
    v, t = box_mesh(ft(6.0), ft(0), ft(Z_PLINTH),
                    ft(COL_12), ft(COL_9), ft(COL_H))
    cb.add_geometry('col_C6', v, t, 'column')

    # C7: front wall column, same orientation as C6
    # x=17 to x=18 (12" along x), y=0 to y=0.75 (9" into building = flush)
    v, t = box_mesh(ft(17.0), ft(0), ft(Z_PLINTH),
                    ft(COL_12), ft(COL_9), ft(COL_H))
    cb.add_geometry('col_C7', v, t, 'column')

    # C8: front-right corner (at x=20, inside right wall)
    v, t = box_mesh(ft(INT_W - COL_9), ft(0), ft(Z_PLINTH),
                    ft(COL_9), ft(COL_12), ft(COL_H))
    cb.add_geometry('col_C8', v, t, 'column')

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
    #   x=0 to x=2.75, starting at y=8.5 going back to y=2.5
    #   9 risers, rising from z=9 to z=15
    v, t = stair_mesh(ft(0), ft(8.5), ft(LANDING_Z),
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
    BEAM_20 = 20.0 / 12.0  # 20 inches = 1.667ft
    BEAM_15 = 15.0 / 12.0  # 15 inches = 1.25ft

    # Back beam (9"x20"): spans x=0-20, at y=25
    v, t = box_mesh(ft(0), ft(INT_D - BEAM_9), ft(Z_SLAB_SOFFIT - BEAM_20),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_20))
    cb.add_geometry('beam_back', v, t, 'beam')

    # Middle beam (9"x20"): spans x=0-20, at y=9
    v, t = box_mesh(ft(0), ft(9.0), ft(Z_SLAB_SOFFIT - BEAM_20),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_20))
    cb.add_geometry('beam_middle', v, t, 'beam')

    # Front beam (9"x15"): spans x=0-20, at y=0
    v, t = box_mesh(ft(0), ft(0), ft(Z_SLAB_SOFFIT - BEAM_15),
                    ft(INT_W), ft(BEAM_9), ft(BEAM_15))
    cb.add_geometry('beam_front', v, t, 'beam')

    # Left beam (9"x15"): spans y=0-25, at x=0
    v, t = box_mesh(ft(0), ft(0), ft(Z_SLAB_SOFFIT - BEAM_15),
                    ft(BEAM_9), ft(INT_D), ft(BEAM_15))
    cb.add_geometry('beam_left', v, t, 'beam')

    # Right beam (9"x15"): spans y=0-25, at x=20
    v, t = box_mesh(ft(INT_W - BEAM_9), ft(0), ft(Z_SLAB_SOFFIT - BEAM_15),
                    ft(BEAM_9), ft(INT_D), ft(BEAM_15))
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

    # The STAIR WELL OPENING: x=0 to x=3, y=0 to y=8.5 (no slab here — OPEN!)
    # Mark with a thin dark indicator at slab level
    v, t = box_mesh(ft(0), ft(0), ft(Z_SLAB_SOFFIT + SLAB_T_FT),
                    ft(3.0), ft(8.5), ft(0.02))
    cb.add_geometry('stair_well_opening', v, t, 'ground')

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

    return cb


def main():
    print("Generating ground floor 3D model...")
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
    print("  - Plinth (raised platform)")
    print("  - Floor slab")
    print("  - External walls (back, left, right, front segments)")
    print("  - Columns C1-C8")
    print("  - Staircase (Flight 1, Landing, Flight 2, partition)")
    print("  - Toilet enclosure")
    print("  - Shutter (rolling)")
    print("  - Gates (stair gate + toilet door)")
    print("  - Ramp (front)")
    print("  - Gate steps")
    print("  - Beams (back, middle, front, left, right)")
    print("  - Roof slab (with 5ft front cantilever)")
    print("  - Shade: PURE CANTILEVER (no walls, no pillars — slab hangs from front beam)")
    print("  - Septic tank + soak pit (underground)")
    print("  - Ground plane")


if __name__ == "__main__":
    main()
