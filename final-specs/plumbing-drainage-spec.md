# Plumbing & Drainage System — Final Specifications

**Project:** G+1 Farm Storage + Residence, Moradabad, UP
**Date:** June 2026
**Status:** Layout finalized, pending construction

---

## 1. SITE CONSTRAINTS

| Constraint | Value | Impact |
|-----------|-------|--------|
| Borewell (submersible, drinking water) | 30ft right of right wall, toward front (x≈51, y≈2) | All soak pits must be 50ft+ away |
| Chakrode (kachchi road) | 10-12ft in front of building (y≈-12) | No pipes cross under road |
| Tractor access | LEFT side of building must be clear | No structures on left side |
| Building plinth | 3ft raised above NGL (farm land at z=0) | Pipes exit through plinth wall, slope down |
| Dragon fruit farming | Back and sides | Soak pits underground, farmable above |

---

## 2. THREE SEPARATE DRAINAGE SYSTEMS

### 2.1 System 1: BLACK WATER (Toilet sewage)

**Sources:** GF Toilet (left-front, x=1, y=1.5) + 1F Toilet (right side, x=18, y=7)

**Route:**
```
GF Toilet (x=1, y=1.5)                    1F Toilet (x=18, y=7)
     │ 4" (110mm) PVC SWR                      │ 4" (110mm) PVC SWR
     │ vertical drop through plinth             │ vertical drop (wall chase)
     │ to z=-1.5 (underground)                  │ to z=-1.5
     │                                          │
     │ runs straight to BACK wall               │ runs straight to BACK wall
     │ (underground, 1:40 slope)                │ (underground, 1:40 slope)
     │                                          │
     └──────────── 45° Y-JUNCTION ─────────────┘
                   (x=-3, y=28, behind back wall)
                         │
                    Inspection Chamber (x=-4, y=27.5)
                    (1.5ft × 1.5ft × 2ft, CI heavy-duty cover)
                         │
                    SEPTIC TANK (x=-5, y=28)
                    (5ft × 2.5ft × 4.5ft deep, 2-chamber RCC)
                         │
                    BW SOAK PIT (x=-5, y=40)
                    (5ft diameter × 7ft deep, honeycomb brick)
```

**Key specifications:**
| Component | Size | Material | Notes |
|-----------|------|----------|-------|
| Pipes (both toilets) | 110mm (4") | PVC SWR | Slope 1:40, only 45° bends |
| Y-Junction | 110mm×110mm | PVC SWR | 45° junction, NOT 90° |
| Inspection Chamber | 1.5ft × 1.5ft × 2ft | Brick, CI cover (Class D) | Heavy-duty for vehicle access |
| Septic Tank | 5ft × 2.5ft × 4.5ft | RCC M20, 6" walls | 2-chamber, ~1500L capacity |
| BW Soak Pit | 5ft ⌀ × 7ft deep | Honeycomb brick (dry laid) | Gravel bottom 2ft |
| Vent pipe | 50mm (2") | PVC | Rises from GF toilet to above roof |

**Critical: NO 90° bends anywhere in black water lines.**

---

### 2.2 System 2: GREY WATER (Kitchen, Basin, Shower — 1F)

**Sources:** 1F Kitchen sink (x=18, y=22) + 1F Basin (x=18, y=8) + 1F Shower (x=16, y=6)

**Route:**
```
Kitchen Sink + Basin + Shower (all on 1F, right/back area)
     │ 75mm (3") PVC SWR (kitchen, basin)
     │ 50mm (2") PVC (shower branch)
     │
     │ all run to BACK wall inside 1F floor
     │
     └── Vertical downpipe (outside back wall, x=18)
              │ 75mm PVC, drops from 1F to underground
              │
              │ underground run to Grease Trap (x=15, y=28)
              │
         GREASE TRAP (600mm × 450mm × 600mm)
              │
         Inspection Chamber (x=12, y=33)
              │
         GW SOAK PIT (x=5, y=40)
         (4ft diameter × 6ft deep)
```

**Key specifications:**
| Component | Size | Material | Notes |
|-----------|------|----------|-------|
| Fixture pipes | 75mm (3") | PVC SWR | Kitchen & basin |
| Shower branch | 50mm (2") | PVC SWR | Joins main before downpipe |
| Main downpipe | 75mm (3") | PVC SWR | Outside back wall |
| Grease Trap | 600×450×600mm | RCC/masonry | Clean every 2-4 weeks |
| GW Soak Pit | 4ft ⌀ × 6ft deep | Honeycomb brick | Gravel bottom 1.5ft |

**Note:** Underground pipe route from back wall to grease trap to be laid BEFORE floor slab pour. Can be capped initially if 1F kitchen/bath not immediately built.

---

### 2.3 System 3: WASH WATER (Floor Drain — GF Storage)

**Source:** GF floor drain channel (x=10, runs full depth of building front to back)

**Route:**
```
Floor Drain Channel (6" wide, center of storage floor, x=10)
     │ sloped 1:100 toward BACK wall
     │
     │ exits BACK wall (underground)
     │ 110mm (4") PVC SWR
     │
     SILT TRAP (x=9, y=28)
     (750mm × 750mm × 750mm)
     │
     OIL & GREASE TRAP (x=8, y=33)
     (750mm × 600mm × 750mm)
     │
     WW SOAK PIT (x=15, y=38)
     (5ft diameter × 6.5ft deep)
```

**Key specifications:**
| Component | Size | Material | Notes |
|-----------|------|----------|-------|
| Floor drain channel | 6" wide × full depth | Cement, trowel-finish | Slope 1:100 toward back |
| Exit pipe | 110mm (4") | PVC SWR | Exits through back plinth wall |
| Silt Trap | 750×750×750mm | Masonry | Clean after heavy wash |
| Oil & Grease Trap | 750×600×750mm | Masonry | Removes diesel/oil from tractor wash |
| WW Soak Pit | 5ft ⌀ × 6.5ft deep | Honeycomb brick | Gravel bottom 1.5ft |

---

### 2.4 System 4: RAINWATER (Completely Independent)

```
Roof → 4 Downpipes (3" PVC at corners) → Surface drainage away from building
```

| Component | Size | Notes |
|-----------|------|-------|
| Downpipes | 4 nos, 75mm (3") PVC | At building corners |
| Exit | Through plinth wall at ground level | Sleeves pre-installed during plinth |
| Disposal | Surface drainage to open farm | OR optional recharge pit |

**Rainwater is NEVER connected to any septic tank, soak pit, or drain system.**

---

## 3. SITE LAYOUT — FINAL POSITIONS

### 3.1 Plan View

```
                              BACK (farming land)
                                   ↑
                                   
    y=40 ─── ● BW Soak Pit ────── 10ft ──── ● GW Soak Pit ───────────
              (x=-5, 5ft⌀)                    (x=5, 4ft⌀)
                                                         10ft
    y=38 ─── ─── ─── ─── ─── ─── ─── ─── ─── ─── ● WW Soak Pit ────
                                                    (x=15, 5ft⌀)
              12ft
    y=28 ─── ■ Septic (x=-5) ─── ■ Silt Trap (x=9) ─── ■ Grease Trap (x=15)
              
    y=33 ─── ─── ─── ─── ─── ─── ■ Oil Trap (x=8) ─── ■ GW Insp.Ch (x=12)
    
    ════════════════════════════════════════════════════════ y=25.75 (back wall)
    ║                                                    ║
    ║              BUILDING (20ft × 25ft)                ║
    ║                                                    ║
    ║  GF Toilet                           1F Toilet     ║
    ║  (x=1,y=1.5)                        (x=18,y=7)   ║        ⊕ BOREWELL
    ║                                                    ║        (x=51, y=2)
    ║            Floor Drain (x=10)                      ║
    ║                                                    ║
    ════════════════════════════════════════════════════════ y=-0.75 (front wall)
                         │
                    10-12ft gap
                         │
    ═══════════════ CHAKRODE (kachchi road) ═══════════════════════
```

### 3.2 Spacing Verification

| From | To | Distance | Minimum Required | Status |
|------|------|----------|-----------------|--------|
| Septic (x=-5,y=28) | BW Pit (x=-5,y=40) | **12ft** | 10ft (3m) | ✓ |
| BW Pit (x=-5,y=40) | GW Pit (x=5,y=40) | **10ft** | 10ft (3m) | ✓ |
| GW Pit (x=5,y=40) | WW Pit (x=15,y=38) | **10.2ft** | 10ft (3m) | ✓ |
| BW Pit (x=-5,y=40) | WW Pit (x=15,y=38) | **20ft** | 10ft | ✓ |
| Septic (x=-5,y=28) | GW Pit (x=5,y=40) | **15.6ft** | 10ft | ✓ |
| All structures | Building foundation | **>5ft** | 3m (10ft) | ✓ |

### 3.3 Borewell Safety Distances

Borewell at x=51, y=2 (30ft right of right wall, toward front).

| Structure | Distance from Borewell | Required | Status |
|-----------|----------------------|----------|--------|
| Septic Tank (x=-5, y=28) | **62ft** | 50ft | ✓ |
| BW Soak Pit (x=-5, y=40) | **68ft** | 50ft | ✓ |
| GW Soak Pit (x=5, y=40) | **60ft** | 50ft | ✓ |
| WW Soak Pit (x=15, y=38) | **51ft** | 45ft (user accepted) | ✓ |

---

## 4. CONSTRUCTION DETAILS

### 4.1 All Structures Are UNDERGROUND

| Structure | Top Level | Bottom Level | Earth Cover Above |
|-----------|-----------|-------------|-------------------|
| Septic Tank | z=0 (flush with farm land) | z=-4.5ft | 0 (RCC lid flush) |
| BW Soak Pit | z=0 | z=-7ft | RCC cover flush |
| GW Soak Pit | z=0 | z=-6ft | RCC cover flush |
| WW Soak Pit | z=0 | z=-6.5ft | RCC cover flush |
| Silt/Oil/Grease Traps | z=0 | z=-2.5ft | Flush covers |
| Inspection Chambers | z=0 | z=-2ft | CI cover flush |
| Underground pipes | z=-1 to z=-2.5 | — | 1.5-2.5ft below ground |

**Building plinth is at z=3 (raised 3ft above farm land). Pipes exit through plinth wall and slope DOWN to reach underground level (z=-1.5).**

### 4.2 Vehicular Load Consideration

The LEFT side is clear for tractors. Soak pits are BEHIND the building. If tractors need to pass over pits:

| Structure | Cover Design for Tractor Load |
|-----------|------------------------------|
| Septic Tank (2.5ft span) | 6" RCC lid — SAFE as-is |
| Soak Pits (4-5ft span) | 8" (200mm) RCC cover + solid brick top ring (2ft) + 2ft earth cover |
| Inspection Chambers | Heavy-duty CI cover (Class D, 40 tonne rated) |
| Traps | 6" RCC cover — SAFE (small span) |

### 4.3 Pipe Specifications

| Pipe Run | Size | Slope | Bends | Material |
|----------|------|-------|-------|----------|
| GF toilet → back wall | 110mm (4") | 1:40 | None (straight run) | PVC SWR |
| 1F toilet → back wall | 110mm (4") | 1:40 | None (straight run) | PVC SWR |
| Behind building (both lines → Y-junction) | 110mm | 1:40 | 45° Y-junction only | PVC SWR |
| Y-junction → Septic | 110mm | 1:40 | None | PVC SWR |
| Septic → BW Soak Pit | 110mm | 1:60 | None (gentle slope) | PVC SWR |
| Grey water (1F fixtures → downpipe) | 75mm (3") | 1:40 | 45° max | PVC SWR |
| GW downpipe → Grease trap | 75mm | 1:40 | 45° | PVC SWR |
| Floor drain → Silt trap | 110mm | 1:60 | None | PVC SWR |
| Silt → Oil trap → WW pit | 110mm | 1:60 | 45° | PVC SWR |
| Vent pipe (GF toilet → roof) | 50mm (2") | Vertical | — | PVC |

### 4.4 Joint Specifications

- All PVC SWR joints: **Solvent cement** (not rubber ring for underground)
- Pipe bedding: **150mm compacted sand** below and sides
- Backfill: **Selected earth (no stones)**, compacted in 150mm layers
- Minimum cover over pipes: **300mm** (under non-traffic areas), **600mm** (under tractor paths)

---

## 5. CONSTRUCTION SEQUENCE (Before Floor Slab Pour)

**All underground pipes must be laid BEFORE the GF floor slab is poured.**

1. Excavate pipe trenches (from toilet positions to back wall exit points)
2. Lay sand bedding (150mm)
3. Install pipe runs with correct slope (check with level)
4. Install Y-junction behind building
5. Connect to inspection chamber stubs
6. Backfill and compact
7. Leave pipe stubs at:
   - GF toilet position (x=1, y=1.5) — active immediately
   - 1F toilet position (x=18, y=7) — cap until 1F built
   - 1F grey water stub (near back wall, x=18) — cap until 1F built
   - Floor drain channel connection point (x=10, at back wall)
8. Pour GF floor slab over the buried pipes
9. Excavate behind building for septic, traps, and soak pits (can be done later)

---

## 6. SEPTIC TANK DESIGN

| Parameter | Value |
|-----------|-------|
| External size | 5ft × 2.5ft × 4.5ft deep |
| Internal size | 4ft × 1.5ft × 4ft (after 6" walls) |
| Capacity | ~1500 litres |
| Type | 2-chamber RCC (M20) |
| Chamber 1 (settling) | 3.3ft long |
| Chamber 2 (clarifying) | 1.2ft long |
| Baffle wall | 4" RCC, openings at 2/3 depth |
| Inlet | 110mm PVC, 6" below top (T-piece for scum retention) |
| Outlet | 110mm PVC, 9" below top (T-piece) |
| Manholes | 2 nos, 18"×18", RCC covers |
| Waterproofing | Internal: 2 coats bitumen emulsion |
| Cleaning interval | Every 2-3 years (tanker pumping) |

---

## 7. SOAK PIT DESIGN (Typical)

| Parameter | BW Pit | GW Pit | WW Pit |
|-----------|--------|--------|--------|
| Diameter | 5ft | 4ft | 5ft |
| Depth | 7ft | 6ft | 6.5ft |
| Wall | Honeycomb brick (dry laid) | Same | Same |
| Top ring (if vehicular) | 2ft solid mortared brick | Same | Same |
| Cover | 8" RCC (if tractor access) or 6" RCC | Same | Same |
| Gravel bed (bottom) | 2ft | 1.5ft | 1.5ft |
| Water table clearance | 13ft+ (WT at 20ft) | Same | Same |

---

## 8. 3D MODEL FILES

| File | Size | Contents |
|------|------|----------|
| `generate-plumbing-3d.py` | ~550 lines | Python generator script |
| `plumbing-3d.dae` | 133 KB | Collada 3D model |
| `plumbing-3d.glb` | 49 KB | GLB 3D model (better colors) |

**View on:** https://3dviewer.net (drag & drop .glb file)

**Color legend in 3D model:**
- Dark maroon = Black water pipes & fixtures
- Medium grey = Grey water pipes & fixtures  
- Sandy ochre = Wash water pipes & fixtures
- Blue = Rainwater downpipes + borewell marker + 50ft safety radius
- Brown strip = Chakrode (road)
- Light grey = Ghost building outline
- Red box = 45° Y-junction

---

## 9. APPLICABLE CODES

| Code | Relevance |
|------|-----------|
| IS 2470 (Part 1 & 2) | Septic tank design & installation |
| IS 1742 | Building drainage code of practice |
| NBC 2016 (Part 9) | Plumbing services |
| IS 5329 | Sanitary fittings |
| IS 14735 | PVC SWR pipe specifications |

---

*This document is the SINGLE SOURCE OF TRUTH for plumbing layout. It overrides any previous plumbing references in other documents.*
