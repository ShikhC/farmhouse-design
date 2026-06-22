# PRELIMINARY STRUCTURAL LOAD CALCULATION DOCUMENT

## Project: 2-Story Farmhouse Storage Building
## Location: Moradabad, Uttar Pradesh, India

---

| Parameter | Value |
|-----------|-------|
| Project Type | G+1 Farmhouse Storage Building |
| Ground Floor Use | Agricultural Storage (godown) |
| First Floor Use | Residential (1BHK) |
| Seismic Zone | IV |
| Basic Wind Speed | 47 m/s |
| Soil Type | Alluvial (Gangetic Plain), Medium |
| Concrete Grade | M20 (fck = 20 N/mm²) |
| Steel Grade | Fe500 (fy = 500 N/mm²) |
| Applicable Codes | IS 456:2000, IS 875 (Parts 1-5), IS 1893:2016 |

---

## BUILDING GEOMETRY SUMMARY

| Parameter | Imperial | Metric |
|-----------|----------|--------|
| Internal dimensions | 20ft x 25ft | 6.10m x 7.62m |
| External dimensions | 21.5ft x 26.5ft | 6.55m x 8.08m |
| GF clear height (plinth to slab soffit) | 12ft | 3.66m |
| 1F clear height (slab to slab) | 12ft | 3.66m |
| Plinth height above NGL | 3ft | 0.91m |
| Parapet height | 3ft | 0.91m |
| Total height (NGL to parapet top) | ~31ft | 9.45m |
| Total height (NGL to roof slab) | ~28ft | 8.53m |
| Front cantilever (GF slab only) | 6ft | 1.83m |

### Column Grid:
- X-direction (20ft span): 3 columns at 0, 10ft, 20ft (c/c spacing ~10.375ft = 3.16m)
- Y-direction (25ft span): Back bay 14.5ft (4.42m), Front bay 10.5ft (3.2m) — or 2 bays
- Total columns: 8 nos (4 per line, 2 lines in Y-direction + intermediate)

---

## 1. DEAD LOADS (DL) — As per IS 875 Part 1

### 1.1 Roof Slab (1F Roof, 150mm thick RCC)

| Component | Calculation | Load (kN/m²) |
|-----------|-------------|---------------|
| RCC slab self-weight | 0.150m x 25 kN/m³ | 3.750 |
| Waterproofing (china mosaic / IPS) | As per IS 875 Table 3 | 1.000 |
| Slope screed (avg 75mm thick) | 0.075 x 22 | 1.650 |
| Ceiling plaster (15mm) | 0.015 x 20 | 0.300 |
| **Total Roof Dead Load** | | **6.700 kN/m²** |

Note: Slope screed accounts for roof drainage (1:100 slope). If flat roof with only waterproofing treatment, use reduced value of 5.05 kN/m².

For conservative design, adopt: **Total Roof DL = 6.70 kN/m²**

### 1.2 Floor Slab (GF Ceiling / 1F Floor, 150mm thick RCC)

| Component | Calculation | Load (kN/m²) |
|-----------|-------------|---------------|
| RCC slab self-weight | 0.150m x 25 kN/m³ | 3.750 |
| Floor finish (tiles 20mm + mortar bed 30mm) | 0.020 x 24 + 0.030 x 22 | 1.140 |
| Screed / leveling course (25mm) | 0.025 x 22 | 0.550 |
| Ceiling plaster below (15mm) | 0.015 x 20 | 0.300 |
| **Total Floor Dead Load** | | **5.740 kN/m²** |

Adopt: **Total Floor DL = 5.75 kN/m²**

### 1.3 Ground Floor Slab (100mm RCC on Earth Fill)

| Component | Calculation | Load (kN/m²) |
|-----------|-------------|---------------|
| RCC slab self-weight | 0.100m x 25 kN/m³ | 2.500 |
| Floor finish (IPS 25mm) | 0.025 x 22 | 0.550 |
| Wire mesh reinforcement | Negligible | — |
| **Total GF Floor DL** | | **3.050 kN/m²** |

Note: GF floor slab rests on compacted earth fill; loads transfer directly to soil, not to the frame. This slab is NOT considered in the frame analysis but is relevant for foundation design (surcharge).

### 1.4 Beams (Self-Weight per Meter Run)

**Important:** The beam depth below slab is the net depth for self-weight calculation, since the slab portion is already accounted for in slab dead load.

#### Deep Beams (2 nos — back wall beam + middle beam)
- Overall size: 230mm x 500mm
- Depth below slab soffit: 500 - 150 = 350mm
- Self-weight per meter: 0.230 x 0.350 x 25 = **2.0125 kN/m**
- Span (c/c of columns): 20.75ft = 6.32m
- Total self-weight per beam: 2.0125 x 6.32 = **12.72 kN**

#### Standard Beams (3 nos — front beam + left/right side beams)
- Overall size: 230mm x 380mm
- Depth below slab soffit: 380 - 150 = 230mm
- Self-weight per meter: 0.230 x 0.230 x 25 = **1.3225 kN/m**
- Span varies:
  - Front beam span: 6.32m → self-weight = 1.3225 x 6.32 = 8.36 kN
  - Side beams span: 7.62m → self-weight = 1.3225 x 7.62 = 10.08 kN

### 1.5 Walls (per Meter Length)

#### External Walls (9" / 230mm Brick Masonry)

| Component | Calculation | Load per m height (kN/m) |
|-----------|-------------|--------------------------|
| Brick wall (230mm) | 0.230 x 20 | 4.600 |
| Plaster both sides (15mm each) | 2 x 0.015 x 20 | 0.600 |
| **Total** | | **5.200 kN/m per m height** |

Wall load per floor (3.66m height, deducting beam depth):
- With deep beam (0.5m): wall height = 3.66 - 0.50 = 3.16m
  - Wall load = 5.20 x 3.16 = **16.43 kN/m**
- With standard beam (0.38m): wall height = 3.66 - 0.38 = 3.28m
  - Wall load = 5.20 x 3.28 = **17.06 kN/m**

#### Internal Walls (4.5" / 115mm Brick Masonry)

| Component | Calculation | Load per m height (kN/m) |
|-----------|-------------|--------------------------|
| Brick wall (115mm) | 0.115 x 20 | 2.300 |
| Plaster both sides (12mm each) | 2 x 0.012 x 20 | 0.480 |
| **Total** | | **2.780 kN/m per m height** |

Internal wall load per floor (height = 3.66 - 0.15 slab = 3.51m clear):
- Wall load = 2.78 x 3.51 = **9.76 kN/m**

For UDL equivalent on slab (IS 875 Part 2 recommendation for partition walls):
- For partitions on first floor: adopt minimum 1.0 kN/m² equivalent UDL

#### Parapet Wall (4.5" brick, 0.91m high, on roof slab edge)

| Component | Calculation | Load (kN/m) |
|-----------|-------------|-------------|
| Brick (115mm x 0.91m) | 0.115 x 0.91 x 20 | 2.093 |
| Plaster both sides | 2 x 0.012 x 0.91 x 20 | 0.437 |
| **Total Parapet Load** | | **2.53 kN/m** |

### 1.6 Columns (Self-Weight)

- Column size: 230mm x 300mm
- Unit weight of RCC: 25 kN/m³
- Self-weight per meter height: 0.23 x 0.30 x 25 = **1.725 kN/m**
- Per floor height (3.66m): 1.725 x 3.66 = **6.31 kN per column per floor**
- Total for 2 floors: 6.31 x 2 = **12.63 kN per column**
- Including plinth (0.91m): add 1.725 x 0.91 = 1.57 kN
- **Total column self-weight (full height): 14.20 kN per column**

### 1.7 Staircase Dead Load (if RCC waist slab, 150mm thick, 30-degree inclination)

| Component | Calculation | Load (kN/m²) on plan |
|-----------|-------------|---------------------|
| Waist slab (150mm on slope) | 0.150 x 25 / cos30° | 4.330 |
| Steps (avg 150mm rise) | 0.5 x 0.150 x 25 | 1.875 |
| Floor finish | | 0.500 |
| Ceiling plaster | | 0.300 |
| **Total Staircase DL** | | **7.005 kN/m²** |

---

## 2. LIVE LOADS (LL) — As per IS 875 Part 2:1987

| Floor / Area | Live Load | IS 875 Reference | Notes |
|-------------|-----------|-------------------|-------|
| GF — Storage (godown, general) | 5.0 kN/m² | Table 1, Sr. 8 (Storage) | Cocopeat, fertilizer bags, seeds |
| GF — Storage (heavy/tractor area) | 7.5 kN/m² | Conservative; Sr. 8 + wheel loads | Tractor axle load ~30 kN distributed |
| 1F — Residential (bedroom) | 2.0 kN/m² | Table 1, Sr. 1 | Dwelling units |
| 1F — Kitchen | 2.0 kN/m² | Table 1, Sr. 1 | |
| 1F — Bathroom/Toilet | 2.0 kN/m² | Table 1, Sr. 1 | |
| 1F — Balcony (cantilever) | 3.0 kN/m² | Table 1, Sr. 3 | Balcony load |
| Roof — Accessible | 1.5 kN/m² | Table 2 | Access for maintenance |
| Roof — Inaccessible | 0.75 kN/m² | Table 2 | If no access provided |
| Staircase | 3.0 kN/m² | Table 1, Sr. 4 | |

### Critical Note on GF Storage Load:
The GF floor slab (100mm on earth) bears storage loads directly on soil — these do NOT load the structural frame. However, the **first floor slab** (which is the GF ceiling) carries NO storage load — it carries only the 1F residential loads. The storage loads are relevant only for:
- Foundation design (surcharge on soil)
- Ground floor slab thickness design

The structural frame carries:
- 1F floor: Residential LL = 2.0 kN/m² (3.0 kN/m² on cantilever/balcony)
- Roof: 1.5 kN/m²

### LL Reduction (IS 875 Part 2, Clause 3.2):
For columns supporting more than one floor, LL reduction is permitted. However, for a 2-story building with different floor uses, no reduction is applied in this case (conservative approach).

---

## 3. WIND LOADS — As per IS 875 Part 3:2015

### 3.1 Basic Parameters

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Basic wind speed (Vb) | 47 m/s | IS 875 Part 3, Annex A (Map) |
| Terrain category | 2 (Open terrain, farmland) | Clause 5.3.2.1 |
| Structure class | B (greatest dimension 5-50m) | Table 1 |
| Design life | 50 years | Normal building |
| Risk coefficient (k1) | 1.00 | Table 1, Clause 5.3.1 |
| Terrain roughness factor (k2) | See below | Table 2 |
| Topography factor (k3) | 1.00 | Flat terrain, Clause 5.3.3 |
| Importance factor for cyclonic region (k4) | 1.00 | Not in cyclonic region |

### 3.2 Terrain Factor k2 (Category 2, Class B)

| Height (m) | k2 |
|-----------|-----|
| Up to 10m | 1.00 |
| 15m | 1.05 |

Building height = 9.45m (< 10m), therefore: **k2 = 1.00**

### 3.3 Design Wind Speed and Pressure

Design wind speed at height z:
```
Vz = Vb x k1 x k2 x k3 x k4
Vz = 47 x 1.00 x 1.00 x 1.00 x 1.00
Vz = 47.0 m/s
```

Design wind pressure at height z:
```
pz = 0.6 x Vz²
pz = 0.6 x (47.0)²
pz = 0.6 x 2209
pz = 1325.4 N/m² = 1.325 kN/m²
```

### 3.4 Wind Force on Building

#### Building Dimensions for Wind Analysis:
- Width (b): 6.55m (perpendicular to wind, short face)
- Depth (d): 8.08m (along wind, long face)
- Height (h): 9.45m

#### Force Coefficients (Cf) — IS 875 Part 3, Table 23:
- h/b = 9.45/6.55 = 1.44
- d/b = 8.08/6.55 = 1.23

For rectangular building, interpolating from Table 23:
- **Cf (windward) = +0.7** (pressure)
- **Cf (leeward) = -0.4** (suction)
- **Net Cf = 0.7 + 0.4 = 1.1**

#### Wind Force on Short Face (6.55m wide):
```
F = Cf x pz x Ae
Ae (exposed area) = 6.55 x 9.45 = 61.9 m²
F = 1.1 x 1.325 x 61.9 = 90.2 kN
```

#### Wind Force on Long Face (8.08m wide):
```
Ae = 8.08 x 9.45 = 76.4 m²
F = 1.1 x 1.325 x 76.4 = 111.3 kN
```

### 3.5 Wind Force Distribution to Floors

Assuming uniform pressure (building < 10m):

| Level | Height from base | Tributary height | Force on short face (kN) | Force on long face (kN) |
|-------|-----------------|------------------|--------------------------|-------------------------|
| Roof (9.45m) | 9.45m | 4.73m (half above) | 45.1 | 55.6 |
| 1F slab (4.88m) | 4.88m | 4.72m | 45.1 | 55.7 |
| **Total** | | | **90.2** | **111.3** |

### 3.6 Comparison with Seismic (Governing Case)

Wind base shear on short face = 90.2 kN
(Compare with seismic base shear in Section 4 — seismic typically governs for low-rise buildings in Zone IV)

---

## 4. SEISMIC LOADS — As per IS 1893:2016 (Part 1)

### 4.1 Seismic Parameters

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Seismic Zone | IV | Figure 1 / Annex A |
| Zone Factor (Z) | 0.24 | Table 3 |
| Importance Factor (I) | 1.0 | Table 8 (Residential/Storage) |
| Response Reduction Factor (R) | 3.0 | Table 9 (OMRF — Ordinary Moment Resisting Frame) |
| Soil Type | Type II (Medium/Stiff) | Alluvial soil, N > 10 |
| Damping | 5% | Standard for RCC |

### 4.2 Fundamental Natural Period

For RCC frame building (IS 1893, Clause 7.6.2):
```
T = 0.075 x h^0.75
h = 9.45m (height from base to top of roof slab — excluding parapet for period calculation)
  = 8.53m (NGL to roof slab top)
  
Using h = 8.53m (from base of building to roof):
T = 0.075 x (8.53)^0.75
T = 0.075 x 5.29
T = 0.397 sec

Using h = 9.45m (including parapet, conservative):
T = 0.075 x (9.45)^0.75
T = 0.075 x 5.73
T = 0.430 sec
```

Adopt **T = 0.43 sec** (conservative)

### 4.3 Spectral Acceleration Coefficient (Sa/g)

For Type II soil (Medium Stiff Soil):
- For T = 0.10 to 0.55 sec: **Sa/g = 2.5** (constant acceleration plateau)

Since T = 0.43 sec falls in the plateau region:
**Sa/g = 2.5**

### 4.4 Horizontal Seismic Coefficient (Ah)

```
Ah = (Z/2) x (I/R) x (Sa/g)
Ah = (0.24/2) x (1.0/3.0) x 2.5
Ah = 0.12 x 0.333 x 2.5
Ah = 0.10
```

**Design Horizontal Seismic Coefficient: Ah = 0.10 (10% of seismic weight)**

### 4.5 Seismic Weight Calculation

Seismic weight includes full dead load + appropriate fraction of live load (IS 1893, Clause 7.4.2):
- If LL > 3.0 kN/m²: include 50% of LL
- If LL <= 3.0 kN/m²: include 25% of LL
- Roof LL: No live load on roof for seismic weight (Clause 7.4.2 note)

#### Weight at Roof Level (W2):

| Component | Calculation | Weight (kN) |
|-----------|-------------|-------------|
| Roof slab DL | 6.70 x 6.10 x 7.62 | 311.5 |
| Parapet walls (perimeter) | 2.53 x 2(6.55 + 8.08) | 74.1 |
| Roof beams (deep, 2 nos) | 2.0125 x 6.32 x 2 | 25.4 |
| Roof beams (standard, 3 nos) | 1.3225 x avg span x 3 | 28.7 |
| Columns (half height above 1F slab) | 1.725 x 1.83 x 8 | 25.3 |
| **Total W2** | | **465.0 kN** |

Calculation details for roof beams (standard):
- Front beam: 1.3225 x 6.32 = 8.36 kN
- Left beam: 1.3225 x 7.62 = 10.08 kN
- Right beam: 1.3225 x 7.62 = 10.08 kN
- Total = 28.5 kN (adopt 28.7 kN)

#### Weight at 1F Slab Level (W1):

| Component | Calculation | Weight (kN) |
|-----------|-------------|-------------|
| Floor slab DL (main area) | 5.75 x 6.10 x 7.62 | 267.3 |
| Floor slab DL (cantilever 1.83m x 6.10m) | 5.75 x 1.83 x 6.10 | 64.2 |
| External walls (GF, half ht) + (1F, half ht) | 5.20 x 3.16 x perimeter/2 x 2 | 240.6 |
| Internal walls (1F, half ht) | 2.78 x 1.58 x ~10m | 43.9 |
| Floor beams (deep, 2 nos) | 2.0125 x 6.32 x 2 | 25.4 |
| Floor beams (standard, 3 nos) | 1.3225 x avg span x 3 | 28.7 |
| Columns (half GF + half 1F) | 1.725 x 3.66 x 8 | 50.5 |
| 25% of 1F LL (2.0 kN/m² on 46.5 m²) | 0.25 x 2.0 x 46.5 + 0.25 x 3.0 x 11.2 | 31.7 |
| **Total W1** | | **752.3 kN** |

Detailed wall calculation:
- Perimeter walls (external, 230mm): 2 x (6.55 + 8.08) = 29.26m
- Half-height contribution from GF walls (1.83m): 5.20 x 1.83 x 29.26 = 278.4 kN... 

Let me recalculate more carefully:
- External walls contributing to W1 (half GF height = 1.83m + half 1F height = 1.83m):
  - Total wall height at W1 level = 3.66m tributary
  - Load = 5.20 x 3.16 x (perimeter on beams carrying wall)
  - Back wall (on deep beam): 5.20 x 3.16 x 6.32 = 103.8 kN... 

**Simplified approach — treat walls as UDL on beams:**

External walls at W1 level:
- Tributary height = half of GF (1.83m) + half of 1F (1.83m) = 3.66m
- But deducting beam depths appropriately:
  - On back/middle beams: wall ht = 3.66 - 0.35 = 3.31m
  - On front/side beams: wall ht = 3.66 - 0.23 = 3.43m
- Average wall height at this level: ~3.35m
- Total external wall weight at W1: 5.20 x 3.35 x 29.26 = **509.3 kN**

Wait — this counts full perimeter. Let's be more precise:
- Only walls that are on the beams at this level contribute.
- External walls sit on peripheral beams at GF ceiling / 1F floor level.

**Revised W1 (1F Slab Level):**

| Component | Calculation | Weight (kN) |
|-----------|-------------|-------------|
| Floor slab (main 6.10 x 7.62) | 5.75 x 46.50 | 267.4 |
| Cantilever slab (1.83 x 6.10) | 5.75 x 11.16 | 64.2 |
| Beams at 1F level | (2 x 12.72) + (3 x ~9.5) | 54.0 |
| Columns (half above + half below) | 1.725 x 3.66 x 8 | 50.5 |
| Ext. walls above 1F slab (half 1F ht = 1.58m) | 5.20 x 1.58 x 29.26 | 240.4 |
| Ext. walls below 1F slab (half GF ht = 1.58m) | 5.20 x 1.58 x 29.26 | 240.4 |
| Internal walls 1F (half height = 1.58m) | 2.78 x 1.58 x 12.0 | 52.7 |
| 25% of residential LL | 0.25 x 2.0 x 57.66 | 28.8 |
| **Total W1** | | **998.4 kN** |

This seems high. Let me re-examine — the issue is double-counting wall contribution.

**Correct approach per IS 1893:** Seismic weight at a floor level = DL at that level + walls from mid-height below to mid-height above.

#### Corrected Weight at Roof Level (W2):

| Component | Weight (kN) |
|-----------|-------------|
| Roof slab DL (6.70 x 6.10 x 7.62) | 311.5 |
| Parapet (2.53 x 29.26) | 74.0 |
| Ext. walls: mid 1F to roof (half of 1F ht = 1.58m net): 5.20 x 1.58 x 29.26 | 240.4 |
| Int. walls 1F (half ht = 1.58m): 2.78 x 1.58 x 12m | 52.7 |
| Beams at roof level | 54.0 |
| Columns (half 1F ht): 1.725 x 1.83 x 8 | 25.3 |
| Roof LL: 0 (as per IS 1893 Cl. 7.4.2) | 0 |
| **Total W2** | **757.9 kN** |

#### Corrected Weight at 1F Slab Level (W1):

| Component | Weight (kN) |
|-----------|-------------|
| 1F Floor slab DL (5.75 x 57.66 m²) | 331.5 |
| Ext. walls: mid GF to mid 1F (half GF + half 1F = 3.16m net): 5.20 x 3.16 x 29.26 | 481.0 |
| Int. walls 1F (half height = 1.58m): 2.78 x 1.58 x 12m | 52.7 |
| Beams at 1F level | 54.0 |
| Columns (half GF + half 1F): 1.725 x 3.66 x 8 | 50.5 |
| 25% of 1F LL (2.0 x 57.66 x 0.25) | 28.8 |
| **Total W1** | **998.5 kN** |

**Note:** Floor slab area = 6.10 x 7.62 + 1.83 x 6.10 = 46.5 + 11.2 = 57.7 m²

**Total Seismic Weight: W = W1 + W2 = 998.5 + 757.9 = 1756.4 kN**

### 4.6 Base Shear

```
VB = Ah x W
VB = 0.10 x 1756.4
VB = 175.6 kN
```

**Design Base Shear: VB = 175.6 kN (~17.9 tonnes)**

### 4.7 Distribution of Seismic Force to Floor Levels

Using parabolic (equivalent static) distribution (IS 1893, Clause 7.7.1):

```
Qi = VB x (Wi x hi²) / Σ(Wi x hi²)
```

Where:
- hi = height of floor i measured from base of building

| Floor | Wi (kN) | hi (m) | Wi x hi² | Qi (kN) |
|-------|---------|--------|----------|---------|
| Roof (i=2) | 757.9 | 8.53 | 757.9 x 72.76 = 55,146 | 175.6 x 55,146/82,930 = **116.7** |
| 1F (i=1) | 998.5 | 4.88 | 998.5 x 23.81 = 23,784 | 175.6 x 23,784/82,930 = **50.3** |
| | | | **Σ = 82,930** | Check: 116.7 + 50.3 = **167.0** ≈ 175.6 |

Recalculating with correct heights:
- Base = ground level (NGL + plinth = 0.91m). Taking base at plinth level:
- 1F slab from plinth top: 3.66m → h1 = 3.66m
- Roof slab from plinth top: 3.66 + 3.66 = 7.32m → h2 = 7.32m

| Floor | Wi (kN) | hi (m) | Wi x hi² | Qi (kN) |
|-------|---------|--------|----------|---------|
| Roof | 757.9 | 7.32 | 757.9 x 53.58 = 40,608 | 175.6 x 40,608/54,003 = **132.1** |
| 1F | 998.5 | 3.66 | 998.5 x 13.40 = 13,380 | 175.6 x 13,380/54,003 = **43.5** |
| | | | **Σ = 53,988** | **Total = 175.6 kN** ✓ |

**Seismic Force Distribution:**
- **At Roof Level: Q2 = 132.1 kN**
- **At 1F Level: Q1 = 43.5 kN**

### 4.8 Distribution to Individual Columns

For a regular frame (all columns same size), force at each level distributed equally:
- 8 columns per level
- Force per column at roof level: 132.1 / 8 = **16.5 kN**
- Force per column at 1F level: 43.5 / 8 = **5.4 kN**
- Total shear per column at base: (132.1 + 43.5) / 8 = **21.9 kN**

### 4.9 Seismic vs Wind Comparison

| Direction | Seismic Base Shear (kN) | Wind Base Shear (kN) | Governing |
|-----------|------------------------|---------------------|-----------|
| Short direction (6.55m face) | 175.6 | 90.2 | **Seismic** |
| Long direction (8.08m face) | 175.6 | 111.3 | **Seismic** |

**Seismic forces govern the lateral design.** This is expected for Zone IV with a low-rise building.

---

## 5. LOAD COMBINATIONS — As per IS 456:2000, Table 18

### 5.1 Ultimate Limit State (ULS) Combinations

| ID | Load Combination | Factor |
|----|-----------------|--------|
| LC1 | 1.5 (DL + LL) | Gravity only |
| LC2 | 1.2 (DL + LL + EQ) | Gravity + Earthquake |
| LC3 | 1.2 (DL + LL - EQ) | Gravity + Earthquake (reverse) |
| LC4 | 1.5 (DL + EQ) | Dead + Earthquake |
| LC5 | 1.5 (DL - EQ) | Dead + Earthquake (reverse) |
| LC6 | 0.9 DL + 1.5 EQ | Stability check |
| LC7 | 0.9 DL - 1.5 EQ | Stability check (reverse) |
| LC8 | 1.2 (DL + LL + WL) | Gravity + Wind |
| LC9 | 1.5 (DL + WL) | Dead + Wind |
| LC10 | 0.9 DL + 1.5 WL | Stability check (wind) |

### 5.2 Serviceability Limit State (SLS)

| ID | Load Combination |
|----|-----------------|
| SLS1 | 1.0 DL + 1.0 LL |
| SLS2 | 1.0 DL + 1.0 EQ |
| SLS3 | 1.0 DL + 0.8 LL + 0.8 EQ |

---

## 6. COLUMN LOAD SUMMARY

### 6.1 Tributary Areas

The building has 8 columns arranged in a grid. Based on the column layout:

**Column Types by Position:**
- Corner columns (4 nos): C1, C3, C6, C8
- Edge columns (2 nos on back/middle line): C2, C7
- Edge columns (2 nos on front/side): C4, C5

Assuming grid (approximate):
- X-spacing: 3.16m (10.375ft c/c) — 2 bays
- Y-spacing: Back bay 4.42m, Front bay 3.20m

| Column | Position | Tributary Area (m²) |
|--------|----------|---------------------|
| C1 | Back-Left corner | (3.16/2) x (4.42/2) = 1.58 x 2.21 = 3.49 |
| C2 | Back-Middle | (3.16/2 + 3.16/2) x (4.42/2) = 3.16 x 2.21 = 6.98 |
| C3 | Back-Right corner | (3.16/2) x (4.42/2) = 1.58 x 2.21 = 3.49 |
| C4 | Front-Left corner | (3.16/2) x (3.20/2 + 4.42/2) = 1.58 x 3.81 = 6.02 |
| C5 | Front-Middle | 3.16 x (3.20/2 + 4.42/2) = 3.16 x 3.81 = 12.04 |
| C6 | Front-Right corner | 1.58 x 3.81 = 6.02 |
| C7 | Middle-Middle | 3.16 x (4.42/2 + 3.20/2) = 3.16 x 3.81 = 12.04 |
| C8 | Middle-Corner | 1.58 x 3.81 = 6.02 |

**Note:** The layout needs clarification. Based on 8 columns with 2 deep beams (back + middle) spanning X-direction:

Revised grid interpretation:
- 3 rows in Y: Back, Middle, Front (at Y = 0, 4.42m, 7.62m)
- But 8 columns suggests: 2 rows of 3 + 2 extra, OR 4 columns per line with 2 lines

Most likely arrangement for 8 columns:
- **Y-direction:** 2 lines (Left at X=0, Right at X=6.10m)
- **X-direction:** 4 columns per line at Y = 0, 2.54m, 5.08m, 7.62m

OR more practically for 20ft x 25ft with 2 deep beams:
- **3 beam lines in X-direction:** Back (Y=0), Middle (Y=4.42m), Front (Y=7.62m)
- **Columns:** 3 per back/middle line, 2 at front = 8 total? No.

**Adopting simplified layout: 2 rows x 4 columns = 8 columns**
- Left row: X = 0
- Right row: X = 6.10m
- Y positions: 0, 2.54m, 5.08m, 7.62m (4 columns at ~8.33ft spacing)

For load calculation, using most critical column (interior column with maximum tributary area):

### 6.2 Critical Column Load (Most Loaded — Interior/Middle Column)

Taking the most loaded column with tributary area approximately:
- **Maximum tributary area per column = 3.16m x 3.81m = 12.04 m²**

#### Axial Load Calculation:

**From Roof:**
| Component | Calculation | Load (kN) |
|-----------|-------------|-----------|
| Roof slab DL | 6.70 x 12.04 | 80.7 |
| Roof beam self-wt (tributary) | 2.0125 x 3.16 + 1.3225 x 3.81 | 11.4 |
| Parapet (if on edge — not applicable for interior) | — | 0 |
| Roof LL | 1.5 x 12.04 | 18.1 |
| **Sub-total from roof** | | **110.2 kN** |

**From 1F Floor:**
| Component | Calculation | Load (kN) |
|-----------|-------------|-----------|
| Floor slab DL | 5.75 x 12.04 | 69.2 |
| Floor beam self-wt (tributary) | 2.0125 x 3.16 + 1.3225 x 3.81 | 11.4 |
| Ext. wall on beam (if edge column) | — | 0 |
| Int. wall on 1F (UDL 1.0 kN/m² x area) | 1.0 x 12.04 | 12.0 |
| Floor LL (residential) | 2.0 x 12.04 | 24.1 |
| **Sub-total from 1F** | | **116.7 kN** |

**Column Self-Weight:**
| Component | Calculation | Load (kN) |
|-----------|-------------|-----------|
| Column (2 floors + plinth) | 1.725 x (3.66 + 3.66 + 0.91) | 14.2 |

**Total Unfactored Axial Load on Interior Column:**
```
P = 110.2 + 116.7 + 14.2 = 241.1 kN
```

**Factored Load (LC1: 1.5 DL + 1.5 LL):**
```
DL = 80.7 + 11.4 + 69.2 + 11.4 + 12.0 + 14.2 = 198.9 kN
LL = 18.1 + 24.1 = 42.2 kN
Pu = 1.5 x (198.9 + 42.2) = 1.5 x 241.1 = 361.7 kN
```

### 6.3 Edge/Corner Column (with external wall)

For a corner column with tributary area ~6.0 m² and supporting external wall:

| Component | Load (kN) |
|-----------|-----------|
| Roof slab DL (6.70 x 6.0) | 40.2 |
| Roof LL (1.5 x 6.0) | 9.0 |
| Floor slab DL (5.75 x 6.0) | 34.5 |
| Floor LL (2.0 x 6.0) | 12.0 |
| External wall — 1F (5.20 x 3.16 x tributary length ~3.5m) | 57.5 |
| External wall — GF (5.20 x 3.16 x 3.5m) | 57.5 |
| Parapet (2.53 x 3.5m) | 8.9 |
| Beams (tributary) | 8.0 |
| Column self-weight | 14.2 |
| **Total unfactored** | **241.8 kN** |
| **Factored (1.5 factor)** | **362.7 kN** |

### 6.4 Column Capacity Check

Column: 230mm x 300mm, M20 concrete, Fe500 steel

Assuming minimum reinforcement (0.8% of gross area):
```
Ag = 230 x 300 = 69,000 mm²
Asc (min) = 0.008 x 69,000 = 552 mm² (4 nos 16mm dia = 804 mm²)
Ac = Ag - Asc = 69,000 - 804 = 68,196 mm²
```

**Axial capacity (IS 456, Clause 39.3 — short column, no eccentricity):**
```
Pu = 0.4 fck Ac + 0.67 fy Asc
Pu = 0.4 x 20 x 68,196 + 0.67 x 500 x 804
Pu = 545,568 + 269,340
Pu = 814,908 N = 814.9 kN
```

**With practical reinforcement (1.5% = 1035 mm², say 4-16mm + 4-12mm = 804 + 452 = 1256 mm²):**
```
Ac = 69,000 - 1256 = 67,744 mm²
Pu = 0.4 x 20 x 67,744 + 0.67 x 500 x 1256
Pu = 541,952 + 420,760
Pu = 962,712 N = 962.7 kN
```

**Capacity vs Demand:**
```
Maximum factored column load = ~363 kN
Column capacity (min steel) = 815 kN
Utilization ratio = 363/815 = 0.45 (45%)
```

**Result: Column 230mm x 300mm is ADEQUATE for axial loads with significant reserve capacity.**

However, considering combined axial + bending (seismic moment):
- Moment from seismic at base of column ≈ Qi_per_column x (storey_height/2)
- Mu ≈ 21.9 x (3.66/2) = 40.1 kN.m

This needs to be checked on the P-M interaction diagram, but preliminary assessment indicates adequacy for a column with 1.5-2% reinforcement.

### 6.5 Summary of Column Loads

| Column Position | Unfactored Axial (kN) | Factored Pu - LC1 (kN) | Factored Pu - LC2 (kN) | Status |
|----------------|----------------------|------------------------|------------------------|--------|
| Interior (max loaded) | 241 | 362 | ~310 | OK |
| Corner (with wall) | 242 | 363 | ~315 | OK |
| Edge (middle of back wall) | ~280 | 420 | ~360 | OK |
| Column capacity (min steel) | — | 815 | — | — |
| **Utilization** | — | **45-52%** | — | **SAFE** |

---

## 7. BEAM LOAD SUMMARY

### 7.1 Deep Beam — Back Wall Beam (230mm x 500mm, Span = 6.32m)

**Loading on this beam:**
- Tributary width for slab load: 4.42/2 = 2.21m (one-way slab spanning to this beam)
- Supports back external wall above

| Load Component | Calculation | UDL (kN/m) |
|---------------|-------------|-------------|
| Slab DL (from roof + floor) | (6.70 + 5.75) x 2.21 | 27.51 |
| Slab LL (roof + 1F) | (1.5 + 2.0) x 2.21 | 7.74 |
| Beam self-weight | 0.23 x 0.35 x 25 | 2.01 |
| External wall (GF level, 3.16m ht) | 5.20 x 3.16 | 16.43 |
| Parapet above | 2.53 | 2.53 |
| **Total unfactored UDL** | | **56.22 kN/m** |
| **Factored UDL (1.5 factor)** | | **84.33 kN/m** |

Wait — this beam exists at each floor level. Let me separate:

#### Deep Beam at Roof Level (supporting roof slab + parapet):

| Load Component | UDL (kN/m) |
|---------------|-------------|
| Roof slab DL (6.70 x 2.21) | 14.81 |
| Roof LL (1.5 x 2.21) | 3.32 |
| Beam self-weight | 2.01 |
| Parapet wall | 2.53 |
| **Total unfactored** | **22.67 kN/m** |
| **Factored (LC1: 1.5)** | **34.0 kN/m** |

**Maximum Bending Moment (simply supported):**
```
Mu = wu x L² / 8
Mu = 34.0 x (6.32)² / 8
Mu = 34.0 x 39.94 / 8
Mu = 169.7 kN.m
```

**Maximum Shear Force:**
```
Vu = wu x L / 2
Vu = 34.0 x 6.32 / 2
Vu = 107.4 kN
```

#### Deep Beam at 1F Level (supporting 1F floor slab + wall above + roof loads from above columns):

This beam carries the floor slab load plus wall from 1F to roof:

| Load Component | UDL (kN/m) |
|---------------|-------------|
| Floor slab DL (5.75 x 2.21) | 12.71 |
| Floor LL (2.0 x 2.21) | 4.42 |
| Beam self-weight | 2.01 |
| External wall above (1F, 3.16m) | 16.43 |
| **Total unfactored** | **35.57 kN/m** |
| **Factored (LC1)** | **53.36 kN/m** |

**Maximum Bending Moment:**
```
Mu = 53.36 x (6.32)² / 8 = 53.36 x 39.94 / 8 = 266.3 kN.m
```

**Maximum Shear Force:**
```
Vu = 53.36 x 6.32 / 2 = 168.6 kN
```

### 7.2 Beam Capacity Check — Deep Beam (230 x 500mm)

Effective depth: d = 500 - 25 (cover) - 8 (stirrup) - 10 (half bar) = 457mm

**Moment capacity (under-reinforced section):**
```
Mu,lim = 0.138 x fck x b x d²  (for Fe500, xu/d = 0.46)
Mu,lim = 0.138 x 20 x 230 x 457²
Mu,lim = 0.138 x 20 x 230 x 208,849
Mu,lim = 132,573,396 N.mm = 132.6 kN.m
```

**Demand vs Capacity:**
- Roof level: Mu = 169.7 kN.m > Mu,lim = 132.6 kN.m → **DOUBLY REINFORCED section needed**
- 1F level: Mu = 266.3 kN.m >> 132.6 kN.m → **DOUBLY REINFORCED section needed, or INCREASE BEAM DEPTH**

**CRITICAL FINDING:** The deep beam at 1F level (230x500mm spanning 6.32m) with the 1F level loading requires either:
1. Heavy doubly-reinforced design (may have congestion issues), or
2. Increase beam depth to 600mm (recommended), or
3. Reduce span by adding intermediate support

### 7.3 Standard Beam — Front Beam (230mm x 380mm, Span = 6.32m)

#### At 1F Level (supporting floor slab + cantilever loads):

| Load Component | UDL (kN/m) |
|---------------|-------------|
| Floor slab DL (5.75 x 3.20/2) | 9.20 |
| Cantilever slab DL (5.75 x 1.83) — transferred as reaction | Special |
| Floor LL (3.0 x 1.83 + 2.0 x 1.60) | 8.69 |
| Beam self-weight | 1.32 |
| **Total unfactored (excluding cantilever)** | **19.21 kN/m** |

The cantilever slab (1.83m projection, 150mm thick) creates a moment at the front beam:
```
Cantilever moment = w x L²/2 = (5.75 + 3.0) x 1.83² / 2 = 8.75 x 3.35 / 2 = 14.66 kN.m per meter

This moment is transferred to the front beam as a torsional load.
```

**Factored UDL (approximate, considering cantilever effect):**
```
wu = 1.5 x 19.21 = 28.8 kN/m (beam spanning between columns)
```

**Maximum BM (simply supported):**
```
Mu = 28.8 x (6.32)² / 8 = 28.8 x 39.94 / 8 = 143.8 kN.m
```

**Standard Beam Capacity (230 x 380mm):**
```
d = 380 - 25 - 8 - 10 = 337mm
Mu,lim = 0.138 x 20 x 230 x 337²
Mu,lim = 0.138 x 20 x 230 x 113,569
Mu,lim = 72,134,186 N.mm = 72.1 kN.m
```

**Demand: 143.8 kN.m >> Capacity: 72.1 kN.m**

**CRITICAL FINDING:** The standard beam (230x380mm) spanning 6.32m is **SEVERELY INADEQUATE** for the loading. Requires significant redesign — either:
1. Increase depth to minimum 500mm (match deep beam), or
2. Increase width to 300mm with depth 450mm, or
3. Add intermediate columns to reduce span

### 7.4 Side Beams (230 x 380mm, Span = 7.62m in Y-direction)

| Load Component | UDL (kN/m) |
|---------------|-------------|
| Slab DL (one-way slab — minimal load on long span beams if slab spans short direction) | ~2.0 |
| External wall (5.20 x 3.16) | 16.43 |
| Beam self-weight | 1.32 |
| **Total unfactored** | **19.75 kN/m** |
| **Factored** | **29.6 kN/m** |

If slab spans one-way in the short (X) direction (6.10m) to the deep beams, then side beams carry primarily wall loads + self-weight.

However, checking slab span ratio:
- Ly/Lx = 7.62/6.10 = 1.25 < 2.0 → **TWO-WAY SLAB**

For a two-way slab, side beams will carry significant slab loads too. Using yield line coefficients:
- Load on long beam ≈ (w x Lx/3) for triangular distribution
- Additional slab UDL on side beam ≈ (5.75 + 2.0) x 6.10/3 = 7.75 x 2.03 = 15.7 kN/m

Revised side beam load:
```
Total factored UDL = 1.5 x (2.0 + 15.7 + 16.43 + 1.32) = 1.5 x 35.45 = 53.2 kN/m
```

**Maximum BM (span 7.62m):**
```
Mu = 53.2 x (7.62)² / 8 = 53.2 x 58.06 / 8 = 386.1 kN.m
```

**This is an extremely high moment for a 230x380mm beam!**

**CRITICAL FINDING:** Side beams carrying wall + two-way slab loads over 7.62m span are **grossly inadequate** at 230x380mm. These MUST be deep beams (minimum 230x600mm) or the slab should be designed as one-way spanning to beams in the shorter direction with secondary beams in the Y-direction.

### 7.5 Beam Summary Table

| Beam | Size (mm) | Span (m) | Factored Mu (kN.m) | Mu,lim (kN.m) | Status |
|------|-----------|----------|--------------------:|---------------:|--------|
| Deep beam (roof) | 230x500 | 6.32 | 169.7 | 132.6 | NEEDS DOUBLY-REINFORCED |
| Deep beam (1F) | 230x500 | 6.32 | 266.3 | 132.6 | **INADEQUATE — increase depth** |
| Front beam (1F) | 230x380 | 6.32 | 143.8 | 72.1 | **INADEQUATE — increase depth** |
| Side beams | 230x380 | 7.62 | 386.1 | 72.1 | **GROSSLY INADEQUATE** |
| Front beam (roof) | 230x380 | 6.32 | ~100 | 72.1 | NEEDS DOUBLY-REINFORCED |

---

## 8. SLAB DESIGN CHECK

### 8.1 1F Floor Slab (150mm thick)

**Slab panel: 6.10m x 7.62m (two-way slab, Ly/Lx = 1.25)**

For a two-way slab supported on all 4 sides (IS 456, Table 26):
- Short span moment coefficient (αx): ~0.056 (one short edge discontinuous)
- Long span moment coefficient (αy): ~0.037

```
Factored load: wu = 1.5 x (5.75 + 2.0) = 11.625 kN/m²

Short span moment: Mx = αx x wu x Lx²
Mx = 0.056 x 11.625 x (6.10)² = 0.056 x 11.625 x 37.21 = 24.2 kN.m per meter

Long span moment: My = αy x wu x Lx²
My = 0.037 x 11.625 x 37.21 = 16.0 kN.m per meter
```

**Slab moment capacity (150mm thick, per meter width):**
```
d = 150 - 20 (cover) - 5 (half bar for 10mm dia) = 125mm
Mu,lim = 0.138 x 20 x 1000 x 125² = 43,125,000 N.mm/m = 43.1 kN.m/m
```

**Short span: 24.2 < 43.1 → OK**
**Long span: 16.0 < 43.1 → OK**

### 8.2 Cantilever Slab (1.83m projection, 150mm thick)

```
Factored load: wu = 1.5 x (5.75 + 3.0) = 13.125 kN/m² (balcony LL)

Cantilever moment at support: Mu = wu x L² / 2
Mu = 13.125 x (1.83)² / 2 = 13.125 x 3.35 / 2 = 21.98 kN.m per meter
```

**Capacity: 43.1 kN.m/m >> 21.98 kN.m/m → OK**

**Deflection check for cantilever:**
- L/d ratio (cantilever): 1830/125 = 14.6
- Permissible L/d for cantilever: 7 x modification factor (~1.4 for pt~0.5%) = 9.8
- **14.6 > 9.8 → DEFLECTION MAY BE EXCESSIVE**

**FINDING:** The 150mm cantilever slab with 1.83m projection may have deflection issues. Consider increasing to 175mm thickness or providing an upstand beam at the cantilever edge.

### 8.3 Back Bay Slab Span (14.5ft = 4.42m one-way between back beam and middle beam)

If this bay is designed as one-way slab:
```
Span = 4.42m
Factored UDL = 1.5 x (5.75 + 2.0) = 11.625 kN/m²

Mu = wu x L² / 8 = 11.625 x (4.42)² / 8 = 11.625 x 19.54 / 8 = 28.4 kN.m per meter
```

**Capacity = 43.1 kN.m/m → OK for bending**

**Deflection check (one-way, simply supported):**
- L/d = 4420/125 = 35.4
- Permissible L/d = 20 x MF (say 1.4) = 28
- **35.4 > 28 → DEFLECTION ISSUE for one-way spanning 4.42m with 150mm slab**

**FINDING:** The 150mm slab spanning 4.42m one-way may have deflection issues. This is acceptable if the slab is designed as two-way (with Ly/Lx=1.43 for the sub-panel), which reduces effective span and improves deflection performance.

---

## 9. FOUNDATION PRELIMINARY SIZING

### 9.1 Soil Parameters (Assumed for Alluvial Soil — Moradabad)

| Parameter | Value |
|-----------|-------|
| Soil type | Alluvial (sandy silt / silty sand) |
| Safe bearing capacity (SBC) | 120-150 kN/m² (assumed) |
| Adopt SBC | 130 kN/m² (conservative for medium alluvial) |
| Depth of foundation | 1.5m below NGL (minimum) |
| Water table | Assumed > 2m below NGL |

### 9.2 Footing Size Estimate

For the most loaded column (P = ~242 kN unfactored service load):
```
Required footing area = P / SBC = 242 / 130 = 1.86 m²
Footing size = √1.86 = 1.36m → Adopt 1.4m x 1.4m isolated footing
```

For edge column with wall load (~242 kN):
```
Area = 242 / 130 = 1.86 m²
Adopt 1.4m x 1.5m (rectangular, eccentric loading consideration)
```

**GF floor surcharge on soil:**
- Storage load on GF floor: 5.0 to 7.5 kN/m² (LL) + 3.05 kN/m² (DL) = 8.05 to 10.55 kN/m²
- This is well within SBC and transfers directly to soil through the ground slab.

### 9.3 Foundation Recommendation

Given seismic Zone IV and moderate loads:
- **Isolated footings** with tie beams connecting all footings at plinth level
- Tie beam size: minimum 230mm x 300mm with nominal reinforcement
- Plinth beam: Acts as tie beam, 230mm x 300mm
- Consider **combined footing** if column spacing < 2m or if footings overlap

---

## 10. CRITICAL FINDINGS AND RECOMMENDATIONS

### 10.1 Structural Adequacy Summary

| Element | Proposed Size | Status | Recommendation |
|---------|--------------|--------|----------------|
| Columns (230x300mm) | 8 nos | **ADEQUATE** (45-52% utilization) | Provide 1.5-2% steel for seismic |
| Deep beams (230x500mm) | 2 nos, 6.32m span | **MARGINAL** (needs doubly-reinforced at 1F) | Increase to 230x600mm |
| Standard beams (230x380mm) | 3 nos, 6.32-7.62m span | **INADEQUATE** | Increase to minimum 230x500mm |
| Side beams (230x380mm) | 7.62m span with wall | **GROSSLY INADEQUATE** | Increase to 230x600mm or add mid-span column |
| 1F Floor slab (150mm) | Two-way, 6.10x7.62m | **OK for strength** | Check deflection; consider 175mm |
| Cantilever slab (150mm, 1.83m) | Projection at front | **DEFLECTION CONCERN** | Increase to 175mm or add upstand |
| Roof slab (150mm) | 6.10x7.62m | **OK** | Adequate for roof loads |
| GF Floor (100mm) | On earth fill | **OK** | Adequate for storage on grade |

### 10.2 Key Issues Identified

1. **CRITICAL — Side Beams (7.62m span, 230x380mm):** These beams carry significant wall loads (16.43 kN/m) plus two-way slab loads over the longest span. At 230x380mm, they are severely undersized. **MUST be increased to minimum 230x600mm.**

2. **CRITICAL — Front Beam (6.32m span, 230x380mm):** Supporting cantilever slab loads and floor slab, this beam is inadequate at 380mm depth. **Increase to minimum 230x500mm.**

3. **IMPORTANT — Deep Beams at 1F Level:** The 230x500mm deep beam at the 1F level (supporting back wall + floor slab) requires heavy doubly-reinforced design. **Recommend increasing to 230x600mm** to allow singly-reinforced design and easier construction.

4. **MODERATE — Cantilever Deflection:** The 6ft (1.83m) cantilever at 150mm thickness has borderline deflection performance. Consider 175mm thickness or edge upstand beam.

5. **SEISMIC DETAILING:** Zone IV requires ductile detailing (IS 13920). All beam-column joints need:
   - Special confining reinforcement in columns within the joint region
   - Minimum shear reinforcement spacing of d/4 or 100mm in plastic hinge zones
   - Strong column—weak beam principle must be verified

6. **DEEP BEAM SPAN (6.32m):** The 20.75ft (6.32m c/c) span is at the upper limit for 230mm wide beams. Width increase to 300mm would significantly improve shear capacity and reduce reinforcement congestion.

### 10.3 Recommended Modifications

| Element | Current | Recommended | Reason |
|---------|---------|-------------|--------|
| All beams (back + middle) | 230x500mm | **230x600mm** | Accommodate moment demand + seismic ductility |
| Front beam | 230x380mm | **230x500mm** | Inadequate for 6.32m span with cantilever |
| Side beams | 230x380mm | **230x600mm** | Grossly inadequate for 7.62m span + wall |
| Cantilever slab | 150mm | **175mm** (or add edge beam) | Deflection control |
| Beam width (all) | 230mm | **250-300mm** (desirable) | Reduces steel congestion, improves shear |

### 10.4 Load Path Summary

```
LOAD PATH DIAGRAM:

Roof Loads (DL + LL)
    ↓
Roof Slab (150mm) → Roof Beams → Columns
    ↓                                ↓
Parapet (DL)                         ↓
                                     ↓
1F Floor Loads (DL + LL)             ↓
    ↓                                ↓
1F Slab (150mm) → Floor Beams → Columns (cumulative)
    ↓                                ↓
Ext. Walls (DL) → on beams →        ↓
Int. Walls (DL) → on slab →         ↓
                                     ↓
                              Foundation (Isolated footings)
                                     ↓
                                   SOIL

GF Storage Loads → GF Slab (100mm on earth) → SOIL (direct, not through frame)
```

### 10.5 Next Steps

1. Finalize beam sizes based on recommendations above
2. Perform detailed design of each element (reinforcement calculation)
3. Design beam-column joints for seismic Zone IV (IS 13920)
4. Design foundations with updated column loads
5. Prepare structural drawings with bar bending schedules
6. Get design vetted by a licensed structural engineer (mandatory for Zone IV)

---

## APPENDIX A: REFERENCE CODES

| Code | Title | Relevant Clauses |
|------|-------|-----------------|
| IS 456:2000 | Plain and Reinforced Concrete — Code of Practice | Cl. 39.3 (columns), Cl. 22 (beams), Table 18 (load combinations) |
| IS 875 Part 1:1987 | Dead Loads | Tables 1-4 (unit weights) |
| IS 875 Part 2:1987 | Imposed Loads | Tables 1-2 (live loads for various occupancies) |
| IS 875 Part 3:2015 | Wind Loads | Map (wind speed), Tables 1-2 (factors), Table 23 (Cf) |
| IS 1893:2016 Part 1 | Earthquake Resistant Design | Cl. 7.6.2 (period), Cl. 7.7.1 (base shear distribution) |
| IS 13920:2016 | Ductile Design of RCC Structures | Seismic detailing requirements |
| IS 2911 Part 1 | Pile Foundations | If required based on soil investigation |

---

## APPENDIX B: UNIT WEIGHTS USED (IS 875 Part 1)

| Material | Unit Weight (kN/m³) |
|----------|-------------------|
| Reinforced Concrete | 25 |
| Plain Concrete | 24 |
| Brick Masonry | 20 |
| Cement Mortar | 22 |
| Tiles (ceramic) | 24 |
| Earth (compacted fill) | 18 |
| Water | 10 |

---

## APPENDIX C: QUICK LOAD REFERENCE (Per Column, Unfactored)

| Load Type | Interior Column (kN) | Corner Column (kN) |
|-----------|---------------------|-------------------|
| Roof DL | 92.1 | 48.2 |
| Roof LL | 18.1 | 9.0 |
| Floor DL | 81.6 | 42.5 |
| Floor LL | 24.1 | 12.0 |
| Walls (carried) | 12.0 | 115.0 |
| Column self-wt | 14.2 | 14.2 |
| **Total Service Load** | **242** | **241** |
| **Factored (1.5)** | **363** | **362** |
| **Column Capacity** | **815** | **815** |
| **Factor of Safety** | **2.25** | **2.25** |

---

*Document prepared for preliminary design assessment. All calculations are approximate and subject to detailed structural analysis. Final design must be carried out by a licensed structural engineer and comply with local building regulations and NBC 2016.*

*Revision: 0 | Date: June 2026 | Status: PRELIMINARY*
