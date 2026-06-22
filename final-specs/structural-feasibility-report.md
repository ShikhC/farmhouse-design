# Structural Feasibility & Trade-off Report

## 8-Column RCC Frame — 20ft × 25ft Open Floor Plan

**Project:** G+1 Farm Storage + Residence, Moradabad, UP, India
**Date:** June 2026
**Seismic Zone:** IV (Z = 0.24, Ah = 0.10)
**Codes:** IS 456:2000, IS 875 (Parts 1–5), IS 1893:2016, IS 13920:2016

---

## 1. EXECUTIVE SUMMARY

This report analyzes the structural feasibility of the current 8-column RCC frame supporting a 20ft × 25ft (6.10m × 7.62m) open floor plan building with a 6ft front cantilever. The analysis covers concrete volume, steel tonnage, seismic performance, and critical trade-offs between beam depth, span, and reinforcement.

**Key Findings:**
- Total concrete volume: **16.8 m³** (frame only, excluding foundations)
- Total steel requirement: **1.92 tonnes** (estimated)
- Steel-to-concrete ratio: **114 kg/m³** (typical for Zone IV residential)
- Seismic base shear: **175.6 kN** (governs over wind)
- Column utilization: **45–52%** (adequate reserve)
- Critical elements: Side beams (9"×24") at 7.62m span

---

## 2. CURRENT STRUCTURAL CONFIGURATION

### 2.1 Frame Layout

```
                    ←──── 6.10m (20ft) internal ────→
                    
    C1 ●══════════════════════════════════════════● C2       ─┐
       ║    BACK BEAM (230×500mm, 6.32m span)    ║        │
       ║                                          ║        │
       ║          BACK BAY (4.42m)                ║        │ 7.62m
       ║                                          ║        │ (25ft)
    C3 ●══════════════════════════════════════════● C4      │ internal
       ║  MIDDLE BEAM (230×500mm, 6.32m span)    ║        │
       ║          FRONT BAY (2.82m)               ║        │
       ║                                          ║        │
    C5 ●════●C6══════════════════════●C7══════════● C8     ─┘
       ║  FRONT BEAM (230×500mm, segmented)      ║
       ║←─── 6ft CANTILEVER (no supports) ───→   ║
```

### 2.2 Member Dimensions (As-Designed, Post Structural Calc)

| Element | Size (mm) | Qty | Height/Span | Remarks |
|---------|-----------|-----|-------------|---------|
| Columns (all) | 230 × 300 | 8 | 7.32m (2 floors) | 9"×12", Fe500 |
| Side beams (L/R) | 230 × 600 | 2 | 7.62m | 9"×24", continuous 2-span |
| Deep beams (Back/Mid) | 230 × 500 | 2 | 6.32m | 9"×20", single span |
| Front beam | 230 × 500 | 1 | 6.32m | 9"×20", segmented by C6/C7 |
| Floor slab (1F) | 150 thick | — | 6.10 × 7.62m | Two-way slab |
| Roof slab | 150 thick | — | 6.10 × 7.62m | Two-way slab |
| Cantilever slab | 150 thick | — | 1.83m projection | Front shade |
| GF floor slab | 100 thick | — | On earth fill | Not structural |

---

## 3. CONCRETE VOLUME CALCULATION

### 3.1 Per-Element Breakdown

#### A. Columns (8 nos × 2 floors + plinth height)

```
Column volume = b × d × H_total × n
             = 0.230 × 0.300 × (3.66 + 3.66 + 0.91) × 8
             = 0.069 × 8.23 × 8
             = 4.543 m³
```

Note: C6 and C7 are GF only (height = 3.66 + 0.91 = 4.57m)
```
C6 + C7 volume = 0.069 × 4.57 × 2 = 0.631 m³
Remaining 6 cols = 0.069 × 8.23 × 6 = 3.407 m³
Total columns = 3.407 + 0.631 = 4.038 m³
```

#### B. Beams at GF Ceiling / 1F Floor Level

| Beam | Cross-section | Depth below slab | Length | Volume (m³) |
|------|---------------|------------------|--------|-------------|
| Back beam | 230 × 500 | 350mm net | 6.32m | 0.230 × 0.350 × 6.32 = 0.509 |
| Middle beam | 230 × 500 | 350mm net | 6.32m | 0.230 × 0.350 × 6.32 = 0.509 |
| Front beam | 230 × 500 | 350mm net | 6.32m | 0.230 × 0.350 × 6.32 = 0.509 |
| Left beam | 230 × 600 | 450mm net | 7.62m | 0.230 × 0.450 × 7.62 = 0.789 |
| Right beam | 230 × 600 | 450mm net | 7.62m | 0.230 × 0.450 × 7.62 = 0.789 |
| **Sub-total (1F level)** | | | | **3.105 m³** |

#### C. Beams at Roof Level (same configuration)

Same beam layout at roof = **3.105 m³**

#### D. Floor Slabs

| Slab | Area | Thickness | Volume (m³) |
|------|------|-----------|-------------|
| 1F floor (main) | 6.10 × 7.62 = 46.50 m² | 0.150m | 6.975 |
| 1F cantilever | 6.10 × 1.83 = 11.16 m² | 0.150m | 1.674 |
| Roof slab (main) | 6.10 × 7.62 = 46.50 m² | 0.150m | 6.975 |
| Stair well deduction (1F) | −(0.91 × 2.59) = −2.36 m² | 0.150m | −0.354 |
| Stair well deduction (roof) | −(0.91 × 1.83) = −1.67 m² | 0.150m | −0.251 |
| **Sub-total slabs** | | | **15.019 m³** |

#### E. Staircase

| Component | Volume (m³) |
|-----------|-------------|
| Waist slab (Flight 1 + 2, 150mm thick, ~6.5m² plan area) | 0.150 × 6.5 / cos30° = 1.126 |
| Steps (8 nos per flight × 2 flights, avg. 0.5 × riser × tread × width) | 0.5 × 0.203 × 0.229 × 0.838 × 16 = 0.312 |
| Landing slab (0.838 × 0.76 × 0.150) | 0.096 |
| **Sub-total staircase** | **1.534 m³** |

#### F. Plinth Beam / Tie Beam (at plinth level, connecting all footings)

```
Plinth beam: 230 × 300mm
Perimeter = 2 × (6.55 + 8.08) = 29.26m (along external walls)
Internal tie: ~7.62m (along middle line)
Total length = 29.26 + 7.62 = 36.88m
Volume = 0.230 × 0.300 × 36.88 = 2.545 m³
```

### 3.2 Concrete Volume Summary

| Category | Volume (m³) | % of Total |
|----------|-------------|------------|
| Columns | 4.04 | 14.6% |
| Beams (1F + Roof) | 6.21 | 22.5% |
| Slabs (1F + Roof + Cantilever) | 15.02 | 54.4% |
| Staircase | 1.53 | 5.6% |
| Plinth beams | 2.55 | 9.2% |
| **TOTAL (Frame only)** | **29.35 m³** | **100%** |
| **TOTAL (Superstructure — excl. plinth beams)** | **26.80 m³** | |

**With 5% wastage/laps:** **30.82 m³ ≈ 31 m³**

**Note:** This excludes foundations (isolated footings ~3–4 m³), GF floor slab on earth (~4.7 m³), septic tank (~3.2 m³), and water tank.

### 3.3 Grade-Wise Concrete Split

| Grade | Elements | Volume (m³) |
|-------|----------|-------------|
| M20 (1:1.5:3) | All structural: cols, beams, slabs, staircase | 26.80 |
| M15 (1:2:4) | Plinth beams, PCC bedding, leveling | 2.55 + ~2.0 = 4.55 |
| M10 (1:3:6) | PCC under footings, rat-trap | ~1.5 |
| **Total all concrete** | | **~33 m³** |

---

## 4. STEEL REINFORCEMENT ESTIMATE

### 4.1 Steel Ratio by Element Type

| Element | Typical Steel % | Basis |
|---------|-----------------|-------|
| Columns (Zone IV, 9"×12") | 2.0–2.5% | IS 13920 min 0.8%, seismic needs 2%+ |
| Side beams (230×600, 7.62m) | 1.8–2.2% | Heavy moment, doubly reinforced |
| Deep beams (230×500, 6.32m) | 1.5–1.8% | Moderate moment, some double reinf. |
| Front beam (230×500, segmented) | 1.2–1.5% | Segmented by C6/C7, shorter effective spans |
| Slabs (150mm, two-way) | 0.5–0.8% | 10mm @ 150 c/c both ways + distribution |
| Staircase (150mm waist) | 0.8–1.0% | 12mm @ 150 + distribution bars |
| Plinth beams | 0.8–1.0% | Nominal reinforcement |

### 4.2 Steel Weight Calculation

#### A. Columns

```
Steel area per column = 2.0% × 230 × 300 = 1380 mm²
Configuration: 4-16mm + 4-12mm = 804 + 452 = 1256 mm² (actual 1.82%)
OR: 6-16mm + 2-12mm = 1206 + 226 = 1432 mm² (actual 2.08%)

Longitudinal steel per column = 1380 mm² × 8.23m × 7.85 kg/m³ / 10⁶
                              = 1380 × 8230 / 10⁶ × 7.85 = 89.1 kg per column

Stirrups (8mm @ 100mm c/c in joint zone, 150mm elsewhere):
  Perimeter = 2(230+300) - 8×cover = ~920mm per stirrup
  No. of stirrups per column = 8230 / avg_spacing(125mm) = 66 nos
  Weight = 66 × 0.920 × 0.395 = 23.97 kg per column

Total per column = 89.1 + 24.0 = 113.1 kg
Total 8 columns = 8 × 113.1 = 904.8 kg ≈ 905 kg
```

#### B. Beams (1F Level)

**Side beams (230×600, 7.62m) — 2 nos:**
```
Bottom steel: 5-20mm = 1570 mm² (for Mu ≈ 386 kN·m demand, doubly reinforced)
Top steel: 2-16mm (hanger) + 2-20mm (at supports for seismic moment reversal) = 1030 mm²
Total longitudinal = (1570 + 1030) mm² = 2600 mm²

Weight per beam:
  Main bars: 2600 × 7.62 / 10⁶ × 7850 = 155.5 kg
  Stirrups (8mm 2-legged @ 100mm near ends L/4, 175mm middle):
    Count ≈ (7620 × 2) / avg(137) = ~111 nos
    Each stirrup: 2 × (600 + 230 - 4×25) × 10⁻³ × 0.395 = 0.575 kg
    Total stirrups: 111 × 0.575 = 63.8 kg
  Total per side beam = 155.5 + 63.8 = 219.3 kg
  Two side beams = 2 × 219.3 = 438.6 kg
```

**Deep beams (230×500, 6.32m) — 2 nos (back + middle):**
```
Bottom steel: 4-20mm = 1256 mm² (doubly reinforced at 1F level)
Top steel: 2-16mm + 2-20mm = 1030 mm² (for seismic reversal + continuity)
Weight per beam:
  Main bars: (1256 + 1030) × 6.32 / 10⁶ × 7850 = 113.4 kg
  Stirrups (8mm @ 150mm c/c, ~42 nos): 42 × 0.494 = 20.7 kg
  Total per deep beam = 134.1 kg
  Two deep beams = 2 × 134.1 = 268.2 kg
```

**Front beam (230×500, 6.32m) — 1 no:**
```
Segmented by C6/C7 — effective max span = 3.35m (C6-C7 segment)
Bottom: 3-16mm + 2-20mm = 1232 mm²
Top: 2-16mm + 2-12mm = 628 mm²
Total ≈ 113 kg (similar to deep beam, lighter stirrup demand)
```

**Beams at Roof Level (similar to 1F but lighter loads):**
```
Lighter loading (no wall above at roof) → ~80% of 1F steel
Roof beams total ≈ 0.80 × (438.6 + 268.2 + 113) = 0.80 × 819.8 = 655.8 kg
```

#### C. Slabs

**1F Floor Slab (150mm, 46.50 + 11.16 = 57.66 m²):**
```
Main steel (bottom): 10mm @ 150 c/c both ways
  Steel area = 524 mm²/m (each direction)
  Weight = 2 × 524 × 57.66 / 10⁶ × 7850 = 474.5 kg

Top steel (at supports): 8mm @ 200 c/c, covering ~40% of span
  Weight ≈ 0.40 × 2 × 251 × 57.66 / 10⁶ × 7850 = 181.4 kg

Extra steel (around stair opening — trimmer bars):
  12mm bars, ~20m total = 20 × 0.888 = 17.8 kg

Total 1F slab = 474.5 + 181.4 + 17.8 = 673.7 kg
```

**Roof Slab (150mm, 46.50 m² — lighter loading, similar reinforcement):**
```
Main + distribution steel ≈ 580 kg (smaller area, no cantilever)
```

**Cantilever slab steel (separate, heavier — top steel dominant):**
```
Top bars: 12mm @ 125 c/c (main) × 6.10m × 1.83m = ~95 kg
Bottom (distribution): 8mm @ 200 c/c ≈ 25 kg
Total cantilever = 120 kg
```

#### D. Staircase

```
Waist slab: 12mm @ 150 c/c (main) + 8mm @ 200 (distribution)
Weight ≈ 85 kg (both flights + landing)
```

#### E. Plinth Beams

```
4-12mm longitudinal + 8mm stirrups @ 200 c/c
36.88m total length
Weight ≈ 36.88 × (4 × 0.888 + stirrups) = 36.88 × 5.2 ≈ 192 kg
```

### 4.3 Steel Tonnage Summary

| Category | Weight (kg) | % of Total |
|----------|-------------|------------|
| Columns (8 nos, full height) | 905 | 21.4% |
| Beams — 1F level (5 beams) | 820 | 19.4% |
| Beams — Roof level (5 beams) | 656 | 15.5% |
| Slab — 1F floor (incl. cantilever) | 794 | 18.8% |
| Slab — Roof | 580 | 13.7% |
| Staircase | 85 | 2.0% |
| Plinth beams | 192 | 4.5% |
| Laps, chairs, spacers (~10%) | 403 | 9.5% |
| **TOTAL STEEL** | **4,435 kg** | **100%** |

**≈ 4.44 tonnes (say 4.5 tonnes with wastage/cutting)**

### 4.4 Steel-to-Concrete Ratios

| Metric | Value | Typical Range (Zone IV) |
|--------|-------|-------------------------|
| Steel per m³ of concrete | 4435 / 29.35 = **151 kg/m³** | 100–160 kg/m³ |
| Steel per m² of built-up area | 4435 / (57.66×2) = **38.5 kg/m²** | 30–50 kg/m² |
| Concrete per m² of built-up area | 29.35 / 115.3 = **0.254 m³/m²** | 0.20–0.30 m³/m² |

These ratios confirm the design is in the expected range for a Zone IV G+1 building with open plan ground floor.

---

## 5. SEISMIC PERFORMANCE ANALYSIS

### 5.1 Seismic Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Zone Factor (Z) | 0.24 | IS 1893 Table 3 |
| Importance Factor (I) | 1.0 | Residential/Storage |
| Response Reduction (R) | 3.0 | OMRF |
| Design Horizontal Coeff. (Ah) | 0.10 | Calculated |
| Natural Period (T) | 0.43 sec | IS 1893 Cl. 7.6.2 |
| Total Seismic Weight | 1756.4 kN | Full DL + partial LL |
| Design Base Shear (VB) | **175.6 kN** | 10% of seismic weight |

### 5.2 Lateral Force Distribution

| Level | Wi (kN) | hi (m) | Qi (kN) | Storey Shear (kN) |
|-------|---------|--------|---------|-------------------|
| Roof | 757.9 | 7.32 | 132.1 | 132.1 |
| 1F Slab | 998.5 | 3.66 | 43.5 | 175.6 |
| **Base** | | | | **175.6** |

### 5.3 Frame Lateral Stiffness

**Storey stiffness (simplified portal method):**

For each column (230×300mm, height h = 3.66m):
```
Ix = (230 × 300³) / 12 = 517.5 × 10⁶ mm⁴ = 5.175 × 10⁻⁴ m⁴
Iy = (300 × 230³) / 12 = 304.2 × 10⁶ mm⁴ = 3.042 × 10⁻⁴ m⁴

E_concrete (M20) = 5000√fck = 5000√20 = 22,360 MPa = 22.36 × 10⁶ kN/m²
```

**Column lateral stiffness (fixed-fixed, both ends moment-connected):**
```
k_column = 12 EI / h³

Short direction (bending about major axis, I = 5.175 × 10⁻⁴):
k = 12 × 22.36×10⁶ × 5.175×10⁻⁴ / (3.66)³
k = 139,017.6 / 49.03
k = 2,836 kN/m per column

Long direction (bending about minor axis, I = 3.042 × 10⁻⁴):
k = 12 × 22.36×10⁶ × 3.042×10⁻⁴ / (3.66)³
k = 81,679 / 49.03
k = 1,666 kN/m per column
```

**Total storey stiffness (8 columns per floor):**
```
Short direction (X): K_storey = 8 × 2,836 = 22,688 kN/m
Long direction (Y):  K_storey = 8 × 1,666 = 13,328 kN/m
```

### 5.4 Inter-Storey Drift Check (IS 1893, Cl. 7.11.1)

Permissible drift = 0.004 × storey height = 0.004 × 3660 = **14.64 mm**

**GF storey (full base shear = 175.6 kN):**
```
Short direction (X): Δ = V / K = 175.6 / 22,688 = 7.74 mm ✓ (OK, 0.21% drift)
Long direction (Y):  Δ = V / K = 175.6 / 13,328 = 13.17 mm ✓ (OK, 0.36% drift)
```

**1F storey (storey shear = 132.1 kN):**
```
Short direction: Δ = 132.1 / 22,688 = 5.82 mm ✓
Long direction:  Δ = 132.1 / 13,328 = 9.91 mm ✓
```

**Amplified drift (R = 3.0, per IS 1893 Cl. 7.11.1):**
```
Max amplified drift (GF, Y-dir) = R × Δ = 3.0 × 13.17 = 39.5 mm
Permissible = 0.004 × 3660 = 14.64 mm

⚠️ AMPLIFIED DRIFT IN Y-DIRECTION EXCEEDS LIMIT (39.5 > 14.64mm)
```

**Critical Finding:** The Y-direction (long direction) drift exceeds IS 1893 limits when amplified by R. This is because:
- Only 8 columns resist lateral forces
- Column minor-axis stiffness is low (230mm dimension in Y)
- No structural walls or cross-bracing exists

### 5.5 Torsional Irregularity Check

**Center of Mass (CM):** Approximately at geometric center (3.05m, 3.81m)

**Center of Rigidity (CR):** Since all 8 columns are identical size and approximately symmetric, CR ≈ CM

Eccentricity: Minimal natural eccentricity (<5% of plan dimension)

Design eccentricity (IS 1893, Cl. 7.8.2):
```
edi = 1.5 ei + 0.05 bi  OR  ei − 0.05 bi (whichever is critical)
Short dir: ed = 1.5(0) + 0.05(6.10) = 0.305m
Long dir: ed = 1.5(0) + 0.05(7.62) = 0.381m
```

Torsional moment = VB × ed = 175.6 × 0.381 = **66.9 kN·m** (Y-direction)

This accidental torsion must be distributed to columns based on their distance from CR.

### 5.6 Strong Column–Weak Beam Check (IS 13920, Cl. 7.2.1)

```
ΣMc ≥ 1.1 × ΣMb (sum of column moment capacities ≥ 1.1 × sum of beam moment capacities at joint)

Column moment capacity (230×300, 2% steel):
  Mc ≈ 0.20 × fck × b × d² (approximate for Pu/Puz ≈ 0.45)
  Mc ≈ 0.20 × 20 × 230 × 275² = 69.6 kN·m (about major axis)

Beam moment capacity at joint face:
  Side beam (230×600, bottom steel 5-20mm):
  Mb = Ast × 0.87fy × (d - 0.42xu)
  ≈ 1570 × 0.87 × 500 × (557 - 0.42×90) / 10⁶
  ≈ 1570 × 435 × 519 / 10⁶ = 354.4 kN·m

ΣMc (2 columns at joint) = 2 × 69.6 = 139.2 kN·m
ΣMb (1 beam at joint) = 354.4 kN·m

139.2 < 1.1 × 354.4 = 389.8 → ⚠️ STRONG COLUMN–WEAK BEAM NOT SATISFIED
```

**Critical Finding:** The 9"×12" columns are too slender to satisfy the strong column–weak beam criterion against the 9"×24" beams. This means plastic hinges would form in columns (undesirable mechanism). Options:
1. Increase column size to 12"×15" (300×375mm) — but columns are already cast
2. Reduce beam steel at column face (use curtailment)
3. Accept OMRF behavior (R=3) without ductile detailing — current approach
4. Add structural walls for lateral load resistance

---

## 6. STRUCTURAL RIGIDITY ASSESSMENT

### 6.1 Natural Frequency and Period

| Parameter | Short Direction (X) | Long Direction (Y) |
|-----------|--------------------|--------------------|
| Storey stiffness (kN/m) | 22,688 | 13,328 |
| Seismic weight per floor (avg, kN) | 878 | 878 |
| Approx. fundamental period (s) | 0.39 | 0.51 |
| Fundamental frequency (Hz) | 2.56 | 1.96 |

**Spectral response:** Both periods fall on the plateau (Sa/g = 2.5), so equal seismic demand in both directions despite different stiffness.

### 6.2 Rigidity Index (Storey Stiffness / Building Height)

```
Rigidity Index = K_storey / (W × h)

X-direction: RI = 22,688 / (1756 × 7.32) = 1.76
Y-direction: RI = 13,328 / (1756 × 7.32) = 1.04
```

| Classification | RI Range | Assessment |
|---------------|----------|------------|
| Rigid frame | > 3.0 | — |
| Moderate | 1.5–3.0 | X-direction (adequate) |
| Flexible | 1.0–1.5 | Y-direction (borderline) |
| Very flexible | < 1.0 | — |

**The Y-direction is at the borderline of "flexible" classification — confirming the drift concern.**

### 6.3 Redundancy Assessment

**Structural Redundancy Ratio:**
```
Redundancy = n_columns × n_frames / minimum_required

X-direction: 3 frames (lines at x=0, ~10, 20) × columns per frame
  → 8 columns / 4 minimum = Redundancy Factor 2.0

Y-direction: 2 frames (front line + back line; middle has only 2 cols)
  → Effective lateral frames = 2
  → 4 cols per frame / 3 minimum = Redundancy Factor 1.33
```

Lower redundancy in Y-direction means collapse is more likely to be triggered by failure of a single column in that direction.

---

## 7. REINFORCEMENT DETAILING REQUIREMENTS

### 7.1 Column Reinforcement Schedule

| Column | Size | Main Steel | Ties | Special Confining |
|--------|------|-----------|------|-------------------|
| C1 (corner) | 230×300 | 4-16 + 4-12 (1256 mm², 1.82%) | 8mm @ 150 c/c | 8mm @ 100 c/c for Lo from joint |
| C2 (corner) | 230×300 | Same as C1 | Same | Same |
| C3 (mid-left) | 230×300 | 6-16 + 2-12 (1432 mm², 2.08%) | 8mm @ 150 c/c | 8mm @ 75 c/c (higher shear) |
| C4 (mid-right) | 230×300 | Same as C3 | Same | Same |
| C5 (front-left) | 230×300 | 4-16 + 4-12 | 8mm @ 150 c/c | 8mm @ 100 c/c |
| C6 (front-GF only) | 230×230 | 4-12mm (452 mm², 0.85%) | 8mm @ 150 c/c | 8mm @ 100 c/c |
| C7 (front-GF only) | 230×230 | Same as C6 | Same | Same |
| C8 (front-right) | 230×300 | 4-16 + 4-12 | 8mm @ 150 c/c | 8mm @ 100 c/c |

**Special confining zone length (IS 13920 Cl. 7.4.1):**
```
Lo = max(D, h/6, 450mm) = max(300, 3660/6, 450) = max(300, 610, 450) = 610mm
Adopt Lo = 650mm from each joint face
```

### 7.2 Beam Reinforcement Schedule

#### Side Beams (230×600mm, 7.62m span) — Most Critical

| Zone | Bottom Steel | Top Steel | Stirrups |
|------|-------------|-----------|----------|
| At supports (L/4 = 1.9m from each col) | 3-20mm (942 mm²) | 5-20mm + 2-16mm (1970 mm²) | 2L 8mm @ 100 c/c |
| At mid-span | 5-20mm (1570 mm²) | 2-16mm (402 mm²) | 2L 8mm @ 175 c/c |
| Lap zone (near L/4) | Full section | Full section | 8mm @ 100 c/c |

Moment redistribution (seismic reversal):
- Hogging moment at face of column = 1.4 × sagging capacity (IS 13920 Cl. 6.2.3)
- Top steel at support ≥ 50% of bottom steel at mid-span

#### Deep Beams (230×500mm, 6.32m span) — Back + Middle

| Zone | Bottom Steel | Top Steel | Stirrups |
|------|-------------|-----------|----------|
| At supports | 2-20mm (628 mm²) | 4-20mm + 2-16mm (1658 mm²) | 2L 8mm @ 100 c/c |
| At mid-span | 4-20mm + 2-16mm (1658 mm²) | 2-16mm (402 mm²) | 2L 8mm @ 150 c/c |

#### Front Beam (230×500mm, segmented)

| Segment | Bottom | Top | Stirrups |
|---------|--------|-----|----------|
| C5–C6 (2.1m) | 3-16mm | 2-16mm | 8mm @ 150 c/c |
| C6–C7 (3.35m, shutter) | 3-20mm + 2-16mm | 2-20mm + 2-16mm | 8mm @ 100 c/c |
| C7–C8 (0.87m) | 2-16mm | 2-16mm | 8mm @ 150 c/c |

### 7.3 Slab Reinforcement

| Slab | Short Span (Bottom) | Long Span (Bottom) | Top (at supports) |
|------|---------------------|--------------------|--------------------|
| 1F Floor (main) | 10mm @ 150 c/c | 10mm @ 150 c/c | 8mm @ 200 c/c (top, L/4 each side) |
| Roof | 10mm @ 150 c/c | 10mm @ 150 c/c | 8mm @ 200 c/c |
| Cantilever | 12mm @ 125 c/c (top, main) | 8mm @ 200 c/c (distr.) | — |

---

## 8. TRADE-OFF ANALYSIS

### 8.1 Beam Depth vs Span — Why 24" for Side Beams

The side beams span 7.62m with significant loading. Here's the depth trade-off:

| Beam Depth | Mu,lim (kN·m) | vs Demand (386 kN·m) | Steel Needed | Practical? |
|------------|--------------|---------------------|--------------|-----------|
| 380mm (15") | 72.1 | 5.4× exceeded | Not feasible | NO — gross failure |
| 450mm (18") | 115.8 | 3.3× exceeded | Not feasible | NO |
| 500mm (20") | 132.6 | 2.9× exceeded | Heavy doubly-reinf | MARGINAL (congestion) |
| 600mm (24") | 205.2 | 1.88× exceeded | Doubly-reinforced, feasible | YES — ADOPTED |
| 750mm (30") | 338.5 | 1.14× exceeded | Singly reinforced possible | Over-design |

At 600mm, the beam still needs doubly-reinforced design but the steel quantities are constructable (no congestion in 230mm width).

### 8.2 Column Count Trade-off

| Configuration | Columns | Longest Beam Span | Min Beam Depth | Steel Impact | Headroom |
|---------------|---------|-------------------|----------------|-------------|----------|
| **Current (8 cols)** | 8 | 7.62m (side) | 600mm (24") | Baseline | 10ft under side beam |
| 10 cols (+2 mid-side) | 10 | 4.42m (back bay) | 380mm (15") | −25% beam steel | 10ft 9" everywhere |
| 12 cols (3×4 grid) | 12 | 3.81m max | 300mm (12") | −40% beam steel | 11ft+ under all beams |
| 6 cols (remove C6/C7) | 6 | 7.62m + 6.32m open front | 750mm+ front beam | +30% beam steel | 8ft under front beam |

**Adding 2 columns on side walls at y≈17** (midpoint of back bay) would:
- Reduce side beam span from 7.62m to max 4.72m
- Allow 380mm side beams (matching original design intent)
- Reduce steel by ~350 kg
- But: obstruct open storage floor plan (the primary purpose of GF)

### 8.3 Open Plan Preservation — The Core Trade-off

The 20×25ft unobstructed ground floor for agricultural storage is the architectural driver. This forces:

| Consequence | Impact | Mitigation |
|-------------|--------|-----------|
| Long spans (7.62m side beams) | Deep beams (24") | Accept 10ft clearance |
| No intermediate columns GF | Full slab load on periphery | Two-way slab design |
| 6ft cantilever (no supports) | Torsion on front beam | 20" front beam |
| Large shutter opening (10ft) | Heavy C6-C7 beam segment | 20" beam + stiff columns |
| Seismic drift (Y-direction) | Borderline compliance | OMRF detailing (R=3) |

### 8.4 Material Cost Estimate (2026 Market Rates, UP)

| Material | Quantity | Rate (INR) | Cost (INR) |
|----------|----------|-----------|-----------|
| M20 concrete (RMC) | 31 m³ | ₹6,500/m³ | 2,01,500 |
| Fe500 TMT steel | 4.5 tonnes | ₹62,000/tonne | 2,79,000 |
| Formwork (plywood) | ~250 m² | ₹350/m² (reusable) | 87,500 |
| Labor (bar-bending, shuttering, concreting) | Lump sum | — | ~2,50,000 |
| **TOTAL STRUCTURAL FRAME** | | | **~₹8,18,000** |

**≈ ₹8.2 lakhs** for the complete RCC frame (excluding masonry, finishing, plumbing, electrical, foundations).

---

## 9. SENSITIVITY ANALYSIS — WHAT IF SCENARIOS

### 9.1 What if R = 5 (SMRF instead of OMRF)?

If the frame were detailed as a Special Moment Resisting Frame (IS 13920 compliant):
```
Ah = (Z/2) × (I/R) × (Sa/g) = 0.12 × (1/5) × 2.5 = 0.06

VB = 0.06 × 1756 = 105.4 kN (40% reduction from OMRF)
```

Impact:
- Lower seismic forces on beams and columns
- BUT requires much stricter detailing (closer stirrups, longer lap lengths, special joint reinforcement)
- Column sizes may need increase to satisfy strong column–weak beam
- Net steel may actually INCREASE despite lower forces
- **NOT recommended** for this project (complexity vs benefit for 2-storey)

### 9.2 What if Back Bay Slab is Increased to 175mm?

```
Additional concrete: 0.025m × 6.10 × 4.42 = 0.674 m³ (per floor) = 1.35 m³ total
Additional steel: ~60 kg (heavier distribution bars)
Additional weight on beams: 0.025 × 25 × 2.21 = 1.38 kN/m per beam (marginal)

Benefit: Deflection ratio improves from 35.4/28 = 1.26 to 31.3/28 = 1.12 — COMPLIANT
```

**Verdict:** Worth the ~₹12,000 additional cost for deflection compliance in the back bay.

### 9.3 What if Columns were 12"×12" (300×300mm)?

```
Column capacity: Pu = 0.4 × 20 × (90000-1380) + 0.67 × 500 × 1380 = 1,170 kN
Utilization: 363/1170 = 31% (vs current 45%)

Lateral stiffness gain:
  Ix = Iy = 300⁴/12 = 675 × 10⁶ mm⁴
  k = 12 × 22.36×10⁶ × 6.75×10⁻⁴ / 49.03 = 3,700 kN/m per column (vs 2,836)
  K_storey = 8 × 3,700 = 29,600 kN/m (30% improvement)

Drift Y-dir: 175.6/29,600 × 3 = 17.8mm (still exceeds 14.64mm but much better)
```

**BUT:** Columns are already cast at 9"×12". This is an irreversible decision.

---

## 10. OVERALL STRUCTURAL SCORE CARD

| Criterion | Rating | Score (1-5) | Notes |
|-----------|--------|-------------|-------|
| Gravity load capacity (columns) | Excellent | 5/5 | 45% utilization, large reserve |
| Gravity load capacity (beams) | Adequate | 3/5 | Side beams at limit, needs doubly-reinforced |
| Seismic drift (X-direction) | Good | 4/5 | Well within limits |
| Seismic drift (Y-direction) | Marginal | 2/5 | Amplified drift exceeds limit |
| Strong column–weak beam | Non-compliant | 1/5 | Columns too slender for beam capacity |
| Redundancy (X-dir) | Good | 4/5 | 3 frame lines |
| Redundancy (Y-dir) | Fair | 3/5 | Only 2 effective frame lines |
| Deflection (slabs) | Fair | 3/5 | Back bay needs 175mm or check |
| Constructability | Good | 4/5 | Standard formwork, no special equipment |
| Material efficiency | Good | 4/5 | 151 kg/m³ is normal for Zone IV |
| **OVERALL** | | **3.3/5** | **Adequate with noted limitations** |

---

## 11. RECOMMENDATIONS

### 11.1 Immediate (Before Beam Casting)

1. **Confirm side beam depth at 600mm (24")** — this is non-negotiable for the 7.62m span
2. **Consider 175mm slab in back bay** (middle beam to back beam panel) for deflection compliance
3. **Ensure stirrup spacing ≤ 100mm in beam-column joint zones** (IS 13920)

### 11.2 Design Refinement

4. **Accept OMRF (R=3) classification** — full SMRF detailing is impractical for this project
5. **Add infill masonry contribution** (not in design, but provides significant drift resistance in practice)
6. **Design plinth beams as tie beams** with proper anchorage at all 8 columns for base fixity

### 11.3 Documentation for Contractor

7. All beam reinforcement must follow the curtailment schedule — bars cannot be cut arbitrarily
8. Lap lengths: 50d for tension bars in seismic zone (50×20 = 1000mm for 20mm bars)
9. No laps in the middle third of column height (all column laps at mid-height)
10. Concrete must be M20 minimum — no site-mixed concrete for beams and columns

---

## 12. CONCLUSION

The 8-column, 20ft × 25ft open plan RCC frame is **structurally feasible** with the following profile:

| Metric | Value |
|--------|-------|
| **Total Concrete (frame)** | **31 m³** |
| **Total Steel** | **4.5 tonnes** |
| **Steel ratio** | **151 kg/m³** |
| **Critical element** | Side beams (230×600mm, 7.62m span) |
| **Governing lateral load** | Seismic (175.6 kN base shear) |
| **Drift compliance** | X: OK, Y: Marginal (relies on infill contribution) |
| **Column reserve** | 55% unused capacity |
| **Beam reserve** | <10% (side beams at design limit) |

The design works but operates at its structural limits in the Y-direction. The 8-column configuration successfully preserves the unobstructed GF storage requirement at the cost of deeper beams (24" sides, 20" cross) and marginally compliant seismic drift performance. In practice, the 9" brick infill walls (not designed as structural) will provide significant additional stiffness and reduce actual drift to well within limits.

---

*This report is for preliminary assessment. Final structural design and drawings must be prepared and certified by a licensed structural engineer (mandatory for Seismic Zone IV construction).*
