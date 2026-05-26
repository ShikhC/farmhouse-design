# Farm Storage — Complete Design Specification

**Location:** Mithanpur Urf Naimtulla Nagar, Moradabad, Uttar Pradesh, India
**Plot Type:** Agricultural farmland (flood-prone)
**Date:** May 2026

---

## 1. Building Overview

| Parameter | Value |
|-----------|-------|
| Building footprint | 20 ft (W) × 25 ft (D) |
| Plinth height | 3 ft above natural ground |
| Ground floor height | 12 ft (floor to slab) |
| Front shade projection | 5 ft (cantilevered slab) |
| Total covered ground area | 20 ft × 30 ft (incl. shade) |
| Tractor ramp | 12 ft wide × 8 ft long (tractor only, trolley unloads at shutter) |
| External walls | 9" brick |
| Internal walls | 4.5" brick |
| Roof | RCC slab (6" thick) — handles 16ft span + future 2nd floor |

### Height from Natural Ground Level
```
+28 ft ─── First floor roof slab (future)
+15 ft ─── First floor slab / Ground floor ceiling
+ 3 ft ─── Platform level (finished floor)
  0 ft ─── Natural ground level
- 3 ft ─── Foundation bottom
```

---

## 2. Ground Floor Plan

### Layout (viewed from above)

```
                              20 ft
         ←─────────────────────────────────────────→
         
         BACK WALL (20 ft)
         ┌─────────────────────────────────────────┐ ─┐
         │ [V]                                [V]  │  │ ← 2 vents (back, 11ft high)
         │                                         │  │
         │                                         │  │
      [V]│                                         │[V]│ ← vents at 10ft
         │                                         │  │
         │           O P E N   S T O R A G E       │  │
         │                                         │  │
         │           12.5 ft × 25 ft = 312 sq ft    │  │
         │           (clear usable area)           │  │  25 ft
         │                                         │  │
      [V]│                                         │[V]│ ← vents at 10ft
         │                                         │  │
         │  ┌───────┐                              │  │
         │  │       │ Flight 2 (coming forward)    │  │
         │  │  3.5  │ ↓↓↓↓↓↓↓↓↓ (9 treads)       │  │
         │  │       │                              │  │
         │  ├───────┤                              │  │
         │  │LANDING│ (3 ft × 7.5 ft)             │  │
         │  ├───────┤                              │  │
         │  │       │ Flight 1 (going backward)    │  │
         │  │  3.5  │ ↑↑↑↑↑↑↑↑↑ (9 treads)       │  │
         │  │       │                              │  │
         │  ├──┬────┤                              │  │
         │  │WC│    │                              │  │
         │  │  │LOBY│                              │  │
         ├──┴──┴─┬──┼─────────────────────────┬────┤ ─┘
         │ GATE  │DR│    10 ft SHUTTER        │WALL│
         │ 3ft   │  │    (rolling, MS)        │2.5│
         └───────┴──┴─────────────────────────┴────┘
         ←─ 7.5ft ─→ ←──────── 10 ft ─────────→←2.5→

         ┌─────────────────────────────────────────┐
         │         5 ft FRONT SHADE                 │ ← Pure cantilever slab
         │    (sitting area on raised platform)     │   (no columns — completely open)
         └─────────────────────────────────────────┘
         ←──────────────── 20 ft ──────────────────→
         
                    ╔═══════════╗
                    ║   RAMP    ║  12 ft wide
                    ║   8 ft    ║  ~1:2.7 slope
                    ║   long    ║  (3 ft rise)
                    ╚═══════════╝
                    
         ═══════════════════════════════════════════  NATURAL GROUND (0 ft)
```

### Dimension Key (Ground Floor)

| Element | Width | Depth | Position |
|---------|-------|-------|----------|
| Staircase total | 7.5 ft | 10 ft | Front-left corner |
| Flight 1 (lower) | 3.5 ft | 7.5 ft | Left side, going backward |
| Flight 2 (upper) | 3.5 ft | 7.5 ft | Right side, coming forward |
| Half-landing | 7.5 ft | 3 ft | Back end of stair zone |
| Gap between flights | 0.5 ft | — | Between F1 and F2 |
| Toilet (WC) | 3 ft | 5 ft | Under Flight 2, near front |
| Lobby | 3 ft | 3 ft | Between gate, WC, and stair |
| Rolling shutter | 10 ft | — | Front wall, 7.5ft to 17.5ft mark |
| Gate | 3 ft | — | Front wall, 0ft to 3ft mark |
| Storage area | ~12.5 ft | 25 ft | Right portion of building |

---

## 3. Staircase Detail

### Specifications

| Parameter | Value |
|-----------|-------|
| Type | Dog-legged (half-turn) |
| Total rise | 12 ft (144 inches) |
| Riser height | 7.2" (20 risers total) |
| Tread depth | 10" |
| Flight width (clear) | 3 ft 6 in (3.5 ft) |
| Risers per flight | 10 |
| Treads per flight | 9 |
| Run per flight | 7 ft 6 in |
| Landing size | 7.5 ft × 3 ft |
| Waist slab thickness | 5" |
| Handrail height | 3 ft (both sides) |
| Handrail material | MS pipe 1.5" dia |
| Nosing | Anti-slip grooved, 1" projection |

### Section Through Staircase (looking from storage side)

```
    FIRST FLOOR SLAB (+15 ft from ground)
    ═══════════════════════════════════════
              ╱ Flight 2                    │
            ╱   (10 risers)                 │
    ──────╱──── HALF LANDING (+6ft)         │ 12 ft
            ╲                               │ internal
              ╲ Flight 1                    │ height
                ╲ (10 risers)               │
    ═══════════════════════════════════════
    PLATFORM LEVEL (+3 ft from ground)
    
    ▓▓▓▓▓▓▓▓▓ EARTH FILL + PCC ▓▓▓▓▓▓▓▓▓
    
    ═══════════════════════════════════════
    NATURAL GROUND (0 ft)
```

### Toilet Under Stairs

```
    Plan view (toilet detail):
    
    ┌────────────────┐
    │    Flight 2    │  ← stair above (headroom 7-11ft)
    │    overhead    │
    ├────────────────┤
    │                │
    │  ┌──┐         │ 5 ft
    │  │WC│  Basin   │ depth
    │  │  │   □     │
    │  └──┘         │
    │          DOOR→ │
    └────────────────┘
         3 ft wide
    
    - Commode: against back wall
    - Basin: wall-mounted, right side
    - Door: 2 ft wide, opens outward into lobby
    - Ventilation: exhaust fan (6") in wall to outside
    - Floor: anti-skid tiles, sloped to floor drain
    - Minimum headroom at commode: 7 ft ✓
```

---

## 4. Front Elevation

```
    ←───────────────────── 20 ft ─────────────────────→
    
                        PARAPET (3 ft above slab)
    ┌─────────────────────────────────────────────────┐ +18 ft
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    │░░░░░░░░░░░░░░ FIRST FLOOR (future) ░░░░░░░░░░░░│
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    ├────────────────────────────────────┬────────────┤ +15 ft
    │           RCC SLAB                 │  CANTILEVER│
    ├────┬───┬──────────────────────┬────┤←── 5ft ──→│
    │    │   │                      │    │           │
    │    │   │                      │    │    SHADE  │
    │    │   │                      │    │    AREA   │ 12 ft
    │    │   │   10ft × 10ft        │    │           │ height
    │GATE│   │   ROLLING SHUTTER    │    │           │
    │3ft │   │                      │2.5│   [COL]  │
    │    │   │                      │    │           │
    ├────┴───┴──────────────────────┴────┼───────────┤ +3 ft
    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ PLINTH ▓▓▓▓▓▓▓▓▓▓│▓▓▓▓▓▓▓▓▓▓▓│ (3 ft)
    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│▓▓▓▓▓▓▓▓▓▓▓│
    ╠════╗▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╠═══════════╣  0 ft
    ║STPS║              RAMP (~1:2.7)       ║           ║
    ╚════╝                                ╚═══════════╝
    
    NATURAL GROUND LEVEL ═══════════════════════════════
```

---

## 5. Side Elevation (Left Wall — 25 ft)

```
    ←───────────────────── 25 ft ─────────────────────→
    
    ┌─────────────────────────────────────────────────┐ +18 ft
    │░░░░░░░░░░░░ FIRST FLOOR (future) ░░░░░░░░░░░░░░│
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    ├─────────────────────────────────────────────────┤ +15 ft
    │                                                 │
    │    [V]         [LINTEL]           [V]           │
    │    9×12        4ft×3ft            9×12          │ 12 ft
    │    vent      (future window)      vent          │
    │              provision            │              │
    │                                                 │
    ├─────────────────────────────────────────────────┤ +3 ft
    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ PLINTH ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    └─────────────────────────────────────────────────┘  0 ft
    
    FRONT ←                                    → BACK
```

---

## 6. Cross Section (Front to Back)

```
    ←─── 5ft ───→←──────────── 25 ft ────────────────→
    (shade)       (building)
    
    ┌────────────────────────────────────────────────┐ +18 ft (parapet)
    │         │  FIRST FLOOR (future room)  │        │
    │ BALCONY │         16 ft               │        │
    │  5+9ft  │                             │        │
    ├─────────┼─────────────────────────────┼────────┤ +15 ft (slab)
    │    ▼    │                             │        │
    │  SHADE  │      G R O U N D            │        │
    │  5ft    │      F L O O R              │        │
    │ cantil- │      S T O R A G E          │        │ 12 ft
    │  ever   │                             │        │
    │ (pure,  │      (12 ft clear height)   │        │
    │ no col) │                             │        │
    ├─────────┼─────────────────────────────┼────────┤ +3 ft (platform)
    │▓▓▓▓▓▓▓▓│▓▓▓ PLINTH (earth fill) ▓▓▓▓▓│▓▓▓▓▓▓▓│
    ├─────────┼─────────────────────────────┼────────┤  0 ft (ground)
    │  RAMP   │     FOUNDATION              │        │
    │         │     (3ft deep)              │        │
    └─────────┴─────────────────────────────┴────────┘ -3 ft
    
    FRONT                                        BACK
```

---

## 7. Structural Layout

### Column Grid Plan

```
    ←─────────────────── 20 ft ───────────────────→
    
    C1════════════════════════════════════════════C2   ─┐
    │  (left corner)   20ft deep beam    (right corner)│    │
    │               (9"×20", no intermediate cols)     │    │ 16 ft
    │                                              │    │ (back bay)
    │                                              │    │
    C3═════════════════════════════════════════════C4   ─┤ ← Deep beam (9"×20")
    │  (left wall)     20ft deep beam    (right wall)│    │   at 9ft from front
    │              (aligns with 1F room partition)  │    │   ROOM PARTITION ABOVE
    │                                              │    │ 9 ft
    │                                              │    │ (front bay)
    C5──────────────C6──────────────C7────────────C8  ─┘
    │     7.5 ft    │    10 ft      │    2.5 ft   │
    FRONT WALL     (shutter edges)
    
    Front shade: PURE CANTILEVER (no columns)
    5ft slab projection, 6" thick at root tapering to 4" at tip
    
    TOTAL COLUMNS: 8 (all wall-embedded) — NO freestanding columns anywhere
    
    COLUMN SIZE: 9" × 12" (all columns, embedded in walls)
    
    COLUMN POSITIONS:
    - C1: Back-left corner (in back + left wall)
    - C2: Back-right corner (in back + right wall)
    - C3: Left wall at 9ft from front (in left wall)
    - C4: Right wall at 9ft from front (in right wall)
    - C5: Front-left corner (in front + left wall)
    - C6: Front wall at 7.5ft from left (stair/shutter boundary)
    - C7: Front wall at 17.5ft from left (shutter right edge)
    - C8: Front-right corner (in front + right wall)
    
    KEY DESIGN DECISIONS:
    - Back beam (C1-C2): 9"×20" spans full 20ft, no intermediate columns
    - Middle beam (C3-C4): 9"×20" at 9ft from front, aligned with 1F room partition
    - First floor room wall sits DIRECTLY on this beam (ideal load transfer)
    - Slab: 6" throughout (handles 16ft back bay span + future 2nd floor)
    - Clear height under deep beams: 10ft 4in (tractor height ~8ft ✓)
    
    FRONT SHADE: Pure 5ft cantilever slab (no columns needed).
    Slab tapers 6" at root to 4" at tip. Top reinforcement
    anchored 10ft into main slab.
```

### Beam Layout

| Beam | Size | Span | Location |
|------|------|------|----------|
| Plinth beams | 9"×12" | Various | Connecting all columns at +3ft |
| **Back beam (C1-C2)** | **9"×20"** | **20 ft** | **Along back wall, no intermediate columns** |
| **Middle beam (C3-C4)** | **9"×20"** | **20 ft** | **At 9ft from front — aligns with 1F room partition** |
| Side beams (C1-C3) | 9"×15" | 16 ft | Left wall, back to middle |
| Side beams (C3-C5) | 9"×15" | 9 ft | Left wall, middle to front |
| Side beams (C2-C4) | 9"×15" | 16 ft | Right wall, back to middle |
| Side beams (C4-C8) | 9"×15" | 9 ft | Right wall, middle to front |
| Front beam (C5-C6-C7-C8) | 9"×15" | 7.5/10/2.5 ft | Segmented, supports shutter |
| Shutter beam | 9"×15" | 10 ft | Above shutter (C6-C7, 10ft span) |
| Cantilever slab | — | 5 ft | Pure cantilever, 6" root to 4" tip, top bars 10mm @ 5" anchored 10ft |
| Lintels (vents) | 9"×6" | 1.5 ft | Above all vent openings |
| Lintels (future windows) | 9"×9" | 5 ft | At window provision points |

**Slab: 6" thick throughout** (increased from 5" to handle 16ft back bay span).
Clear height under deep beams: 12ft - 20" = 10ft 4in. Rest of ceiling at 12ft - 6" slab = 11ft 6in.

### Foundation Detail

```
    SECTION THROUGH COLUMN FOOTING:
    
         COLUMN 9"×12"
            │  │
    ────────┤  ├──────── Platform (+3ft)
    ▓▓▓▓▓▓▓│  │▓▓▓▓▓▓▓  Earth fill
    ▓▓▓▓▓▓▓│  │▓▓▓▓▓▓▓
    ────────┤  ├──────── Ground level (0ft)
            │  │
            │  │         Column extends
            │  │         to foundation
    ┌───────┴──┴───────┐
    │   FOOTING        │  -2.5ft to -3ft
    │   3ft × 3ft      │
    │   12" thick RCC  │
    ├──────────────────┤
    │   PCC bed (6")   │  -3ft to -3.5ft
    └──────────────────┘
    
    Concrete: M20 (RCC), M15 (PCC bed)
    Steel: Fe500, 12mm bars @ 6" c/c both ways
```

---

## 8. Ventilation Plan

```
    ┌─────────────────────────────────────────┐
    │ [V6]                              [V5]  │  BACK WALL
    │  ↑                                 ↑    │  (11 ft height)
    │  exhaust                      exhaust   │
    │                                         │
    │                                         │
[V4]│                                         │[V2]  SIDE WALLS
    │← intake                      intake →   │     (10 ft height)
    │                                         │
    │                                         │
    │                                         │
[V3]│                                         │[V1]  SIDE WALLS
    │← intake                      intake →   │     (10 ft height)
    │                                         │
    │                                         │
    └─────────┬──┬─────────────────────┬──────┘
              │  │     SHUTTER         │        FRONT
              GATE     (open = intake) 
    
    VENT SIZE: 9" wide × 12" high
    COVER: MS grill (security) + wire mesh (insects)
    
    AIRFLOW PATTERN:
    Hot air rises → exits from back vents (V5, V6) at 11ft
    Fresh air enters → side vents (V1-V4) at 10ft + shutter when open
    Cross-ventilation: Left-to-Right through V3↔V1 and V4↔V2
```

---

## 9. Plumbing & Drainage Layout

```
    ROOF LEVEL:
    ┌──────────┐
    │ 500L     │  ← HDPE tank (Sintex type)
    │ TANK     │    Position: above toilet/stair zone
    │          │    Fed by: submersible pump
    └────┬─────┘
         │ (1/2" CPVC supply pipe, embedded in wall)
         │
    GROUND FLOOR:
    ┌─────────────────────────────────────────┐
    │                                         │
    │                                         │
    │              FLOOR DRAIN                │
    │              (central channel)          │
    │              ═══════════════→ exits at   │
    │                               front     │
    │                              (below     │
    │  ┌────┐                       ramp)     │
    │  │ WC │←── 4" PVC soil pipe             │
    │  │    │         │                       │
    │  │BSNS│←── 2" waste pipe                │
    │  └────┘         │                       │
    │        ─────────┘                       │
    ├─────────────────────────────────────────┤
    │              │                          │
    └──────────────┴──────────────────────────┘
                   │
                   │ 4" PVC underground
                   │ (1:40 min slope)
                   │
                   ▼
              ┌─────────┐
              │ SOAK PIT │  10 ft from building
              │ 4ft dia  │  (back or side)
              │ 6ft deep │
              │ Brick    │
              │ honeycomb│
              └─────────┘
    
    
    EXTERNAL TAP: On right side wall, near front (for cleaning/washing)
    PUMP: Submersible in existing borewell → 1" HDPE pipe → tank
```

### Soak Pit Construction

| Parameter | Value |
|-----------|-------|
| Diameter | 4 ft |
| Depth | 6 ft |
| Wall | Brick honeycomb (gaps for seepage) |
| Cover | RCC slab with inspection opening |
| Distance from building | Minimum 10 ft |
| Distance from water source | Minimum 50 ft |
| Bottom | No floor (open earth for seepage) |
| Fill | Gravel/stone aggregate (bottom 1 ft) |

---

## 10. Future Window Provisions

```
    LEFT WALL (25 ft, inside view):
    
    ┌──────────────────────────────────────────────────┐
    │                                                  │ 12 ft
    │    ┌─LINTEL─┐          ┌─LINTEL─┐               │
    │    │ ▒▒▒▒▒▒ │          │ ▒▒▒▒▒▒ │               │ ← 10 ft (top of window)
    │    │ ▒▒▒▒▒▒ │          │ ▒▒▒▒▒▒ │               │
    │    │ ▒BRICK▒ │          │ ▒BRICK▒ │               │ ← 7 ft (bottom of window)
    │    │ ▒FILL▒▒ │          │ ▒FILL▒▒ │               │   = 3ft from floor (sill)
    │    └────────┘          └────────┘               │
    │    ← 4ft →              ← 4ft →                  │
    │                                                  │
    │   @8ft from front      @18ft from front          │
    └──────────────────────────────────────────────────┘ 0 ft (floor)
    FRONT                                          BACK
    
    WINDOW PROVISION SPECS:
    - Opening size: 4 ft wide × 3 ft high
    - Sill height: 3 ft from floor (7 ft from ground)
    - Lintel: RCC 9"×9", extending 6" beyond opening each side
    - Fill: Standard brickwork (can be knocked out later)
    - Total provisions: 2 per side wall + 1-2 on back wall = 5-6 total
```

---

## 11. First Floor Plan (Future Construction)

```
    ←─── 5ft ───→←──────────────── 20 ft ──────────────────→
    (extension)   (within building footprint)
    
    ┌─────────────┬────────────────────────────────────────┐ ─┐
    │             │                                        │  │
    │             │                                        │  │
    │             │         R O O M                        │  │
    │             │       (20 ft × 16 ft)                  │  │ 16 ft
    │   EXTENDED  │       Living Space                     │  │
    │   BALCONY   │         320 sq ft                      │  │
    │             │                                        │  │
    │  (open      │                                        │  │
    │   terrace)  ├────────────────────────────────────────┤ ─┤
    │             │                                        │  │
    │   20×5 ft   │     COVERED BALCONY / VERANDAH         │  │
    │             │          (20 ft × 9 ft)                │  │ 9 ft
    │   Sheet     │   ┌──────┐                             │  │
    │   roof      │   │STAIR │  RCC slab overhead          │  │
    │   above     │   │WELL  │  (future 2nd floor/solar)   │  │
    │             │   │7.5ft×3ft│                           │  │
    │   Railing   │   └──────┘                             │  │
    │   at edge   │                                        │  │
    └─────────────┴────────────────────────────────────────┘ ─┘
                                 FRONT
    
    STAIR WELL: 7.5 ft × 3 ft opening in slab (with railing around)
    ROOM entry: From balcony into room (door on the partition line)
    RAILING: 3.5 ft high MS pipe railing on balcony + extended area
```

### First Floor Specifications

| Element | Detail |
|---------|--------|
| Room | 20 ft × 16 ft = 320 sq ft enclosed |
| Balcony (within building) | 20 ft × 9 ft, covered by RCC slab |
| Extended terrace | 20 ft × 5 ft, cantilevered, sheet roof above |
| Total first floor area | 600 sq ft (320 enclosed + 280 open) |
| Room height | 10 ft (floor to ceiling) |
| Roof over room | RCC slab 6" (for future 2nd floor / solar) |
| Roof over balcony | Same RCC slab |
| Roof over extension | GI insulated sheet (sandwich panel) |
| Floor | First floor slab = ground floor ceiling (already cast) |
| Walls | 9" external, 4.5" internal (room partition) |

---

## 12. Heat Management (47°C Summer)

### Roof Treatment
1. **White china mosaic** on RCC slab top (reflects ~80% solar radiation)
2. **Waterproofing**: Bitumen felt + china mosaic tiles in white cement
3. **Future**: Solar panels will self-shade the roof when installed

### Wall Treatment
- External plaster finished with **white weatherproof paint** (heat reflective)
- Consider: Cavity wall (double wall with air gap) on west-facing wall if budget allows

### Ventilation Enhancement
- High-level vents create **stack effect** (hot air exits at top)
- Cross-ventilation from side vents
- Shutter + gate allow full airflow when open during working hours

### First Floor Room (future)
- **Double roof**: RCC slab + air gap + secondary sheet (creates insulating air layer)
- **Ceiling**: False ceiling with thermocol/EPS insulation
- **Option**: Spray foam insulation under slab soffit (2" polyurethane foam)

---

## 13. Floor Specification (Ground Floor)

### Layer Build-up (bottom to top)

```
    ┌──────────────────────────────────┐
    │  FINISHED FLOOR (IPS/smooth)     │  ← 1" cement + IPS finish
    ├──────────────────────────────────┤
    │  RCC SLAB WITH WIRE MESH         │  ← 4" M20 concrete
    │  (6mm bars @ 6" × 6" grid)      │     with welded wire mesh
    ├──────────────────────────────────┤
    │  PCC BASE                        │  ← 3" M15 plain concrete
    ├──────────────────────────────────┤
    │  COMPACTED EARTH FILL            │  ← ~30" compacted murum
    │  (in 6" layers, watered)         │     (fills plinth cavity)
    ├──────────────────────────────────┤
    │  NATURAL GROUND                  │
    └──────────────────────────────────┘
```

### Why Wire Mesh Reinforced Floor
- Tractor wheel point loads: ~2-3 tonnes per wheel
- Wire mesh distributes load, prevents cracking
- 6mm Fe500 bars at 150mm (6") centers both ways
- 4" slab thickness adequate for this loading
- Alternative: 8mm bars at 200mm if heavier equipment expected

### Floor Finish Options

| Option | Cost | Durability | Maintenance |
|--------|------|------------|-------------|
| IPS (Indian Patent Stone) | Medium | High | Needs polish every 2-3 yrs |
| Plain cement with hardener | Low | Medium | Can crack under wheels |
| Kota stone | High | Very high | Almost zero |
| Tremix (VDF) flooring | Medium-High | Very high | Best for heavy loads |

**Recommendation:** IPS flooring (cement + marble chips, machine polished). Strong, good-looking, easy to clean farm products. The wire mesh in the base slab handles structural load regardless of finish.

---

## 14. Tractor Ramp Detail

```
    PLAN VIEW:
    
    ┌───────────────────────────┐  ← SHUTTER (10 ft)
    │      PLATFORM (+3ft)      │
    │                           │
    ├─────┬─────────────┬───────┤  ← Ramp starts at platform edge
    │     │             │       │
    │     │    RAMP     │       │  8 ft long
    │     │   12 ft W   │       │  (tractor only)
    │     │   Grooved   │       │
    │     │   concrete  │       │
    └─────┴─────────────┴───────┘  ← Meets natural ground (0 ft)
          ← 12 ft →
    
    
    SECTION VIEW:
    
    PLATFORM ═══════════════╗ +3 ft
                            ║ ╲
                            ║   ╲  ~1:2.7 slope
                            ║     ╲  (steeper, tractor only)
                            ║       ╲
    GROUND  ════════════════╩════════╗ 0 ft
                            
            ←──── 8 ft ────→
    
    RAMP SPECS:
    - Width: 12 ft (wider than shutter for alignment ease)
    - Length: 8 ft (~1:2.7 slope, tractor only — trolley stays at shutter)
    - Surface: Grooved/textured RCC (anti-slip for tractor tires)
    - Side walls: 1.5 ft high, 4.5" brick with coping
    - Thickness: 6" RCC slab on compacted earth
    - Transitions: ROUNDED at top and bottom (prevent belly/axle scraping)
    - Note: Trolley unloads at shutter level; only unloaded tractor drives up
```

---

## 15. Gate & Steps Detail

```
    FRONT VIEW (gate area):
    
         GATE (MS fabricated)
         3 ft wide × 7 ft high
    ┌─────────────────┐
    │                 │    ← Platform level (+3ft)
    │  ┌───────────┐  │
    │  │           │  │
    │  │   GATE    │  │    7 ft gate height
    │  │   (MS)    │  │
    │  │           │  │
    │  │           │  │
    │  └───────────┘  │
    ├──┤           ├──┤    ← Step line
    │S5│           │  │    Steps going down
    │S4│           │  │
    │S3│           │  │    5 risers × 7" = 35" ≈ 3 ft
    │S2│           │  │
    │S1│           │  │
    └──┘           └──┘    ← Ground level (0 ft)
    
    STEP SPECS:
    - Risers: 5 nos. × 7" each = 35" rise
    - Treads: 10" deep
    - Width: 3 ft (matching gate)
    - Material: RCC or brick + cement plaster
    - Landing: 3 ft × 3 ft at platform level (before gate)
    - Handrail: MS pipe on one side
```

---

## 16. Construction Sequence

1. **Site preparation** — clear vegetation, mark layout with lime/thread
2. **Excavation** — dig column footing pits (3ft × 3ft × 3.5ft deep each)
3. **PCC bed** — pour 6" M15 concrete in each pit, level, cure 2 days
4. **Footings** — RCC footings (12" thick, 3ft × 3ft), cure 7 days
5. **Column stubs** — raise column bars from footing to plinth level (+3ft)
6. **Plinth walls** — 9" brick walls between columns up to +3ft
7. **Earth filling** — fill inside plinth in 6" layers, water, compact each layer
8. **PCC over fill** — 3-4" M15 concrete, level, cure
9. **Floor slab** — lay wire mesh, pour 4" M20 concrete, cure 14 days
10. **Columns** — cast columns from +3ft to +15ft (in 2 lifts if needed)
11. **Walls** — raise 9" external walls + 4.5" internal walls
12. **Leave openings** — shutter, gate, vents, toilet exhaust
13. **Cast lintels** — RCC lintels at all openings + future window positions
14. **Build staircase** — dog-legged, cast waist slabs + steps in one pour
15. **Beam formwork** — install formwork for all beams at +15ft level
16. **Slab formwork** — formwork for entire ceiling slab including 5ft cantilever
17. **Slab steel** — lay reinforcement (main + distribution bars + cantilever bars)
18. **Concrete pour** — pour entire slab in one go (M20, avoid cold joints)
19. **Curing** — wet cure slab for minimum 21 days
20. **Plumbing** — install pipes in walls (before plastering)
21. **Plastering** — cement plaster (1:4 inside, 1:6 outside)
22. **Flooring** — IPS or chosen finish on ground floor
23. **Toilet finishing** — tiles, commode, basin, connections
24. **External works** — ramp, steps, soak pit, water tank
25. **Painting** — white weatherproof paint (external), distemper (internal)
26. **Installations** — shutter, gate, grills, handrails, electrical (if any)

---

## 17. Critical Dimensions Summary (for Contractor)

| Item | Dimension | Hindi/Local Term |
|------|-----------|-----------------|
| Building width | 20 ft | Chaudai |
| Building depth | 25 ft | Lambai |
| Plinth height | 3 ft | Plinth / Chabootra |
| Room height | 12 ft | Kamre ki unchai |
| External wall | 9 inch | Do eet (2 brick) |
| Internal wall | 4.5 inch | Ek eet (1 brick) |
| Column | 9" × 12" | Pillar |
| Middle beam (deep) | 9" × 20" (spans 20ft) | Bada beam |
| Other beams | 9" × 15" | Beam / Dhal |
| Slab thickness | 6 inch | Chhat / Slab |
| Floor slab | 4 inch + mesh | Farshe ki slab |
| Riser height | 7 inch | Seedhi ki unchai |
| Tread depth | 10 inch | Seedhi ki chaudai |
| Shutter opening | 10 ft × 10 ft | Shutter |
| Gate opening | 3 ft × 7 ft | Gate / Darwaza |
| Vent size | 9" × 12" | Roshandaan |
| Ramp slope | ~1:2.7 | Dhalaan |
| Ramp length | 8 ft | Ramp |
| Footing size | 3ft × 3ft × 1ft | Neev / Foundation |
