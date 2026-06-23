#!/usr/bin/env python3
"""
Generate a professional PLUMBING BLUEPRINT PDF for the G+1 farmhouse.
8 pages covering all 4 drainage systems, site layout, pipe routes, and specs.
Both English and Hindi (bilingual for contractor use).
"""

from fpdf import FPDF
import os

HINDI_FONT_PATH = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'

MM = 1
A4_W, A4_H = 210, 297
A3_W, A3_H = 420, 297


class PlumbingPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=False)
        self.add_font('Hindi', '', HINDI_FONT_PATH)
        self.add_font('HindiB', '', HINDI_FONT_PATH)

    def add_a4_page(self):
        self.add_page(orientation='P', format='A4')

    def add_a3_page(self):
        self.add_page(orientation='L', format='A3')

    def title_block(self, title, subtitle=''):
        self.set_font('HindiB', '', 10)
        self.set_xy(10, 8)
        self.cell(0, 5, title, align='L')
        if subtitle:
            self.set_font('Hindi', '', 7)
            self.set_xy(10, 13)
            self.cell(0, 4, subtitle, align='L')
        self.set_draw_color(0)
        self.set_line_width(0.5)
        self.line(10, 18, self.w - 10, 18)

    def border_frame(self):
        self.set_draw_color(0)
        self.set_line_width(0.4)
        self.rect(5, 5, self.w - 10, self.h - 10)

    def section_header(self, y, text):
        self.set_font('HindiB', '', 9)
        self.set_xy(12, y)
        self.cell(0, 5, text)
        return y + 6


def build_pdf():
    pdf = PlumbingPDF()

    # ========== PAGE 1: TITLE & OVERVIEW (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()

    pdf.set_font('HindiB', '', 16)
    pdf.set_xy(0, 40)
    pdf.cell(210, 10, 'PLUMBING & DRAINAGE BLUEPRINT', align='C')
    pdf.set_font('Hindi', '', 11)
    pdf.set_xy(0, 52)
    pdf.cell(210, 6, 'G+1 Farm Storage + Residence, Moradabad, UP', align='C')
    pdf.set_xy(0, 60)
    pdf.cell(210, 6, 'G+1 फार्म स्टोरेज + आवास - जल निकासी एवं नलसाजी', align='C')

    pdf.set_font('Hindi', '', 8)
    info = [
        ('Building / भवन', '20ft x 25ft internal, G+1 (Storage + Residence)'),
        ('Systems / प्रणाली', '4 SEPARATE drainage systems (Black + Grey + Wash + Rain)'),
        ('Borewell / बोरवेल', '30ft right of building, toward front (drinking water)'),
        ('Road / चकरोड', '10-12ft in front of building (kachchi road)'),
        ('Septic Tank / सेप्टिक', '5ft x 2.5ft x 4.5ft, 2-chamber RCC, behind building (left)'),
        ('BW Soak Pit', '5ft dia x 7ft deep, back-left (x=-5, y=40)'),
        ('GW Soak Pit', '4ft dia x 6ft deep, back-center (x=5, y=40)'),
        ('WW Soak Pit', '5ft dia x 6.5ft deep, back-right (x=15, y=38)'),
        ('Min. spacing / दूरी', '10ft between all pits (IS 2470)'),
        ('Borewell safety', 'All pits 50ft+ from borewell'),
        ('', ''),
        ('Pipe material', 'PVC SWR (IS 14735) - Ashirvad / Supreme / Finolex'),
        ('Joints / जोड़', 'Solvent cement (underground). No rubber rings for buried pipes.'),
        ('Concrete', 'M20 for septic tank (1:1.5:3)'),
        ('Slope / ढलान', 'Black water: 1:40. Grey/Wash water: 1:60'),
        ('Bends / मोड़', 'ONLY 45 degree Y-junctions. NO 90 degree bends for sewage.'),
        ('', ''),
        ('Codes / कोड', 'IS 2470 (Septic), IS 1742 (Drainage), NBC 2016 Part 9'),
        ('Date / दिनांक', 'June 2026'),
        ('Drawing No.', 'PLB-001'),
    ]

    y = 78
    for label, value in info:
        if label == '':
            y += 3
            continue
        pdf.set_font('HindiB', '', 7)
        pdf.set_xy(20, y)
        pdf.cell(50, 4.5, label)
        pdf.set_font('Hindi', '', 7)
        pdf.cell(130, 4.5, value)
        y += 4.5

    # Color legend
    y += 8
    pdf.set_font('HindiB', '', 8)
    pdf.set_xy(20, y)
    pdf.cell(0, 5, 'COLOR CODE / रंग कोड:')
    y += 6
    colors = [
        ((140, 30, 30), 'BLACK WATER (काला पानी - शौचालय) - Dark Maroon'),
        ((100, 110, 120), 'GREY WATER (धूसर पानी - रसोई/नहान) - Grey'),
        ((180, 140, 40), 'WASH WATER (धुलाई पानी - फर्श/ट्रैक्टर) - Ochre/Sandy'),
        ((40, 100, 180), 'RAINWATER (बारिश का पानी - छत) - Blue'),
    ]
    for (r, g, b), label in colors:
        pdf.set_fill_color(r, g, b)
        pdf.rect(22, y, 12, 3, 'F')
        pdf.set_font('Hindi', '', 6.5)
        pdf.set_xy(36, y - 0.5)
        pdf.cell(0, 4, label)
        y += 5

    # ========== PAGE 2: SITE PLAN - ALL SYSTEMS (A3 Landscape) ==========
    pdf.add_a3_page()
    pdf.border_frame()
    pdf.title_block('SHEET 2: SITE PLAN - ALL DRAINAGE SYSTEMS',
                    'Plan View. Building = center. All underground structures shown. Borewell safety radius = 50ft.')

    ox, oy = 160, 220  # building front-left corner on page
    scale = 5  # 1ft = 5mm (need to show wide area: -25 to +55 in x, -15 to +45 in y)

    def px(ft_x): return ox + ft_x * scale
    def py(ft_y): return oy - ft_y * scale  # y goes up on page

    # Ground
    pdf.set_fill_color(235, 240, 230)
    pdf.rect(px(-25), py(45), 80 * scale, 60 * scale, 'F')

    # Road (chakrode)
    pdf.set_fill_color(200, 185, 160)
    pdf.rect(px(-25), py(-2), 80 * scale, 10 * scale, 'F')
    pdf.set_font('Hindi', '', 5)
    pdf.set_xy(px(5), py(-6))
    pdf.cell(30, 3, 'CHAKRODE / चकरोड (kachchi road)')

    # Building outline
    pdf.set_draw_color(0)
    pdf.set_line_width(0.5)
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(px(-0.75), py(25.75), 21.5 * scale, 26.5 * scale, 'DF')
    pdf.set_font('HindiB', '', 6)
    pdf.set_xy(px(4), py(13))
    pdf.cell(30, 4, 'BUILDING 20x25ft')

    # Borewell
    pdf.set_fill_color(40, 100, 180)
    pdf.circle(px(51), py(2), 2, 'F')
    pdf.set_font('Hindi', '', 5)
    pdf.set_xy(px(49), py(2) + 3)
    pdf.cell(20, 3, 'BOREWELL / बोरवेल')
    # 50ft radius (partial arc shown as dashed circle)
    pdf.set_draw_color(40, 100, 180)
    pdf.set_line_width(0.2)
    pdf.set_dash_pattern(2, 1)
    pdf.circle(px(51), py(2), 50 * scale, 'D')
    pdf.set_dash_pattern()
    pdf.set_font('Hindi', '', 4)
    pdf.set_xy(px(51) - 15, py(2) - 50 * scale - 4)
    pdf.cell(30, 3, '50ft safety radius')

    # GF Toilet marker
    pdf.set_fill_color(140, 30, 30)
    pdf.rect(px(0.5), py(2.5), 1.5 * scale, 2 * scale, 'F')
    pdf.set_font('Hindi', '', 4)
    pdf.set_xy(px(0.2), py(3.5))
    pdf.cell(10, 3, 'GF WC')

    # 1F Toilet marker
    pdf.rect(px(17), py(8.5), 1.5 * scale, 2 * scale, 'F')
    pdf.set_xy(px(17), py(9.5))
    pdf.cell(10, 3, '1F WC')

    # Floor drain
    pdf.set_fill_color(180, 140, 40)
    pdf.set_line_width(0.3)
    pdf.line(px(10), py(0), px(10), py(25))

    # === SYSTEM 1: BLACK WATER PIPES (maroon) ===
    pdf.set_draw_color(140, 30, 30)
    pdf.set_line_width(0.8)
    # GF toilet to back
    pdf.line(px(1), py(1.5), px(1), py(27))
    # 1F toilet to back
    pdf.line(px(18), py(7), px(18), py(27))
    # Both merge behind building
    pdf.line(px(1), py(27), px(-3), py(28))
    pdf.line(px(18), py(27), px(-3), py(28))
    # Y-junction to septic
    pdf.line(px(-3), py(28), px(-5), py(28))

    # Septic tank
    pdf.set_fill_color(100, 50, 25)
    pdf.rect(px(-7.5), py(30.5), 5 * scale, 2.5 * scale, 'DF')
    pdf.set_font('Hindi', '', 4.5)
    pdf.set_xy(px(-7.5), py(29.5))
    pdf.cell(20, 3, 'SEPTIC 5x2.5x4.5ft')

    # Septic to BW soak pit
    pdf.set_draw_color(140, 30, 30)
    pdf.line(px(-5), py(30.5), px(-5), py(37.5))

    # BW Soak pit
    pdf.set_fill_color(90, 30, 20)
    pdf.circle(px(-5), py(40), 2.5 * scale, 'DF')
    pdf.set_font('Hindi', '', 4.5)
    pdf.set_xy(px(-8), py(40) - 2.5 * scale - 4)
    pdf.cell(20, 3, 'BW PIT 5ft x 7ft')

    # === SYSTEM 2: GREY WATER (grey) ===
    pdf.set_draw_color(100, 110, 120)
    pdf.set_line_width(0.6)
    # Downpipe at back wall
    pdf.line(px(18), py(25.75), px(18), py(27))
    # Run behind building to grease trap
    pdf.line(px(18), py(27), px(15), py(28))

    # Grease trap
    pdf.set_fill_color(140, 130, 70)
    pdf.rect(px(14.5), py(29), 2 * scale, 1.5 * scale, 'DF')
    pdf.set_font('Hindi', '', 4)
    pdf.set_xy(px(14), py(28))
    pdf.cell(15, 3, 'GREASE TRAP')

    # To GW inspection chamber
    pdf.set_draw_color(100, 110, 120)
    pdf.line(px(15), py(29), px(12), py(33))
    # IC
    pdf.set_fill_color(130, 130, 130)
    pdf.rect(px(11.5), py(33.75), 1 * scale, 1 * scale, 'F')

    # To GW soak pit
    pdf.line(px(12), py(33), px(5), py(38.5))
    # GW pit
    pdf.set_fill_color(100, 110, 120)
    pdf.circle(px(5), py(40), 2 * scale, 'DF')
    pdf.set_font('Hindi', '', 4.5)
    pdf.set_xy(px(2), py(40) - 2 * scale - 4)
    pdf.cell(20, 3, 'GW PIT 4ft x 6ft')

    # === SYSTEM 3: WASH WATER (ochre) ===
    pdf.set_draw_color(180, 140, 40)
    pdf.set_line_width(0.6)
    # Floor drain exits back
    pdf.line(px(10), py(25.75), px(10), py(27))
    # To silt trap
    pdf.line(px(10), py(27), px(9), py(28))
    # Silt trap
    pdf.set_fill_color(140, 110, 70)
    pdf.rect(px(8.5), py(29.25), 1.5 * scale, 1.5 * scale, 'DF')
    pdf.set_font('Hindi', '', 4)
    pdf.set_xy(px(8), py(28))
    pdf.cell(15, 3, 'SILT TRAP')
    # To oil trap
    pdf.set_draw_color(180, 140, 40)
    pdf.line(px(9), py(29.25), px(8), py(33))
    # Oil trap
    pdf.set_fill_color(160, 130, 60)
    pdf.rect(px(7.5), py(34), 1.5 * scale, 1.2 * scale, 'DF')
    pdf.set_font('Hindi', '', 4)
    pdf.set_xy(px(7), py(33))
    pdf.cell(15, 3, 'OIL TRAP')
    # To WW pit
    pdf.line(px(8), py(34), px(15), py(36))
    # WW pit
    pdf.set_fill_color(180, 140, 40)
    pdf.circle(px(15), py(38), 2.5 * scale, 'DF')
    pdf.set_font('Hindi', '', 4.5)
    pdf.set_xy(px(12), py(38) - 2.5 * scale - 4)
    pdf.cell(20, 3, 'WW PIT 5ft x 6.5ft')

    # === SYSTEM 4: RAINWATER (blue) ===
    pdf.set_draw_color(40, 100, 180)
    pdf.set_line_width(0.4)
    # 4 downpipes at corners going outward
    corners = [(-0.5, -0.5), (20.5, -0.5), (-0.5, 25.5), (20.5, 25.5)]
    for cx, cy in corners:
        pdf.circle(px(cx), py(cy), 1, 'D')

    # Legend on right
    pdf.set_font('HindiB', '', 6)
    pdf.set_xy(320, 30)
    pdf.cell(60, 4, 'SPACING / दूरी:')
    pdf.set_font('Hindi', '', 5.5)
    spacings = [
        'Septic to BW Pit: 12ft',
        'BW Pit to GW Pit: 10ft',
        'GW Pit to WW Pit: 10.2ft',
        'All pits to borewell: 50ft+',
        'Pits to building: 5ft+',
        'Left side: CLEAR (tractors)',
    ]
    ny = 36
    for s in spacings:
        pdf.set_xy(320, ny)
        pdf.cell(60, 3.5, s)
        ny += 4

    # ========== PAGE 3: UNDERGROUND PIPE LAYOUT (A3 Landscape) ==========
    pdf.add_a3_page()
    pdf.border_frame()
    pdf.title_block('SHEET 3: UNDERGROUND PIPE LAYOUT (Before Floor Slab Pour)',
                    'ALL pipes must be laid BEFORE GF floor slab is poured. Show pipe sizes, slopes, and exit points.')

    ox, oy = 80, 50
    scale = 8

    def px(ft_x): return ox + ft_x * scale
    def py(ft_y): return oy + (25 - ft_y) * scale

    # Building outline
    pdf.set_draw_color(0)
    pdf.set_line_width(0.4)
    pdf.rect(px(0), py(25), 20 * scale, 25 * scale)
    pdf.set_font('Hindi', '', 5)
    pdf.set_xy(px(7), py(13))
    pdf.cell(30, 3, 'BUILDING FLOOR (20x25ft)')

    # Pipe routes INSIDE building (before slab pour)
    # BW: GF toilet (x=1,y=1.5) straight to back wall
    pdf.set_draw_color(140, 30, 30)
    pdf.set_line_width(1.0)
    pdf.line(px(1), py(1.5), px(1), py(25))
    pdf.set_font('Hindi', '', 4.5)
    pdf.set_xy(px(1.5), py(12))
    pdf.cell(20, 3, '4" PVC (1:40 slope)')

    # BW: 1F toilet (x=18,y=7) straight to back
    pdf.line(px(18), py(7), px(18), py(25))
    pdf.set_xy(px(18.5), py(15))
    pdf.cell(20, 3, '4" PVC (capped)')

    # WW: Floor drain channel (x=10, full depth)
    pdf.set_draw_color(180, 140, 40)
    pdf.set_line_width(0.6)
    pdf.line(px(10), py(0), px(10), py(25))
    pdf.set_xy(px(10.5), py(12))
    pdf.cell(20, 3, '4" floor drain (1:100)')

    # GW: stub at x=18, near back wall (capped for future)
    pdf.set_draw_color(100, 110, 120)
    pdf.set_line_width(0.6)
    pdf.set_dash_pattern(2, 1)
    pdf.line(px(18), py(22), px(18), py(25))
    pdf.set_dash_pattern()
    pdf.set_xy(px(18.5), py(23))
    pdf.cell(20, 3, '3" GW (capped - future)')

    # Exit points through back wall (marked with arrows)
    pdf.set_draw_color(0)
    pdf.set_line_width(0.3)
    exits = [
        (1, 'BW exit (4" active)'),
        (10, 'WW exit (4" active)'),
        (18, 'GW exit (3" capped)'),
    ]
    for ex_x, label in exits:
        pdf.set_fill_color(255, 0, 0)
        pdf.circle(px(ex_x), py(25), 1.5, 'D')
        pdf.set_font('Hindi', '', 4)
        pdf.set_xy(px(ex_x) - 5, py(25) - 5)
        pdf.cell(20, 3, label)

    # Notes
    pdf.set_font('HindiB', '', 7)
    pdf.set_xy(310, 40)
    pdf.cell(80, 4, 'CRITICAL NOTES / ज़रूरी बातें:')
    pdf.set_font('Hindi', '', 6)
    notes = [
        '1. ALL 3 pipe routes MUST be laid BEFORE floor slab.',
        '   तीनों पाइप मार्ग फर्श की ढलाई से पहले बिछाएँ!',
        '2. Pipe 1 (BW): Active immediately (toilet connected).',
        '3. Pipe 2 (GW): CAPPED both ends (open when 1F built).',
        '4. Pipe 3 (WW): Active (floor drain channel connected).',
        '5. 150mm sand bedding below and sides of all pipes.',
        '   पाइप के नीचे और बगल में 6 इंच रेत बिछाएँ।',
        '6. Backfill with selected earth (no stones/bricks).',
        '   चुनी हुई मिट्टी से भराई (पत्थर/ईंट नहीं)।',
        '7. Minimum 1ft cover above pipes before slab.',
        '8. Check slope with spirit level before backfill.',
        '   भराई से पहले ढलान स्पिरिट लेवल से जाँचें।',
    ]
    ny = 46
    for n in notes:
        pdf.set_xy(310, ny)
        pdf.cell(90, 3.5, n)
        ny += 4

    # ========== PAGE 4: SEPTIC TANK DETAIL (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()
    pdf.title_block('SHEET 4: SEPTIC TANK DETAIL / सेप्टिक टैंक विवरण',
                    '2-Chamber RCC tank. Position: behind building, left side (x=-5, y=28).')

    y = 22
    y = pdf.section_header(y, 'A. SEPTIC TANK SPECIFICATIONS / विशेषताएँ')

    pdf.set_font('HindiB', '', 7)
    widths = [45, 55, 80]
    headers = ['Parameter / मद', 'Value / मान', 'Notes / टिप्पणी']
    pdf.set_xy(12, y)
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 5, h, border=1)
    y += 5

    rows = [
        ('Size / आकार', '5ft x 2.5ft x 4.5ft deep', 'External dimensions / बाहरी माप'),
        ('Internal', '4ft x 1.5ft x 4ft deep', 'After 6" walls / 6 इंच दीवार के बाद'),
        ('Capacity / क्षमता', '~1500 litres', 'For 3-5 users toilet only'),
        ('Type / प्रकार', '2-chamber RCC', 'Settling + Clarifying'),
        ('Wall thickness', '6" RCC (M20)', '150mm, waterproof inside'),
        ('Base slab', '6" RCC (M20)', 'With 150mm PCC below'),
        ('Top slab / ढक्कन', '6" RCC with 2 manholes', '18"x18" openings for cleaning'),
        ('Chamber 1 (settling)', '3.3ft long', '2/3 of tank length'),
        ('Chamber 2 (clarifying)', '1.2ft long', '1/3 of tank length'),
        ('Baffle wall / बैफल', '4" RCC, openings at 2/3 depth', 'Prevents short-circuiting'),
        ('Inlet pipe', '4" (110mm) PVC, 6" below top', 'With T-piece for scum retention'),
        ('Outlet pipe', '4" (110mm) PVC, 9" below top', 'With T-piece, to soak pit'),
        ('Waterproofing', '2 coats bitumen emulsion inside', 'Before backfilling'),
        ('Cleaning / सफाई', 'Every 2-3 years (tanker pump)', 'सेप्टिक टैंकर से खाली करें'),
        ('Position / स्थान', 'x=-5, y=28 (behind bldg, left)', 'Top flush with ground / ज़मीन बराबर'),
    ]
    pdf.set_font('Hindi', '', 6)
    for row in rows:
        pdf.set_xy(12, y)
        for i, val in enumerate(row):
            pdf.cell(widths[i], 4.5, val, border=1)
        y += 4.5

    y += 8
    y = pdf.section_header(y, 'B. SOAK PIT SPECIFICATIONS / सोक पिट')

    pdf.set_font('HindiB', '', 6.5)
    pw = [35, 35, 35, 55]
    pdf.set_xy(12, y)
    for i, h in enumerate(['Parameter', 'BW Pit (काला)', 'GW Pit (धूसर)', 'WW Pit (धुलाई)']):
        pdf.cell(pw[i], 5, h, border=1)
    y += 5

    pit_rows = [
        ('Diameter / व्यास', '5ft (1.5m)', '4ft (1.2m)', '5ft (1.5m)'),
        ('Depth / गहराई', '7ft (2.1m)', '6ft (1.8m)', '6.5ft (2.0m)'),
        ('Position (x, y)', 'x=-5, y=40', 'x=5, y=40', 'x=15, y=38'),
        ('Wall / दीवार', 'Honeycomb brick', 'Honeycomb brick', 'Honeycomb brick'),
        ('Gravel bed', '2ft bottom', '1.5ft bottom', '1.5ft bottom'),
        ('Cover / ढक्कन', '8" RCC (tractor rated)', '6" RCC', '6" RCC'),
        ('Dist. from borewell', '68ft', '60ft', '51ft'),
    ]
    pdf.set_font('Hindi', '', 6)
    for row in pit_rows:
        pdf.set_xy(12, y)
        for i, val in enumerate(row):
            pdf.cell(pw[i], 4.5, val, border=1)
        y += 4.5

    # ========== PAGE 5: PIPE SCHEDULE (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()
    pdf.title_block('SHEET 5: PIPE SCHEDULE & SPECIFICATIONS / पाइप सूची')

    y = 22
    y = pdf.section_header(y, 'A. PIPE SCHEDULE / पाइप विवरण')

    pdf.set_font('HindiB', '', 6.5)
    pp = [40, 22, 22, 20, 22, 50]
    pdf.set_xy(12, y)
    for i, h in enumerate(['Pipe Run / मार्ग', 'Size', 'Material', 'Slope', 'Bends', 'Notes / टिप्पणी']):
        pdf.cell(pp[i], 5, h, border=1)
    y += 5

    pipe_rows = [
        ('GF toilet to back wall', '4" (110mm)', 'PVC SWR', '1:40', 'None', 'Active now / अभी चालू'),
        ('1F toilet to back wall', '4" (110mm)', 'PVC SWR', '1:40', 'None', 'Active now / अभी चालू'),
        ('Behind bldg (BW merge)', '4" (110mm)', 'PVC SWR', '1:40', '45 deg Y', 'Y-junction, not 90 deg!'),
        ('Y-jn to Septic', '4" (110mm)', 'PVC SWR', '1:40', 'None', 'Short run ~5ft'),
        ('Septic to BW pit', '4" (110mm)', 'PVC SWR', '1:60', 'None', 'Gentle slope / हल्की ढलान'),
        ('GW fixtures to downpipe', '3" (75mm)', 'PVC SWR', '1:40', '45 max', 'Inside 1F floor'),
        ('GW downpipe (vertical)', '3" (75mm)', 'PVC SWR', 'Vertical', 'None', 'Outside back wall'),
        ('GW to grease trap', '3" (75mm)', 'PVC SWR', '1:40', '45 deg', 'Underground'),
        ('Grease trap to GW pit', '3" (75mm)', 'PVC SWR', '1:60', 'None', 'Underground'),
        ('Floor drain channel', '6" wide', 'Cement', '1:100', 'N/A', 'In GF floor slab / फर्श में'),
        ('WW exit to silt trap', '4" (110mm)', 'PVC SWR', '1:60', 'None', 'Exits back wall'),
        ('Silt to oil trap', '4" (110mm)', 'PVC SWR', '1:60', 'None', 'Underground'),
        ('Oil trap to WW pit', '4" (110mm)', 'PVC SWR', '1:60', 'None', 'Underground'),
        ('Vent pipe (toilet)', '2" (50mm)', 'PVC', 'Vertical', 'None', 'GF toilet to above roof'),
        ('Rainwater downpipes', '3" (75mm)', 'PVC', 'Vertical', 'None', '4 nos at corners'),
    ]
    pdf.set_font('Hindi', '', 5.5)
    for row in pipe_rows:
        pdf.set_xy(12, y)
        for i, val in enumerate(row):
            pdf.cell(pp[i], 4, val, border=1)
        y += 4

    y += 8
    y = pdf.section_header(y, 'B. PIPE BRANDS (Moradabad) / उपलब्ध ब्रांड')
    pdf.set_font('Hindi', '', 7)
    brands = [
        'PVC SWR Pipes: Ashirvad (preferred) / Supreme / Finolex / Prince',
        'Solvent Cement: Ashirvad/Supreme brand (matching pipe brand)',
        'CI Covers (manholes): Heavy-duty Class D - local Moradabad foundry',
        'Floor Traps: Jaquar / Hindware / Parryware (CP brass)',
        'Nahani Trap: PVC with SS jali - 6"x6" for bathroom, 4"x4" for kitchen',
    ]
    for b in brands:
        pdf.set_xy(14, y)
        pdf.cell(0, 4, b)
        y += 4.5

    # ========== PAGE 6: CONSTRUCTION SEQUENCE (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()
    pdf.title_block('SHEET 6: CONSTRUCTION SEQUENCE / निर्माण क्रम',
                    'Step-by-step for the mistri/contractor. ठेकेदार/मिस्त्री के लिए कदम-दर-कदम।')

    y = 22
    y = pdf.section_header(y, 'PLUMBING CONSTRUCTION SEQUENCE / नलसाजी कार्य क्रम')

    steps = [
        ('1. नींव खोदने के बाद (After foundation digging):', [
            'a) सेप्टिक टैंक का गड्ढा खोदें (x=-5, y=28) - 6ft x 3.5ft x 5.5ft',
            'b) 3 सोक पिट के गड्ढे खोदें (see Sheet 4 for positions)',
            'c) सेप्टिक टैंक बनाएँ: PCC bed > base slab > walls > baffle > lid',
            'd) सोक पिट बनाएँ: gravel bed > honeycomb brick > RCC cover',
        ]),
        ('2. प्लिंथ भराई से पहले (Before plinth fill):', [
            'a) 3 pipe trenches खोदें (GF floor level से 1.5ft नीचे)',
            'b) 150mm रेत बिछाएँ (sand bedding)',
            'c) Pipe 1 (BW): toilet position (x=1,y=1.5) to back wall exit',
            'd) Pipe 2 (GW): stub at (x=18,y=22) to back wall - CAP BOTH ENDS',
            'e) Pipe 3 (WW): from center (x=10) to back wall exit',
            'f) Slope check with spirit level! ढलान जाँचें!',
            'g) Backfill carefully with selected earth (मिट्टी से भराई)',
        ]),
        ('3. प्लिंथ भराई के बाद / GF फ्लोर से पहले (After plinth, before GF slab):', [
            'a) Floor drain channel shuttering (x=10, 6" wide, full depth)',
            'b) Toilet floor trap position mark (x=1, y=1.5)',
            'c) All pipe stubs should be visible above fill level',
        ]),
        ('4. GF फ्लोर ढलाई (GF floor slab pour):', [
            'a) Pipe stubs sealed with plastic caps during pour',
            'b) Floor drain channel cast-in with slope (1:100 toward back)',
            'c) After curing: connect toilet to pipe stub',
        ]),
        ('5. बाहर का काम (External work - can be done anytime):', [
            'a) Connect BW exit pipe to inspection chamber to septic',
            'b) Connect septic outlet to BW soak pit',
            'c) Connect WW exit to silt trap > oil trap > WW pit',
            'd) Lay GW underground route (capped) to grease trap location',
            'e) Install rainwater downpipe sleeves through plinth wall',
        ]),
        ('6. पहली मंजिल बनने के बाद (After 1F is built):', [
            'a) Open GW pipe cap, connect to 1F kitchen/bath downpipe',
            'b) Install grease trap at position (x=15, y=28)',
            'c) Connect grease trap to inspection chamber to GW soak pit',
            'd) Install 1F toilet, connect to BW vertical pipe (already in wall chase)',
        ]),
    ]

    for step_title, items in steps:
        pdf.set_font('HindiB', '', 7)
        pdf.set_xy(12, y)
        pdf.cell(0, 4.5, step_title)
        y += 5
        pdf.set_font('Hindi', '', 6)
        for item in items:
            pdf.set_xy(16, y)
            pdf.cell(0, 3.5, item)
            y += 3.8
        y += 2

    # ========== PAGE 7: TRAPS & CHAMBERS DETAIL (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()
    pdf.title_block('SHEET 7: TRAPS, CHAMBERS & FITTINGS / ट्रैप एवं चेम्बर')

    y = 22
    y = pdf.section_header(y, 'A. INSPECTION CHAMBERS / निरीक्षण चेम्बर')
    pdf.set_font('Hindi', '', 7)
    ic_info = [
        'Size: 1.5ft x 1.5ft x 2ft deep (450mm x 450mm x 600mm)',
        'Construction: Brick masonry with 1:4 cement mortar plaster inside',
        'Cover: CI (Cast Iron) heavy-duty Class D frame + cover (40 tonne rated)',
        'Benching: Smooth cement slope inside to direct flow (half-channel at bottom)',
        'Quantity: 2 nos (1 for BW system, 1 for GW system)',
        'Position: BW chamber at (x=-4, y=27.5). GW chamber at (x=12, y=33).',
        'Purpose: Access for cleaning blockages. Tanker pump connection for septic.',
    ]
    for item in ic_info:
        pdf.set_xy(14, y)
        pdf.cell(0, 4, item)
        y += 4.5

    y += 5
    y = pdf.section_header(y, 'B. GREASE TRAP / ग्रीस ट्रैप (Grey Water)')
    pdf.set_font('Hindi', '', 7)
    gt_info = [
        'Size: 600mm x 450mm x 600mm deep (2ft x 1.5ft x 2ft)',
        'Position: x=15, y=28 (behind building, near kitchen downpipe)',
        'Construction: RCC / Masonry with inlet and outlet at different heights',
        'Inlet: 3" pipe enters 2" below top',
        'Outlet: 3" pipe exits 4" below top (grease floats, clean water exits lower)',
        'Baffle: Vertical plate between inlet and outlet (forces water under)',
        'Cleaning: Scoop floating grease every 2-4 weeks',
        'Brand: Can use prefab FRP grease trap (Plasto/Supreme brand)',
    ]
    for item in gt_info:
        pdf.set_xy(14, y)
        pdf.cell(0, 4, item)
        y += 4.5

    y += 5
    y = pdf.section_header(y, 'C. SILT TRAP & OIL TRAP / सिल्ट एवं ऑयल ट्रैप (Wash Water)')
    pdf.set_font('Hindi', '', 7)
    st_info = [
        'SILT TRAP: 750mm x 750mm x 750mm (2.5ft cube) at x=9, y=28',
        '  Purpose: Settles mud, sand from tractor wash / ट्रैक्टर धोने का कीचड़',
        '  Cleaning: After every heavy wash / हर भारी धुलाई के बाद साफ करें',
        '',
        'OIL & GREASE TRAP: 750mm x 600mm x 750mm at x=8, y=33',
        '  Purpose: Removes diesel, engine oil from wash water',
        '  Construction: 2-chamber with baffle wall',
        '  Cleaning: Monthly - scoop floating oil / हर महीने तेल निकालें',
        '',
        'Both traps: Masonry construction, CI covers, at ground level',
    ]
    for item in st_info:
        if item == '':
            y += 2
            continue
        pdf.set_xy(14, y)
        pdf.cell(0, 4, item)
        y += 4.5

    y += 5
    y = pdf.section_header(y, 'D. IMPORTANT RULES / ज़रूरी नियम')
    pdf.set_font('HindiB', '', 7)
    rules = [
        'NEVER connect rainwater to any soak pit or septic!',
        '   बारिश का पानी कभी भी सेप्टिक/सोक पिट में न डालें!',
        'NEVER use 90-degree bends for black water pipes!',
        '   काले पानी की पाइप में 90 डिग्री मोड़ कभी न लगाएँ!',
        'NEVER mix black water and grey water systems!',
        '   काला पानी और धूसर पानी की लाइन अलग रखें!',
        'All soak pits MUST be 50ft+ from borewell!',
        '   सोक पिट बोरवेल से 50 फुट दूर होना ज़रूरी!',
    ]
    for rule in rules:
        pdf.set_xy(14, y)
        pdf.cell(0, 4, rule)
        y += 4.5

    # ========== PAGE 8: RAINWATER & WATER SUPPLY (A4) ==========
    pdf.add_a4_page()
    pdf.border_frame()
    pdf.title_block('SHEET 8: RAINWATER SYSTEM & WATER SUPPLY / वर्षा जल एवं पानी की आपूर्ति')

    y = 22
    y = pdf.section_header(y, 'A. RAINWATER DRAINAGE / बारिश का पानी')
    pdf.set_font('Hindi', '', 7)
    rain_info = [
        'Downpipes: 4 nos, 3" (75mm) PVC at building corners',
        'Exit: Through plinth wall at ground level (sleeves pre-installed)',
        'Disposal: Surface drainage directed AWAY from building into farm',
        'Alternative: Rainwater recharge pit (3ft dia x 10ft, gravel-filled)',
        'IMPORTANT: Rainwater is NEVER connected to septic/soak pit!',
        '  महत्वपूर्ण: बारिश का पानी सेप्टिक/सोक पिट से जोड़ना मना है!',
        '',
        'Roof drainage: Slab slope 1:100 toward corners (slope screed)',
        'Gutter: Not required (flat roof with parapet, water to downpipes)',
    ]
    for item in rain_info:
        if item == '':
            y += 2
            continue
        pdf.set_xy(14, y)
        pdf.cell(0, 4, item)
        y += 4.5

    y += 6
    y = pdf.section_header(y, 'B. WATER SUPPLY (FUTURE) / पानी की आपूर्ति')
    pdf.set_font('Hindi', '', 7)
    supply_info = [
        'Source: Borewell with submersible pump (30ft right of building)',
        'Tank: 1000L plastic tank on roof (2F level, on MS stand)',
        'Supply pipe: 1" (25mm) GI or CPVC from pump to tank',
        'Distribution: 3/4" (20mm) CPVC to kitchen, bathroom, toilet flush',
        '',
        'WATER SUPPLY TO BE DESIGNED SEPARATELY.',
        'This blueprint covers DRAINAGE only.',
        '',
        'Local brands for supply pipes:',
        '  CPVC: Ashirvad FlowGuard / Supreme CPVC / Astral',
        '  GI: Tata/Jindal (ISI marked)',
        '  Tank: Sintex / Supreme / Penguin (1000L, 3-layer)',
    ]
    for item in supply_info:
        if item == '':
            y += 2
            continue
        pdf.set_xy(14, y)
        pdf.cell(0, 4, item)
        y += 4.5

    return pdf


def main():
    print("Generating plumbing blueprint PDF...")
    pdf = build_pdf()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'plumbing-blueprint.pdf')
    pdf.output(output_path)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"PDF saved: {output_path}")
    print(f"  Size: {size_kb:.0f} KB")
    print(f"  Pages: 8")
    print(f"\nContents:")
    print("  Page 1: Title & Overview (A4)")
    print("  Page 2: Site Plan - All Systems (A3 Landscape)")
    print("  Page 3: Underground Pipe Layout (A3 Landscape)")
    print("  Page 4: Septic Tank & Soak Pit Details (A4)")
    print("  Page 5: Pipe Schedule & Brands (A4)")
    print("  Page 6: Construction Sequence (A4)")
    print("  Page 7: Traps, Chambers & Rules (A4)")
    print("  Page 8: Rainwater & Water Supply (A4)")


if __name__ == '__main__':
    main()
