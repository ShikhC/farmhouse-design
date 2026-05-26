# बिजली और प्लंबिंग विवरण

**भवन:** फार्म स्टोरेज, 20ft × 25ft, मुरादाबाद, UP
**बिजली का भार:** हल्का (lighting + sockets + pump)
**पानी का स्रोत:** Submersible borewell (मौजूदा)

---

## भाग A: बिजली (ELECTRICAL)

---

### 1. बिजली का लेआउट प्लान

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

### 2. लाइट की अनुसूची (Lighting Schedule)

| पॉइंट | जगह | फिक्सचर | वॉट | ऊंचाई | Switch |
|--------|------|---------|------|--------|--------|
| L1 | Storage (आगे-बीच) | LED tube 4ft | 36W | 11 ft | SW1 (DB के पास) |
| L2 | Storage (आगे-दायां) | LED tube 4ft | 36W | 11 ft | SW1 (वही switch) |
| L3 | Storage (पीछे-बायां) | LED tube 4ft | 36W | 11 ft | SW2 (पीछे) |
| L4 | Storage (पीछे-दायां) | LED tube 4ft | 36W | 11 ft | SW2 (वही switch) |
| L5 | सीढ़ी लैंडिंग | LED bulb | 9W | 7 ft (लैंडिंग पर) | SW3 (सीढ़ी के नीचे) |
| L6 | शौचालय | LED bulb (IP44 rated) | 9W | 7 ft | SW4 (WC दरवाज़े के बाहर) |
| L7 | आगे शेड (बायां) | LED tube 4ft | 36W | 11 ft (soffit) | SW5 (गेट के पास) |
| L8 | आगे शेड (दायां) | LED tube 4ft | 36W | 11 ft (soffit) | SW5 (वही) |
| SEC1 | Security - गेट | LED floodlight | 20W | 10 ft (गेट के ऊपर) | SW6 + motion sensor |
| SEC2 | Security - शटर | LED floodlight | 30W | 10 ft (शटर के ऊपर) | SW6 (वही circuit) |

**कुल lighting भार: ~290W**

---

### 2A. छत के पंखों की अनुसूची (6 नग)

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

| पंखा | जगह | स्पेक | रॉड | Switch |
|------|------|-------|-----|--------|
| F1 | Storage पीछे-बायां | 48" / 1200mm, 75W | 2ft drop rod | SW7 + regulator |
| F2 | Storage पीछे-बीच | 48" / 1200mm, 75W | 2ft drop rod | SW7 (वही) |
| F3 | Storage पीछे-दायां | 48" / 1200mm, 75W | 2ft drop rod | SW7 (वही) |
| F4 | Storage आगे-बायां | 48" / 1200mm, 75W | 2ft drop rod | SW8 + regulator |
| F5 | Storage आगे-बीच | 48" / 1200mm, 75W | 2ft drop rod | SW8 (वही) |
| F6 | Storage आगे-दायां | 48" / 1200mm, 75W | 2ft drop rod | SW8 (वही) |

**पंखे की विशेषताएं:**
- साइज़: 48 inch (1200mm) sweep
- वॉट: 75W प्रत्येक (या 35W BLDC एनर्जी-सेविंग टाइप)
- ड्रॉप रॉड: 2ft MS rod (पंखा फर्श से ~10ft पर आएगा, बीम लेवल के नीचे)
- रेगुलेटर: Electronic step regulator (5-speed)
- ब्रांड: Havells/Crompton/Orient

**कुल पंखा भार: 6 × 75W = 450W (या 210W अगर BLDC पंखे लगाए)**

---

### 2B. कोने की लाइट — अंदर (4 नग)

| लैंप | जगह | फिक्सचर | वॉट | ऊंचाई | Switch |
|------|------|---------|------|--------|--------|
| IL1 | Storage — पीछे-बायां कोना | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL2 | Storage — पीछे-दायां कोना | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL3 | Storage — आगे-बायां कोना (सीढ़ी के ऊपर) | LED wall-mount bracket light | 15W | 9 ft | SW9 |
| IL4 | Storage — आगे-दायां कोना | LED wall-mount bracket light | 15W | 9 ft | SW9 |

**कुल अंदर की कोने की लाइट भार: 4 × 15W = 60W**

---

### 2C. बाहर के पोल लैंप (4 नग)

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

| लैंप | जगह | फिक्सचर | वॉट | ऊंचाई | Switch |
|------|------|---------|------|--------|--------|
| PL1 | बायां-पीछे कोना (बाहर) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (dusk-to-dawn sensor) |
| PL2 | दायां-पीछे कोना (बाहर) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (वही) |
| PL3 | दायां-आगे कोना (बाहर) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (वही) |
| PL4 | बायां-आगे कोना (बाहर) | 20W LED pole light, IP65 | 20W | 10 ft pole | SW10 (वही) |

**पोल विशेषताएं:**
- पोल: 10ft MS pipe (2" dia), galvanized, 1.5ft × 1.5ft × 2ft कंक्रीट बेस में लगा हुआ
- लाइट: 20W LED street light head (IP65, daylight white)
- ऑटो: Dusk-to-dawn photocell sensor (रात को अपने आप ON, सुबह OFF)
- मैनुअल: SW10 अंदर storage में

**कुल बाहर की पोल लैंप भार: 4 × 20W = 80W**

---

### 2D. CCTV कैमरा सिस्टम (4 नग)

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

| कैमरा | जगह | कवरेज | स्पेक |
|--------|------|--------|-------|
| CAM1 | बायीं दीवार, बीच (बाहर) | बायां साइड + आगे/पीछे का हिस्सा | 3MP bullet, IR night vision 30m |
| CAM2 | पीछे की दीवार, बीच (बाहर) | पूरा पीछे का हिस्सा | 3MP bullet, IR night vision 30m |
| CAM3 | दायीं दीवार, बीच (बाहर) | दायां साइड + आगे/पीछे का हिस्सा | 3MP bullet, IR night vision 30m |
| CAM4 | आगे शेड soffit (बाहर की तरफ) | शटर, रैंप, गेट एरिया | 3MP bullet, IR night vision 30m |

**CCTV सिस्टम विशेषताएं:**
| सामान | विवरण |
|--------|--------|
| कैमरे | 4 × 3MP IP bullet cameras, IP67, IR 30m |
| NVR | 4-channel NVR, 1TB HDD, H.265 compression |
| केबल | CAT6 LAN cable (PoE — Power over Ethernet) |
| पावर | PoE switch (LAN केबल से कैमरों को बिजली देता है) |
| NVR जगह | DB के पास, storage के अंदर (दीवार पर शेल्फ) |
| मॉनिटर | ऐच्छिक — मोबाइल app पर देख सकते हैं (WiFi connected NVR) |
| बैकअप पावर | Inverter/battery circuit पर कनेक्ट (बिजली कटने पर भी रिकॉर्ड करता है) |
| स्टोरेज | 1TB ≈ 15-20 दिन की रिकॉर्डिंग 3MP पर |

**केबल रूटिंग:**
- CAT6 केबल हर कैमरे से → दीवार में conduit से होकर → NVR तक
- सभी केबल 25mm PVC conduits में छुपी हुई (बिजली वाली ही)
- कैमरे की बिजली PoE से (अलग से पावर केबल नहीं चाहिए)

**कुल CCTV भार: 4 cameras × 15W + NVR 30W = 90W**

---

### 2E. Solar Hybrid Inverter + Battery सिस्टम

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

**सिस्टम विशेषताएं:**

| सामान | विवरण |
|--------|--------|
| Inverter प्रकार | Solar hybrid (solar DC + grid AC दोनों लेता है) |
| क्षमता | 3 kVA (5 kVA तक बढ़ा सकते हैं) |
| इनपुट | Grid AC (single phase) + Solar DC (भविष्य में) |
| आउटपुट | 230V AC, pure sine wave |
| बैटरी | 2 × 150Ah, 12V tall tubular (Luminous/Exide) |
| बैटरी बैंक | 24V system (2 बैटरी series में) |
| बैकअप टाइम | Lights + fans + cameras ≈ 6-8 घंटे |
| Solar ready | MPPT charge controller built-in (2-4 panels लगा सकते हैं) |
| Transfer time | <10ms (UPS-grade, कोई झिलमिलाहट नहीं) |
| जगह | 5ft W × 2ft D × 4ft H (DB के पास, हवादार जगह) |
| ब्रांड | Luminous/Microtek/Growatt (solar hybrid) |

**कनेक्शन डायग्राम:**
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

**बैटरी बैकअप पर चलने वाले ज़रूरी circuit:**
- सारी lights (290W)
- सारे fans (450W)
- CCTV system (90W)
- कुल बैकअप भार: ~830W
- बैकअप टाइम: 2 × 150Ah × 12V / 830W ≈ **4.3 घंटे** (पूरा भार पर)
- व्यावहारिक (50% भार): **6-8 घंटे**

**कुल inverter/battery भार: 3000W अधिकतम क्षमता**

---

### अपडेटेड लोड सारांश

| Circuit | भार | नोट |
|---------|------|------|
| Lighting (tubes + bulbs) | 290W | L1-L8, SEC1-SEC2 |
| छत के पंखे (6 नग) | 450W | F1-F6 (या 210W BLDC से) |
| अंदर कोने के लैंप (4 नग) | 60W | IL1-IL4 |
| बाहर पोल लैंप (4 नग) | 80W | PL1-PL4 |
| CCTV सिस्टम | 90W | 4 cameras + NVR |
| पावर sockets | 3000W | S1-S5 (एक समय एक भारी उपकरण) |
| Pump | 750W | 1 HP submersible |
| Inverter standby | 30W | बिना भार का खर्चा |
| **कुल कनेक्टेड भार** | **~4750W** | — |
| **अधिकतम मांग (diversity)** | **~3500W** | सब एक साथ नहीं चलता |

**सुझाव: Single phase, 5 kW कनेक्शन** (diversity factor के साथ पर्याप्त)

| पॉइंट | जगह | प्रकार | ऊंचाई | उपयोग |
|--------|------|--------|--------|--------|
| S1 | आगे की दीवार (शटर के दायें, अंदर) | 15A + switch | 4 ft | उपकरण, pump switch |
| S2 | बायीं दीवार (बीच) | 15A + switch | 4 ft | टूल्स, चार्जर |
| S3 | दायीं दीवार (बीच) | 15A + switch | 4 ft | सामान्य उपयोग |
| S4 | आगे की दीवार (बाहर, शेड के नीचे) | 15A weatherproof | 3 ft | बाहरी उपकरण |
| S5 | शौचालय (अंदर) | 5A + switch | 5 ft | भविष्य में गीज़र / exhaust fan |

**कुल socket पॉइंट: 5 (4 × 15A + 1 × 5A)**
**अनुमानित socket भार: ~3000W अधिकतम (एक समय एक उपकरण)**

---

### 4. Distribution Board (DB)

**जगह:** Storage के अंदर, आगे-दायीं दीवार, 5ft ऊंचाई पर (ट्रैक्टर रास्ते से दूर, आसानी से पहुंचने लायक)
**नोट:** Inverter का आउटपुट DB main switch के बाद जुड़ता है (बिजली कटने पर सारे circuit चालू रहेंगे)

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

**DB विशेषताएं:**
- बॉक्स: 12-way TPN (Triple Pole Neutral), metal, IP43 rated
- ब्रांड: Havells/Legrand/Schneider
- Main: 63A DP MCB
- ELCB: 63A, 30mA sensitivity (जीवन सुरक्षा)
- MCBs: C-curve सामान्य भार के लिए (10 एक्टिव + 2 स्पेयर स्लॉट)
- Busbar: Copper, 63A रेटेड
- Inverter integration: Grid input → Inverter → DB (सारे circuit को बैकअप मिलेगा)

---

### 5. Earthing सिस्टम

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

**Earth pit बनाने का तरीका:**
1. 2ft × 2ft × 8ft गहरा गड्ढा खोदें
2. 2" dia GI pipe (8ft लंबा, नीचे 3ft में छेद करके) डालें
3. पाइप के चारों तरफ भरें: कोयला (6") + नमक (3") + मिट्टी — बारी-बारी परतें
4. पाइप के ऊपर से 8 SWG GI तार DB earth bar तक जोड़ें
5. CI inspection plate से ढकें
6. समय-समय पर गड्ढे में पानी डालें (खासकर बारिश से पहले) ताकि conductivity बनी रहे
7. सभी sockets, धातु के फिक्सचर, और DB body को earth से जोड़ें

---

### 6. Meter Board (बाहरी)

**जगह:** बाहर, आगे-दायीं दीवार (मीटर रीडर की पहुंच में)
**ऊंचाई:** प्लेटफार्म से 5 ft (ज़मीन से 8 ft)

सामान:
- Energy meter (single phase) — बिजली विभाग लगाएगा
- Main 63A fuse / MCB (मीटर से पहले)
- बिजली के खंभे से service wire entry
- Meter board से DB तक conduit (दीवार से होकर)

**Service कनेक्शन:**
- प्रकार: Single phase, 5 kW कनेक्शन (इस भार के लिए पर्याप्त)
- तार: 2 × 6 sq mm + 1 × 6 sq mm earth (खंभे से service cable)
- भविष्य: अगर पहली मंज़िल पर भारी मशीनरी लगानी हो तो 3-phase में अपग्रेड कर सकते हैं

---

### 7. वायरिंग विशेषताएं

| सामान | विवरण |
|--------|--------|
| वायरिंग प्रकार | Concealed (दीवार में PVC conduit में छुपी हुई) |
| Conduit साइज़ | 20mm (light), 25mm (power) |
| Light circuit तार | 1.5 sq mm FR (flame retardant) copper |
| Power circuit तार | 2.5 sq mm FR copper |
| Pump circuit तार | 4 sq mm FR copper |
| Earth तार | 1.5 sq mm green/yellow FR copper (सभी circuits) |
| Conduit | Heavy gauge PVC, ISI marked |
| Switch/socket ब्रांड | Anchor/Havells/Legrand (modular type) |
| Switch board | हर पॉइंट पर 6-module boards |

**वायरिंग का रास्ता (दीवार में concealed):**
- सारी वायरिंग PVC conduits में, प्लास्टर करते समय दीवार में फिट
- Horizontal (आड़ी) लाइन: छत से 1ft नीचे या फर्श से 1ft ऊपर
- Vertical (खड़ी) लाइन: switch से सीधी ऊपर/नीचे horizontal लाइन तक
- कोई तिरछी वायरिंग नहीं (बाद में ढूंढना नामुमकिन हो जाता है)
- हर मोड़/शाखा पर junction box (खोलने लायक)

---

### 8. Security Lighting विवरण

| सामान | विवरण |
|--------|--------|
| SEC1 (गेट) | 20W LED floodlight, warm white, PIR motion sensor के साथ |
| SEC2 (शटर) | 30W LED floodlight, daylight white, manual + motion sensor |
| Sensor रेंज | 8-10 meters, 120° detection angle |
| Override | Manual switch (SW6) — ज़रूरत पर लगातार ON रख सकते हैं |
| Timer | ऐच्छिक dusk-to-dawn photocell (रात को अपने आप ON) |
| ऊंचाई | प्लेटफार्म से 10 ft (ज़मीन से 13 ft) |
| IP rating | IP65 (बारिश/धूल से सुरक्षित) |

---

## भाग B: प्लंबिंग (PLUMBING)

---

### 9. पानी की सप्लाई सिस्टम

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

**पाइप साइज़:**
| पाइप | साइज़ | मटीरियल | उपयोग |
|------|-------|---------|--------|
| Rising main (pump → tanki) | 1" (25mm) | GI (galvanized iron) | Pump का प्रेशर सहता है |
| Main distribution | 3/4" (20mm) | CPVC | टंकी से नीचे |
| Branch lines | 1/2" (15mm) | CPVC | हर फिक्सचर तक |
| Overflow | 1" (25mm) | PVC | टंकी overflow |
| Vent pipe | 1" (25mm) | PVC | टंकी हवा निकास |

**वाल्व:**
| वाल्व | जगह | उपयोग |
|--------|------|--------|
| Gate valve (1") | टंकी इनलेट पर | रखरखाव के लिए टंकी बंद करना |
| Gate valve (3/4") | टंकी के नीचे, main पर | पूरी सप्लाई बंद करना |
| Angle valve (1/2") | हर फिक्सचर पर | शौचालय/नल अलग-अलग बंद करना |
| NRV (non-return) | Pump के बाद | पानी वापस न जाए |
| Float valve | टंकी के अंदर | टंकी भरने पर अपने आप बंद |

---

### 10. शौचालय प्लंबिंग (विस्तार से)

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

**मुख्य विशेषताएं:**
| हिस्सा | विवरण |
|---------|--------|
| Soil pipe (WC से) | 4" PVC SWR (Soil, Waste, Rain) |
| Waste pipe (basin से) | 2" PVC SWR |
| Vent pipe | 2" PVC, छत से 1ft ऊपर जाएगा (drain में हवा अटकने से रोकता है) |
| P-trap (basin) | 2" PVC, 75mm water seal |
| S-trap (WC) | Commode में बना हुआ (floor-mounted) |
| Floor trap (नहानी) | 4" CI, SS जाली के साथ |
| ज़मीन के नीचे का pipe | 4" PVC, रेत पर बिछा हुआ, 1:40 ढलान |
| Pipe जोड़ | Solvent cement (PVC) / threaded (CPVC) |

---

### 11. निकासी प्रणाली (Drainage)

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

### 12. बाहरी नल (External Water Tap)

**जगह:** दायीं दीवार, आगे की तरफ (शटर एरिया से पहुंचने लायक)
**ऊंचाई:** प्लेटफार्म से 2 ft (ज़मीन से 5 ft)

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

**विशेषताएं:**
- नल: 15mm (1/2") heavy duty brass bib cock
- Stop valve: 15mm angle valve (नल बंद करने के लिए बिना शौचालय पर असर के)
- प्लेटफार्म: 2ft × 2ft कंक्रीट धुलाई क्षेत्र, ढलान के साथ
- निकासी: छोटा PVC pipe पानी को plinth से दूर ले जाता है
- उपयोग: उपकरण साफ करना, धुलाई, सामान्य खेती का काम

---

## भाग C: भविष्य के प्रावधान

---

### 13. पहली मंज़िल के लिए बिजली Conduits

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

**प्रावधान की जगहें (3 conduits):**

| # | कहां से | कहां तक | रास्ता | उपयोग |
|---|---------|---------|--------|--------|
| 1 | DB (MCB 6 - spare) | आगे-बायीं तरफ slab opening | सीढ़ी की दीवार/कॉलम से ऊपर | 1F के लिए मुख्य power feed (4 sq mm तार भविष्य में) |
| 2 | DB के पास | पीछे-दायीं तरफ slab opening | दायीं दीवार से ऊपर | 1F का दूसरा circuit (lighting/AC) |
| 3 | Gate/switch एरिया | सीढ़ी के पास slab opening | सीढ़ी की partition दीवार के साथ | ग्राउंड से 1F तक सीढ़ी lighting |

**विशेषताएं:**
- Conduit: 25mm heavy gauge PVC
- Draw wire: 16 SWG GI wire (conduit में डाला हुआ, भविष्य में केबल खींचने के लिए)
- Slab sleeve: 2" PVC pipe हर conduit exit पर slab में डाला हुआ
- Cap: Tape/plug से बंद (construction के दौरान कंक्रीट अंदर न जाए)
- Label: Slab के ऊपर और नीचे permanent marker से जगह चिह्नित करें

---

### 14. पहली मंज़िल के लिए प्लंबिंग Sleeves

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

**Sleeve अनुसूची:**

| Sleeve | साइज़ | जगह | उपयोग |
|--------|-------|------|--------|
| S1 | 4" PVC | मौजूदा शौचालय के ऊपर (आगे-बायां) | भविष्य 1F बाथरूम soil pipe |
| S2 | 2" PVC | S1 के बगल में | भविष्य 1F बाथरूम supply pipe |
| S3 | 4" PVC | पीछे-दायां हिस्सा | भविष्य 1F किचन waste pipe |

**लगाने के निर्देश:**
- Slab डालते समय sleeves लगाएं (slab formwork में PVC pipes खड़ी रखें)
- डालते समय sleeves के अंदर अखबार/foam भरें (कंक्रीट अंदर न जाए)
- Slab पक्का होने के बाद: packing निकालें, दोनों सिरे PVC caps से बंद करें
- Sleeves भविष्य के pipe से 2" बड़ी होनी चाहिए (S1: 4" pipe के लिए 6" PVC sleeve)

---

### 15. Solar Panel वायरिंग Conduit

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

**विशेषताएं:**
- Conduit: 32mm PVC (DC केबल मोटी होती है इसलिए बड़ी)
- रास्ता: छत parapet (दायीं तरफ) → दायीं दीवार से नीचे → ग्राउंड फ्लोर DB के पास
- छत पर junction box: weatherproof IP65, solar panel MC4 cables जोड़ने के लिए
- नीचे junction box: DB के पास, inverter/charge controller कनेक्शन के लिए
- Draw wire: 14 SWG GI wire conduit के अंदर
- भविष्य केबल: 2 × 6 sq mm DC solar cable (positive + negative)
- DB के पास जगह: 2ft × 2ft दीवार की जगह भविष्य inverter/battery के लिए रिज़र्व

---

## भाग D: ठेकेदार नोट्स (बिजली + प्लंबिंग)

---

### 16. कब क्या करना है (क्रम)

| निर्माण का चरण | बिजली का काम | प्लंबिंग का काम |
|----------------|--------------|-----------------|
| **नींव (Foundation)** | Earth pit की खुदाई | ज़मीन के नीचे drain pipe (शौचालय → soak pit) |
| **Plinth की दीवारें** | — | Floor drain channel बनाना |
| **फर्श का slab** | फर्श के नीचे conduit (अगर कोई हो) | Floor trap लगाना |
| **दीवारें उठना** | दीवारों में conduit लगाना (प्लास्टर से पहले!) | दीवारों में supply pipes लगाना |
| **सीढ़ी** | सीढ़ी light conduit | — |
| **Slab डालने से पहले** | भविष्य conduit sleeves slab से | भविष्य plumbing sleeves slab से |
| **Slab डालना** | Solar conduit sleeve | Pipe sleeves slab में डालना |
| **Slab पक्का होने के बाद** | तार खींचना, DB लगाना, switches, lights | टंकी लगाना, pump जोड़ना, flush टेस्ट |
| **प्लास्टर** | Conduits ढकना (पहले से लगी हुई) | Pipes ढकना (पहले से लगी हुई) |
| **फिनिशिंग** | फिक्सचर लगाना (lights, fans, sockets) | फिक्सचर लगाना (commode, basin, नल) |

### 17. ज़रूरी चेतावनियां

**⚠️ बिजली:**
- सारे conduits प्लास्टर से पहले लगा दें — प्लास्टर के बाद दीवार तोड़ना पड़ेगा
- Conduit सीधी रखें (सिर्फ आड़ी/खड़ी) — कोई तिरछी लाइन नहीं
- हर मोड़ पर junction box लगाएं — conduit को तेज़ कोण पर न मोड़ें
- Conduit लगाते समय ही draw wire अंदर डालें — बाद में खींचना बहुत मुश्किल
- हर switch/socket पॉइंट पर 12" extra तार छोड़ें (कनेक्शन के लिए)
- मेन से जोड़ने से पहले megger से सारे circuit टेस्ट करें
- सभी धातु फिक्सचर (lights, fans, socket bodies) को earth से जोड़ें

**⚠️ प्लंबिंग:**
- ज़मीन के नीचे के drain pipes फर्श slab डालने से पहले बिछाने ज़रूरी हैं
- सभी drain pipes में 1:40 ढलान बनाए रखें (spirit level + straight edge से चेक करें)
- CPVC pipes गर्मी में फैलती हैं — जोड़ों पर 1" गैप छोड़ें (thermal expansion के लिए)
- दीवार में छुपाने से पहले supply pipes की लीक टेस्ट करें (24 घंटे pressure test)
- शौचालय की vent pipe छत के ऊपर जानी चाहिए (नहीं तो हवा अटकेगी = धीमी निकासी)
- टंकी का प्लेटफार्म 500 kg सहने लायक मज़बूत होना चाहिए (भरी टंकी का वज़न)

---

### 18. सामान की सूची (बिजली + प्लंबिंग)

**बिजली:**
| सामान | मात्रा | विवरण |
|--------|--------|--------|
| PVC conduit 20mm | 200 rft | Heavy gauge, ISI marked |
| PVC conduit 25mm | 120 rft | Power + fan + CCTV circuits के लिए |
| PVC conduit 32mm | 40 rft | Solar conduit के लिए |
| तार 1.5 sq mm | 300 m | FR copper, light + fan circuits |
| तार 2.5 sq mm | 200 m | FR copper, power + fan circuits |
| तार 4 sq mm | 50 m | FR copper, pump + inverter |
| Earth तार 1.5 sq mm | 150 m | Green-yellow FR copper |
| DB box 12-way TPN | 1 | Metal, IP43 |
| MCBs (6A, 10A, 16A) | 10 | C-curve |
| ELCB 63A/30mA | 1 | जीवन सुरक्षा |
| Main switch 63A DP | 1 | — |
| छत के पंखे 48" | 6 | 75W (या BLDC 35W), drop rods के साथ |
| Fan drop rods 2ft | 6 | MS chromed |
| Fan regulators (electronic) | 2 | 5-speed step type |
| LED tubes 4ft 36W | 6 | फिटिंग सहित |
| LED bulbs 9W | 2 | Holder + bulb |
| LED wall bracket lights 15W | 4 | अंदर कोने के लैंप |
| LED pole lights 20W (IP65) | 4 | बाहरी, photocell के साथ |
| MS poles 2" × 10ft | 4 | Galvanized, बाहरी लैंप के लिए |
| Pole base concrete | 4 | 1.5ft × 1.5ft × 2ft प्रत्येक |
| LED floodlight 20W | 1 | IP65, PIR sensor के साथ |
| LED floodlight 30W | 1 | IP65, PIR sensor के साथ |
| IP bullet camera 3MP | 4 | IP67, IR 30m night vision |
| NVR 4-channel | 1 | 1TB HDD, H.265, WiFi |
| PoE switch 4+1 port | 1 | 10/100 Mbps, 60W budget |
| CAT6 LAN cable | 100 m | Outdoor-rated, camera runs के लिए |
| Solar hybrid inverter 3kVA | 1 | MPPT, pure sine wave |
| Tall tubular battery 150Ah | 2 | 12V, Luminous/Exide |
| Battery rack/trolley | 1 | MS, 2-battery capacity |
| Modular switches | 12 | 6A, piano type |
| Modular sockets 15A | 4 | Switch के साथ |
| Modular socket 5A | 1 | Switch के साथ |
| Switch boards (6-module) | 10 | Surface/flush mount |
| Junction boxes | 15 | PVC, round |
| GI earth pipe 2" × 8ft | 2 | Earth pits के लिए |
| GI wire 8 SWG | 30 m | Earth continuity |
| Draw wire 16 SWG | 100 m | भविष्य में तार खींचने के लिए |

**प्लंबिंग:**
| सामान | मात्रा | विवरण |
|--------|--------|--------|
| CPVC pipe 3/4" | 20 rft | टंकी से main supply |
| CPVC pipe 1/2" | 60 rft | Branch supply lines |
| CPVC fittings (elbows, tees) | 1 set | ज़रूरत अनुसार |
| PVC SWR pipe 4" | 50 rft | Soil pipe + underground |
| PVC SWR pipe 3" | 60 rft | Downpipes (4 नग × 15ft) |
| PVC SWR pipe 2" | 20 rft | Waste pipe + vent |
| PVC fittings (bends, Y, tees) | 1 set | SWR type |
| GI pipe 1" | 30 rft | Rising main (pump से tanki) |
| Gate valves 1" | 2 | टंकी inlet + main पर |
| Angle valves 1/2" | 4 | हर fixture पर |
| Float valve 1" | 1 | टंकी के अंदर |
| NRV (non-return valve) 1" | 1 | Pump के बाद |
| Bib cock (brass) 15mm | 2 | बाहरी नल + शौचालय नल |
| Floor trap 4" | 2 | नहानी (SS जाली) |
| P-trap 2" | 1 | Basin |
| Western commode (S-trap) | 1 | सीट सहित, Hindware/Cera |
| Concealed flush tank | 1 | 8/10L dual flush |
| Wash basin (wall mount) | 1 | 12"×18" pedestal/bracket सहित |
| PVC solvent cement | 2 टिन | PVC जोड़ों के लिए |
| CPVC solvent cement | 1 टिन | CPVC जोड़ों के लिए |
| Teflon tape | 5 रोल | Threaded जोड़ों के लिए |
| 500L HDPE tank | 1 | Sintex/Supreme |
| MS angle stand (tank) | 1 set | 2ft ऊंचाई, छत पर |
| Submersible pump 1 HP | 1 | (मौजूदा इस्तेमाल हो सकता है) |
| Water level controller | 1 | Electronic, auto ON/OFF |
