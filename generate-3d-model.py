#!/usr/bin/env python3
"""
Generate a Collada (.dae) 3D model of the farm storage building.
All dimensions in meters (converted from feet).
Color-coded elements for easy identification in SketchUp.
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

# Conversion
FT_TO_M = 0.3048
IN_TO_M = 0.0254

# Building dimensions (in meters)
WIDTH = 20 * FT_TO_M       # 6.096m (x-axis)
DEPTH = 25 * FT_TO_M       # 7.62m (y-axis)
PLINTH_H = 3 * FT_TO_M     # 0.9144m
ROOM_H = 12 * FT_TO_M      # 3.6576m
SLAB_T = 6 * IN_TO_M       # 0.1524m
WALL_EXT = 9 * IN_TO_M     # 0.2286m
WALL_INT = 4.5 * IN_TO_M   # 0.1143m
SHADE_PROJ = 5 * FT_TO_M   # 1.524m
RAMP_L = 8 * FT_TO_M       # 2.4384m
RAMP_W = 12 * FT_TO_M      # 3.6576m
STAIR_W = 7.5 * FT_TO_M    # 2.286m (total zone: 3.5 + 0.5 + 3.5)
STAIR_D = 10 * FT_TO_M     # 3.048m
STAIR_FLIGHT_W = 3.5 * FT_TO_M  # 1.0668m per flight
SHUTTER_W = 10 * FT_TO_M   # 3.048m
SHUTTER_H = 10 * FT_TO_M   # 3.048m
GATE_W = 3 * FT_TO_M       # 0.9144m
GATE_H = 7 * FT_TO_M       # 2.1336m

# Colors (RGBA, 0-1) — Vibrant, aesthetic palette
COLORS = {
    'plinth': (0.72, 0.53, 0.26, 1.0),        # warm terracotta brown
    'wall_ext': (0.96, 0.93, 0.85, 1.0),       # warm white/cream
    'wall_int': (0.92, 0.87, 0.78, 1.0),       # soft beige
    'slab_floor': (0.78, 0.75, 0.70, 1.0),     # polished concrete
    'slab_roof': (0.55, 0.58, 0.62, 1.0),      # slate grey
    'column': (0.35, 0.38, 0.42, 1.0),         # dark concrete
    'beam': (0.42, 0.44, 0.48, 1.0),           # steel grey
    'stair': (0.85, 0.72, 0.55, 1.0),          # sandstone warm
    'ramp': (0.78, 0.68, 0.52, 1.0),           # sandy concrete
    'shade': (0.4, 0.65, 0.85, 0.7),           # sky blue translucent
    'shutter': (0.18, 0.22, 0.28, 1.0),        # dark charcoal metal
    'gate': (0.45, 0.25, 0.12, 1.0),           # rich mahogany wood
    'toilet': (0.55, 0.82, 0.78, 1.0),         # fresh mint/teal
    'tank': (0.2, 0.55, 0.82, 1.0),            # ocean blue
    'first_floor': (0.65, 0.78, 0.92, 0.45),   # light sky (translucent)
    'lobby': (0.6, 0.75, 0.55, 1.0),           # sage green
    'ground': (0.28, 0.45, 0.22, 1.0),         # grass green
}

def box_mesh(x, y, z, w, d, h):
    """Generate vertices and triangles for a box at (x,y,z) with dimensions (w,d,h)."""
    verts = [
        (x, y, z), (x+w, y, z), (x+w, y+d, z), (x, y+d, z),           # bottom
        (x, y, z+h), (x+w, y, z+h), (x+w, y+d, z+h), (x, y+d, z+h),  # top
    ]
    # 12 triangles (2 per face)
    tris = [
        (0,1,2), (0,2,3),  # bottom
        (4,6,5), (4,7,6),  # top
        (0,1,5), (0,5,4),  # front
        (2,3,7), (2,7,6),  # back
        (0,3,7), (0,7,4),  # left
        (1,2,6), (1,6,5),  # right
    ]
    return verts, tris


def ramp_mesh(x, y, z_bottom, z_top, w, length):
    """Generate a ramp (sloped surface) from z_bottom to z_top."""
    verts = [
        (x, y, z_bottom), (x+w, y, z_bottom),                          # bottom-front
        (x+w, y+length, z_top), (x, y+length, z_top),                  # top-back (at building)
        (x, y, z_bottom), (x+w, y, z_bottom),                          # same bottom (for thickness)
        (x+w, y+length, z_top), (x, y+length, z_top),                  # same top
        # Add thickness (0.15m)
        (x, y, z_bottom-0.15), (x+w, y, z_bottom-0.15),
        (x+w, y+length, z_top-0.15), (x, y+length, z_top-0.15),
    ]
    tris = [
        (0,1,2), (0,2,3),    # top surface
        (8,10,9), (8,11,10),  # bottom surface
        (0,1,9), (0,9,8),    # front face
        (2,3,11), (2,11,10), # back face
        (0,3,11), (0,11,8),  # left face
        (1,2,10), (1,10,9),  # right face
    ]
    return verts, tris


def stair_mesh(x, y, z_start, num_risers, riser_h, tread_d, width, going_y=True):
    """Generate staircase steps."""
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
        # Offset triangle indices
        bt_offset = [(a+offset, b+offset, c+offset) for a,b,c in bt]
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

        # Asset
        asset = ET.SubElement(root, 'asset')
        unit = ET.SubElement(asset, 'unit', {'name': 'meter', 'meter': '1'})
        up = ET.SubElement(asset, 'up_axis')
        up.text = 'Z_UP'

        # Effects
        lib_effects = ET.SubElement(root, 'library_effects')
        for mat_name, color in self.materials:
            effect = ET.SubElement(lib_effects, 'effect', {'id': f'{mat_name}-effect'})
            profile = ET.SubElement(effect, 'profile_COMMON')
            technique = ET.SubElement(profile, 'technique', {'sid': 'common'})
            phong = ET.SubElement(technique, 'phong')
            diffuse = ET.SubElement(phong, 'diffuse')
            c = ET.SubElement(diffuse, 'color')
            c.text = f'{color[0]} {color[1]} {color[2]} {color[3]}'

        # Materials
        lib_materials = ET.SubElement(root, 'library_materials')
        for mat_name, _ in self.materials:
            mat = ET.SubElement(lib_materials, 'material', {'id': f'{mat_name}-mat', 'name': mat_name})
            inst = ET.SubElement(mat, 'instance_effect', {'url': f'#{mat_name}-effect'})

        # Geometries
        lib_geom = ET.SubElement(root, 'library_geometries')
        for name, verts, tris, _ in self.geometries:
            geom = ET.SubElement(lib_geom, 'geometry', {'id': f'{name}-geom', 'name': name})
            mesh = ET.SubElement(geom, 'mesh')

            # Positions source
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

            # Vertices
            vertices = ET.SubElement(mesh, 'vertices', {'id': f'{name}-vertices'})
            ET.SubElement(vertices, 'input', {'semantic': 'POSITION', 'source': f'#{name}-positions'})

            # Triangles
            triangles = ET.SubElement(mesh, 'triangles', {'count': str(len(tris))})
            ET.SubElement(triangles, 'input', {'semantic': 'VERTEX', 'source': f'#{name}-vertices', 'offset': '0'})
            p = ET.SubElement(triangles, 'p')
            p.text = ' '.join(str(idx) for tri in tris for idx in tri)

        # Visual scene
        lib_scenes = ET.SubElement(root, 'library_visual_scenes')
        vscene = ET.SubElement(lib_scenes, 'visual_scene', {'id': 'Scene', 'name': 'FarmStorage'})

        for name, mat_name in self.scene_nodes:
            node = ET.SubElement(vscene, 'node', {'id': f'{name}-node', 'name': name, 'type': 'NODE'})
            inst_geom = ET.SubElement(node, 'instance_geometry', {'url': f'#{name}-geom'})
            bind_mat = ET.SubElement(inst_geom, 'bind_material')
            tc = ET.SubElement(bind_mat, 'technique_common')
            ET.SubElement(tc, 'instance_material', {
                'symbol': mat_name,
                'target': f'#{mat_name}-mat'
            })

        # Scene
        scene = ET.SubElement(root, 'scene')
        ET.SubElement(scene, 'instance_visual_scene', {'url': '#Scene'})

        return root

    def save(self, filepath):
        root = self.build_xml()
        xml_str = ET.tostring(root, encoding='unicode')
        dom = minidom.parseString(xml_str)
        pretty = dom.toprettyxml(indent='  ')
        # Remove extra XML declaration line from minidom
        lines = pretty.split('\n')
        lines = [l for l in lines if not l.startswith('<?xml')]
        final = '<?xml version="1.0" encoding="utf-8"?>\n' + '\n'.join(lines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final)


def build_model():
    cb = ColladaBuilder()

    # Add materials
    for name, color in COLORS.items():
        cb.add_material(name, color)

    # Ground level = 0, Plinth top = PLINTH_H, Roof = PLINTH_H + ROOM_H
    # Front wall layout (left to right as viewed from front):
    #   LEFT: Gate(3ft) + Wall(4.5ft) = 7.5ft stair zone
    #   CENTER: Shutter(10ft)
    #   RIGHT: Wall(2.5ft)

    stair_zone_w = STAIR_W  # 7.5ft
    shutter_start_x = stair_zone_w  # shutter starts after stair zone
    right_wall_start = stair_zone_w + SHUTTER_W  # 17.5ft
    right_wall_w = WIDTH - right_wall_start  # 2.5ft

    # ============ PLINTH ============
    v, t = box_mesh(0, 0, 0, WIDTH, DEPTH, PLINTH_H)
    cb.add_geometry('plinth', v, t, 'plinth')

    # ============ FLOOR SLAB ============
    floor_z = PLINTH_H
    v, t = box_mesh(0, 0, floor_z, WIDTH, DEPTH, 0.1)
    cb.add_geometry('floor_slab', v, t, 'slab_floor')

    # ============ EXTERNAL WALLS ============
    wall_z = floor_z + 0.1
    wall_h = ROOM_H - 0.1

    # Back wall (full)
    v, t = box_mesh(0, DEPTH - WALL_EXT, wall_z, WIDTH, WALL_EXT, wall_h)
    cb.add_geometry('wall_back', v, t, 'wall_ext')

    # Left wall (full)
    v, t = box_mesh(0, 0, wall_z, WALL_EXT, DEPTH, wall_h)
    cb.add_geometry('wall_left', v, t, 'wall_ext')

    # Right wall (full)
    v, t = box_mesh(WIDTH - WALL_EXT, 0, wall_z, WALL_EXT, DEPTH, wall_h)
    cb.add_geometry('wall_right', v, t, 'wall_ext')

    # Front wall - stair zone (left: gate + wall above + mid wall)
    # Gate opening: 0 to GATE_W (3ft), height GATE_H (7ft)
    # Above gate:
    above_gate_z = wall_z + GATE_H
    above_gate_h = wall_h - GATE_H
    v, t = box_mesh(0, 0, above_gate_z, GATE_W, WALL_EXT, above_gate_h)
    cb.add_geometry('wall_above_gate', v, t, 'wall_ext')

    # Wall between gate and shutter (3ft to 7.5ft = 4.5ft wide, full height)
    mid_wall_start = GATE_W
    mid_wall_w = stair_zone_w - GATE_W  # 4.5ft
    v, t = box_mesh(mid_wall_start, 0, wall_z, mid_wall_w, WALL_EXT, wall_h)
    cb.add_geometry('wall_front_mid', v, t, 'wall_ext')

    # Above shutter (7.5ft to 17.5ft, 2ft height above shutter)
    above_shutter_z = wall_z + SHUTTER_H
    above_shutter_h = wall_h - SHUTTER_H
    v, t = box_mesh(shutter_start_x, 0, above_shutter_z, SHUTTER_W, WALL_EXT, above_shutter_h)
    cb.add_geometry('wall_above_shutter', v, t, 'wall_ext')

    # Right of shutter wall (17.5ft to 20ft = 2.5ft, full height)
    v, t = box_mesh(right_wall_start, 0, wall_z, right_wall_w, WALL_EXT, wall_h)
    cb.add_geometry('wall_front_right', v, t, 'wall_ext')

    # ============ SHUTTER ============
    v, t = box_mesh(shutter_start_x, 0, wall_z, SHUTTER_W, 0.05, SHUTTER_H)
    cb.add_geometry('shutter', v, t, 'shutter')

    # ============ GATE ============
    v, t = box_mesh(0, 0, wall_z, GATE_W, 0.05, GATE_H)
    cb.add_geometry('gate', v, t, 'gate')

    # ============ STAIR PARTITION WALL ============
    # At x = STAIR_W (7.5ft), running from front to 10ft deep
    v, t = box_mesh(STAIR_W - WALL_INT, WALL_EXT, wall_z, WALL_INT, STAIR_D, wall_h)
    cb.add_geometry('wall_stair_partition', v, t, 'wall_int')

    # ============ TOILET (under Flight 2, LEFT side = x=0 to 3.5ft) ============
    # When looking from outside: Gate(left) → Lobby → Toilet(leftmost, under Flight 2)
    # Flight 2 is the upper flight, placed at LEFT (x=0 to STAIR_FLIGHT_W)
    # Toilet is under it, starts after lobby (y = lobby_depth)
    lobby_depth = 3 * FT_TO_M
    toilet_w = STAIR_FLIGHT_W  # 3.5ft
    toilet_d = 5 * FT_TO_M
    toilet_h = 8 * FT_TO_M
    toilet_x = 0  # starts at left edge (under Flight 2 which is also at x=0)
    toilet_y = WALL_EXT + lobby_depth  # starts after lobby (y=3ft from front)

    # Toilet back wall (at y = lobby + toilet_depth)
    v, t = box_mesh(toilet_x, toilet_y + toilet_d, wall_z, toilet_w, WALL_INT, toilet_h)
    cb.add_geometry('toilet_back_wall', v, t, 'toilet')
    # Toilet right wall (partition between toilet and Flight 1)
    v, t = box_mesh(toilet_x + toilet_w, toilet_y, wall_z, WALL_INT, toilet_d, toilet_h)
    cb.add_geometry('toilet_side_wall', v, t, 'toilet')
    # Toilet front wall at lobby boundary (with door)
    v, t = box_mesh(toilet_x, toilet_y - WALL_INT, wall_z, toilet_w, WALL_INT, toilet_h)
    cb.add_geometry('toilet_front_wall', v, t, 'toilet')

    # ============ COLUMNS (8 total, all in walls) ============
    col_w = 9 * IN_TO_M
    col_d = 12 * IN_TO_M
    col_h = wall_h

    # C1: back-left corner
    v, t = box_mesh(0, DEPTH - col_d, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C1', v, t, 'column')
    # C2: back-right corner
    v, t = box_mesh(WIDTH - col_w, DEPTH - col_d, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C2', v, t, 'column')
    # C3: left wall at 16ft from front (9ft from front = 16ft from back)
    beam_y = 16 * FT_TO_M  # 16ft from front... wait, 9ft from front
    beam_y = 9 * FT_TO_M  # middle beam at 9ft from front
    v, t = box_mesh(0, beam_y, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C3', v, t, 'column')
    # C4: right wall at 9ft from front
    v, t = box_mesh(WIDTH - col_w, beam_y, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C4', v, t, 'column')
    # C5: front-left corner
    v, t = box_mesh(0, 0, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C5', v, t, 'column')
    # C6: front wall at 7.5ft (stair/shutter boundary)
    c6_x = STAIR_W
    v, t = box_mesh(c6_x - col_w, 0, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C6', v, t, 'column')
    # C7: front wall at 17.5ft (shutter right edge)
    c7_x = right_wall_start
    v, t = box_mesh(c7_x, 0, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C7', v, t, 'column')
    # C8: front-right corner
    v, t = box_mesh(WIDTH - col_w, 0, wall_z, col_w, col_d, col_h)
    cb.add_geometry('col_C8', v, t, 'column')

    # ============ BEAMS ============
    beam_depth_deep = 20 * IN_TO_M  # deep beams (9"×20")
    beam_depth_std = 15 * IN_TO_M   # standard beams
    beam_w = 9 * IN_TO_M
    roof_z = floor_z + ROOM_H
    deep_beam_z = roof_z - beam_depth_deep
    std_beam_z = roof_z - beam_depth_std

    # Back beam (deep, C1-C2)
    v, t = box_mesh(0, DEPTH - beam_w, deep_beam_z, WIDTH, beam_w, beam_depth_deep)
    cb.add_geometry('beam_back', v, t, 'beam')
    # Middle beam (deep, C3-C4, at 9ft from front)
    v, t = box_mesh(0, beam_y, deep_beam_z, WIDTH, beam_w, beam_depth_deep)
    cb.add_geometry('beam_middle', v, t, 'beam')
    # Front beam (standard)
    v, t = box_mesh(0, 0, std_beam_z, WIDTH, beam_w, beam_depth_std)
    cb.add_geometry('beam_front', v, t, 'beam')
    # Left side beam
    v, t = box_mesh(0, 0, std_beam_z, beam_w, DEPTH, beam_depth_std)
    cb.add_geometry('beam_left', v, t, 'beam')
    # Right side beam
    v, t = box_mesh(WIDTH - beam_w, 0, std_beam_z, beam_w, DEPTH, beam_depth_std)
    cb.add_geometry('beam_right', v, t, 'beam')

    # ============ ROOF SLAB (with 5ft cantilever at FRONT = -y direction) ============
    # Front wall is at y=0. Shade extends toward -y (in front of building)
    v, t = box_mesh(0, -SHADE_PROJ, roof_z, WIDTH, DEPTH + SHADE_PROJ, SLAB_T)
    cb.add_geometry('roof_slab', v, t, 'slab_roof')

    # ============ STAIRCASE ============
    # Lobby: 0 to lobby_depth (3ft) from front wall, full stair zone width
    # Stairs start at lobby_depth going back
    # Layout (viewed from outside, left to right):
    #   LEFT (x=0 to 3.5ft): Flight 2 (upper, toilet underneath)
    #   GAP (x=3.5 to 4ft): wall/gap between flights
    #   RIGHT (x=4 to 7.5ft): Flight 1 (lower, starts at ground)
    # ALL stairs must fit within x=0 to STAIR_W (7.5ft zone)
    tread_d = 10 * IN_TO_M
    riser_h = 7.2 * IN_TO_M
    gap = 0.5 * FT_TO_M

    # Flight 1 (lower flight, RIGHT side of stair zone)
    flight1_x = STAIR_FLIGHT_W + gap  # starts after Flight 2 + gap
    flight1_y = WALL_EXT + lobby_depth  # starts after lobby
    v, t = stair_mesh(flight1_x, flight1_y, wall_z, 10, riser_h, tread_d, STAIR_FLIGHT_W, going_y=True)
    cb.add_geometry('stair_flight1', v, t, 'stair')

    # Flight 2 (upper flight, LEFT side of stair zone, toilet underneath)
    flight2_x = 0  # starts at left edge
    flight2_y_start = flight1_y + 9 * tread_d  # starts at far end (landing)
    v, t = stair_mesh(flight2_x, flight2_y_start, wall_z + 10 * riser_h, 10, riser_h, tread_d, STAIR_FLIGHT_W, going_y=False)
    cb.add_geometry('stair_flight2', v, t, 'stair')

    # Landing (at the back of stair zone, full width)
    landing_z = wall_z + 10 * riser_h
    landing_y = flight1_y + 9 * tread_d
    v, t = box_mesh(0, landing_y, landing_z - riser_h, STAIR_W, 3*FT_TO_M, riser_h)
    cb.add_geometry('stair_landing', v, t, 'stair')

    # ============ RAMP ============
    # In front of shutter (front wall at y=0), extending in -y direction
    # Centered on shutter: shutter is at x=7.5 to x=17.5, ramp 12ft wide centered
    ramp_center_x = shutter_start_x + SHUTTER_W / 2  # center of shutter
    ramp_x = ramp_center_x - RAMP_W / 2
    v, t = ramp_mesh(ramp_x, -RAMP_L, 0, PLINTH_H, RAMP_W, RAMP_L)
    cb.add_geometry('ramp', v, t, 'ramp')

    # ============ GATE STEPS ============
    step_w = GATE_W
    step_riser = 7 * IN_TO_M
    step_tread = 10 * IN_TO_M
    for i in range(5):
        sz = i * step_riser
        sy = -(5 - i) * step_tread
        v, t = box_mesh(0, sy, sz, step_w, step_tread, step_riser)
        cb.add_geometry(f'step_{i}', v, t, 'stair')

    # ============ WATER TANK ============
    tank_x = 0.3
    tank_y = 0.3
    tank_z = roof_z + SLAB_T + 0.6
    v, t = box_mesh(tank_x, tank_y, tank_z, 1.0, 0.8, 0.8)
    cb.add_geometry('water_tank', v, t, 'tank')
    v, t = box_mesh(tank_x, tank_y, roof_z + SLAB_T, 1.0, 0.8, 0.6)
    cb.add_geometry('tank_stand', v, t, 'column')

    # ============ FIRST FLOOR (future) ============
    ff_z = roof_z + SLAB_T
    ff_h = 10 * FT_TO_M  # 10ft room height
    ff_room_depth = 16 * FT_TO_M
    ff_balcony_depth = 9 * FT_TO_M

    # Room walls (using first_floor color from COLORS dict)
    # Back wall (1F)
    v, t = box_mesh(0, DEPTH - WALL_INT, ff_z, WIDTH, WALL_INT, ff_h)
    cb.add_geometry('ff_wall_back', v, t, 'first_floor')
    # Left wall (1F room portion)
    v, t = box_mesh(0, ff_balcony_depth, ff_z, WALL_INT, ff_room_depth, ff_h)
    cb.add_geometry('ff_wall_left', v, t, 'first_floor')
    # Right wall (1F room portion)
    v, t = box_mesh(WIDTH - WALL_INT, ff_balcony_depth, ff_z, WALL_INT, ff_room_depth, ff_h)
    cb.add_geometry('ff_wall_right', v, t, 'first_floor')
    # Room partition (at 9ft from front)
    v, t = box_mesh(0, ff_balcony_depth, ff_z, WIDTH, WALL_INT, ff_h)
    cb.add_geometry('ff_partition', v, t, 'first_floor')

    # First floor roof slab
    ff_roof_z = ff_z + ff_h
    v, t = box_mesh(0, 0, ff_roof_z, WIDTH, DEPTH, SLAB_T)
    cb.add_geometry('ff_roof_slab', v, t, 'slab_roof')

    # ============ LOBBY FLOOR (highlighted) ============
    # Lobby is x=0 to STAIR_W, y=0 to lobby_depth (3ft from front wall)
    lobby_floor_z = floor_z + 0.11  # just above floor slab
    v, t = box_mesh(0, WALL_EXT, lobby_floor_z, STAIR_W, lobby_depth, 0.02)
    cb.add_geometry('lobby_floor', v, t, 'lobby')

    # ============ GROUND PLANE ============
    # Large flat area around the building at z=0
    ground_size = 30 * FT_TO_M
    ground_offset = 10 * FT_TO_M
    v, t = box_mesh(-ground_offset, -ground_offset, -0.05,
                    WIDTH + 2*ground_offset, DEPTH + 2*ground_offset, 0.05)
    cb.add_geometry('ground_plane', v, t, 'ground')

    # ============ SHADE CANTILEVER HIGHLIGHT ============
    # Thin colored layer on the underside of the roof slab cantilever
    v, t = box_mesh(0, -SHADE_PROJ, roof_z - 0.02, WIDTH, SHADE_PROJ, 0.02)
    cb.add_geometry('shade_highlight', v, t, 'shade')

    return cb


def main():
    print("🏗️  Generating 3D model...")
    cb = build_model()

    output_path = "/Users/schowdhary/codebases/farmhouse_design/farmhouse-3d-model.dae"
    cb.save(output_path)

    import os
    size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ Collada model saved: {output_path}")
    print(f"   Size: {size_kb:.0f} KB")
    print(f"\n📌 To use in SketchUp:")
    print(f"   1. Open https://app.sketchup.com/app")
    print(f"   2. File → Import → select farmhouse-3d-model.dae")
    print(f"   3. The model will appear with color-coded elements")
    print(f"\n🎨 Color Legend:")
    print(f"   Brown = Plinth/Platform")
    print(f"   Cream = External Walls")
    print(f"   Grey = Columns, Beams, Slabs")
    print(f"   Warm grey = Staircase + Ramp")
    print(f"   Blue-grey = Shade canopy")
    print(f"   Dark = Shutter + Gate")
    print(f"   Teal = Toilet enclosure")
    print(f"   Blue = Water tank")


if __name__ == "__main__":
    main()
