# Electrical & Plumbing Specification

**Building:** Farm Storage, 20ft × 25ft, Moradabad, UP
**Electrical Load:** Light duty (lighting + sockets + pump)
**Water Source:** Submersible borewell (existing)

---

## PART A: ELECTRICAL

---

### 1. Electrical Layout Plan

```
                        20 ft
    ←──────────────────────────────────────→
    ┌──────────────────────────────────────┐ ─┐
    │                                      │  │
    │  [L3]              [L4]              │  │  ← 2 LED tubes (storage, back)
    │                                      │  │
    │                                      │  │
    │            [S2]                       │  │  ← Socket (15A, left wall)
    │                                      │  │
    │  [L1]              [L2]              │  │  ← 2 LED tubes (storage, front)
    │                                      │  │  25 ft
    │                          [S3]        │  │  ← Socket (15A, right wall)
    │                                      │  │
    │  ┌────────┐                          │  │
    │  │[L5]    │                          │  │  ← LED (stair landing)
    │  │ STAIR  │                          │  │
    │  ├──┬─────┤                          │  │
    │  │[L6]    │                          │  │  ← LED (toilet)
    │  │WC│LOBBY│              [S1]        │  │  ← Socket (15A, near shutter)
    ├──┴──┴──┬──┼──────────────────────┬───┤ ─┘
    │[SEC1]  │  │[SEC2]           [S4] │   │
    │GATE    │  │  SHUTTER             │   │  ← Security lights + socket
    └────────┴──┴──────────────────────┴───┘
    │               [L7] [L8]              │
    │          FRONT SHADE LIGHTS          │  ← 2 LEDs under shade
    └──────────────────────────────────────┘
    
    [DB] = Distribution Board (inside, front-right wall, 5ft height)
    [MB] = Meter Board (outside, front-right wall)
    [E1][E2] = Earth pits (outside, right side)
```

---

### 2. Lighting Schedule

| Point | Location | Fixture | Wattage | Height | Switch |
|-------|----------|---------|---------|--------|--------|
| L1 | Storage (front-center) | LED tube 4ft | 36W | 11 ft | SW1 (near DB) |
| L2 | Storage (front-right) | LED tube 4ft | 36W | 11 ft | SW1 (same switch) |
| L3 | Storage (back-left) | LED tube 4ft | 36W | 11 ft | SW2 (near back) |
| L4 | Storage (back-right) | LED tube 4ft | 36W | 11 ft | SW2 (same switch) |
| L5 | Staircase landing | LED bulb | 9W | 7 ft (at landing) | SW3 (at stair base) |
| L6 | Toilet | LED bulb (IP44 rated) | 9W | 7 ft | SW4 (outside WC door) |
| L7 | Front shade (left) | LED tube 4ft | 36W | 11 ft (soffit) | SW5 (near gate) |
| L8 | Front shade (right) | LED tube 4ft | 36W | 11 ft (soffit) | SW5 (same) |
| SEC1 | Security - gate | LED floodlight | 20W | 10 ft (above gate) | SW6 + motion sensor |
| SEC2 | Security - shutter | LED floodlight | 30W | 10 ft (above shutter) | SW6 (same circuit) |

**Total lighting load: ~290W**

---

### 2A. Ceiling Fan Schedule (6 nos.)

```
    CEILING FAN LAYOUT (storage area, 14ft × 25ft):
    
    ┌──────────────────────────────────────┐
    │                                      │
    │    [F1]          [F2]          [F3]  │  ← Row 1 (back third)
    │                                      │
    │                                      │
    │    [F4]          [F5]          [F6]  │  ← Row 2 (front third)
    │                                      │
    │  STAIR                               │
    │  AREA                                │
    └──────────────────────────────────────┘
    
    Grid: 3 across (at ~5ft, 9ft, 13ft from left wall)
          2 deep (at ~8ft and 17ft from front wall)
    All fans on 2ft drop rods from slab (operating height: ~10ft)
```

| Fan | Location | Spec | Rod | Switch |
|-----|----------|------|-----|--------|
| F1 | Storage back-left | 48" / 1200mm, 75W | 2ft drop rod | SW7 + regulator |
| F2 | Storage back-center | 48" / 1200mm, 75W | 2ft drop rod | SW7 (same) |
| F3 | Storage back-right | 48" / 1200mm, 75W | 2ft drop rod | SW7 (same) |
| F4 | Storage front-left | 48" / 1200mm, 75W | 2ft drop rod | SW8 + regulator |
| F5 | Storage front-center | 48" / 1200mm, 75W | 2ft drop rod | SW8 (same) |
| F6 | Storage front-right | 48" / 1200mm, 75W | 2ft drop rod | SW8 (same) |

**Fan specs:**
- Size: 48 inch (1200mm) sweep
- Wattage: 75W each (or 35W BLDC energy-efficient type)
- Drop rod: 2ft MS rod (brings fan to ~10ft from floor, below beam level)
- Regulator: Electronic step regulator (5-speed)
- Brand: Havells/Crompton/Orient

**Total fan load: 6 × 75W = 450W (or 210W if BLDC fans used)**

---

### 2B. Corner Lamps — Indoor (4 nos.)

| Lamp | Location | Fixture | Wattage | Height | Switch |
|------|----------|---------|---------|--------|--------|
| IL1 | Storage — back-left corner | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL2 | Storage — back-right corner | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL3 | Storage — front-left corner (above stair) | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL4 | Storage — front-right corner | LED wall-mount bracket light | 15W | 9 ft | SW9 |

**Total indoor corner lamp load: 4 × 15W = 60W**

---

### 2C. Outdoor Pole Lamps (4 nos.)

```
    POLE LAMP POSITIONS (building perimeter):
    
              [PL2]
    ┌─────────────────────────┐
    │                         │
[PL1]│       BUILDING         │[PL3]
    │                         │
    └─────────────────────────┘
              [PL4]
              FRONT
    
    Each pole: 10ft MS pipe (2" dia) set in concrete base
    Light: 20W LED street light (IP65) on top
    Positioned: 3ft away from building wall at each corner
```

| Lamp | Location | Fixture | Wattage | Height | Switch |
|------|----------|---------|---------|--------|--------|
| PL1 | Left-back corner (outside) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (dusk-to-dawn sensor) |
| PL2 | Right-back corner (outside) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (same) |
| PL3 | Right-front corner (outside) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (same) |
| PL4 | Left-front corner (outside) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (same) |

**Pole specs:**
- Pole: 10ft MS pipe (2" dia), galvanized, set in 1.5ft × 1.5ft × 2ft concrete base
- Light: 20W LED street light head (IP65, daylight white)
- Auto: Dusk-to-dawn photocell sensor (auto ON at night, OFF at dawn)
- Manual override: SW10 inside storage

**Total outdoor pole lamp load: 4 × 20W = 80W**

---

### 2D. CCTV Camera System (4 nos.)

```
    CAMERA POSITIONS:
    
                 [CAM2 - back wall]
    ┌──────────────────↓───────────────────┐
    │                  ◉                    │
    │                                       │
[CAM1]◉                                   ◉[CAM3]
    │ left wall                   right wall│
    │                                       │
    │                                       │
    └────────────────────────────────────────┘
                 ◉ [CAM4 - front/shutter]
                 FRONT
    
    All cameras: ceiling/wall mounted at 10ft height
    Coverage: 360° perimeter (no blind spots)
    Recording: NVR with 1TB HDD (near DB)
```

| Camera | Location | Coverage | Spec |
|--------|----------|----------|------|
| CAM1 | Left wall, mid-point (outside) | Left side + part of front/back | 3MP bullet, IR night vision 30m |
| CAM2 | Back wall, center (outside) | Entire back area | 3MP bullet, IR night vision 30m |
| CAM3 | Right wall, mid-point (outside) | Right side + part of front/back | 3MP bullet, IR night vision 30m |
| CAM4 | Front shade soffit (facing outward) | Shutter, ramp, gate area | 3MP bullet, IR night vision 30m |

**CCTV System specs:**
| Item | Specification |
|------|---------------|
| Cameras | 4 × 3MP IP bullet cameras, IP67, IR 30m |
| NVR | 4-channel NVR, 1TB HDD, H.265 compression |
| Cable | CAT6 LAN cable (PoE — Power over Ethernet) |
| Power | PoE switch (powers cameras through LAN cable) |
| NVR location | Near DB, inside storage (wall-mounted shelf) |
| Monitor | Optional — can view on mobile app (WiFi connected NVR) |
| Backup power | Connected to inverter/battery circuit (records during power cut) |
| Storage | 1TB ≈ 15-20 days recording at 3MP |

**Cable routing:**
- CAT6 cable from each camera → through conduit in wall → to NVR location
- All cables concealed in 25mm PVC conduits (same as electrical)
- Camera power via PoE (no separate power cable needed)

**Total CCTV load: 4 cameras × 15W + NVR 30W = 90W**

---

### 2E. Solar Hybrid Inverter + Battery System

```
    SYSTEM LAYOUT (near DB, front-right wall):
    
    ┌─────────────────────────────────────┐
    │                                     │
    │  ┌──────────┐  ┌──────┐  ┌──────┐  │  Wall-mounted / floor-standing
    │  │ HYBRID   │  │ BATT │  │ BATT │  │  against front-right wall
    │  │ INVERTER │  │  1   │  │  2   │  │
    │  │  3-5 kVA │  │150Ah │  │150Ah │  │  Height from floor: 1-3ft
    │  │          │  │ 12V  │  │ 12V  │  │
    │  └──────────┘  └──────┘  └──────┘  │
    │       ↑              ↑         ↑    │
    │       │              └────┬────┘    │
    │   From DB ───────── Battery bank    │
    │   + Solar conduit   (series/parallel│
    │     (from roof)      as needed)     │
    │                                     │
    └─────────────────────────────────────┘
    
    Total space required: 5ft wide × 2ft deep × 4ft high
    Location: Inside storage, front-right corner (near DB)
    Ventilation: Area must be ventilated (batteries emit gas)
```

**System specifications:**

| Item | Specification |
|------|---------------|
| Inverter type | Solar hybrid (accepts solar DC + grid AC) |
| Capacity | 3 kVA (expandable to 5 kVA) |
| Input | Grid AC (single phase) + Solar DC (future) |
| Output | 230V AC, pure sine wave |
| Battery | 2 × 150Ah, 12V tall tubular (Luminous/Exide) |
| Battery bank | 24V system (2 batteries in series) |
| Backup time | Lights + fans + cameras ≈ 6-8 hours |
| Solar ready | MPPT charge controller built-in (accepts 2-4 panels) |
| Transfer time | <10ms (UPS-grade, no flicker) |
| Space | 5ft W × 2ft D × 4ft H (near DB, ventilated area) |
| Brand | Luminous/Microtek/Growatt (solar hybrid) |

**Connection diagram:**
```
    SOLAR PANELS (future)          GRID SUPPLY (from meter)
         │ DC cables                      │ AC
         │ (via 32mm conduit              │ (from DB main)
         │  from roof)                    │
         ▼                                ▼
    ┌────────────────────────────────────────┐
    │         SOLAR HYBRID INVERTER          │
    │         (3-5 kVA)                      │
    │                                        │
    │  MPPT charge     │    AC charger       │
    │  controller      │    (grid to batt)   │
    └────────┬─────────┴──────────┬──────────┘
             │                    │
             ▼                    ▼
    ┌────────────────┐    ┌──────────────────┐
    │  BATTERY BANK  │    │  OUTPUT TO DB    │
    │  2 × 150Ah    │    │  (powers all     │
    │  (24V system) │    │   circuits via   │
    └────────────────┘    │   MCBs)          │
                          └──────────────────┘
    
    PRIORITY: Solar → Battery → Grid (automatic switching)
    During power cut: Battery powers essential circuits
    With solar: Panels charge battery + power loads (grid backup only)
```

**Essential circuits on battery backup:**
- All lights (290W)
- All fans (450W)
- CCTV system (90W)
- Total backup load: ~830W
- Backup time: 2 × 150Ah × 12V / 830W ≈ **4.3 hours** (at full load)
- Practical (50% load): **6-8 hours**

**Total inverter/battery load: 3000W max capacity**

---

### UPDATED LOAD SUMMARY

| Circuit | Load | Notes |
|---------|------|-------|
| Lighting (tubes + bulbs) | 290W | L1-L8, SEC1-SEC2 |
| Ceiling fans (6 nos.) | 450W | F1-F6 (or 210W with BLDC) |
| Indoor corner lamps (4 nos.) | 60W | IL1-IL4 |
| Outdoor pole lamps (4 nos.) | 80W | PL1-PL4 |
| CCTV system | 90W | 4 cameras + NVR |
| Power sockets | 3000W | S1-S5 (max one heavy device) |
| Pump | 750W | 1 HP submersible |
| Inverter standby | 30W | Idle consumption |
| **TOTAL CONNECTED LOAD** | **~4750W** | — |
| **Maximum demand (diversity)** | **~3500W** | Not everything runs together |

**Recommended connection: Single phase, 5 kW** (adequate with diversity factor)

| Point | Location | Type | Height | Purpose |
|-------|----------|------|--------|---------|
| S1 | Front wall (right of shutter, inside) | 15A + switch | 4 ft | Equipment, pump switch |
| S2 | Left wall (mid-height) | 15A + switch | 4 ft | Tools, chargers |
| S3 | Right wall (mid-section) | 15A + switch | 4 ft | General purpose |
| S4 | Front wall (outside, under shade) | 15A weatherproof | 3 ft | External equipment |
| S5 | Toilet (inside) | 5A + switch | 5 ft | Future geyser / exhaust fan |

**Total socket points: 5 (4 × 15A + 1 × 5A)**
**Assumed socket load: ~3000W max (one device at a time)**

---

### 4. Distribution Board (DB)

**Location:** Inside storage, front-right wall, at 5ft height (away from tractor path, accessible)
**Note:** Inverter output connects AFTER the DB main switch (powers all circuits during outage)

```
┌─────────────────────────────────────────────────────────┐
│                 DISTRIBUTION BOARD (12-way)              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  GRID INPUT ──→ INVERTER ──→ MAIN SWITCH 63A DP MCB    │
│       │              │              │                   │
│       │              │              ├── MCB 1: 6A ──── Lighting 1         │
│       │              │              │       (L1-L4 storage tubes)         │
│       │              │              │                                     │
│       │              │              ├── MCB 2: 6A ──── Lighting 2         │
│       │              │              │       (L5-L8, SEC1-SEC2, IL1-IL4)   │
│       │              │              │                                     │
│       │              │              ├── MCB 3: 6A ──── Outdoor Lighting   │
│       │              │              │       (PL1-PL4 pole lamps)          │
│       │              │              │                                     │
│       │              │              ├── MCB 4: 10A ─── Ceiling Fans 1     │
│       │              │              │       (F1, F2, F3 — back row)       │
│       │              │              │                                     │
│       │              │              ├── MCB 5: 10A ─── Ceiling Fans 2     │
│       │              │              │       (F4, F5, F6 — front row)      │
│       │              │              │                                     │
│       │              │              ├── MCB 6: 16A ─── Power Sockets      │
│       │              │              │       (S1-S5, all sockets)          │
│       │              │              │                                     │
│       │              │              ├── MCB 7: 16A ─── Pump Circuit       │
│       │              │              │       (submersible pump, dedicated) │
│       │              │              │                                     │
│       │              │              ├── MCB 8: 6A ──── CCTV System        │
│       │              │              │       (PoE switch + NVR)            │
│       │              │              │                                     │
│       │              │              ├── MCB 9: 16A ─── Inverter Charging  │
│       │              │              │       (grid → inverter charger)     │
│       │              │              │                                     │
│       │              │              └── MCB 10: 16A ── SPARE (future 1F)  │
│       │              │                   (conduit to first floor)         │
│       │              │                                                    │
│  ELCB/RCCB: 63A, 30mA ─── Earth Leakage Protection                      │
│  (protects all circuits, trips on 30mA earth leakage)                    │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

**DB Specifications:**
- Box: 12-way TPN (Triple Pole Neutral), metal, IP43 rated
- Brand: Havells/Legrand/Schneider
- Main: 63A DP MCB
- ELCB: 63A, 30mA sensitivity (life safety)
- MCBs: C-curve for general loads (10 active + 2 spare slots)
- Busbar: Copper, rated for 63A
- Inverter integration: Grid input → Inverter → DB (all circuits get backup)

---

### 5. Earthing System

```
    BUILDING (right side)
    ═══════════════════════
              │
    ──────────┼──── 8 SWG GI wire (earth continuity conductor)
              │     runs along wall at plinth level
              │
         ┌────┴────┐
         │         │
    ┌────┴───┐ ┌───┴────┐
    │EARTH   │ │EARTH   │
    │PIT 1   │ │PIT 2   │     2 earth pits, 6ft apart
    │(body)  │ │(neutral)│
    └────────┘ └────────┘
    
    Each pit: 2ft × 2ft × 8ft deep
    Contents: GI pipe (2" dia, 8ft long) + salt + charcoal layers
    Top: CI cover plate (inspection lid)
    Resistance target: < 5 ohms (test with megger)
```

**Earth pit construction:**
1. Dig 2ft × 2ft × 8ft deep pit
2. Insert 2" dia GI pipe (8ft long, with holes drilled at bottom 3ft)
3. Fill around pipe: alternate layers of charcoal (6") + salt (3") + earth
4. Connect 8 SWG GI wire from pipe top to DB earth bar
5. Cover with CI inspection plate
6. Water the pit periodically (especially before monsoon) to maintain conductivity
7. Connect all sockets, metal fixtures, and DB body to earth

---

### 6. Meter Board (External)

**Location:** Outside, front-right wall (accessible to meter reader)
**Height:** 5 ft from platform level (8 ft from ground)

Contents:
- Energy meter (single phase) — installed by electricity board
- Main 63A fuse / MCB (before meter)
- Service wire entry from electricity pole
- Conduit from meter board → DB (through wall)

**Service connection:**
- Type: Single phase, 5 kW connection (adequate for this load)
- Wire: 2 × 6 sq mm + 1 × 6 sq mm earth (service cable from pole)
- Future: Can upgrade to 3-phase if adding heavy machinery on first floor

---

### 7. Wiring Specifications

| Item | Specification |
|------|--------------|
| Wiring type | Concealed (in PVC conduits embedded in walls) |
| Conduit size | 20mm (light), 25mm (power) |
| Light circuit wire | 1.5 sq mm FR (flame retardant) copper |
| Power circuit wire | 2.5 sq mm FR copper |
| Pump circuit wire | 4 sq mm FR copper |
| Earth wire | 1.5 sq mm green/yellow FR copper (all circuits) |
| Conduit | Heavy gauge PVC, ISI marked |
| Switch/socket brand | Anchor/Havells/Legrand (modular type) |
| Switch board | 6-module boards at each point |

**Wiring route (concealed in walls):**
- All wiring in PVC conduits embedded during plastering stage
- Horizontal runs at 1ft below ceiling or 1ft above floor
- Vertical runs straight up/down from switches to horizontal run
- No diagonal wiring (makes future tracing impossible)
- Junction boxes at every branch/turn (accessible)

---

### 8. Security Lighting Detail

| Item | Specification |
|------|--------------|
| SEC1 (Gate) | 20W LED floodlight, warm white, with PIR motion sensor |
| SEC2 (Shutter) | 30W LED floodlight, daylight white, manual + motion sensor |
| Sensor range | 8-10 meters, 120° detection angle |
| Override | Manual switch (SW6) to keep ON continuously when needed |
| Timer | Optional dusk-to-dawn photocell (auto ON at night) |
| Height | 10 ft from platform (13 ft from ground) |
| IP rating | IP65 (weatherproof for rain/dust) |

---

## PART B: PLUMBING

---

### 9. Water Supply System

```
    ROOF LEVEL (+15 ft):
    ┌─────────────────┐
    │   500L HDPE     │  ← Overhead tank (Sintex/Supreme)
    │   TANK          │     on MS angle stand (2ft above slab)
    │                 │     Position: above toilet zone (front-left)
    ├────┬────────────┤
    │    │ OVERFLOW    │──→ 1" PVC pipe → away from building
    │    │ (1")       │
    └────┼────────────┘
         │
         │ 3/4" CPVC (main distribution pipe)
         │
    ┌────┼──────────── DISTRIBUTION AT CEILING LEVEL ──────────┐
    │    │                                                      │
    │    ├────── 1/2" CPVC ──→ TOILET (commode flush + basin)  │
    │    │                                                      │
    │    ├────── 1/2" CPVC ──→ EXTERNAL TAP (right side wall)  │
    │    │                                                      │
    │    └────── 1/2" CPVC ──→ FUTURE (1F sleeve, capped)     │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
    
    
    SUPPLY TO TANK (from borewell):
    
    BOREWELL ──→ SUBMERSIBLE PUMP (1 HP) ──→ 1" GI PIPE (rising main)
                                              ──→ NRV (non-return valve)
                                              ──→ GATE VALVE (at roof)
                                              ──→ TANK INLET
    
    AUTO CONTROL:
    - Float valve inside tank (mechanical) OR
    - Electronic water level controller (pump auto ON/OFF)
    - Dry-run protector on pump (prevents damage if water table drops)
```

**Pipe sizing:**
| Pipe | Size | Material | Purpose |
|------|------|----------|---------|
| Rising main (pump → tank) | 1" (25mm) | GI (galvanized iron) | Handles pump pressure |
| Main distribution | 3/4" (20mm) | CPVC | From tank downward |
| Branch lines | 1/2" (15mm) | CPVC | To each fixture |
| Overflow | 1" (25mm) | PVC | Tank overflow |
| Vent pipe | 1" (25mm) | PVC | Tank air vent |

**Valves:**
| Valve | Location | Purpose |
|-------|----------|---------|
| Gate valve (1") | At tank inlet | Isolate tank for maintenance |
| Gate valve (3/4") | Below tank, on main | Shut off entire supply |
| Angle valve (1/2") | At each fixture | Isolate toilet/tap individually |
| NRV (non-return) | After pump | Prevent backflow |
| Float valve | Inside tank | Auto-stop when tank full |

---

### 10. Toilet Plumbing (Detailed)

```
    PLAN VIEW (toilet 3ft × 5ft):
    
    ┌──────────────────────────┐
    │      ┌──── 1/2" CPVC supply (concealed in wall)
    │      │                   │
    │  ┌───┴──┐                │
    │  │FLUSH │ ← Concealed flush tank (8/10L dual)
    │  │TANK  │                │
    │  ├──────┤                │
    │  │      │    ┌──────┐    │
    │  │ WC   │    │BASIN │←── 1/2" supply
    │  │      │    │  □   │    │
    │  └──┬───┘    └──┬───┘    │
    │     │           │        │
    │  4" SOIL     2" WASTE    │
    │  PIPE        PIPE        │
    │     │           │        │
    │     └─────┬─────┘        │
    │           │              │
    │     ┌─────┴─────┐        │
    │     │ FLOOR TRAP │        │ ← Nahani trap (for floor washing)
    │     │ (jali)     │        │
    │     └─────┬─────┘        │
    │           │              │
    └───────────┼──────────────┘
                │
            4" PVC (underground)
                │
    ════════════╪═══════════════ (below floor slab)
                │
                │  Slope: 1:40 minimum (2.5%)
                │  Depth: 1.5 ft below floor
                │
                ▼
    ┌──────────────────┐
    │    SOAK PIT      │  (10 ft from building)
    │    4ft dia       │
    │    6ft deep      │
    └──────────────────┘
    
    
    SECTION VIEW (toilet plumbing):
    
    ROOF ─────────────────────
         │ 2" VENT PIPE ↑     (goes above roof for air)
         │              │
    +12ft├──────────────┼─── 1/2" CPVC supply from tank
         │              │
         │  ┌─FLUSH─┐   │
         │  │ TANK  │   │
         │  └───┬───┘   │
         │      │        │
    +1ft │   WC │        │ BASIN
         │      │        │
    FLOOR├──────┼────────┼───
         │   4" PVC   2" PVC     FLOOR SLAB (4" RCC)
         │      │        │
         │      └────┬───┘       PCC + EARTH FILL
         │           │
    -1ft │       COMBINED 4" PVC (below floor)
         │           │
         │     slope: 1:40 →→→→→ toward soak pit
    ─────┴───────────┴───────────
```

**Key specifications:**
| Element | Spec |
|---------|------|
| Soil pipe (from WC) | 4" PVC SWR (Soil, Waste, Rain) |
| Waste pipe (from basin) | 2" PVC SWR |
| Vent pipe | 2" PVC, extends 1ft above roof (prevents air lock in drain) |
| P-trap (basin) | 2" PVC, 75mm water seal |
| S-trap (WC) | Built into commode (floor-mounted) |
| Floor trap (nahani) | 4" CI with SS grill |
| Underground pipe | 4" PVC, bedded on sand, 1:40 slope |
| Pipe joints | Solvent cement (PVC) / threaded (CPVC) |

---

### 11. Drainage System

```
    ROOF DRAINAGE:
    
    ┌──────────────────────────────────────┐
    │            ROOF SLAB                 │
    │                                      │
    │  [DP1]                        [DP2]  │  ← Downpipes at back corners
    │                                      │
    │                                      │
    │  [DP3]                        [DP4]  │  ← Downpipes at front corners
    │                                      │
    └──────────────────────────────────────┘
    
    Downpipes: 3" (75mm) PVC
    From roof → along external wall → to ground drain
    Ground drain: Open channel (6" wide) → directed away from building
    Roof slope: 1:100 toward downpipe corners (formed in china mosaic)
    
    
    FLOOR DRAINAGE (storage):
    
    ┌──────────────────────────────────────┐
    │                                      │
    │                                      │
    │  ═══════════════════════════════════  │  ← Floor drain channel
    │         (center, 6" wide)            │     (shallow V-channel in floor)
    │         slope: 1:100 toward front    │
    │                                      │
    │                                      │
    ├──────────────────────────────────────┤
    │         ║ drain exits here           │  ← Through front wall
    └─────────╨────────────────────────────┘     (below shutter threshold)
              │
              ▼ Exits through plinth wall to outside
              (open drain away from building)
    
    Floor slope: Entire storage floor slopes 1:100 toward the center channel
    Channel: 6" wide × 3" deep, cement finish, with removable SS grill on top
    Purpose: Wash water, spills, cleaning — drains out front without pooling
```

---

### 12. External Water Tap

**Location:** Right side wall, near front (accessible from shutter area)
**Height:** 2 ft from platform level (5 ft from ground)

```
    RIGHT SIDE WALL (outside view):
    
    ┌─────────────────────────────────┐  ROOF
    │                                 │
    │  ← 1/2" CPVC (concealed,       │
    │     coming from distribution    │
    │     pipe at ceiling level)      │
    │                                 │
    │            │                    │
    │       ┌────┴────┐               │
    │       │ ANGLE   │ ← Stop valve  │  @ 2ft from floor
    │       │ VALVE   │               │
    │       └────┬────┘               │
    │       ┌────┴────┐               │
    │       │BIB COCK │ ← Brass tap   │  @ 2ft from floor
    │       │ (tap)   │   (heavy duty)│
    │       └─────────┘               │
    │                                 │
    │       ┌─────────┐               │
    │       │CONCRETE │ ← Small wash  │  @ platform level
    │       │PLATFORM │   platform    │
    │       │+ DRAIN  │   with drain  │
    │       └─────────┘               │
    │                                 │
    ├─────────────────────────────────┤  PLINTH TOP (+3ft)
    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    └─────────────────────────────────┘  GROUND (0ft)
```

**Specs:**
- Tap: 15mm (1/2") heavy duty brass bib cock
- Stop valve: 15mm angle valve (to isolate tap without affecting toilet)
- Platform: 2ft × 2ft concrete wash area with drain slope
- Drain: Small PVC pipe directing water away from plinth
- Use: Cleaning equipment, washing, general farm use

---

## PART C: FUTURE PROVISIONS

---

### 13. Electrical Conduits for First Floor

```
    SECTION (showing conduit path from GF to 1F):
    
    FIRST FLOOR (future) ──────────────────
         │                        │
         │  Conduit exits here    │  ← Stub out at floor level
         │  (capped with tape)   │     for future connection
         │                        │
    SLAB ─╪════════════════════════╪─── Sleeve through slab (PVC)
         │                        │
         │  ┌── 25mm PVC conduit  │
         │  │   (with draw wire   │
         │  │    inside)          │
         │  │                     │
         │  │   Embedded in       │
         │  │   column/wall       │
         │  │                     │
    DB ──┼──┘                     │
         │                        │
    GROUND FLOOR ─────────────────────
```

**Provision locations (3 conduits):**

| # | From | To | Route | Purpose |
|---|------|----|-------|---------|
| 1 | DB (MCB 6 - spare) | Slab opening near front-left | Up through stair wall column | Main power feed for 1F (4 sq mm wire future) |
| 2 | Near DB | Slab opening near back-right | Up through right wall | Second circuit for 1F (lighting/AC) |
| 3 | Gate/switch area | Slab opening near stairwell | Along stair partition wall | Staircase lighting from ground to 1F |

**Specifications:**
- Conduit: 25mm heavy gauge PVC
- Draw wire: 16 SWG GI wire (pulled through conduit for future cable pulling)
- Slab sleeve: 2" PVC pipe cast into slab at each conduit exit point
- Cap: Sealed with tape/plug to prevent concrete entry during construction
- Label: Mark location with permanent marker on slab top and soffit

---

### 14. Plumbing Sleeves for First Floor

```
    SLAB (plan view — showing sleeve positions):
    
    ┌──────────────────────────────────────┐
    │                                      │
    │                     ┌──┐             │  ← SLEEVE 3: Kitchen area (future)
    │                     │S3│             │     4" PVC pipe, capped
    │                     └──┘             │
    │                                      │
    │                                      │
    │  ┌──┐ ┌──┐                           │  ← SLEEVE 1 + 2: Above current toilet
    │  │S1│ │S2│                           │     (future 1F bathroom)
    │  └──┘ └──┘                           │     S1: 4" (soil), S2: 2" (supply)
    │                                      │
    ├──────────────────────────────────────┤
    │                                      │
    └──────────────────────────────────────┘
         FRONT
    
    All sleeves: PVC pipe cast into slab, 2" larger than the pipe that
    will pass through. Capped/sealed on both sides until needed.
```

**Sleeve schedule:**

| Sleeve | Size | Location | Purpose |
|--------|------|----------|---------|
| S1 | 4" PVC | Above current toilet (front-left) | Future 1F bathroom soil pipe |
| S2 | 2" PVC | Adjacent to S1 | Future 1F bathroom supply pipe |
| S3 | 4" PVC | Back-right quadrant | Future 1F kitchen waste pipe |

**Installation notes:**
- Cast sleeves during slab pour (place PVC pipes vertically in slab formwork)
- Fill sleeves with newspaper/foam during pour (prevent concrete blocking)
- After slab cure: remove packing, cap both ends with PVC caps
- Sleeves must be 2" larger than future pipe (S1: use 6" PVC as sleeve for 4" pipe)

---

### 15. Solar Panel Wiring Conduit

```
    ROOF LEVEL:
    ┌──────────────────────────────────────┐
    │                                      │
    │   SOLAR PANELS (future)              │
    │                                      │
    │                  ┌──┐                │  ← Conduit starts at parapet
    │                  │  │ 32mm PVC       │     (junction box location for
    │                  │  │                │      DC cables from panels)
    ├──────────────────┼──┼────────────────┤
    │   FIRST FLOOR    │  │                │
    │                  │  │ (inside wall)  │
    ├──────────────────┼──┼────────────────┤
    │   GROUND FLOOR   │  │                │
    │                  │  │                │
    │              ┌───┴──┴───┐            │
    │              │ INVERTER  │            │  ← Inverter/charge controller
    │              │ LOCATION  │            │     location (near DB)
    │              │ (near DB) │            │
    │              └───────────┘            │
    └──────────────────────────────────────┘
```

**Specifications:**
- Conduit: 32mm PVC (larger for DC cables which are thicker)
- Route: From roof parapet (right side) → down through right wall → to ground floor near DB
- Junction box at roof: weatherproof IP65, for connecting solar panel MC4 cables
- Junction box at ground: near DB, for inverter/charge controller connection
- Draw wire: 14 SWG GI wire inside conduit
- Future cables: 2 × 6 sq mm DC solar cable (positive + negative)
- Space near DB: Reserve 2ft × 2ft wall space for future inverter/battery mounting

---

## PART D: CONTRACTOR NOTES (Electrical + Plumbing)

---

### 16. When to Do What (Sequence)

| Construction Phase | Electrical Work | Plumbing Work |
|-------------------|-----------------|---------------|
| **Foundation** | Earth pit excavation | Underground drain pipe (toilet → soak pit) |
| **Plinth walls** | — | Floor drain channel formation |
| **Floor slab** | Conduit under floor (if any) | Floor trap embedding |
| **Walls going up** | Embed conduits in walls (BEFORE plastering!) | Embed supply pipes in walls |
| **Staircase** | Stair light conduit | — |
| **Before slab pour** | Future conduit sleeves through slab | Future plumbing sleeves through slab |
| **Slab pour** | Solar conduit sleeve | Pipe sleeves cast in slab |
| **After slab cure** | Pull wires, fix DB, switches, lights | Fix tank, connect pump, test flush |
| **Plastering** | Cover conduits (already embedded) | Cover pipes (already embedded) |
| **Finishing** | Fix fixtures (lights, fans, sockets) | Fix fixtures (commode, basin, taps) |

### 17. Critical Reminders

**Electrical:**
- Embed ALL conduits BEFORE plastering — you cannot chase walls after plaster without damage
- Keep conduit runs straight (horizontal/vertical only) — no diagonals
- Use junction boxes at every turn — don't bend conduits at sharp angles
- Pull draw wire through during embedding — pulling later is very difficult
- Leave 12" extra wire at every switch/socket point (for connections)
- Test all circuits with megger BEFORE connecting to mains
- Earth ALL metal fixtures (lights, fans, socket bodies)

**Plumbing:**
- Underground drain pipes MUST be laid BEFORE floor slab is poured
- Maintain 1:40 slope on all drain pipes (check with spirit level + straight edge)
- CPVC pipes expand in heat — leave 1" gap at joints for thermal expansion
- Test water supply for leaks BEFORE concealing in walls (24-hour pressure test)
- Vent pipe from toilet MUST go above roof level (prevents air lock = slow drainage)
- Tank platform must be strong enough for 500 kg (full tank weight)

---

### 18. Material List (Electrical + Plumbing)

**Electrical:**
| Item | Qty | Specification |
|------|-----|---------------|
| PVC conduit 20mm | 200 rft | Heavy gauge, ISI marked |
| PVC conduit 25mm | 120 rft | For power + fan + CCTV circuits |
| PVC conduit 32mm | 40 rft | For solar conduit |
| Wire 1.5 sq mm | 300 m | FR copper, light + fan circuits |
| Wire 2.5 sq mm | 200 m | FR copper, power + fan circuits |
| Wire 4 sq mm | 50 m | FR copper, pump + inverter |
| Earth wire 1.5 sq mm | 150 m | Green-yellow FR copper |
| DB box 12-way TPN | 1 | Metal, IP43 |
| MCBs (6A, 10A, 16A) | 10 | C-curve |
| ELCB 63A/30mA | 1 | Life safety |
| Main switch 63A DP | 1 | — |
| Ceiling fans 48" | 6 | 75W (or BLDC 35W), with drop rods |
| Fan drop rods 2ft | 6 | MS chromed |
| Fan regulators (electronic) | 2 | 5-speed step type |
| LED tubes 4ft 36W | 6 | With fittings |
| LED bulbs 9W | 2 | Holder + bulb |
| LED wall bracket lights 15W | 4 | Indoor corner lamps |
| LED pole lights 20W (IP65) | 4 | Outdoor, with photocell |
| MS poles 2" × 10ft | 4 | Galvanized, for outdoor lamps |
| Pole base concrete | 4 | 1.5ft × 1.5ft × 2ft each |
| LED floodlight 20W | 1 | IP65, with PIR sensor |
| LED floodlight 30W | 1 | IP65, with PIR sensor |
| IP bullet camera 3MP | 4 | IP67, IR 30m night vision |
| NVR 4-channel | 1 | 1TB HDD, H.265, WiFi |
| PoE switch 4+1 port | 1 | 10/100 Mbps, 60W budget |
| CAT6 LAN cable | 100 m | Outdoor-rated for camera runs |
| Solar hybrid inverter 3kVA | 1 | MPPT, pure sine wave |
| Tall tubular battery 150Ah | 2 | 12V, Luminous/Exide |
| Battery rack/trolley | 1 | MS, 2-battery capacity |
| Modular switches | 12 | 6A, piano type |
| Modular sockets 15A | 4 | With switch |
| Modular socket 5A | 1 | With switch |
| Switch boards (6-module) | 10 | Surface/flush mount |
| Junction boxes | 15 | PVC, round |
| GI earth pipe 2" × 8ft | 2 | For earth pits |
| GI wire 8 SWG | 30 m | Earth continuity |
| Draw wire 16 SWG | 100 m | For future pulling |

**Plumbing:**
| Item | Qty | Specification |
|------|-----|---------------|
| CPVC pipe 3/4" | 20 rft | Main supply from tank |
| CPVC pipe 1/2" | 60 rft | Branch supply lines |
| CPVC fittings (elbows, tees) | 1 set | As required |
| PVC SWR pipe 4" | 50 rft | Soil pipe + underground |
| PVC SWR pipe 3" | 60 rft | Downpipes (4 nos. × 15ft) |
| PVC SWR pipe 2" | 20 rft | Waste pipe + vent |
| PVC fittings (bends, Y, tees) | 1 set | SWR type |
| GI pipe 1" | 30 rft | Rising main (pump to tank) |
| Gate valves 1" | 2 | At tank inlet + main |
| Angle valves 1/2" | 4 | At each fixture |
| Float valve 1" | 1 | Inside tank |
| NRV (non-return valve) 1" | 1 | After pump |
| Bib cock (brass) 15mm | 2 | External tap + toilet tap |
| Floor trap 4" | 2 | Nahani (SS grill) |
| P-trap 2" | 1 | Basin |
| Western commode (S-trap) | 1 | With seat, Hindware/Cera |
| Concealed flush tank | 1 | 8/10L dual flush |
| Wash basin (wall mount) | 1 | 12"×18" with pedestal/bracket |
| PVC solvent cement | 2 tins | For PVC joints |
| CPVC solvent cement | 1 tin | For CPVC joints |
| Teflon tape | 5 rolls | For threaded joints |
| 500L HDPE tank | 1 | Sintex/Supreme |
| MS angle stand (tank) | 1 set | 2ft height, on roof |
| Submersible pump 1 HP | 1 | (may use existing) |
| Water level controller | 1 | Electronic, auto ON/OFF |
