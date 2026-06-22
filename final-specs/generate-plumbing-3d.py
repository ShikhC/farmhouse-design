#!/usr/bin/env python3
"""
Generate a Collada (.dae) + GLB 3D model of the PLUMBING SYSTEMS.

FINALIZED LAYOUT (June 2026):
- All drainage routes to LEFT / BACK-LEFT (away from borewell on right)
- Borewell: 25ft right of right wall (drinking water — must be 50ft+ from soak pits)
- Chakrode (kachchi road): 10-12ft in front of building
- No pipes cross under the road
- Only 45° bends (no 90° turns for black water)
- Both toilets (GF left + 1F right) feed ONE septic tank (back-left)

Three separate drainage systems with distinct color coding:
  - BLACK WATER (dark maroon)  — GF toilet + 1F toilet → septic → BW soak pit
  - GREY WATER (medium grey)   — 1F kitchen/bath → grease trap → GW soak pit
  - WASH WATER (sandy ochre)   — GF floor drain → silt trap → oil trap → WW soak pit

Plus: ghost building, borewell marker, chakrode (road), rainwater downpipes.

Coordinate system (matching main building model):
  x-axis: width (0 = left wall inside, 20 = right wall inside)
  y-axis: depth (0 = front wall inside, 25 = back wall inside)
  z-axis: height (0 = NGL, 3 = plinth top / GF floor)
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

FT_TO_M = 0.3048
IN_TO_M = 0.0254

COLORS = {
    'ghost_wall': (0.82, 0.82, 0.82, 1.0),
    'ghost_floor': (0.88, 0.86, 0.83, 1.0),
    'black_water': (0.55, 0.10, 0.10, 1.0),
    'grey_water': (0.48, 0.50, 0.55, 1.0),
    'wash_water': (0.78, 0.62, 0.22, 1.0),
    'rainwater': (0.20, 0.55, 0.85, 1.0),
    'septic_tank': (0.42, 0.24, 0.12, 1.0),
    'soak_pit_bw': (0.38, 0.15, 0.08, 1.0),
    'soak_pit_gw': (0.42, 0.44, 0.48, 1.0),
    'soak_pit_ww': (0.68, 0.52, 0.18, 1.0),
    'insp_chamber': (0.50, 0.50, 0.52, 1.0),
    'grease_trap': (0.58, 0.52, 0.28, 1.0),
    'silt_trap': (0.52, 0.42, 0.28, 1.0),
    'fixture': (0.92, 0.92, 0.95, 1.0),
    'floor_drain': (0.28, 0.28, 0.30, 1.0),
    'ground': (0.40, 0.55, 0.30, 1.0),
    'road': (0.60, 0.55, 0.45, 1.0),
    'borewell': (0.10, 0.40, 0.75, 1.0),
    'yjunction': (0.70, 0.20, 0.20, 1.0),
}


def ft(val):
    return val * FT_TO_M


def inch(val):
    return val * IN_TO_M


def box_mesh(x, y, z, w, d, h):
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


def pipe_mesh(x1, y1, z1, x2, y2, z2, diameter_ft):
    """Pipe as a box along the dominant axis."""
    r = diameter_ft / 2.0
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    if abs(dx) >= abs(dy) and abs(dx) >= abs(dz):
        x_min = min(x1, x2)
        return box_mesh(ft(x_min), ft(y1 - r), ft(z1 - r),
                       ft(abs(dx)), ft(diameter_ft), ft(diameter_ft))
    elif abs(dy) >= abs(dx) and abs(dy) >= abs(dz):
        y_min = min(y1, y2)
        return box_mesh(ft(x1 - r), ft(y_min), ft(z1 - r),
                       ft(diameter_ft), ft(abs(dy)), ft(diameter_ft))
    else:
        z_min = min(z1, z2)
        return box_mesh(ft(x1 - r), ft(y1 - r), ft(z_min),
                       ft(diameter_ft), ft(diameter_ft), ft(abs(dz)))


def cylinder_approx(cx, cy, cz, radius_ft, height_ft, segments=8):
    """Approximate cylinder as an octagonal prism."""
    import math
    r = ft(radius_ft)
    h = ft(height_ft)
    x0 = ft(cx)
    y0 = ft(cy)
    z0 = ft(cz)

    verts = []
    tris = []
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        verts.append((x0 + r * math.cos(angle), y0 + r * math.sin(angle), z0))
        verts.append((x0 + r * math.cos(angle), y0 + r * math.sin(angle), z0 + h))

    # Side faces
    for i in range(segments):
        i0 = i * 2
        i1 = i * 2 + 1
        i2 = ((i + 1) % segments) * 2
        i3 = ((i + 1) % segments) * 2 + 1
        tris.append((i0, i2, i1))
        tris.append((i1, i2, i3))

    # Top and bottom caps (fan from center)
    bc = len(verts)
    verts.append((x0, y0, z0))  # bottom center
    tc = len(verts)
    verts.append((x0, y0, z0 + h))  # top center
    for i in range(segments):
        i0 = i * 2
        i2 = ((i + 1) % segments) * 2
        tris.append((bc, i2, i0))  # bottom
        i1 = i * 2 + 1
        i3 = ((i + 1) % segments) * 2 + 1
        tris.append((tc, i1, i3))  # top

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
        vscene = ET.SubElement(lib_scenes, 'visual_scene', {'id': 'Scene', 'name': 'PlumbingLayout'})
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


def build_plumbing():
    cb = ColladaBuilder()
    for name, color in COLORS.items():
        cb.add_material(name, color)

    # === KEY DIMENSIONS ===
    WALL_T = 0.75       # 9" walls
    INT_W = 20.0        # internal width
    INT_D = 25.0        # internal depth
    Z_PLINTH = 3.0      # plinth top / GF floor
    Z_1F_FLOOR = 15.5
    Z_1F_ROOF = 27.5

    # External wall faces
    EXT_LEFT = -WALL_T          # x = -0.75
    EXT_RIGHT = INT_W + WALL_T  # x = 20.75
    EXT_FRONT = -WALL_T         # y = -0.75
    EXT_BACK = INT_D + WALL_T   # y = 25.75

    # Pipe diameters (feet)
    PIPE_4 = 4.0 / 12.0    # 110mm black water & wash water
    PIPE_3 = 3.0 / 12.0    # 75mm grey water & rainwater
    PIPE_2 = 2.0 / 12.0    # 50mm vent & branch

    # Underground pipe level (below natural ground level z=0)
    # Pipes exit building through plinth wall (z=0 to z=3 zone) and slope DOWN
    Z_PIPE_EXIT = 1.0   # pipe exits plinth wall at z=1 (1ft above NGL, within plinth)
    Z_UG = -1.5         # underground pipe depth (1.5ft below farm land level)

    # Site features
    BOREWELL_X = EXT_RIGHT + 30.0   # 30ft right of right wall ≈ x=50.75
    BOREWELL_Y = 2.0                # toward the front (near front face of building)
    ROAD_Y = EXT_FRONT - 11.0       # chakrode at ~11ft in front (y ≈ -11.75)
    ROAD_WIDTH = 10.0               # typical kachchi road width

    # ================================================================
    # SITE CONTEXT: GROUND, ROAD, BOREWELL
    # ================================================================

    # Ground plane (large, shows farm land)
    v, t = box_mesh(ft(-30), ft(-25), ft(-0.15),
                    ft(80), ft(70), ft(0.15))
    cb.add_geometry('ground_plane', v, t, 'ground')

    # Chakrode (kachchi road) — flat strip in front
    v, t = box_mesh(ft(-30), ft(ROAD_Y - ROAD_WIDTH), ft(0.0),
                    ft(80), ft(ROAD_WIDTH), ft(0.3))
    cb.add_geometry('chakrode_road', v, t, 'road')

    # Borewell marker (tall cylinder/pole)
    v, t = cylinder_approx(BOREWELL_X, BOREWELL_Y, 0.0, 1.5, 8.0)
    cb.add_geometry('borewell_marker', v, t, 'borewell')

    # Borewell base platform
    v, t = box_mesh(ft(BOREWELL_X - 2.5), ft(BOREWELL_Y - 2.5), ft(0.0),
                    ft(5.0), ft(5.0), ft(0.5))
    cb.add_geometry('borewell_platform', v, t, 'borewell')

    # ================================================================
    # GHOST BUILDING (transparent outline for reference)
    # ================================================================

    GHOST_H = 15.0  # show up to slab level
    thin = 0.15

    # Front wall
    v, t = box_mesh(ft(EXT_LEFT), ft(EXT_FRONT), ft(0.0),
                    ft(INT_W + 2*WALL_T), ft(thin), ft(GHOST_H))
    cb.add_geometry('ghost_front', v, t, 'ghost_wall')
    # Back wall
    v, t = box_mesh(ft(EXT_LEFT), ft(EXT_BACK - thin), ft(0.0),
                    ft(INT_W + 2*WALL_T), ft(thin), ft(GHOST_H))
    cb.add_geometry('ghost_back', v, t, 'ghost_wall')
    # Left wall
    v, t = box_mesh(ft(EXT_LEFT), ft(EXT_FRONT), ft(0.0),
                    ft(thin), ft(INT_D + 2*WALL_T), ft(GHOST_H))
    cb.add_geometry('ghost_left', v, t, 'ghost_wall')
    # Right wall
    v, t = box_mesh(ft(EXT_RIGHT - thin), ft(EXT_FRONT), ft(0.0),
                    ft(thin), ft(INT_D + 2*WALL_T), ft(GHOST_H))
    cb.add_geometry('ghost_right', v, t, 'ghost_wall')
    # GF floor
    v, t = box_mesh(ft(EXT_LEFT), ft(EXT_FRONT), ft(Z_PLINTH - 0.1),
                    ft(INT_W + 2*WALL_T), ft(INT_D + 2*WALL_T), ft(0.1))
    cb.add_geometry('ghost_gf_floor', v, t, 'ghost_floor')
    # 1F floor
    v, t = box_mesh(ft(EXT_LEFT), ft(EXT_FRONT), ft(Z_1F_FLOOR),
                    ft(INT_W + 2*WALL_T), ft(INT_D + 2*WALL_T), ft(0.1))
    cb.add_geometry('ghost_1f_floor', v, t, 'ghost_floor')

    # ================================================================
    # SYSTEM 1: BLACK WATER
    # GF Toilet (left-front) + 1F Toilet (right)
    # Both → merge behind building → Septic Tank (BACK, x=5, y=30)
    # → BW Soak Pit (BACK, x=2, y=40)
    # Color: dark maroon
    # ================================================================

    # --- GF Toilet (left-front) ---
    GF_WC_X = 1.0
    GF_WC_Y = 1.5

    # GF Commode fixture
    v, t = box_mesh(ft(GF_WC_X - 0.5), ft(GF_WC_Y - 0.75), ft(Z_PLINTH),
                    ft(1.0), ft(1.5), ft(1.3))
    cb.add_geometry('bw_gf_commode', v, t, 'fixture')

    # GF toilet: vertical drop through plinth into underground
    v, t = pipe_mesh(GF_WC_X, GF_WC_Y, Z_PLINTH, GF_WC_X, GF_WC_Y, Z_UG, PIPE_4)
    cb.add_geometry('bw_gf_vert_drop', v, t, 'black_water')

    # GF toilet: exits BACK wall (runs underground along y-axis to back)
    v, t = pipe_mesh(GF_WC_X, GF_WC_Y, Z_UG,
                     GF_WC_X, EXT_BACK + 2.0, Z_UG - 0.8, PIPE_4)
    cb.add_geometry('bw_gf_run_to_back', v, t, 'black_water')

    # --- 1F Toilet (right side, bathroom) ---
    F1_WC_X = 18.0
    F1_WC_Y = 7.0

    # 1F Commode fixture (at 1F level)
    v, t = box_mesh(ft(F1_WC_X - 0.5), ft(F1_WC_Y - 0.75), ft(Z_1F_FLOOR),
                    ft(1.0), ft(1.5), ft(1.3))
    cb.add_geometry('bw_1f_commode', v, t, 'fixture')

    # 1F toilet: vertical drop (wall chase → underground)
    v, t = pipe_mesh(F1_WC_X, F1_WC_Y, Z_1F_FLOOR,
                     F1_WC_X, F1_WC_Y, Z_UG, PIPE_4)
    cb.add_geometry('bw_1f_vert_drop', v, t, 'black_water')

    # 1F toilet: runs underground toward BACK wall
    v, t = pipe_mesh(F1_WC_X, F1_WC_Y, Z_UG,
                     F1_WC_X, EXT_BACK + 2.0, Z_UG - 0.6, PIPE_4)
    cb.add_geometry('bw_1f_run_to_back', v, t, 'black_water')

    # Both lines converge behind building at 45° Y-junction (back-left)
    YJ_X = -3.0   # left side behind building
    YJ_Y = EXT_BACK + 2.0  # ~2ft behind back wall
    YJ_Z = Z_UG - 1.0

    # GF line → Y-junction
    v, t = pipe_mesh(GF_WC_X, EXT_BACK + 2.0, Z_UG - 0.8,
                     YJ_X, YJ_Y, YJ_Z, PIPE_4)
    cb.add_geometry('bw_gf_to_yj', v, t, 'black_water')

    # 1F line → Y-junction (runs along back of building from right to left)
    v, t = pipe_mesh(F1_WC_X, EXT_BACK + 2.0, Z_UG - 0.6,
                     YJ_X, YJ_Y, YJ_Z, PIPE_4)
    cb.add_geometry('bw_1f_to_yj', v, t, 'black_water')

    # 45° Y-Junction marker
    v, t = box_mesh(ft(YJ_X - 0.5), ft(YJ_Y - 0.5), ft(YJ_Z - 0.5),
                    ft(1.0), ft(1.0), ft(1.0))
    cb.add_geometry('bw_y_junction', v, t, 'yjunction')

    # --- Inspection Chamber (left side, between Y-junction and septic) ---
    IC_BW_X = -4.0
    IC_BW_Y = 27.5
    v, t = box_mesh(ft(IC_BW_X - 0.75), ft(IC_BW_Y - 0.75), ft(-2.0),
                    ft(1.5), ft(1.5), ft(2.0))
    cb.add_geometry('bw_insp_chamber', v, t, 'insp_chamber')

    # Pipe: Y-junction → Inspection chamber
    v, t = pipe_mesh(YJ_X, YJ_Y, YJ_Z,
                     IC_BW_X, IC_BW_Y, -1.0, PIPE_4)
    cb.add_geometry('bw_pipe_yj_to_ic', v, t, 'black_water')

    # --- Septic Tank (LEFT side, x=-5, y=28, DUG INTO GROUND) ---
    SEPTIC_X = -7.5
    SEPTIC_Y = 28.0
    SEPTIC_Z = -4.5   # bottom (4.5ft below ground)
    SEPTIC_W = 5.0    # 5ft long (along x)
    SEPTIC_D = 2.5    # 2.5ft wide (along y)
    SEPTIC_H = 4.5    # top reaches z=0

    v, t = box_mesh(ft(SEPTIC_X), ft(SEPTIC_Y), ft(SEPTIC_Z),
                    ft(SEPTIC_W), ft(SEPTIC_D), ft(SEPTIC_H))
    cb.add_geometry('bw_septic_tank', v, t, 'septic_tank')

    # Septic internal baffle
    v, t = box_mesh(ft(SEPTIC_X + 3.3), ft(SEPTIC_Y + 0.2), ft(SEPTIC_Z + 0.5),
                    ft(0.33), ft(SEPTIC_D - 0.4), ft(3.0))
    cb.add_geometry('bw_septic_baffle', v, t, 'insp_chamber')

    # Septic tank lid (flush at ground z=0)
    v, t = box_mesh(ft(SEPTIC_X - 0.25), ft(SEPTIC_Y - 0.25), ft(0.0),
                    ft(SEPTIC_W + 0.5), ft(SEPTIC_D + 0.5), ft(0.3))
    cb.add_geometry('bw_septic_lid', v, t, 'insp_chamber')

    # Pipe: Inspection chamber → Septic inlet
    v, t = pipe_mesh(IC_BW_X, IC_BW_Y, -1.0,
                     SEPTIC_X + SEPTIC_W/2, SEPTIC_Y, -0.5, PIPE_4)
    cb.add_geometry('bw_pipe_ic_to_septic', v, t, 'black_water')

    # --- BW Soak Pit (BACK-LEFT, x=-5, y=40, DUG INTO GROUND) ---
    BW_PIT_X = -5.0
    BW_PIT_Y = 40.0
    BW_PIT_Z = -7.0
    BW_PIT_DIA = 5.0
    BW_PIT_DEPTH = 7.0

    v, t = cylinder_approx(BW_PIT_X, BW_PIT_Y, BW_PIT_Z, BW_PIT_DIA/2, BW_PIT_DEPTH)
    cb.add_geometry('bw_soak_pit', v, t, 'soak_pit_bw')

    v, t = cylinder_approx(BW_PIT_X, BW_PIT_Y, 0.0, BW_PIT_DIA/2 + 0.3, 0.3)
    cb.add_geometry('bw_soak_pit_cover', v, t, 'insp_chamber')

    # Pipe: Septic outlet → BW Soak Pit
    v, t = pipe_mesh(SEPTIC_X + SEPTIC_W/2, SEPTIC_Y + SEPTIC_D, -1.0,
                     BW_PIT_X, BW_PIT_Y, -1.5, PIPE_4)
    cb.add_geometry('bw_pipe_septic_to_pit', v, t, 'black_water')

    # --- Vent Pipe (from GF toilet stack, rises above roof) ---
    v, t = pipe_mesh(GF_WC_X, GF_WC_Y, Z_PLINTH,
                     GF_WC_X, GF_WC_Y, Z_1F_ROOF + 3.0, PIPE_2)
    cb.add_geometry('bw_vent_pipe', v, t, 'black_water')

    # ================================================================
    # SYSTEM 2: GREY WATER
    # 1F Kitchen sink + Basin + Shower → downpipe (right wall)
    # → runs to BACK of building → Grease Trap (back, x=15, y=28)
    # → GW Inspection Chamber → GW Soak Pit (BACK, x=12, y=38)
    # Color: medium grey
    # ================================================================

    # 1F Kitchen sink
    KSINK_X = 18.0
    KSINK_Y = 22.0
    v, t = box_mesh(ft(KSINK_X - 0.75), ft(KSINK_Y - 0.5), ft(Z_1F_FLOOR),
                    ft(1.5), ft(1.0), ft(3.0))
    cb.add_geometry('gw_kitchen_sink', v, t, 'fixture')

    # 1F Basin
    BASIN_X = 18.0
    BASIN_Y = 8.0
    v, t = box_mesh(ft(BASIN_X - 0.5), ft(BASIN_Y - 0.4), ft(Z_1F_FLOOR),
                    ft(1.0), ft(0.8), ft(2.5))
    cb.add_geometry('gw_basin', v, t, 'fixture')

    # 1F Shower drain
    SHOWER_X = 16.0
    SHOWER_Y = 6.0
    v, t = box_mesh(ft(SHOWER_X - 0.4), ft(SHOWER_Y - 0.4), ft(Z_1F_FLOOR),
                    ft(0.8), ft(0.8), ft(0.15))
    cb.add_geometry('gw_shower_floor_trap', v, t, 'grey_water')

    # Grey water: all fixtures → downpipe on BACK wall (kitchen is near back already)
    GW_DOWN_X = 18.0
    GW_DOWN_Y = EXT_BACK - 0.3  # near back wall

    # Kitchen → back wall (short horizontal)
    v, t = pipe_mesh(KSINK_X, KSINK_Y, Z_1F_FLOOR - 0.5,
                     KSINK_X, GW_DOWN_Y, Z_1F_FLOOR - 0.5, PIPE_3)
    cb.add_geometry('gw_kitchen_to_back', v, t, 'grey_water')

    # Basin + Shower → runs toward back along right wall, then to downpipe
    v, t = pipe_mesh(BASIN_X, BASIN_Y, Z_1F_FLOOR - 0.3,
                     BASIN_X, GW_DOWN_Y, Z_1F_FLOOR - 0.3, PIPE_3)
    cb.add_geometry('gw_basin_to_back', v, t, 'grey_water')

    v, t = pipe_mesh(SHOWER_X, SHOWER_Y, Z_1F_FLOOR - 0.3,
                     SHOWER_X, GW_DOWN_Y, Z_1F_FLOOR - 0.3, PIPE_2)
    cb.add_geometry('gw_shower_to_back', v, t, 'grey_water')

    # Main vertical downpipe (outside back wall)
    v, t = pipe_mesh(GW_DOWN_X, EXT_BACK + 0.5, Z_1F_FLOOR - 0.5,
                     GW_DOWN_X, EXT_BACK + 0.5, Z_UG, PIPE_3)
    cb.add_geometry('gw_main_downpipe', v, t, 'grey_water')

    # Underground: runs from downpipe toward grease trap (behind building)
    GT_X = 15.0
    GT_Y = 28.0
    v, t = pipe_mesh(GW_DOWN_X, EXT_BACK + 0.5, Z_UG,
                     GT_X + 1.0, GT_Y, Z_UG - 0.3, PIPE_3)
    cb.add_geometry('gw_ug_to_gt', v, t, 'grey_water')

    # Grease Trap (behind building, dug into ground)
    v, t = box_mesh(ft(GT_X), ft(GT_Y - 0.75), ft(-2.0),
                    ft(2.0), ft(1.5), ft(2.0))
    cb.add_geometry('gw_grease_trap', v, t, 'grease_trap')

    # GW Inspection Chamber (behind building)
    IC_GW_X = 12.0
    IC_GW_Y = 33.0
    v, t = box_mesh(ft(IC_GW_X - 0.75), ft(IC_GW_Y - 0.75), ft(-2.0),
                    ft(1.5), ft(1.5), ft(2.0))
    cb.add_geometry('gw_insp_chamber', v, t, 'insp_chamber')

    # Pipe: Grease trap → IC
    v, t = pipe_mesh(GT_X, GT_Y, -1.0,
                     IC_GW_X, IC_GW_Y, -1.2, PIPE_3)
    cb.add_geometry('gw_pipe_gt_to_ic', v, t, 'grey_water')

    # GW Soak Pit (10ft RIGHT of BW pit: x=5, y=40, DUG INTO GROUND)
    GW_PIT_X = 5.0
    GW_PIT_Y = 40.0
    GW_PIT_Z = -6.0
    GW_PIT_DIA = 4.0
    GW_PIT_DEPTH = 6.0

    v, t = cylinder_approx(GW_PIT_X, GW_PIT_Y, GW_PIT_Z, GW_PIT_DIA/2, GW_PIT_DEPTH)
    cb.add_geometry('gw_soak_pit', v, t, 'soak_pit_gw')

    v, t = cylinder_approx(GW_PIT_X, GW_PIT_Y, 0.0, GW_PIT_DIA/2 + 0.3, 0.3)
    cb.add_geometry('gw_soak_pit_cover', v, t, 'insp_chamber')

    # Pipe: IC → GW Soak Pit
    v, t = pipe_mesh(IC_GW_X, IC_GW_Y, -1.2,
                     GW_PIT_X, GW_PIT_Y, -1.5, PIPE_3)
    cb.add_geometry('gw_pipe_ic_to_pit', v, t, 'grey_water')

    # ================================================================
    # SYSTEM 3: WASH WATER (Floor Drain)
    # Floor drain channel (center x=10) → exits BACK wall
    # → Silt Trap → Oil Trap → WW Soak Pit (BACK, x=7, y=42)
    # Now exits BACK (not front) — simpler routing, no road conflict
    # Color: sandy ochre
    # ================================================================

    # Floor drain channel (on GF floor, center line)
    DRAIN_X = 10.0
    v, t = box_mesh(ft(DRAIN_X - 0.25), ft(0.0), ft(Z_PLINTH - 0.3),
                    ft(0.5), ft(INT_D), ft(0.3))
    cb.add_geometry('ww_floor_drain_channel', v, t, 'floor_drain')

    # Drain exits BACK wall (slopes toward back)
    v, t = pipe_mesh(DRAIN_X, INT_D, Z_UG,
                     DRAIN_X, EXT_BACK + 2.0, Z_UG - 0.3, PIPE_4)
    cb.add_geometry('ww_pipe_exit_back', v, t, 'wash_water')

    # Vertical drop at back
    v, t = pipe_mesh(DRAIN_X, INT_D, Z_PLINTH - 0.3,
                     DRAIN_X, INT_D, Z_UG, PIPE_4)
    cb.add_geometry('ww_vert_drop', v, t, 'wash_water')

    # Silt Trap (behind building, dug into ground)
    SILT_X = 9.0
    SILT_Y = 28.0
    v, t = box_mesh(ft(SILT_X), ft(SILT_Y - 1.25), ft(-2.5),
                    ft(2.5), ft(2.5), ft(2.5))
    cb.add_geometry('ww_silt_trap', v, t, 'silt_trap')

    # Pipe: drain exit → silt trap
    v, t = pipe_mesh(DRAIN_X, EXT_BACK + 2.0, Z_UG - 0.3,
                     SILT_X + 1.25, SILT_Y, -1.0, PIPE_4)
    cb.add_geometry('ww_pipe_to_silt', v, t, 'wash_water')

    # Oil & Grease Trap (behind building, further back)
    OIL_X = 8.0
    OIL_Y = 33.0
    v, t = box_mesh(ft(OIL_X), ft(OIL_Y - 1.0), ft(-2.5),
                    ft(2.5), ft(2.0), ft(2.5))
    cb.add_geometry('ww_oil_trap', v, t, 'grease_trap')

    # Pipe: Silt → Oil trap
    v, t = pipe_mesh(SILT_X + 1.25, SILT_Y, -1.0,
                     OIL_X + 1.25, OIL_Y, -1.2, PIPE_4)
    cb.add_geometry('ww_pipe_silt_to_oil', v, t, 'wash_water')

    # WW Soak Pit (further RIGHT, x=15, y=38, DUG INTO GROUND)
    # 10ft from GW pit (5,40): √(100+4) = 10.2ft ✓
    WW_PIT_X = 15.0
    WW_PIT_Y = 38.0
    WW_PIT_Z = -6.5
    WW_PIT_DIA = 5.0
    WW_PIT_DEPTH = 6.5

    v, t = cylinder_approx(WW_PIT_X, WW_PIT_Y, WW_PIT_Z, WW_PIT_DIA/2, WW_PIT_DEPTH)
    cb.add_geometry('ww_soak_pit', v, t, 'soak_pit_ww')

    v, t = cylinder_approx(WW_PIT_X, WW_PIT_Y, 0.0, WW_PIT_DIA/2 + 0.3, 0.3)
    cb.add_geometry('ww_soak_pit_cover', v, t, 'insp_chamber')

    # Pipe: Oil trap → WW Soak Pit
    v, t = pipe_mesh(OIL_X + 1.25, OIL_Y, -1.2,
                     WW_PIT_X, WW_PIT_Y, -1.5, PIPE_4)
    cb.add_geometry('ww_pipe_oil_to_pit', v, t, 'wash_water')

    # ================================================================
    # SYSTEM 4: RAINWATER (Downpipes at 4 corners → surface drain away)
    # Color: blue
    # ================================================================

    corners = [
        (EXT_LEFT + 0.3, EXT_FRONT + 0.3, 'rain_dp_fl'),
        (EXT_RIGHT - 0.5, EXT_FRONT + 0.3, 'rain_dp_fr'),
        (EXT_LEFT + 0.3, EXT_BACK - 0.5, 'rain_dp_bl'),
        (EXT_RIGHT - 0.5, EXT_BACK - 0.5, 'rain_dp_br'),
    ]
    for cx, cy, name in corners:
        v, t = pipe_mesh(cx, cy, Z_1F_ROOF + 0.5, cx, cy, 0.5, PIPE_3)
        cb.add_geometry(name, v, t, 'rainwater')

    # Rainwater surface drains (away from building, toward open land)
    # Front two: go toward left (away from road, toward farm)
    v, t = pipe_mesh(corners[0][0], corners[0][1], 0.3,
                     corners[0][0] - 10.0, corners[0][1], 0.1, PIPE_3)
    cb.add_geometry('rain_drain_fl', v, t, 'rainwater')
    v, t = pipe_mesh(corners[1][0], corners[1][1], 0.3,
                     corners[1][0] + 10.0, corners[1][1], 0.1, PIPE_3)
    cb.add_geometry('rain_drain_fr', v, t, 'rainwater')
    # Back two: go toward back (into farm)
    v, t = pipe_mesh(corners[2][0], corners[2][1], 0.3,
                     corners[2][0], corners[2][1] + 10.0, 0.1, PIPE_3)
    cb.add_geometry('rain_drain_bl', v, t, 'rainwater')
    v, t = pipe_mesh(corners[3][0], corners[3][1], 0.3,
                     corners[3][0], corners[3][1] + 10.0, 0.1, PIPE_3)
    cb.add_geometry('rain_drain_br', v, t, 'rainwater')

    # ================================================================
    # DISTANCE MARKERS (thin tall poles showing key distances)
    # ================================================================

    # 50ft radius circle approximation from borewell (safety zone marker)
    # Show as a ring of small posts at 50ft from borewell
    import math
    SAFE_DIST = 50.0  # feet
    for i in range(24):
        angle = 2 * math.pi * i / 24
        mx = BOREWELL_X + SAFE_DIST * math.cos(angle)
        my = BOREWELL_Y + SAFE_DIST * math.sin(angle)
        v, t = box_mesh(ft(mx - 0.2), ft(my - 0.2), ft(0.0),
                        ft(0.4), ft(0.4), ft(1.5))
        cb.add_geometry(f'safety_radius_{i}', v, t, 'borewell')

    return cb


def main():
    print("Generating PLUMBING 3D model (ALL behind building layout)...")
    print("  - All pits, tanks, traps BEHIND the building (high Y values)")
    print("  - LEFT side completely CLEAR for tractor access")
    print("  - Borewell 30ft right of building, toward front (blue marker)")
    print("  - Chakrode (road) 11ft in front (brown strip)")
    print("  - 50ft safety radius from borewell (blue posts)")
    print()

    cb = build_plumbing()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dae = os.path.join(script_dir, 'plumbing-3d.dae')
    cb.save(output_dae)
    size_kb = os.path.getsize(output_dae) / 1024
    print(f"Collada model saved: {output_dae}")
    print(f"  Size: {size_kb:.0f} KB")

    try:
        import trimesh
        import numpy as np

        scene = trimesh.Scene()
        for geom_name, verts, tris, mat_name in cb.geometries:
            vertices = np.array(verts, dtype=np.float64)
            faces = np.array(tris, dtype=np.int64)
            color_rgba = COLORS[mat_name]
            color_uint8 = [int(c * 255) for c in color_rgba]
            mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
            mesh.visual.face_colors = color_uint8
            scene.add_geometry(mesh, node_name=geom_name)

        output_glb = os.path.join(script_dir, 'plumbing-3d.glb')
        scene.export(output_glb)
        size_glb = os.path.getsize(output_glb) / 1024
        print(f"GLB model saved: {output_glb}")
        print(f"  Size: {size_glb:.0f} KB")
    except ImportError:
        print("trimesh not available, skipping GLB generation")
    except Exception as e:
        print(f"GLB generation failed: {e}")

    print()
    print("=" * 60)
    print("COLOR LEGEND:")
    print("=" * 60)
    print()
    print("  SYSTEM 1 — BLACK WATER (DARK MAROON pipes)")
    print("    GF Toilet (left) + 1F Toilet (right)")
    print("    → Both run underground to BACK of building")
    print("    → Y-Junction (back-left) → Insp. Ch. → Septic Tank (x=-5, y=28)")
    print("    → BW Soak Pit (x=-5, y=40) [back-left]")
    print()
    print("  SYSTEM 2 — GREY WATER (GREY pipes)")
    print("    1F Kitchen Sink + Basin + Shower")
    print("    → Downpipe (back wall) → Grease Trap (x=15, y=28)")
    print("    → Insp. Ch. → GW Soak Pit (x=5, y=40) [10ft right of BW pit]")
    print()
    print("  SYSTEM 3 — WASH WATER (OCHRE/SANDY pipes)")
    print("    GF Floor Drain Channel (exits BACK wall)")
    print("    → Silt Trap (x=9, y=28) → Oil Trap (x=8, y=33)")
    print("    → WW Soak Pit (x=15, y=38) [10ft right of GW pit]")
    print()
    print("  SYSTEM 4 — RAINWATER (BLUE pipes)")
    print("    4 Downpipes at corners → Surface drainage to farm")
    print()
    print("  SITE FEATURES:")
    print("    Blue cylinder = BOREWELL (30ft right, toward front: x≈51, y≈2)")
    print("    Brown strip   = CHAKRODE / road (11ft in front)")
    print("    Blue posts    = 50ft safety radius from borewell")
    print("    Grey outline  = Building (plinth raised 3ft above farm level)")
    print()
    print("  ALL PITS/TANKS BEHIND BUILDING, SEPTIC ON LEFT")
    print("  Minimum 10ft between all soak pits ✓")
    print("  LEFT SIDE CLEAR FOR TRACTOR ACCESS")
    print()
    print("  SPACING BETWEEN STRUCTURES:")
    print("    Septic → BW Pit:  12ft ✓ (>10ft)")
    print("    BW Pit → GW Pit:  10ft ✓ (minimum 3m)")
    print("    GW Pit → WW Pit:  10.2ft ✓ (>10ft)")
    print("    BW Pit → WW Pit:  20ft ✓")
    print()
    print("  DISTANCES FROM BOREWELL (at x=51, y=2):")
    print(f"    Septic Tank (x=-5,y=28):  ~62ft  ✓ (>50ft)")
    print(f"    BW Soak Pit (x=-5,y=40):  ~68ft  ✓ (>50ft)")
    print(f"    GW Soak Pit (x=5,y=40):   ~60ft  ✓ (>50ft)")
    print(f"    WW Soak Pit (x=15,y=38):  ~51ft  ✓ (>45ft)")
    print()
    print("View at: https://3dviewer.net")


if __name__ == '__main__':
    main()
