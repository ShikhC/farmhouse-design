# FINAL SPECIFICATION — Ground Floor Civil Work

**Document Status:** FINAL & AUTHORITATIVE (overrides all previous versions)
**Date:** June 2026
**Building Type:** Agricultural Storage + Staircase Access to First Floor Residence

---

## 1. BUILDING OVERVIEW

| Parameter | Value |
|-----------|-------|
| Internal width (chaudai) | 20ft (C5 to C8, inside face to inside face) |
| Internal depth (lambai/gehrai) | 25ft (front to back, inside face to inside face) |
| External width (overall) | 20ft + 9" + 9" = 21ft 6" |
| External depth (overall) | 25ft + 9" + 9" = 26ft 6" |
| Plinth height (chabutra) | 3ft above natural ground level (NGL) |
| Ground floor height | 12ft (plinth top to slab soffit) |
| External walls (bahari deewar) | 9" brick (230mm) |
| Internal partition walls | 4.5" brick (115mm) |
| Number of columns (pillar) | 8 nos. (all embedded in walls) |
| Column size | 9" x 12" RCC |
| Ground floor use | Storage (godown) + Staircase + Toilet |

---

## 2. STRUCTURAL GRID & COLUMN SCHEDULE

### 2.1 Column Positions

All columns are 9" x 12" RCC. The 12" dimension faces the front wall (i.e., 12" along the width/x-axis, 9" along the depth/z-axis).

**Coordinate System:**
- X-axis: Left to Right (as viewed from OUTSIDE), origin at C5 inner face
- Z-axis: Front to Back, origin at front wall inner face
- Y-axis: Vertical (up from plinth top)

| Column | Position | Location Description |
|--------|----------|---------------------|
| C1 | x=0, z=25 | Back-left corner |
| C2 | x=20, z=25 | Back-right corner |
| C3 | x=0, z=16 | Left wall, 9ft from front (16ft from back) |
| C4 | x=20, z=16 | Right wall, 9ft from front (16ft from back) |
| C5 | x=0, z=0 | Front-left corner |
| C6 | x=6, z=0 | Front wall, 6ft from C5 |
| C7 | x=17, z=0 | Front wall, 6+1+10 = 17ft from C5 |
| C8 | x=20, z=0 | Front-right corner |

**Note:** C3 and C4 are at z=16 (i.e., 16ft from back wall = 9ft from front wall). This aligns with the first floor room partition above.

### 2.2 Beam Schedule

| Beam | Span | Size | Position | Notes |
|------|------|------|----------|-------|
| Back beam (C1-C2) | 20ft | 9" x 20" RCC | y=25 (back wall) | Main structural beam |
| Middle beam (C3-C4) | 20ft | 9" x 20" RCC | y=9 (9ft from front) | Supports 1F partition |
| Front beam (C5-C6-C7-C8) | 20ft | 9" x 20" RCC | y=0 (front wall) | Increased from 15" per structural calc |
| Left beam (C1-C3-C5) | 25ft | 9" x 24" RCC | x=0 (left wall) | Continuous, 2-span. Increased from 15" — 7.62m span requires deeper beam |
| Right beam (C2-C4-C8) | 25ft | 9" x 24" RCC | x=20 (right wall) | Continuous, 2-span. Increased from 15" — 7.62m span requires deeper beam |

**Beam Reinforcement (per structural load calculations):**
- 9" x 24" beams (side): 5-20mm tor bottom + 2-16mm tor top + 8mm stirrups @ 100mm c/c (ends L/4), 175mm c/c (middle)
- 9" x 20" beams (cross): 4-20mm tor bottom + 2-16mm tor top + 8mm stirrups @ 150mm c/c (ends), 200mm c/c (middle)

**IMPORTANT:** See `structural-load-calculations.md` for full design verification. Side beams were found INADEQUATE at 9"×15" and increased to 9"×24" (230×600mm). Front beam increased from 9"×15" to 9"×20".

---

## 3. FLOOR PLAN (Plan View — as seen from ABOVE)

**Orientation:** Viewed from OUTSIDE, Left = West side, Right = East side, Front = South, Back = North.

```
                        20ft INTERNAL WIDTH
    ←───────────────────────────────────────────────────→
    │                                                     │
    ├─────────────────────────────────────────────────────┤ ← z=25 (BACK WALL)
    │C1          BACK BEAM (9"×20")                    C2│     Back wall (9" brick)
    │                                                     │
    │                                                     │
    │                                                     │
    │                                                     │
    │              S T O R A G E                           │
    │              A R E A                                 │
    │              (godown)                                │
    │              Clear height: 12ft                      │
    │              Floor: IPS finish                       │
    │                                                     │   25ft
    │                                                     │   INTERNAL
    │                                                     │   DEPTH
    │                                                     │
    │                                                     │
    ├─────────────────────────────────────────────────────┤ ← z=16 (MIDDLE BEAM)
    │C3        MIDDLE BEAM (9"×20")                    C4│     (9ft from front)
    │                                                     │
    │         ┃                                           │
    │         ┃  4.5" partition                           │
    │         ┃  wall                                     │
    │         ┃                                           │
    │ STAIR   ┃         S T O R A G E                     │
    │ ZONE    ┃         (continued)                       │
    │         ┃                                           │
    │         ┃                                           │
    │         ┃                                           │
    ├──6ft────╋───────────────────────────────────────────┤ ← z=0 (FRONT WALL)
    │C5  │  │C6│        SHUTTER 10ft         │C7│wall│C8│
    └────┴──┴───┴───────────────────────────────┴───┴────┘

    ←2ft→←2.75→←1ft→←────────10ft─────────→←1ft→←2ft→
    toilet stair  C6      ROLLING SHUTTER      C7  solid
    door  gate                                      wall
```

### 3.1 Detailed Front Wall Layout (Left to Right, viewed from OUTSIDE)

```
    ←──────────────────── 20ft INTERNAL ────────────────────────→

    ┌───────────────┬───┬───────────────────────────────┬───┬────┐
    │  6ft clear    │   │        10ft clear              │   │2ft │
    │               │C6 │                                │C7 │    │
    │ ┌──┐  ┌────┐ │1ft│    ROLLING SHUTTER             │1ft│WALL│
    │ │TD│  │ SG │ │   │    (MS galvanized, 10ft H)     │   │    │
    │ │2'│  │2.75│ │   │                                │   │    │
    │ └──┘  └────┘ │   │                                │   │    │
    └───────────────┴───┴───────────────────────────────┴───┴────┘
      C5                                                       C8

    TD = Toilet Door (2ft wide, hinged outward, left side)
    SG = Stair Gate (2.75ft wide, hinged outward, right side)
    Gap between TD and SG: ~1.25ft (partition wall face visible)
```

### 3.2 Stair Zone Detail (Plan View)

```
              6ft (full zone width)
    ←─────────────────────────────────→
    ┌─────────────┬─────┬─────────────┐
    │             │0.5ft│             │  ← z=8.5 (LANDING top)
    │  FLIGHT 2   │wall │  FLIGHT 1   │
    │  (upper)    │     │  (lower)    │
    │  2.75ft wide│     │  2.75ft wide│
    │             │     │             │
    │  Goes       │     │  Goes       │
    │  FORWARD    │     │  BACKWARD   │
    │  (z=8.5→    │     │  (z=0→z=6) │
    │   z=1.5)    │     │             │
    │             │     │             │
    │             │     │             │
    ├─────────────┴─────┴─────────────┤ ← z=6 (LANDING bottom)
    │         LANDING                  │
    │         6ft × 2.5ft             │
    │         at 6ft height            │
    ├─────────────┬─────┬─────────────┤ ← z=8.5
    │             │     │             │
    │             │     │             │
    │             │     │             │
    └─────────────┴─────┴─────────────┘ ← z=16 (middle beam)

    (LEFT side)        (RIGHT side)
    outer wall         toward C6

    TOILET is under Flight 2 (left side), z=0 to z=5
```

Corrected stair zone plan (from front z=0 looking in):

```
              6ft (full zone width)
    ←─────────────────────────────────→
    x=0          x=2.75  x=3.25       x=6

    z=0  ┌──────────┬───────┬──────────┐  FRONT WALL
         │ TOILET   │ 0.5ft │ FLIGHT 1 │
         │ (under   │ wall  │ (lower)  │
         │ Flight 2)│       │          │
         │ 2.75ft W │       │ 2.75ft W │
         │          │       │ ↓ going  │
    z=5  │..........│       │   back   │
         │ (Flight 2│       │          │
         │ above,   │       │          │
         │ coming   │       │          │
         │ forward) │       │          │
    z=7  ├──────────┴───────┴──────────┤  LANDING (z=6 to z=8.5)
         │       6ft × 2.5ft           │  at height = 6ft
    z=8.5├─────────────────────────────┤
         │                             │
         │  (storage area beyond)      │
         │                             │
```

---

## 4. FRONT ELEVATION

```
                            FRONT ELEVATION (viewed from outside)
                    ←───────── 21ft 6" (external) ──────────→
                    ┌─────────────────────────────────────────┐
                    │           FIRST FLOOR SLAB              │ ← +15ft (slab top)
    ════════════════╪═════════════════════════════════════════╪══════════
                    │    FIRST FLOOR (shown for reference)    │
                    │         12ft height                     │
                    ├─────────────────────────────────────────┤ ← +12ft (GF slab soffit/1F floor)
                    │                                         │
    6ft extension   │   9"×20" FRONT BEAM (C5-C6-C7-C8)     │
    (shade/balcony  ├────┬──┬──┬─┬──────────────────┬─┬──┬──┤
     for 1F above)  │    │  │  │ │                  │ │  │  │
                    │    │TD│SG│C│  ROLLING SHUTTER  │C│  │  │ ← +10ft (shutter top)
                    │    │  │  │6│   10ft × 10ft    │7│  │  │
                    │    │  │  │ │  MS Galvanized   │ │  │  │
                    │    │2'│  │ │                  │ │  │  │
                    │    │  │  │1│                  │1│  │  │
                    │    │  │2.│f│                  │f│  │2ft│
                    │    │  │75│t│                  │t│  │wall│
                    │    │  │  │ │                  │ │  │  │
                    │    │  │  │ │                  │ │  │  │
    ════════════════╪════╪══╪══╪═╪══════════════════╪═╪══╪══╪══ ← +0ft (PLINTH TOP)
                    │         PLINTH (3ft)                    │
                    │         9" stone/brick masonry          │
    ────────────────┴─────────────────────────────────────────┴─── NGL (Natural Ground)
                    ├────┤                          ├────────┤
                     STEPS                            RAMP
                    (5 nos.)                         (8ft long)
                    6ft wide                         12ft wide

    TD = Toilet Door (2ft × 7ft)
    SG = Stair Gate (2.75ft × 7ft)
    C6, C7 = Pillars (1ft wide × 12ft height visible)
```

---

## 5. SECTION VIEW (Cut through center, looking left)

```
    CROSS-SECTION (through storage area, looking toward left wall)

                         ┌─────────────────────┐
                         │   6" RCC SLAB (M20)  │ ← Slab top = +12ft 6"
                         ├─────────────────────┤ ← Slab soffit = +12ft
                         │                     │
                         │  9"×24" SIDE BEAM    │ ← Beam soffit = +12ft - 24" = +10ft 0"
                         ├─────────────────────┤
                         │                     │
                         │                     │
                         │    GROUND FLOOR     │   12ft clear height
                         │    (STORAGE)        │   (plinth top to slab soffit)
                         │                     │
                         │                     │
                         │  Vent (9"×12")      │ ← +10ft height
                         │  @ MS grill         │
                         │                     │
                         │                     │
                         │                     │
    ═════════════════════╪═════════════════════╪═══════ PLINTH TOP (+0ft)
                         │                     │
    ─────────────────────┤  FLOOR LAYERS:      ├─────── (see detail below)
    IPS/Cement finish    │  ← IPS finish       │
    4" RCC slab (M20)   │  ← 4" RCC + mesh    │
    3-4" PCC bed (M15)  │  ← PCC bed          │
    Compacted earth fill │  ← Earth fill       │
    ─────────────────────┤                     ├───────
                         │  PLINTH WALL        │   3ft plinth
                         │  (9" stone/brick)   │
                         │                     │
    ═════════════════════╪═════════════════════╪═══════ NGL (Natural Ground Level)
                         │  FOUNDATION         │
                         │  (as per foundation │
                         │   spec document)    │
                         └─────────────────────┘
```

### 5.1 Floor Layer Detail

```
    FLOOR CONSTRUCTION (from top to bottom):

    ┌─────────────────────────────────────┐
    │  IPS/Cement smooth finish (12mm)    │  ← Storage area finish
    ├─────────────────────────────────────┤
    │  4" RCC Floor Slab (M20 concrete)   │  ← 6mm wire mesh @ 6"×6" embedded
    │  (100mm thick)                       │     mesh on 1" cover blocks (spacers)
    ├─────────────────────────────────────┤
    │  3-4" PCC Bed (M15 / 1:2:4)        │  ← Plain cement concrete leveling
    │  (75-100mm thick)                    │
    ├─────────────────────────────────────┤
    │                                     │
    │  Compacted Earth Fill               │  ← Filled in 6" layers,
    │  (murrum/soil, watered & rammed)    │     each layer watered & compacted
    │                                     │     with plate compactor/hand rammer
    │                                     │
    ├─────────────────────────────────────┤
    │  Anti-termite treatment             │  ← Chemical barrier on soil
    ├─────────────────────────────────────┤
    │  PLINTH BEAM / Foundation           │
    └─────────────────────────────────────┘

    DPC (Damp Proof Course):
    20mm waterproof cement mortar (1:3 cement:sand + waterproofing compound)
    Applied on TOP of all plinth walls before superstructure starts.
```

---

## 6. STAIRCASE DETAIL

### 6.1 Staircase Specifications

| Parameter | Value |
|-----------|-------|
| Type | Dog-legged (half-turn) (kutta-teda seedhi) |
| Total rise (oonchaayi) | 12ft (144") |
| Total risers | 18 (9 per flight) |
| Riser height (oonchaayi per step) | 8" (203mm) |
| Treads per flight | 8 |
| Tread depth (chaurai per step) | 9" (229mm) |
| Flight width (seedhi ki chaurai) | 2.75ft (838mm) each |
| Partition between flights | 0.5ft (6") — 4.5" brick + plaster |
| Total zone width | 6ft (2.75 + 0.5 + 2.75) |
| Flight 1 run (horizontal) | 7ft (z=0 to z=7) |
| Flight 2 run (horizontal) | 7ft (z=8.5 to z=1.5) |
| Landing size | 6ft wide x 2.5ft deep (z=6 to z=8.5) |
| Landing height | 6ft above GF floor (halfway) |
| Waist slab thickness | 5" RCC (125mm) |
| Handrail (jangla) | MS pipe 1.5" dia, both sides, 3ft height |
| Nosing | 1" rounded edge, anti-slip groove |
| Headroom at landing | 6ft (12ft total - 6ft landing = 6ft above landing to slab) |

### 6.2 Stair Flight Details

**Flight 1 (Lower Flight) — RIGHT side of zone (near C6):**
- Direction: Going BACKWARD (from z=0 toward z=7)
- Start: At front wall (z=0), at plinth level (+0ft)
- End: At landing (z=7), at +6ft height
- Width: 2.75ft
- 9 risers × 8" = 6ft rise (72") — Wait, 9 × 8 = 72" = 6ft ✓
- 8 treads × 9" = 84" = 6ft run ✓

**Landing:**
- Position: z=6 to z=8.5 (2.5ft deep)
- Width: 6ft (full zone width — both flights share it)
- Height: 6ft above GF floor
- Construction: 6" RCC slab, supported on side walls + middle beam
- **Clearance check:** Landing at z=6 to z=8.5, Middle beam at z=16 (9ft from front). Gap = 16 - 8.5 = 7.5ft. NO BEAM CONFLICT. ✓

**Flight 2 (Upper Flight) — LEFT side of zone (outer wall side):**
- Direction: Coming FORWARD (from z=8.5 toward z=1.5)
- Start: At landing (z=8.5), at +6ft height
- End: At z=1.5, at +12ft height (first floor level)
- Width: 2.75ft
- 9 risers × 8" = 72" = 6ft rise (from 6ft to 12ft) ✓
- 8 treads × 9" = 84" = 6ft run ✓

### 6.3 Staircase Section View

```
    STAIRCASE SECTION (cut through Flight 1, looking toward right/C6 side)

    1F SLAB ═══════════════════════════════════════════ +12ft
              │                                    ╱
              │ Flight 2                         ╱  (coming forward)
              │ (behind, LEFT side)            ╱
              │                              ╱
              │                            ╱
              ├────────── LANDING ────────╱─── +6ft (z=6 to z=8.5)
              │         (6ft × 2.5ft)    │
              │                          │
              │         ╱                │
              │       ╱  Flight 1        │
              │     ╱    (RIGHT side)    │
              │   ╱      going back      │
              │ ╱                        │
    ══════════╱══════════════════════════════════ PLINTH TOP (+0ft)
         z=0                            z=7    z=8.5

    Waist slab: 5" RCC throughout
    Steps: Built on waist slab with brick + cement mortar
```

### 6.4 Stair Reinforcement

| Element | Reinforcement |
|---------|--------------|
| Waist slab (5" thick) | 12mm tor @ 150mm c/c (main), 8mm tor @ 200mm c/c (distribution) |
| Landing slab (6" thick) | 12mm tor @ 150mm c/c both ways |
| Steps | Brick masonry built on waist slab, plastered smooth |
| Cover | 20mm (bottom), 15mm (top) |
| Concrete grade | M20 (1:1.5:3) |

---

## 7. TOILET DETAIL

### 7.1 Toilet Location & Dimensions

| Parameter | Value |
|-----------|-------|
| Position | Under Flight 2, LEFT side of stair zone |
| X-extent | x=0 to x=2.75ft (against outer left wall) |
| Z-extent | z=0 to z=5 (5ft deep) |
| Width | 2.75ft |
| Depth | 5ft |
| Door | 2ft wide, on front wall, hinged outward |
| Min headroom | ~6ft+ at entry (Flight 2 arrives at 1F at z=1.5, so at z=0 full 12ft, at z=5 approx 8.5ft headroom under flight) |

### 7.2 Toilet Fixtures & Finishes

| Item | Specification |
|------|--------------|
| WC | Western commode (European seat), wall-mounted flush tank |
| Wash basin | Wall-mounted, 18" × 12", with mirror above |
| Floor | Anti-skid ceramic tiles, sloped 1:40 toward floor trap |
| Walls | Ceramic tiles up to 5ft height, cement plaster above |
| Ceiling | Cement plaster (underside of Flight 2 waist slab) |
| Door | MS frame + flush door, 2ft × 6.5ft, opens outward |
| Ventilation | 12" × 9" exhaust opening on left wall + exhaust fan |
| Drain | 4" PVC floor trap → 4" PVC SWR pipe → septic tank |
| Water supply | 15mm CPVC cold water line (from overhead tank on 1F) |

---

## 8. STORAGE AREA

### 8.1 Storage Specifications

| Parameter | Value |
|-----------|-------|
| Clear width | ~14ft (from stair partition at x=6ft to right wall at x=20ft) |
| Clear depth | 25ft (full building depth) |
| Clear height | 12ft (plinth to slab soffit), reduced to ~10ft under side beams (9"×24"), ~10ft 4" under cross beams (9"×20") |
| Area | ~350 sq.ft (14ft × 25ft) |
| Access | 10ft × 10ft rolling shutter (front wall, C6 to C7) |
| Floor finish | IPS / cement smooth (polished cement) |
| Obstructions | NONE — completely column-free open space |

### 8.2 Storage Floor

- 4" RCC slab with 6mm wire mesh @ 6" × 6" c/c
- M20 concrete (1:1.5:3)
- IPS (Indian Patent Stone) finish — smooth, hard-wearing
- Floor drain channel: 6" wide, along center line, sloped toward front (1:100 gradient)
- Floor level: same as plinth top (flush)

### 8.3 Rolling Shutter (Shutter / Gala ka Shutter)

| Parameter | Value |
|-----------|-------|
| Type | MS galvanized rolling shutter |
| Clear opening | 10ft wide × 10ft high |
| Material | 18-gauge MS laths, galvanized |
| Guide channels | MS C-channel, 4" × 2", both sides (embedded in C6, C7 columns) |
| Bottom rail | MS flat 50mm × 6mm with rubber seal |
| Locking | Center lock + side locks (tower bolts) |
| Operation | Manual (chain/gear operated) |
| Lintel above | Part of front beam (9" × 20" RCC) — no separate lintel needed |
| Hood box | MS cover at top, painted |

---

## 9. RAMP DETAIL

### 9.1 Ramp Specifications

| Parameter | Value |
|-----------|-------|
| Purpose | Tractor/vehicle access to storage floor at plinth level |
| Width | 12ft (wider than 10ft shutter for alignment margin) |
| Length (slope) | 8ft (horizontal run) |
| Rise | 3ft (plinth height) |
| Gradient | 1:2.67 (approx 20.5 degrees) — steep, tractor-only |
| Surface | Grooved/textured RCC (anti-slip chevron pattern) |
| Thickness | 6" RCC with 8mm mesh @ 150mm c/c |
| Side walls | 9" brick, 1.5ft high (parapet/guide walls) |
| Transitions | Rounded/curved at top and bottom (R=2ft) to prevent tractor belly scraping |
| Position | Centered on shutter opening (extends from front wall outward) |
| Concrete | M20 |

### 9.2 Ramp Section

```
    RAMP SECTION (side view)

    ┌───────────────────────┐
    │   STORAGE FLOOR       │ ← Plinth top (+3ft above NGL)
    │                       │
    ════════════════════════╗
                            ║╲
                            ║  ╲  RAMP (8ft long)
                            ║    ╲  6" RCC, grooved surface
                            ║      ╲
                            ║    R=2ft╲  Rounded transition
    ════════════════════════╩══════════╧══════ NGL (ground level)
                            ←── 8ft ──→

    Top transition: curved (no sharp edge)
    Bottom transition: curved (tractor doesn't scrape)
    Side walls: 1.5ft high brick parapets both sides
```

---

## 10. GATE STEPS (Stair/Toilet Entry Steps)

### 10.1 Step Specifications

| Parameter | Value |
|-----------|-------|
| Purpose | Pedestrian access to stair gate and toilet door |
| Location | In front of left portion of building (C5 to C6 zone) |
| Width | 6ft (covers full stair+toilet zone frontage) |
| Number of steps | 5 |
| Total rise | 3ft (36") |
| Riser height | 7.2" each (36" / 5) |
| Tread depth | 10" |
| Total run | 4ft 2" (5 treads × 10") |
| Material | Brick masonry + cement mortar, plastered smooth |
| Nosing | Rounded, 1" projection |
| Finish | Cement plaster with IPS top, anti-slip groove at edge |
| Handrail | MS pipe 1.5" dia, one side (center), 3ft height |

### 10.2 Steps Section

```
    STEPS SECTION (side view)

    FRONT WALL
    ┌──────────┐
    │ TD │ SG  │ ← Plinth top (+3ft)
    ════════════╗
               ┌╫─────┐
              ┌╫┤     │  Step 1 (top)
             ┌╫┤│     │  Step 2
            ┌╫┤││     │  Step 3
           ┌╫┤│││     │  Step 4
    ═══════╧┤││││     │  Step 5 (bottom)
    NGL ────┴┴┴┴┴─────┘
            ←── ~4ft 2" ──→
            (5 treads × 10")
```

---

## 11. DRAINAGE & SEPTIC SYSTEMS (Per Architect Consultation, 19 June 2026)

**THREE completely separate drainage systems are required:**

### 11.1 SYSTEM 1: Black Water (Toilet Only)

```
Toilet → 110mm SWR Pipe → Inspection Chamber → Septic Tank → Black Water Soak Pit
```

**Septic Tank:**
| Parameter | Value |
|-----------|-------|
| Capacity | ~1500 litres (toilet-only, 3-5 users) |
| Type | 2-chamber RCC tank |
| Size | 5ft × 2.5ft × 4.5ft (as per architect's recommendation for toilet-only load) |
| Wall thickness | 6" RCC (M20) |
| Position | 5-10ft from building |
| Cover | RCC slab with access opening for de-sludging |
| Inlet | 110mm PVC, 6" below top |
| Outlet | 110mm PVC, 9" below top (to soak pit) |
| Baffle wall | RCC, 4" thick, with openings at 2/3 depth |
| Cleaning interval | Every 2-3 years (tanker pumping) |

**Black Water Soak Pit:**
| Parameter | Value |
|-----------|-------|
| Diameter | 5ft |
| Depth | 7ft |
| Construction | Dry brick honeycomb (no mortar, for seepage) |
| Fill | Bottom 2ft with gravel |
| Cover | RCC slab with access opening |
| Position | 5-10ft from septic tank, 50ft from borewell |
| Water table | 20ft deep (13ft soil filtration gap — safe) |

**Inspection Chamber (1 no.):**
| Parameter | Value |
|-----------|-------|
| Size | 1.5ft × 1.5ft × 2ft deep |
| Position | Between building exit and septic tank |
| Purpose | Access point for maintenance/blockage clearing |
| Cover | CI frame + cover at ground level |

---

### 11.2 SYSTEM 2: Grey Water (Kitchen, Basin, Bath — Future 1F)

```
Kitchen Sink / Wash Basin / Bath → Grease Trap → Inspection Chamber → Grey Water Soak Pit (SEPARATE!)
```

**Note:** Grey water fixtures are on the FIRST FLOOR (future). But the underground pipe route must be laid NOW (before floor slab pour). Pipe will be capped at both ends until 1F is built.

**Underground provision NOW:**
- Lay 75mm (3") PVC SWR pipe from the building RIGHT SIDE (where 1F kitchen/bathroom will be above) to the grey water soak pit location
- Cap both ends with PVC caps (open later when 1F is built)
- Leave a pipe stub poking above floor level at the grey water exit point (right side of building, through plinth wall)

**Grease Trap (to be installed later with 1F kitchen):**
| Parameter | Value |
|-----------|-------|
| Size | 600mm × 450mm × 600mm (minimum) |
| Position | Near kitchen down-pipe (ground level, outside building) |
| Purpose | Removes oil, grease, food particles before grey water enters soak pit |
| Cleaning | Every 2-4 weeks (scoop floating grease) |

**Grey Water Soak Pit (SEPARATE from black water pit):**
| Parameter | Value |
|-----------|-------|
| Diameter | 4ft |
| Depth | 6ft |
| Construction | Dry brick honeycomb |
| Position | Different side of building from black water pit (to distribute load on soil) |
| Note | Receives only pre-filtered water (grease trap removes oil/solids) |

**Inspection Chamber (1 no.):**
| Parameter | Value |
|-----------|-------|
| Size | 1.5ft × 1.5ft × 2ft deep |
| Position | Between grease trap and grey water soak pit |

---

### 11.3 SYSTEM 3: Tractor/Floor Wash Water (Separate)

```
Floor drain channel / Tractor wash → Silt Trap → Oil & Grease Trap → Wash Water Soak Pit (SEPARATE!)
```

**The storage floor drain channel exits at the front of the building. This wash water must NOT enter the septic tank or either soak pit. It needs its own treatment.**

**Silt Trap / Mud Trap:**
| Parameter | Value |
|-----------|-------|
| Size | 750mm × 750mm × 750mm (for tractor-level mud) |
| Position | At the floor drain exit point (outside, front of building) |
| Purpose | Settles mud, sand, soil particles |
| Cleaning | As needed (after heavy wash) |

**Oil & Grease Trap:**
| Parameter | Value |
|-----------|-------|
| Size | 750mm × 600mm × 750mm |
| Position | After silt trap |
| Purpose | Removes diesel, oil, grease from tractor wash water |

**Wash Water Soak Pit:**
| Parameter | Value |
|-----------|-------|
| Diameter | 5ft |
| Depth | 6.5ft |
| Position | Near the ramp/front area (convenient to floor drain exit) |

---

### 11.4 SYSTEM 4: Rainwater (Completely Independent)

```
Roof → 4 Downpipes (3" PVC at corners) → Recharge Pit / Surface Drainage
```

**Rainwater is NEVER connected to any septic tank, soak pit, or drain system.**

| Parameter | Value |
|-----------|-------|
| Downpipes | 4 nos., 3" (75mm) PVC at building corners |
| Exit | Through plinth wall at ground level (already provisioned during plinth construction) |
| Disposal | Surface drainage directed away from building OR rainwater recharge pit |
| Recharge pit (optional) | 3ft dia × 10ft deep, filled with gravel, for groundwater recharge |

---

### 11.5 Underground Pipe Layout Summary (BEFORE floor slab pour):

```
PLAN VIEW (underground pipes):

                    BUILDING (20ft × 25ft)
    ┌──────────────────────────────────────────┐
    │                                          │
    │  TOILET ══► ─── PIPE 1 (110mm, black) ──┼──► Insp.Ch → Septic → BW Soak Pit
    │  (left)                                  │
    │                                          │
    │         ══► ─── PIPE 2 (75mm, grey,      │
    │  (right,        CAPPED for future 1F) ───┼──► (future) Grease Trap → Insp.Ch → GW Soak Pit
    │   stub)                                  │
    │                                          │
    │  FLOOR DRAIN ══► PIPE 3 (exits front) ───┼──► Silt Trap → Oil Trap → WW Soak Pit
    │  (center channel)                        │
    │                                          │
    │  RAIN DOWNPIPES (4 corners) ─────────────┼──► Surface drain / Recharge pit
    │                                          │
    └──────────────────────────────────────────┘
```

**Critical: ALL 4 pipe routes must be laid BEFORE the floor slab is poured.**
- Pipe 1 (black water): active immediately (toilet on GF)
- Pipe 2 (grey water): capped now, activated when 1F kitchen/bath is built
- Pipe 3 (wash water): active immediately (floor drain channel)
- Pipe 4 (rain): downpipe sleeves through plinth wall (connect later)

### 11.6 Drainage Pipe Specifications

| Pipe | Size | Material | Slope | Bedding | Joints |
|------|------|----------|-------|---------|--------|
| Black water (toilet) | 110mm (4") | PVC SWR | 1:40 to 1:60 | 150mm sand | Solvent cement |
| Grey water (future) | 75mm (3") | PVC SWR | 1:40 to 1:60 | 150mm sand | Solvent cement |
| Floor wash drain | 110mm (4") | PVC SWR | 1:60 | 100mm sand | Solvent cement |
| Rainwater sleeves | 75mm (3") | PVC | N/A (through wall) | N/A | Fitted in plinth wall |

---

## 12. GF SHADE / CANOPY (Chhat / Chhajja)

### 12.1 Shade Structure — PURE CANTILEVER

| Parameter | Value |
|-----------|-------|
| Description | First floor slab extends 5ft beyond front wall as a **PURE CANTILEVER** |
| Function | Covered shade at GF (shutter rain protection + sitting area), balcony floor for 1F |
| Extension | 6ft forward from front wall line (z=0 to z=-5) |
| Width | Full building width |
| Height | 12ft (from plinth top to slab soffit) |
| **Support** | **NONE — pure cantilever from the front beam (C5-C6-C7-C8)** |
| **NO side walls** | Side walls STOP at z=0 (front wall line). They do NOT extend forward. |
| **NO front pillars** | No columns/pillars at the outer edge. Slab hangs freely. |
| Slab | 6" RCC (continuous with main GF ceiling slab, tapers to 4-5" at tip) |
| **Reinforcement** | Top bars: 10mm @ 5" c/c, anchored **10ft** back into the main slab (critical!) |
| Deflection | Expect 5-8mm tip deflection over time (acceptable, not visible) |

**Note:** The shade area below (z=0 to z=-5) is COMPLETELY OPEN — no walls, no pillars. Just the slab overhead providing shade. The ramp and steps are in this zone.

---

## 13. VENTILATION

### 13.1 Wall Vents (Roshandaan)

| Location | Quantity | Size | Height | Finish |
|----------|----------|------|--------|--------|
| Left wall (25ft) | 2 nos. | 9" × 12" | 10ft above floor | MS grill + wire mesh |
| Right wall (25ft) | 2 nos. | 9" × 12" | 10ft above floor | MS grill + wire mesh |
| Back wall (20ft) | 2 nos. | 9" × 12" | 11ft above floor | MS grill + wire mesh |
| Total | 6 nos. | | | |

**Spacing:** Evenly distributed along wall length (approx 8-9ft apart on side walls, 7ft apart on back wall).

### 13.2 Future Window Provisions

- RCC lintels (9" × 6") to be cast at designated positions during wall construction
- Positions marked on walls for future window openings (bricks can be removed later)
- Suggested window size: 4ft × 3ft (when needed)
- 2 windows per side wall, 1 window on back wall (tentative positions)

---

## 14. GF CEILING / FIRST FLOOR SLAB

### 14.1 Slab Specifications

| Parameter | Value |
|-----------|-------|
| Thickness | 6" (150mm) RCC |
| Concrete grade | M20 (1:1.5:3) |
| Reinforcement | 10mm tor @ 150mm c/c both ways (bottom) + 8mm tor @ 200mm c/c (top, at supports) |
| Cover | 20mm (bottom), 15mm (top) |
| Span | Multiple panels supported by beams (max clear span ~10ft between beams) |
| Extent | Main: 20ft × 25ft (building footprint) + 6ft front extension |
| Total slab area | 20ft × 30ft = 600 sq.ft (approx, including extension) |
| Stairwell opening | **3ft wide × 8.5ft deep** (x=0 to x=3, y=0 to y=8.5). Above Flight 2 (left side). Stops before beam at y=9. Trimmer bars around all edges. |
| Curing | Minimum 14 days continuous water curing (ponding method) |

### 14.2 Slab Support

The slab is supported on all four beams plus middle beam:
- Panel 1 (rear): Front beam to middle beam (9ft span) — supported on left and right beams
- Panel 2 (back): Middle beam to back beam (16ft span) — NOTE: This is a large span. Additional reinforcement required or design as two-way slab with adequate thickness.

**IMPORTANT (confirmed by structural load calculations):** The 16ft span (middle beam to back beam) is at the LIMIT for a 6" (150mm) slab. Options:
- Increase slab to 7" (175mm) in the back bay with 12mm @ 125mm c/c bottom steel
- OR increase to 8" (200mm) for additional safety margin
- OR add a secondary beam at mid-span (y≈17, would require new columns on side walls)

---

## 15. DPC (Damp Proof Course)

| Parameter | Value |
|-----------|-------|
| Position | On top of ALL plinth walls, before superstructure walls begin |
| Thickness | 20mm |
| Mix | 1:3 cement mortar + waterproofing compound (Sika/Dr. Fixit @ 1% by weight of cement) |
| Width | Full wall width (9" for external, 4.5" for internal) |
| Application | Smooth, level surface — troweled and cured 3 days |

---

## 16. MATERIAL SPECIFICATIONS

### 16.1 Concrete

| Grade | Mix Ratio | Use |
|-------|-----------|-----|
| M20 | 1:1.5:3 | Columns, beams, slab, floor slab, stair waist slab, septic tank |
| M15 | 1:2:4 | PCC bed, leveling, non-structural |
| M10 | 1:3:6 | Foundation PCC (bed below footing) |

**Materials:**
- Cement: OPC 43/53 grade (Ultratech, ACC, or equivalent), fresh stock (< 3 months old)
- Sand (ret/baalu): River sand, Zone-II grading, clean, free from organic matter
- Aggregate (gitti): 20mm crushed stone (for slabs/beams), 40mm (for footings)
- Water: Clean, potable, free from salts/oil

### 16.2 Steel Reinforcement

| Type | Grade | Use |
|------|-------|-----|
| TMT bars (sariya) | Fe500 / Fe500D | All RCC work — columns, beams, slab, stair |
| Wire mesh (jali) | 6mm mild steel | Floor slab reinforcement |
| Stirrups (ring) | 8mm TMT | Column ties, beam stirrups |
| Binding wire | 18-gauge GI | Tying reinforcement |

### 16.3 Masonry

| Item | Specification |
|------|--------------|
| Bricks (eent) | First class table-moulded, 9" × 4.5" × 3", well-burnt, copper-colored, uniform |
| Mortar — walls | 1:6 cement:sand (for walls above plinth) |
| Mortar — plinth | 1:4 cement:sand (for plinth masonry, stronger) |
| Stone — plinth | Local stone rubble (if available) OR first-class brick |

### 16.4 Miscellaneous Materials

| Item | Specification |
|------|--------------|
| Rolling shutter | MS galvanized, 18-gauge laths, manual gear |
| MS pipes (handrail) | 1.5" outer diameter, 16-gauge, galvanized |
| PVC pipes (drain) | 4" (110mm) SWR type, IS 13592 |
| Anti-termite | Chlorpyrifos 20% EC @ 5L/sq.m (as per IS 6313) |
| Waterproofing compound | Integral type (Sika/Dr. Fixit) for DPC and toilet |
| IPS finish | Cement + marble dust polish, smooth troweled |

---

## 17. CONSTRUCTION SEQUENCE (Summary)

This is a brief sequence overview. Refer to the detailed contractor-brief for step-by-step instructions.

### Phase 1: Foundation & Plinth (Neenv aur Chabutra)
1. Excavation (khudaayi) for footings as per foundation document
2. PCC bed (M10) in footing trenches
3. Footing construction (stepped/pad footings for columns, strip for walls)
4. Column starter bars (from footing, projecting up through plinth)
5. Plinth wall construction (stone/brick masonry in CM 1:4) — up to 3ft height
6. Anti-termite treatment on soil inside plinth
7. Earth filling (mitti bharaayi) in 6" layers — water + compact each layer
8. DPC on all plinth walls
9. PCC bed (3-4" M15) over compacted fill

### Phase 2: Ground Floor Superstructure (Deewar aur Pillar)
10. Column casting (pillar dhulaayi) — all 8 columns, 12ft height, M20
11. External wall construction (9" brick in CM 1:6) — up to beam level
12. Internal partition wall (4.5" brick) — stair zone partition
13. Leave openings for: toilet door, stair gate, rolling shutter, vents, future windows
14. Cast RCC lintels above all openings (except shutter — beam acts as lintel)
15. Cast RCC lintel at future window positions

### Phase 3: Beams & Slab (Beam aur Chhat)
16. Shuttering (centering) for all beams (sanchya lagaana)
17. Beam reinforcement — tie as per schedule, ensure lap lengths (40d)
18. Slab shuttering — level, properly propped (support from below)
19. Slab reinforcement — lay as per design, tie securely, use cover blocks
20. Leave stairwell opening (block with temporary form, do not pour there)
21. Concrete pouring — all beams + slab in ONE continuous pour (M20)
22. Curing — minimum 14 days ponding (paani bharna)
23. De-shuttering — beams/slab props remain 21 days minimum

### Phase 4: Staircase & Finishes (Seedhi aur Finishing)
24. Stair waist slab casting (5" RCC) — after GF structure is done
25. Build steps on waist slab (brick masonry + plaster)
26. Landing slab (6" RCC) — supported on side walls
27. Toilet floor (anti-skid tiles, sloped to drain)
28. Storage floor (4" RCC + IPS finish)
29. Plumbing rough-in (toilet drain, water supply)
30. Install rolling shutter, doors, gates
31. Handrail fabrication and installation
32. External plaster + internal plaster
33. Paint / whitewash

### Phase 5: External Works (Baahari Kaam)
34. Ramp construction (RCC, grooved surface)
35. Gate steps construction
36. Septic tank construction (RCC)
37. Soak pit construction
38. Underground drainage pipeline
39. Backfilling and site leveling

---

## 18. KEY DIMENSIONS SUMMARY (Quick Reference)

```
    ┌─────────────────────────────────────────────────────────┐
    │                  QUICK REFERENCE                         │
    ├─────────────────────────────────────────────────────────┤
    │ Building internal:     20ft (W) × 25ft (D) × 12ft (H)  │
    │ External walls:        9" (230mm)                       │
    │ Internal partition:    4.5" (115mm)                      │
    │ Columns:               9" × 12", total 8 nos.          │
    │ Plinth height:         3ft above NGL                    │
    │ Slab thickness:        6" RCC (M20)                     │
    │ Beams (back/middle):   9" × 20"                        │
    │ Beams (front):         9" × 20"                        │
    │ Beams (left/right):    9" × 24"                        │
    │ Shutter opening:       10ft W × 10ft H                  │
    │ Stair zone:            6ft W × ~9ft D                   │
    │ Toilet:                2.75ft W × 5ft D                 │
    │ Storage clear:         ~14ft W × 25ft D = 350 sq.ft    │
    │ Ramp:                  12ft W × 8ft L, slope 1:2.67    │
    │ Steps:                 5 nos., 6ft wide                 │
    │ Septic tank:           8ft × 4ft × 5.5ft (2000L)       │
    │ Soak pit:              5ft dia × 7ft deep               │
    └─────────────────────────────────────────────────────────┘
```

---

## 19. IMPORTANT NOTES & CLARIFICATIONS

1. **20ft is INTERNAL width** — side walls (9" each) are extra on both sides. Total external width = 21ft 6".

2. **25ft is INTERNAL depth** — front/back walls (9" each) are extra. Total external depth = 26ft 6".

3. **All columns are IN walls** — no column face is exposed inside the storage area. The storage space is completely clear and column-free.

4. **C6 and C7 pillar widths (1ft each)** reduce the total internal 20ft into segments: 6ft + 1ft + 10ft + 1ft + 2ft = 20ft ✓

5. **Middle beam at z=16 (9ft from front wall)** — this is measured from the inner face of the front wall. It aligns with the first floor room partition that will be built above it.

6. **Stair landing is at z=6 to z=8.5** — this is safely BEFORE the middle beam at z=16. No beam conflict exists. Headroom under beam (from landing): beam soffit at +10ft 9" (12ft - 15" beam), landing at +6ft, clearance = 4ft 9" at landing (adequate for passage, user is on landing turning not standing).

7. **The toilet is UNDER Flight 2** — since Flight 2 goes from z=8.5 (at 12ft height) to z=1.5 (at 6ft height), the headroom at z=0 (toilet entry) is full 12ft, and decreases as you go deeper. At z=5 (toilet back wall), Flight 2 is at approximately 6 + (8.5-5)/(8.5-1.5) × 6 = 6 + 3 = 9ft height. So minimum headroom in toilet ≈ 9ft. Very comfortable.

8. **No lobby at stairs** — the stair gate opens directly to the first step of Flight 1. Users enter from outside through the 2.75ft gate and immediately start climbing.

9. **Structural engineer to verify** the 16ft clear span between middle beam and back beam for the 6" slab. This may need thicker slab or additional reinforcement in that panel.

10. **The 6ft front extension (shade)** is a PURE CANTILEVER — no walls, no pillars below it. Slab hangs from the front beam. Top reinforcement (10mm @ 5" c/c, anchored 10ft into main slab) is CRITICAL. Side walls stop at the front wall line (z=0).

---

## 20. DRAWING INDEX

For complete construction, refer to the following documents:
- Foundation specification (separate document)
- First floor specification (separate document)
- Electrical & plumbing layout
- Bill of quantities
- Contractor brief (detailed construction instructions)

---

**END OF DOCUMENT**

*This is the FINAL authoritative specification for the Ground Floor Civil Work. All previous versions, discussions, and preliminary drawings are superseded by this document. In case of any conflict with earlier documents, THIS document prevails.*
