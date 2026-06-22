# Column Grid Plan — Centerline & Structural Analysis

**Building:** Farm Storage + Residence, Moradabad, UP
**Footprint:** 20ft × 25ft (internal clear dimensions)
**Date:** June 2026

---

## 1. Column Spatial Coordinates

### Ground Floor Columns (z = 3.0ft to 15.0ft, height = 12ft)
### First Floor Columns (z = 15.5ft to 27.5ft, height = 12ft)

All columns are 9"×12" RCC. Position is where the column starts (x_start, y_start). Center = geometric center.

| Column | X_start (ft) | Y_start (ft) | Width_X (ft) | Depth_Y (ft) | **Center_X** | **Center_Y** | Wall | Orientation |
|--------|-------------|-------------|-------------|-------------|------------|------------|------|-------------|
| C1 | -0.750 | 24.000 | 0.750 (9") | 1.000 (12") | **-0.375** | **24.500** | Back + Left corner | 12" along Y |
| C2 | 20.000 | 24.000 | 0.750 (9") | 1.000 (12") | **20.375** | **24.500** | Back + Right corner | 12" along Y |
| C3 | -0.750 | 8.500 | 0.750 (9") | 1.000 (12") | **-0.375** | **9.000** | Left wall @ 9ft from front | 12" along Y |
| C4 | 20.000 | 8.500 | 0.750 (9") | 1.000 (12") | **20.375** | **9.000** | Right wall @ 9ft from front | 12" along Y |
| C5 | -0.750 | -0.750 | 0.750 (9") | 1.000 (12") | **-0.375** | **-0.250** | Front + Left corner | 12" along Y |
| C6 | 6.000 | -0.750 | 1.000 (12") | 0.750 (9") | **6.500** | **-0.375** | Front wall @ 6ft | 12" along X |
| C7 | 17.000 | -0.750 | 1.000 (12") | 0.750 (9") | **17.500** | **-0.375** | Front wall @ 17ft | 12" along X |
| C8 | 20.000 | -0.750 | 0.750 (9") | 1.000 (12") | **20.375** | **-0.250** | Front + Right corner | 12" along Y |

**Note:** 
- Negative coordinates indicate the column is in the WALL zone (outside the 20×25ft internal space)
- All columns flush within 9" walls (not protruding)
- C6, C7 have 12" along X-axis (front wall direction); all others have 12" along Y-axis (side wall direction)
- First floor columns (col_1f_*) are at SAME X,Y positions, different Z range (15.5-27.5ft)
- C6 and C7 do NOT extend to first floor (front wall doesn't exist at 1F)

---

## 2. Column Grid Plan (2D Centerline)

```
    Y-AXIS (DEPTH: front=0, back=25)
    ↑
    │
25.0├─────────────────────────────────────────────────────────────── BACK WALL
    │
24.5├────●C1─────────────────────────────────────────────────●C2──── Grid Line A
    │    │                                                    │       (y=24.5)
    │    │                                                    │
    │    │              BACK BAY                              │
    │    │         (C3-C1 span: 15.5ft)                      │
    │    │                                                    │
    │    │                                                    │
    │    │                                                    │
 9.0├────●C3─────────────────────────────────────────────────●C4──── Grid Line B
    │    │              (y=9.0)                               │       (y=9.0)
    │    │                                                    │
    │    │              FRONT BAY                             │
    │    │         (C5-C3 span: 9.25ft)                      │
    │    │                                                    │
    │    │                                                    │
-0.3├────●C5──────────●C6────────────────────●C7─────────────●C8──── Grid Line C
    │              (y≈-0.3)                                          (y≈-0.3)
    │
────┼────┼─────────────┼──────────────────────┼──────────────┼─────→ X-AXIS
   -0.4  │            6.5                    17.5           20.4     (WIDTH)
         │             │                      │              │
    Grid Line 1   Grid Line 2           Grid Line 3    Grid Line 4
    (x=-0.375)    (x=6.5)              (x=17.5)       (x=20.375)
```

---

## 3. Center-to-Center Distances

### X-Direction (along front wall, Grid Line C):

| From | To | Distance (c/c) | Clear Span | Zone |
|------|------|----------------|------------|------|
| C5 | C6 | **6.875 ft** | 6.0 ft | Gate + Stair zone |
| C6 | C7 | **11.000 ft** | 10.0 ft | **SHUTTER (longest X-span!)** |
| C7 | C8 | **2.875 ft** | 2.0 ft | Solid wall |
| C5 | C8 | **20.750 ft** | — | Total width (external) |

### Y-Direction (along left wall, Grid Line 1):

| From | To | Distance (c/c) | Clear Span | Zone |
|------|------|----------------|------------|------|
| C5 | C3 | **9.250 ft** | 8.25 ft | Front bay (stair + balcony zone) |
| C3 | C1 | **15.500 ft** | 14.50 ft | **BACK BAY (longest Y-span!)** |
| C5 | C1 | **24.750 ft** | — | Total depth (external) |

### Y-Direction (along right wall, Grid Line 4):

| From | To | Distance (c/c) | Clear Span | Zone |
|------|------|----------------|------------|------|
| C8 | C4 | **9.250 ft** | 8.25 ft | Front bay |
| C4 | C2 | **15.500 ft** | 14.50 ft | **BACK BAY (longest Y-span!)** |

### Cross-Width Beam Spans (X-direction, full width):

| Beam | From | To | Span (c/c) | Beam Size |
|------|------|------|-----------|-----------|
| Back beam | C1 | C2 | **20.750 ft** | 9"×20" (DEEP) |
| Middle beam | C3 | C4 | **20.750 ft** | 9"×20" (DEEP) |
| Front beam | C5 | C8 | **20.750 ft** | 9"×15" (segmented by C6, C7) |

---

## 4. Maximum Clear Spans & Critical Load Points

### Sorted by Span Length (largest first):

| Rank | Span | Clear Distance | Beam Required | Load Type |
|------|------|---------------|---------------|-----------|
| **1** | C3→C1 (Y-dir) | **14.50 ft** | Side beams 9"×15" (continuous 2-span) | Slab tributary load |
| **2** | C6→C7 (X-dir) | **10.00 ft** | Front beam 9"×15" (shutter span) | Wall above shutter + slab |
| **3** | C5→C3 (Y-dir) | **8.25 ft** | Side beams 9"×15" | Slab + stair loads |
| **4** | Back beam C1→C2 | **20.75 ft c/c** | 9"×20" DEEP beam | Full width, back wall + 1F room |
| **5** | Middle beam C3→C4 | **20.75 ft c/c** | 9"×20" DEEP beam | Full width, 1F partition + room |
| **6** | C5→C6 (X-dir) | **6.00 ft** | Front beam 9"×15" | Stair zone wall |
| **7** | C7→C8 (X-dir) | **2.00 ft** | Front beam 9"×15" | Small solid wall |

### Heaviest Beam Loads (where most reinforcement needed):

| Priority | Beam | Why Heaviest |
|----------|------|--------------|
| **🔴 #1** | **Back beam (C1-C2), 9"×20"** | Spans 20.75ft, carries: back wall weight + 1F room slab (16ft tributary) + future roof load. LONGEST single-span beam in the building. |
| **🔴 #2** | **Middle beam (C3-C4), 9"×20"** | Spans 20.75ft, carries: 1F partition wall + slab from both sides (front bay 9ft + back bay 15.5ft tributary) + 1F room load above. Also supports the sloped stair-slab. |
| **🟡 #3** | **Shutter beam (C6-C7), 9"×15"** | Spans 11ft c/c (10ft clear), carries: wall above 10ft×10ft opening + 1F slab load. Critical because it has a large opening below (no wall support beneath). |
| **🟡 #4** | **Side beams (left/right), 9"×15"** | 2-span continuous (9.25ft + 15.5ft), carries: slab tributary width (~10ft) on each side. The 15.5ft back span is the critical section. |

---

## 5. Grid Summary Diagram

```
                    ←─────────── 20.75 ft (c/c, full width) ──────────────→

                    C1                                                   C2
              ●═════════════════════════════════════════════════════════════●  ─┐
              ║         BACK BEAM (9"×20", 20.75ft span)                   ║   │
              ║                                                            ║   │
              ║                                                            ║   │
              ║                                                            ║   │ 15.50 ft
              ║              BACK BAY                                       ║   │ (c/c)
              ║         (critical: longest Y-span)                         ║   │
              ║                                                            ║   │
              ║                                                            ║   │
              ║                                                            ║   │
              C3                                                           C4  │
              ●═════════════════════════════════════════════════════════════●  ─┤
              ║         MIDDLE BEAM (9"×20", 20.75ft span)                 ║   │
              ║                                                            ║   │
              ║              FRONT BAY                                      ║   │ 9.25 ft
              ║                                                            ║   │ (c/c)
              ║                                                            ║   │
              C5          C6                          C7                   C8  │
              ●═══════════●═══════════════════════════●════════════════════●  ─┘
              ←── 6.875 ──→←──────── 11.000 ────────→←──── 2.875 ───→
                  ft            ft (SHUTTER)              ft

              FRONT BEAM (9"×15", segmented: 6.875 + 11.0 + 2.875)
```

---

## 6. Structural Verification Notes

1. **Back bay Y-span (14.5ft clear):** The 6" slab spanning 14.5ft needs verification. For residential loads, maximum slab span for 6" is typically 12-14ft. At 14.5ft, the slab is at its LIMIT. Consider:
   - Increasing slab to 7" in the back bay, OR
   - Adding a secondary beam at mid-span (would need a new column on each side wall at y≈17)

2. **Deep beams (20.75ft span):** These are the most critical elements. Ensure:
   - Bottom steel: 4-20mm tor (minimum)
   - Stirrups at 150mm c/c near supports (within L/4 from each column)
   - No holes/sleeves cut through these beams

3. **Shutter beam (11ft span with 10ft opening below):** No masonry support beneath for 10ft — the beam carries everything. Ensure adequate reinforcement for this unsupported span.

4. **Slab panels:**
   - Front bay: 9.25ft × 11ft (or 6.875 + 2.875 sub-panels) — comfortable
   - Back bay: 15.5ft × 20.75ft — CRITICAL (needs structural engineer verification for 6" slab)
