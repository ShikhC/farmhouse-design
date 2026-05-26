#!/usr/bin/env python3
"""
Generate a GLB (binary GLTF) 3D model of the farm storage building.
GLB format embeds colors/materials properly and works in:
- 3dviewer.net
- Sketchfab
- WhatsApp/social media 3D preview
- Any modern 3D viewer

Also fixes the DAE file material binding for color support.
"""

import numpy as np
import trimesh
import os

FT = 0.3048  # feet to meters
IN = 0.0254  # inches to meters

# Building dimensions
WIDTH = 20 * FT
DEPTH = 25 * FT
PLINTH_H = 3 * FT
ROOM_H = 12 * FT
SLAB_T = 6 * IN
WALL_T = 9 * IN
WALL_INT_T = 4.5 * IN
SHADE = 5 * FT
STAIR_W = 7.5 * FT
STAIR_FLIGHT = 3.5 * FT
SHUTTER_W = 10 * FT
SHUTTER_H = 10 * FT
GATE_W = 3 * FT
GATE_H = 7 * FT
RAMP_W = 12 * FT
RAMP_L = 8 * FT

# Colors (RGBA 0-255)
COLORS = {
    'plinth': [184, 134, 66, 255],        # warm terracotta
    'wall': [245, 237, 224, 255],          # cream white
    'wall_int': [235, 222, 200, 255],      # beige
    'column': [74, 74, 85, 255],           # dark concrete
    'beam': [90, 92, 100, 255],            # steel grey
    'slab_floor': [200, 195, 185, 255],    # polished concrete
    'slab_roof': [107, 110, 118, 255],     # slate grey
    'stair': [212, 165, 116, 255],         # sandstone
    'ramp': [200, 168, 112, 255],          # sandy
    'shade': [100, 170, 220, 180],         # sky blue translucent
    'shutter': [45, 48, 56, 255],          # dark charcoal
    'gate': [107, 58, 30, 255],            # mahogany
    'toilet': [125, 212, 200, 255],        # mint teal
    'tank': [52, 152, 219, 255],           # ocean blue
    'first_floor': [160, 200, 230, 100],   # translucent sky
    'lobby': [140, 180, 120, 255],         # sage green
    'ground': [70, 120, 55, 255],          # grass
    'handrail': [120, 120, 130, 255],      # metal grey
}


def colored_box(extents, transform, color):
    """Create a colored box mesh."""
    box = trimesh.creation.box(extents=extents)
    box.apply_transform(transform)
    box.visual.face_colors = color
    return box


def T(x, y, z):
    """Translation matrix."""
    m = np.eye(4)
    m[0, 3] = x
    m[1, 3] = y
    m[2, 3] = z
    return m


def build_model():
    meshes = []

    # Coordinate system: x=width(20ft), y=depth(25ft), z=height
    # Front wall at y=0, back at y=DEPTH
    # Ground at z=0, plinth top at z=PLINTH_H

    # ============ GROUND PLANE ============
    ground = colored_box(
        [WIDTH + 20*FT, DEPTH + 20*FT, 0.05],
        T(WIDTH/2, DEPTH/2, -0.025),
        COLORS['ground']
    )
    meshes.append(ground)

    # ============ PLINTH ============
    plinth = colored_box([WIDTH, DEPTH, PLINTH_H], T(WIDTH/2, DEPTH/2, PLINTH_H/2), COLORS['plinth'])
    meshes.append(plinth)

    # ============ FLOOR SLAB ============
    floor = colored_box([WIDTH, DEPTH, 0.1], T(WIDTH/2, DEPTH/2, PLINTH_H + 0.05), COLORS['slab_floor'])
    meshes.append(floor)

    wz = PLINTH_H + 0.1  # wall base z
    wh = ROOM_H - 0.1     # wall height

    # ============ EXTERNAL WALLS ============
    # Back wall
    meshes.append(colored_box([WIDTH, WALL_T, wh], T(WIDTH/2, DEPTH - WALL_T/2, wz + wh/2), COLORS['wall']))
    # Left wall
    meshes.append(colored_box([WALL_T, DEPTH, wh], T(WALL_T/2, DEPTH/2, wz + wh/2), COLORS['wall']))
    # Right wall
    meshes.append(colored_box([WALL_T, DEPTH, wh], T(WIDTH - WALL_T/2, DEPTH/2, wz + wh/2), COLORS['wall']))

    # Front wall segments
    shutter_x = STAIR_W  # shutter starts at 7.5ft from left
    right_wall_x = STAIR_W + SHUTTER_W  # 17.5ft

    # Above gate (0 to 3ft wide, above 7ft)
    ag_h = wh - GATE_H
    meshes.append(colored_box([GATE_W, WALL_T, ag_h], T(GATE_W/2, WALL_T/2, wz + GATE_H + ag_h/2), COLORS['wall']))

    # Wall between gate and shutter (3ft to 7.5ft = 4.5ft, full height)
    mid_w = STAIR_W - GATE_W
    meshes.append(colored_box([mid_w, WALL_T, wh], T(GATE_W + mid_w/2, WALL_T/2, wz + wh/2), COLORS['wall']))

    # Above shutter (7.5ft to 17.5ft, 2ft high)
    as_h = wh - SHUTTER_H
    meshes.append(colored_box([SHUTTER_W, WALL_T, as_h], T(shutter_x + SHUTTER_W/2, WALL_T/2, wz + SHUTTER_H + as_h/2), COLORS['wall']))

    # Right of shutter (17.5ft to 20ft = 2.5ft, full height)
    rw = WIDTH - right_wall_x
    meshes.append(colored_box([rw, WALL_T, wh], T(right_wall_x + rw/2, WALL_T/2, wz + wh/2), COLORS['wall']))

    # ============ SHUTTER ============
    meshes.append(colored_box([SHUTTER_W, 0.05, SHUTTER_H], T(shutter_x + SHUTTER_W/2, 0.025, wz + SHUTTER_H/2), COLORS['shutter']))

    # ============ GATE ============
    meshes.append(colored_box([GATE_W, 0.05, GATE_H], T(GATE_W/2, 0.025, wz + GATE_H/2), COLORS['gate']))

    # ============ STAIR PARTITION ============
    meshes.append(colored_box([WALL_INT_T, 10*FT, wh], T(STAIR_W - WALL_INT_T/2, WALL_T + 5*FT, wz + wh/2), COLORS['wall_int']))

    # ============ COLUMNS (8, all in walls) ============
    col_w, col_d, col_h = 9*IN, 12*IN, wh
    col_color = COLORS['column']

    # C1: back-left
    meshes.append(colored_box([col_w, col_d, col_h], T(col_w/2, DEPTH - col_d/2, wz + col_h/2), col_color))
    # C2: back-right
    meshes.append(colored_box([col_w, col_d, col_h], T(WIDTH - col_w/2, DEPTH - col_d/2, wz + col_h/2), col_color))
    # C3: left at 9ft from front
    meshes.append(colored_box([col_w, col_d, col_h], T(col_w/2, 9*FT, wz + col_h/2), col_color))
    # C4: right at 9ft from front
    meshes.append(colored_box([col_w, col_d, col_h], T(WIDTH - col_w/2, 9*FT, wz + col_h/2), col_color))
    # C5: front-left
    meshes.append(colored_box([col_w, col_d, col_h], T(col_w/2, col_d/2, wz + col_h/2), col_color))
    # C6: at 7.5ft (stair boundary)
    meshes.append(colored_box([col_w, col_d, col_h], T(STAIR_W - col_w/2, col_d/2, wz + col_h/2), col_color))
    # C7: at 17.5ft (shutter right)
    meshes.append(colored_box([col_w, col_d, col_h], T(right_wall_x + col_w/2, col_d/2, wz + col_h/2), col_color))
    # C8: front-right
    meshes.append(colored_box([col_w, col_d, col_h], T(WIDTH - col_w/2, col_d/2, wz + col_h/2), col_color))

    # ============ BEAMS ============
    roof_z = PLINTH_H + ROOM_H
    deep_h = 20 * IN
    std_h = 15 * IN
    beam_w = 9 * IN

    # Back beam (deep)
    meshes.append(colored_box([WIDTH, beam_w, deep_h], T(WIDTH/2, DEPTH - beam_w/2, roof_z - deep_h/2), COLORS['beam']))
    # Middle beam (deep, at 9ft from front)
    meshes.append(colored_box([WIDTH, beam_w, deep_h], T(WIDTH/2, 9*FT, roof_z - deep_h/2), COLORS['beam']))
    # Front beam (standard)
    meshes.append(colored_box([WIDTH, beam_w, std_h], T(WIDTH/2, beam_w/2, roof_z - std_h/2), COLORS['beam']))
    # Left beam
    meshes.append(colored_box([beam_w, DEPTH, std_h], T(beam_w/2, DEPTH/2, roof_z - std_h/2), COLORS['beam']))
    # Right beam
    meshes.append(colored_box([beam_w, DEPTH, std_h], T(WIDTH - beam_w/2, DEPTH/2, roof_z - std_h/2), COLORS['beam']))

    # ============ ROOF SLAB (with 5ft cantilever at front) ============
    # Slab extends from y=-SHADE to y=DEPTH
    slab_total_depth = DEPTH + SHADE
    meshes.append(colored_box([WIDTH, slab_total_depth, SLAB_T], T(WIDTH/2, DEPTH/2 - SHADE/2, roof_z + SLAB_T/2), COLORS['slab_roof']))

    # Shade highlight (on underside of cantilever)
    meshes.append(colored_box([WIDTH, SHADE, 0.02], T(WIDTH/2, -SHADE/2, roof_z - 0.01), COLORS['shade']))

    # ============ STAIRCASE ============
    lobby_d = 3 * FT
    gap = 0.5 * FT
    tread = 10 * IN
    riser = 7.2 * IN

    # Flight 1 (right side of stair zone, x = STAIR_FLIGHT+gap to STAIR_W)
    f1_x = STAIR_FLIGHT + gap
    for i in range(10):
        step_z = wz + i * riser
        step_y = WALL_T + lobby_d + i * tread
        meshes.append(colored_box(
            [STAIR_FLIGHT, tread, riser],
            T(f1_x + STAIR_FLIGHT/2, step_y + tread/2, step_z + riser/2),
            COLORS['stair']
        ))

    # Landing
    landing_z = wz + 10 * riser
    landing_y = WALL_T + lobby_d + 9 * tread
    meshes.append(colored_box([STAIR_W, 3*FT, riser], T(STAIR_W/2, landing_y + 1.5*FT, landing_z), COLORS['stair']))

    # Flight 2 (left side, x = 0 to STAIR_FLIGHT, coming forward)
    for i in range(10):
        step_z = landing_z + i * riser
        step_y = landing_y + 3*FT - i * tread
        meshes.append(colored_box(
            [STAIR_FLIGHT, tread, riser],
            T(STAIR_FLIGHT/2, step_y - tread/2, step_z + riser/2),
            COLORS['stair']
        ))

    # Handrails (simplified as thin boxes along flights)
    rail_h = 3 * FT
    rail_thick = 0.04
    # Left rail of Flight 1
    f1_len = 10 * tread
    meshes.append(colored_box(
        [rail_thick, f1_len, rail_h],
        T(f1_x, WALL_T + lobby_d + f1_len/2, wz + 5*riser + rail_h/2),
        COLORS['handrail']
    ))
    # Right rail of Flight 1
    meshes.append(colored_box(
        [rail_thick, f1_len, rail_h],
        T(f1_x + STAIR_FLIGHT, WALL_T + lobby_d + f1_len/2, wz + 5*riser + rail_h/2),
        COLORS['handrail']
    ))

    # ============ TOILET (under Flight 2, left side) ============
    toilet_y = WALL_T + lobby_d
    toilet_d = 5 * FT
    toilet_h = 8 * FT
    # Back wall
    meshes.append(colored_box([STAIR_FLIGHT, WALL_INT_T, toilet_h], T(STAIR_FLIGHT/2, toilet_y + toilet_d, wz + toilet_h/2), COLORS['toilet']))
    # Side wall (between toilet and Flight 1)
    meshes.append(colored_box([WALL_INT_T, toilet_d, toilet_h], T(STAIR_FLIGHT + WALL_INT_T/2, toilet_y + toilet_d/2, wz + toilet_h/2), COLORS['toilet']))
    # Front wall (with door implied)
    meshes.append(colored_box([STAIR_FLIGHT, WALL_INT_T, toilet_h], T(STAIR_FLIGHT/2, toilet_y, wz + toilet_h/2), COLORS['toilet']))

    # ============ LOBBY FLOOR ============
    meshes.append(colored_box([STAIR_W, lobby_d, 0.03], T(STAIR_W/2, WALL_T + lobby_d/2, wz + 0.11), COLORS['lobby']))

    # ============ RAMP ============
    # Custom geometry: slopes from z=PLINTH_H at y=0 down to z=0 at y=-RAMP_L
    ramp_verts = np.array([
        # Top surface
        [shutter_x - 1*FT, 0, PLINTH_H],              # top-left
        [shutter_x + SHUTTER_W + 1*FT, 0, PLINTH_H],  # top-right
        [shutter_x + SHUTTER_W + 1*FT, -RAMP_L, 0],   # bottom-right
        [shutter_x - 1*FT, -RAMP_L, 0],               # bottom-left
        # Bottom surface (0.1m below)
        [shutter_x - 1*FT, 0, PLINTH_H - 0.1],
        [shutter_x + SHUTTER_W + 1*FT, 0, PLINTH_H - 0.1],
        [shutter_x + SHUTTER_W + 1*FT, -RAMP_L, -0.1],
        [shutter_x - 1*FT, -RAMP_L, -0.1],
    ])
    ramp_faces = np.array([
        [0, 1, 2], [0, 2, 3],  # top
        [4, 6, 5], [4, 7, 6],  # bottom
        [0, 4, 5], [0, 5, 1],  # front (at building)
        [2, 6, 7], [2, 7, 3],  # back (at ground)
        [0, 3, 7], [0, 7, 4],  # left
        [1, 5, 6], [1, 6, 2],  # right
    ])
    ramp = trimesh.Trimesh(vertices=ramp_verts, faces=ramp_faces)
    ramp.visual.face_colors = COLORS['ramp']
    meshes.append(ramp)

    # ============ GATE STEPS ============
    for i in range(5):
        step_z = PLINTH_H - (i + 1) * (PLINTH_H / 5)
        step_y = -(i + 1) * (10 * IN)
        meshes.append(colored_box(
            [GATE_W, 10*IN, PLINTH_H/5],
            T(GATE_W/2, step_y - 5*IN, step_z + PLINTH_H/10),
            COLORS['stair']
        ))

    # ============ WATER TANK ============
    tank_z = roof_z + SLAB_T + 0.6
    meshes.append(colored_box([1.0, 0.8, 0.8], T(1.0, 1.0, tank_z + 0.4), COLORS['tank']))
    # Stand legs
    for dx, dy in [(0.6, 0.6), (1.4, 0.6), (0.6, 1.4), (1.4, 1.4)]:
        meshes.append(colored_box([0.05, 0.05, 0.6], T(dx, dy, roof_z + SLAB_T + 0.3), COLORS['handrail']))

    # ============ FIRST FLOOR (translucent) ============
    ff_z = roof_z + SLAB_T
    ff_h = 10 * FT
    balcony_d = 9 * FT
    room_d = 16 * FT

    # Room walls
    meshes.append(colored_box([WIDTH, WALL_INT_T, ff_h], T(WIDTH/2, DEPTH - WALL_INT_T/2, ff_z + ff_h/2), COLORS['first_floor']))
    meshes.append(colored_box([WALL_INT_T, room_d, ff_h], T(WALL_INT_T/2, balcony_d + room_d/2, ff_z + ff_h/2), COLORS['first_floor']))
    meshes.append(colored_box([WALL_INT_T, room_d, ff_h], T(WIDTH - WALL_INT_T/2, balcony_d + room_d/2, ff_z + ff_h/2), COLORS['first_floor']))
    # Partition (balcony/room)
    meshes.append(colored_box([WIDTH, WALL_INT_T, ff_h], T(WIDTH/2, balcony_d, ff_z + ff_h/2), COLORS['first_floor']))

    # Balcony railing
    rail_ht = 3.5 * FT
    meshes.append(colored_box([WIDTH, 0.05, rail_ht], T(WIDTH/2, -SHADE, ff_z + rail_ht/2), COLORS['handrail']))
    meshes.append(colored_box([0.05, balcony_d + SHADE, rail_ht], T(0, balcony_d/2 - SHADE/2, ff_z + rail_ht/2), COLORS['handrail']))
    meshes.append(colored_box([0.05, balcony_d + SHADE, rail_ht], T(WIDTH, balcony_d/2 - SHADE/2, ff_z + rail_ht/2), COLORS['handrail']))

    # First floor roof slab
    ff_roof_z = ff_z + ff_h
    meshes.append(colored_box([WIDTH, DEPTH, SLAB_T], T(WIDTH/2, DEPTH/2, ff_roof_z + SLAB_T/2), COLORS['slab_roof']))

    # ============ COMBINE AND EXPORT ============
    scene = trimesh.Scene(meshes)
    return scene


def main():
    print("🏗️  Generating 3D model with colors...")
    scene = build_model()

    base_path = "/Users/schowdhary/codebases/farmhouse_design"

    # Export GLB (binary GLTF — best compatibility, colors embedded)
    glb_path = os.path.join(base_path, "farmhouse-3d-model.glb")
    scene.export(glb_path, file_type='glb')
    glb_size = os.path.getsize(glb_path) / 1024
    print(f"✅ GLB saved: {glb_path} ({glb_size:.0f} KB)")

    # Export GLTF (text-based, for reference)
    gltf_path = os.path.join(base_path, "farmhouse-3d-model.gltf")
    scene.export(gltf_path, file_type='gltf')
    print(f"✅ GLTF saved: {gltf_path}")

    # Also re-export DAE with proper material binding
    dae_path = os.path.join(base_path, "farmhouse-3d-model.dae")
    scene.export(dae_path, file_type='dae')
    dae_size = os.path.getsize(dae_path) / 1024
    print(f"✅ DAE saved (fixed colors): {dae_path} ({dae_size:.0f} KB)")

    print(f"""
📌 Usage:
   • GLB: Upload to 3dviewer.net, Sketchfab, or share on WhatsApp/social media
   • GLTF: Open in any 3D viewer or code editor
   • DAE: Import into SketchUp, Blender, etc.

🎨 All files have colors properly embedded!

🌐 To share:
   • 3dviewer.net: Drag & drop the .glb file
   • Sketchfab: Upload .glb → get shareable link + auto-generated video
   • GitHub: The .glb renders directly in GitHub file viewer!
""")


if __name__ == "__main__":
    main()
