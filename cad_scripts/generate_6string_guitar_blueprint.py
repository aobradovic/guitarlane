import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle, Arc, Wedge
import numpy as np

fig = plt.figure(figsize=(24, 15), dpi=180)
fig.patch.set_facecolor('#0a0e17')

gs = fig.add_gridspec(2, 3, width_ratios=[1.25, 1.0, 1.15], height_ratios=[1.25, 1.0], hspace=0.24, wspace=0.20)

def style_ax(ax, title, subtitle=''):
    ax.set_facecolor('#0f1623')
    ax.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.7)
    ax.minorticks_on()
    ax.grid(True, which='minor', color='#141d2b', linestyle=':', linewidth=0.4)
    ax.tick_params(colors='#94a3b8', labelsize=8)
    for s in ax.spines.values():
        s.set_color('#334155')
    ax.set_title(title, color='#f8fafc', fontsize=11.5, fontweight='bold', pad=18)
    if subtitle:
        ax.text(0.5, 1.015, subtitle, transform=ax.transAxes, color='#38bdf8', fontsize=8.5, ha='center', fontweight='bold')

# Exact 6-String Guitar Millimeter Coordinates (y=0 at bottom of Titanium U-Guard, y=721 at top of String Lock)
# Total length = 721 mm (28.38")
# y_guard_bottom = 0
# y_guard_top = 24 (U-guard shields barrel tuners from y=0 to y=24)
# y_saddle = 55 (Bridge saddle line)
# Scale length = 648 mm -> y_nut (Zero-Fret) = 55 + 648 = 703 mm
# y_headpiece_top = 703 + 18 = 721 mm
# y_24th_fret = 703 - (648 * 0.75) = 703 - 486 = 217 mm

def draw_6string_top(ax, with_wings=True, xray=False):
    y_nut = 703.0
    y_24 = 217.0
    y_saddle = 55.0
    nut_w = 43.0
    heel_w = 57.0
    guard_w = 82.0

    # 1. Spine Body (y=20 to y=217)
    pts_spine = [
        (-guard_w/2, 22),
        (-guard_w/2, 115),
        (-heel_w/2, y_24),
        (heel_w/2, y_24),
        (guard_w/2, 115),
        (guard_w/2, 22),
    ]
    spine_fc = '#161f30' if not xray else '#0f172a'
    ax.add_patch(Polygon(pts_spine, closed=True, facecolor=spine_fc, edgecolor='#e2e8f0', lw=1.8, zorder=4))

    if xray:
        # Draw internal 5-axis CNC honeycomb triangular pockets inside spine & neck!
        for yc in range(120, 210, 28):
            ax.add_patch(Polygon([(-24, yc), (-4, yc+12), (-24, yc+24)], closed=True, facecolor='#090d14', edgecolor='#38bdf8', lw=0.8, alpha=0.8, zorder=5))
            ax.add_patch(Polygon([(24, yc), (4, yc+12), (24, yc+24)], closed=True, facecolor='#090d14', edgecolor='#38bdf8', lw=0.8, alpha=0.8, zorder=5))
        # Rear Tremolo Spring Cavity in X-Ray (48x78mm)
        ax.add_patch(Rectangle((-24, 52), 48, 62, facecolor='#090d14', edgecolor='#f59e0b', lw=1.2, linestyle='--', zorder=5))
        for sx in [-14, 0, 14]:
            ax.plot([sx, sx], [56, 108], color='#fbbf24', lw=1.8, linestyle=':', zorder=6)

    # 2. CNC Titanium Rear U-Guard (y=0 to y=32, wraps around tuners)
    pts_uguard_outer = [
        (-guard_w/2, 32),
        (-guard_w/2, 8),
        (-guard_w/2 + 8, 0),
        (guard_w/2 - 8, 0),
        (guard_w/2, 8),
        (guard_w/2, 32),
        (guard_w/2 - 9, 32),
        (guard_w/2 - 9, 10),
        (-guard_w/2 + 9, 10),
        (-guard_w/2 + 9, 32),
    ]
    ax.add_patch(Polygon(pts_uguard_outer, closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=2.0, zorder=7))

    # 3. Neck & Richlite Fretboard (y=217 to y=703)
    pts_neck = [
        (-heel_w/2, y_24),
        (heel_w/2, y_24),
        (nut_w/2, y_nut),
        (-nut_w/2, y_nut),
    ]
    ax.add_patch(Polygon(pts_neck, closed=True, facecolor='#0b0f17', edgecolor='#cbd5e1', lw=1.6, zorder=5))

    if xray:
        # Internal Truss Rod + 2x Carbon Spars
        ax.add_patch(Rectangle((-3, 225), 6, 465, facecolor='#f59e0b', edgecolor='none', alpha=0.7, zorder=6))
        ax.add_patch(Rectangle((-13, 130), 4, 560, facecolor='#38bdf8', edgecolor='none', alpha=0.8, zorder=6))
        ax.add_patch(Rectangle((9, 130), 4, 560, facecolor='#38bdf8', edgecolor='none', alpha=0.8, zorder=6))

    # 4. 24 Stainless Frets + Zero-Fret at y_nut=703
    for f in range(0, 25):
        fy = y_nut - 648.0 * (1.0 - 2.0**(-f/12.0))
        fw = nut_w + (heel_w - nut_w) * ((y_nut - fy) / (y_nut - y_24))
        lw = 1.6 if f == 0 else 0.75
        col = '#38bdf8' if f == 0 else '#94a3b8'
        ax.plot([-fw/2, fw/2], [fy, fy], color=col, lw=lw, zorder=6)
        if f in [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]:
            prev_fy = y_nut - 648.0 * (1.0 - 2.0**(-(f-1)/12.0))
            mid_y = (fy + prev_fy)/2.0
            mid_w = nut_w + (heel_w - nut_w) * ((y_nut - mid_y) / (y_nut - y_24))
            # Luminlay side dots on bass side
            ax.add_patch(Circle((-mid_w/2 + 2.2, mid_y), 1.6, facecolor='#22d3ee', edgecolor='none', zorder=8))

    # 5. CNC LowPro String Lock Headpiece (y=703 to y=721)
    pts_head = [
        (-nut_w/2, y_nut),
        (nut_w/2, y_nut),
        (nut_w/2 - 2, 721),
        (-nut_w/2 + 2, 721),
    ]
    ax.add_patch(Polygon(pts_head, closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.6, zorder=7))

    # 6. Single High-Gain Soapbar Humbucker (Fishman Fluence Modern: 70mm x 38mm, centered at y=162)
    ax.add_patch(FancyBboxPatch((-35, 143), 70, 38, boxstyle='round,pad=0,rounding_size=4', facecolor='#090d14', edgecolor='#f8fafc', lw=1.5, zorder=7))
    ax.text(0, 162, 'FISHMAN\nFLUENCE', color='#94a3b8', fontsize=6.5, ha='center', va='center', fontweight='bold', zorder=8)

    # 7. Hipshot / Tan 6-String Headless Tremolo Bridge (y=26 to y=88, width=66mm)
    ax.add_patch(FancyBboxPatch((-33, 28), 66, 58, boxstyle='round,pad=0,rounding_size=3', facecolor='#1e293b', edgecolor='#38bdf8', lw=1.5, zorder=7))
    # 6 Saddles + 6 Barrel Tuners protruding into U-guard window (y=12 to y=28)
    for s in range(6):
        sx = -26.25 + s * 10.5 # 10.5mm string spacing (52.5mm E-to-e at bridge)
        nx = -17.5 + s * 7.0   # 7.0mm string spacing (35.0mm E-to-e at nut)
        # Saddle
        ax.add_patch(Rectangle((sx - 4.2, 48), 8.4, 18, facecolor='#334155', edgecolor='#cbd5e1', lw=0.8, zorder=8))
        # Barrel Tuner inside U-Guard Window
        ax.add_patch(Rectangle((sx - 3.5, 13), 7.0, 15, facecolor='#0f172a', edgecolor='#94a3b8', lw=0.9, zorder=8))
        # String
        ax.plot([nx, sx], [712, 55], color='#e2e8f0', lw=0.6 + (5-s)*0.15, alpha=0.85, zorder=9)

    # Tremolo Arm on treble side
    ax.plot([29, 38, 22], [58, 125, 195], color='#cbd5e1', lw=2.8, solid_capstyle='round', zorder=10)

    # Side-Edge Thumbwheel Volume + Neutrik Jack (on Treble edge y=135 & y=105)
    ax.add_patch(Rectangle((36, 136), 6, 20, facecolor='#f59e0b', edgecolor='#f8fafc', lw=1, zorder=8))
    ax.add_patch(Rectangle((38, 98), 4, 18, facecolor='#22c55e', edgecolor='#f8fafc', lw=1, zorder=8))

    if with_wings:
        # 3A Upper Contoured Horn Blade (Bolts into Bass Side at y=220..265, reaches up to y=410 / 12th fret!)
        pts_3a = [
            (-27, 215),
            (-24, 275),
            (-42, 295),
            (-78, 365),
            (-92, 415), # Strap pin at 12th fret balance point!
            (-96, 405),
            (-90, 345),
            (-72, 275),
            (-95, 195),
            (-82, 188),
            (-52, 235),
        ]
        ax.add_patch(Polygon(pts_3a, closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.8, zorder=3))
        # Captive Quarter-Turn Red Pin on 3A
        ax.add_patch(Circle((-31, 245), 4.5, facecolor='#ef4444', edgecolor='#f8fafc', lw=1, zorder=9))
        # Strap Lock on 3A tip
        ax.add_patch(Circle((-94, 412), 4.0, facecolor='#94a3b8', edgecolor='#f8fafc', lw=1, zorder=9))

        # 3B Skeletal Lower Leg Rail (Bolts into Treble Side of U-Guard at y=15..65, curves out to x=+135, y=210)
        pts_3b = [
            (41, 12),
            (85, 22),
            (122, 65),
            (136, 135),
            (126, 215),
            (112, 212),
            (120, 135),
            (108, 75),
            (76, 38),
            (41, 32),
        ]
        ax.add_patch(Polygon(pts_3b, closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.8, zorder=3))
        # Santoprene Warm-Touch Rubber Grip Strip along outer thigh curve of 3B!
        ax.plot([85, 122, 136, 126], [20, 63, 135, 215], color='#22c55e', lw=3.5, solid_capstyle='round', zorder=8)
        # Captive Quarter-Turn Red Pin on 3B
        ax.add_patch(Circle((46, 22), 4.5, facecolor='#ef4444', edgecolor='#f8fafc', lw=1, zorder=9))


# ==========================================
# PANEL 1 (Top-Left): ASSEMBLED TOP VIEW (1:1 Millimeter Scale)
# ==========================================
ax1 = fig.add_subplot(gs[:, 0])
style_ax(ax1, '1. TOP VIEW — ASSEMBLED (WITH 3A & 3B WINGS)', 'Total Length: 721 mm (28.38") | Assembled Width: 232 mm (9.1")')
ax1.set_xlim(-140, 175)
ax1.set_ylim(-45, 765)
ax1.set_aspect('equal')
draw_6string_top(ax1, with_wings=True, xray=False)

# Dimension & Feature Callouts on Panel 1
ax1.annotate('CNC LowPro String Lock\n+ Stainless Zero-Fret (43mm)', xy=(-21.5, 708), xytext=(-132, 708),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#f8fafc', fontsize=8, fontweight='bold')
ax1.annotate('3A Upper Horn Blade\n(Strap Lock at 12th-Fret Balance Point)', xy=(-92, 410), xytext=(-135, 475),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')
ax1.annotate('Red Quarter-Turn Pin #1\n(Push & Twist 90° to Detach)', xy=(-31, 245), xytext=(-135, 315),
             arrowprops=dict(arrowstyle='->', color='#ef4444', lw=1.2), color='#fca5a5', fontsize=8, fontweight='bold')
ax1.annotate('Side Knurled Volume Wheel\n(Push-Push Voice Switch)', xy=(42, 146), xytext=(68, 255),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.2), color='#fbbf24', fontsize=8, fontweight='bold')
ax1.annotate('Flush Neutrik Locking Jack', xy=(42, 105), xytext=(68, 225),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.2), color='#4ade80', fontsize=8, fontweight='bold')
ax1.annotate('3B Lower Leg Rail w/ Flush\n2mm Santoprene Warm Grip Strip', xy=(132, 125), xytext=(55, -28),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.2), color='#4ade80', fontsize=8, fontweight='bold')
ax1.annotate('CNC Titanium Rear U-Guard\n(Shields Tuners from Leg Contact)', xy=(-20, 4), xytext=(-135, -28),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')


# ==========================================
# PANEL 2 (Top-Center): BARE "ONE-STRIPE" SPINE + X-RAY LATTICE VIEW
# ==========================================
ax2 = fig.add_subplot(gs[:, 1])
style_ax(ax2, '2. BARE SPINE (LEFT) & INTERNAL CNC LATTICE (RIGHT)', 'Stripped Width: 43mm Nut -> 57mm 24th Fret -> 82mm (3.23") Max!')
ax2.set_xlim(-145, 145)
ax2.set_ylim(-45, 765)
ax2.set_aspect('equal')

# Draw Bare Spine shifted to x=-65, and X-Ray Internal Lattice Spine shifted to x=+65
# Helper wrapper using matplotlib transforms
import matplotlib.transforms as mtransforms

# Draw bare spine by temporarily shifting patches or drawing directly:
def draw_shifted_spine(ax, x_off, xray=False, title_tag=''):
    y_nut, y_24 = 703.0, 217.0
    nut_w, heel_w, guard_w = 43.0, 57.0, 82.0
    pts_spine = [(x_off-guard_w/2, 22), (x_off-guard_w/2, 115), (x_off-heel_w/2, y_24), (x_off+heel_w/2, y_24), (x_off+guard_w/2, 115), (x_off+guard_w/2, 22)]
    ax.add_patch(Polygon(pts_spine, closed=True, facecolor='#161f30' if not xray else '#090d14', edgecolor='#e2e8f0' if not xray else '#38bdf8', lw=1.6, zorder=4))
    
    pts_uguard = [(x_off-guard_w/2, 32), (x_off-guard_w/2, 8), (x_off-guard_w/2+8, 0), (x_off+guard_w/2-8, 0), (x_off+guard_w/2, 8), (x_off+guard_w/2, 32), (x_off+guard_w/2-9, 32), (x_off+guard_w/2-9, 10), (x_off-guard_w/2+9, 10), (x_off-guard_w/2+9, 32)]
    ax.add_patch(Polygon(pts_uguard, closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=1.8, zorder=7))

    pts_neck = [(x_off-heel_w/2, y_24), (x_off+heel_w/2, y_24), (x_off+nut_w/2, y_nut), (x_off-nut_w/2, y_nut)]
    ax.add_patch(Polygon(pts_neck, closed=True, facecolor='#0b0f17', edgecolor='#cbd5e1' if not xray else '#38bdf8', lw=1.5, zorder=5))

    if not xray:
        for f in range(0, 25):
            fy = y_nut - 648.0 * (1.0 - 2.0**(-f/12.0))
            fw = nut_w + (heel_w - nut_w) * ((y_nut - fy) / (y_nut - y_24))
            ax.plot([x_off-fw/2, x_off+fw/2], [fy, fy], color='#64748b', lw=0.7, zorder=6)
        ax.add_patch(FancyBboxPatch((x_off-35, 143), 70, 38, boxstyle='round,pad=0,rounding_size=4', facecolor='#090d14', edgecolor='#f8fafc', lw=1.3, zorder=7))
        ax.add_patch(FancyBboxPatch((x_off-33, 28), 66, 58, boxstyle='round,pad=0,rounding_size=3', facecolor='#1e293b', edgecolor='#38bdf8', lw=1.3, zorder=7))
        for s in range(6):
            sx = x_off - 26.25 + s * 10.5
            ax.add_patch(Rectangle((sx - 3.5, 13), 7.0, 15, facecolor='#0f172a', edgecolor='#94a3b8', lw=0.8, zorder=8))
    else:
        # Internal CNC 7075 Lattice + Truss Rod + Carbon Spars + Tremolo Spring Pocket
        ax.add_patch(Rectangle((x_off-3, 225), 6, 465, facecolor='#f59e0b', alpha=0.85, zorder=6))
        ax.add_patch(Rectangle((x_off-14, 125), 4.5, 565, facecolor='#38bdf8', alpha=0.9, zorder=6))
        ax.add_patch(Rectangle((x_off+9.5, 125), 4.5, 565, facecolor='#38bdf8', alpha=0.9, zorder=6))
        # Triangular weight-relief pockets along neck & body core
        for yc in range(230, 660, 36):
            ax.add_patch(Rectangle((x_off-20, yc), 5, 24, facecolor='#1e293b', edgecolor='#38bdf8', lw=0.6, zorder=6))
            ax.add_patch(Rectangle((x_off+15, yc), 5, 24, facecolor='#1e293b', edgecolor='#38bdf8', lw=0.6, zorder=6))
        for yc in range(125, 205, 26):
            ax.add_patch(Polygon([(x_off-32, yc), (x_off-16, yc+10), (x_off-32, yc+20)], closed=True, facecolor='#1e293b', edgecolor='#38bdf8', lw=0.8, zorder=6))
            ax.add_patch(Polygon([(x_off+32, yc), (x_off+16, yc+10), (x_off+32, yc+20)], closed=True, facecolor='#1e293b', edgecolor='#38bdf8', lw=0.8, zorder=6))
        # Rear Tremolo Spring Cavity
        ax.add_patch(Rectangle((x_off-24, 48), 48, 68, facecolor='#090d14', edgecolor='#f59e0b', lw=1.4, linestyle='--', zorder=6))
        for sx in [-14, 0, 14]:
            ax.plot([x_off+sx, x_off+sx], [54, 110], color='#fbbf24', lw=1.6, zorder=7)
        # Battery + Control Cavity
        ax.add_patch(Rectangle((x_off+16, 125), 18, 65, facecolor='#090d14', edgecolor='#22c55e', lw=1.2, zorder=6))

    ax.add_patch(Polygon([(x_off-nut_w/2, y_nut), (x_off+nut_w/2, y_nut), (x_off+nut_w/2-2, 721), (x_off-nut_w/2+2, 721)], closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.4, zorder=7))
    ax.text(x_off, 738, title_tag, color='#f8fafc', fontsize=8.5, ha='center', fontweight='bold')

draw_shifted_spine(ax2, -62, xray=False, title_tag='BARE TRAVEL STICK\n(82mm Max Width)')
draw_shifted_spine(ax2, 62, xray=True, title_tag='X-RAY INTERNAL VIEW\n(CNC Lattice + Carbon Spars)')

ax2.annotate('', xy=(-62-41, -18), xytext=(-62+41, -18), arrowprops=dict(arrowstyle='<->', color='#38bdf8', lw=1.5))
ax2.text(-62, -34, '82 mm (3.23 in)', color='#38bdf8', fontsize=8.5, ha='center', fontweight='bold')

ax2.annotate('2x Carbon I-Beams\n+ Dual-Action Truss Rod', xy=(62, 460), xytext=(-15, 530),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.5, ha='center', fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='#0f172a', edgecolor='#38bdf8'))
ax2.annotate('Rear Tremolo\nSpring Cavity', xy=(62, 80), xytext=(0, 15),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.2), color='#fbbf24', fontsize=7.5, ha='center', fontweight='bold')


# ==========================================
# PANEL 3 (Top-Right): SIDE PROFILE ELEVATION (Showing Thickness, Action & Recessed U-Guard)
# ==========================================
ax3 = fig.add_subplot(gs[0, 2])
style_ax(ax3, '3. SIDE PROFILE ELEVATION (THICKNESS & ACTION)', 'Neck: 18.5mm -> 20.0mm | Bridge Spine: 38.0mm (1.50") | Action: 0.9mm')
ax3.set_xlim(-20, 750)
ax3.set_ylim(-60, 110)
ax3.set_aspect('equal')

# Draw horizontal side profile from x=0 (Tail of U-Guard) to x=721 (Headpiece)
# Top surface of spine = y=0 from x=24 to x=217
# Fretboard sits from y=0 to y=+6.0mm (x=217 to x=703)
# Frets sit up to y=+7.45mm
# Neck back contour: at x=703 (nut), thickness=18.5mm (so y=+6 - 18.5 = -12.5mm). At x=400 (12th fret), thickness=20.0mm (y=-14.0mm). At x=217 (heel), tapers smoothly into y=-38.0mm bridge block!
pts_side_body = [
    (22, 0),
    (703, 0),
    (703, -12.5),
    (400, -14.0),
    (250, -16.0),
    (195, -38.0),
    (22, -38.0),
]
ax3.add_patch(Polygon(pts_side_body, closed=True, facecolor='#1e293b', edgecolor='#f8fafc', lw=1.8, zorder=4))

# Warm-Touch 2mm Carbon Fiber Back-of-Neck Shell (Highlighted in Cyan along back of neck!)
pts_carbon_back = [
    (703, -10.5),
    (400, -12.0),
    (250, -14.0),
    (250, -16.0),
    (400, -14.0),
    (703, -12.5),
]
ax3.add_patch(Polygon(pts_carbon_back, closed=True, facecolor='#38bdf8', edgecolor='none', zorder=6))

# Richlite Fretboard (6mm thick, x=217 to x=703)
ax3.add_patch(Rectangle((217, 0), 486, 6.0, facecolor='#090d14', edgecolor='#38bdf8', lw=1.4, zorder=5))

# CNC LowPro Headpiece at x=703..721
ax3.add_patch(Polygon([(703, 0), (721, 0), (721, 9.5), (703, 11.0)], closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=1.5, zorder=6))

# Pickup (x=143 to x=181, protruding 4mm above top)
ax3.add_patch(Rectangle((143, -12), 38, 16, facecolor='#090d14', edgecolor='#f8fafc', lw=1.4, zorder=6))

# Hipshot Tremolo + Sustain Block inside x=28..86 + Barrel Tuners at x=12..28
ax3.add_patch(Rectangle((28, -32), 58, 41, facecolor='#334155', edgecolor='#38bdf8', lw=1.4, zorder=6))
ax3.add_patch(Rectangle((12, -16), 18, 12, facecolor='#090d14', edgecolor='#fbbf24', lw=1.4, zorder=7)) # Barrel tuners

# CNC Titanium U-Guard in Side View (x=0 to x=32, extends 4mm BELOW barrel tuners so leg never touches tuners!)
pts_side_uguard = [
    (0, 2),
    (32, 2),
    (32, -4),
    (8, -4),
    (8, -22),
    (32, -22),
    (32, -28),
    (0, -28),
]
ax3.add_patch(Polygon(pts_side_uguard, closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=1.8, zorder=8))

# String line from Zero-Fret (x=703, y=7.5) to Bridge Saddle (x=55, y=9.5)
ax3.plot([55, 703], [9.5, 7.5], color='#4ade80', lw=1.2, zorder=9)

ax3.annotate('CNC Titanium U-Guard\nShields Tuners Below & Behind!', xy=(4, -25), xytext=(40, -52),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')
ax3.annotate('38 mm (1.50")\nBridge Spine Depth', xy=(120, -38), xytext=(150, -52),
             arrowprops=dict(arrowstyle='->', color='#f8fafc', lw=1.2), color='#f8fafc', fontsize=8, fontweight='bold')
ax3.annotate('2.0mm Warm-Touch Carbon/Cerakote\nNeck Shell (18.5mm -> 20.0mm Thin)', xy=(450, -13), xytext=(380, -48),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')
ax3.annotate('0.9mm Ultra-Low Action\nOver 24 Stainless Jumbo Frets', xy=(450, 8), xytext=(380, 45),
             arrowprops=dict(arrowstyle='->', color='#4ade80', lw=1.2), color='#4ade80', fontsize=8, fontweight='bold')


# ==========================================
# PANEL 4 (Bottom-Right): NECK CROSS-SECTION AT 12TH FRET (Showing Why It Never Feels Cold!)
# ==========================================
ax4 = fig.add_subplot(gs[1, 2])
style_ax(ax4, '4. NECK CROSS-SECTION AT 12TH FRET (50.0 x 20.0 mm)', 'Explains Why Your Hand Never Touches Cold Metal & How It Achieves Zero-Flex')
ax4.set_xlim(-34, 34)
ax4.set_ylim(-20, 14)
ax4.set_aspect('equal')

# Draw asymmetric Wizard/Enduro-C neck profile (width = 50mm at 12th fret: x=-25 to +25, depth = 20mm: y=+6 down to y=-14)
theta = np.linspace(np.pi, 2*np.pi, 100)
x_outer = 25.0 * np.cos(theta)
# Slight asymmetric flatten on bass/thumb side (x < 0)
y_outer = 14.0 * np.sin(theta)
x_inner = 22.8 * np.cos(theta)
y_inner = 11.8 * np.sin(theta)

# Outer 2.2mm Carbon Fiber / Cerakote Thermal Insulating Shell
pts_shell = np.vstack([np.column_stack([x_outer, y_outer]), np.column_stack([x_inner[::-1], y_inner[::-1]])])
ax4.add_patch(Polygon(pts_shell, closed=True, facecolor='#0f172a', edgecolor='#38bdf8', lw=2.2, zorder=4))

# Internal 7075 CNC Lattice Core inside the Carbon Shell
pts_core = np.column_stack([x_inner, y_inner])
ax4.add_patch(Polygon(pts_core, closed=True, facecolor='#334155', edgecolor='#94a3b8', lw=1.2, zorder=3))

# Weight-relief air channels in CNC core
ax4.add_patch(Circle((-14, -4.5), 3.2, facecolor='#090d14', edgecolor='#38bdf8', lw=1, zorder=5))
ax4.add_patch(Circle((14, -4.5), 3.2, facecolor='#090d14', edgecolor='#38bdf8', lw=1, zorder=5))

# Center Dual-Action Truss Rod (6mm x 9.5mm)
ax4.add_patch(Rectangle((-3.0, -9.5), 6.0, 9.5, facecolor='#451a03', edgecolor='#f59e0b', lw=1.5, zorder=6))
ax4.add_patch(Circle((0, -3.0), 1.8, facecolor='#fbbf24', zorder=7))
ax4.add_patch(Circle((0, -7.0), 1.8, facecolor='#fbbf24', zorder=7))

# Two Pultruded High-Modulus Carbon Fiber I-Beam Spars (4mm x 10mm) flanking the truss rod
ax4.add_patch(Rectangle((-9.5, -10.0), 4.0, 10.0, facecolor='#090d14', edgecolor='#38bdf8', lw=1.6, zorder=6))
ax4.add_patch(Rectangle((5.5, -10.0), 4.0, 10.0, facecolor='#090d14', edgecolor='#38bdf8', lw=1.6, zorder=6))

# Richlite Black Diamond Fretboard (50mm wide x 6mm thick, with 1.5mm Rolled Comfort Edges!)
ax4.add_patch(FancyBboxPatch((-25.0, 0), 50.0, 6.0, boxstyle='round,pad=0,rounding_size=2.0', facecolor='#090d14', edgecolor='#cbd5e1', lw=1.8, zorder=7))

# Luminlay 2.5mm Glowing Side Dot on Bass Side (x=-23.5, y=3.0)
ax4.add_patch(Circle((-23.2, 3.0), 1.3, facecolor='#22d3ee', edgecolor='#fff', lw=0.6, zorder=8))

# Jescar FW57110-S Stainless Steel Jumbo Fret + 6 Strings on 16"-20" Compound Radius
ax4.add_patch(FancyBboxPatch((-23.5, 6.0), 47.0, 1.45, boxstyle='round,pad=0,rounding_size=0.7', facecolor='#e2e8f0', edgecolor='#38bdf8', lw=1.2, zorder=8))
for s in range(6):
    sx = -21.0 + s * 8.4
    ax4.add_patch(Circle((sx, 8.3), 0.65 - s*0.06, facecolor='#4ade80', edgecolor='#fff', lw=0.5, zorder=9))

# Callouts on Cross-Section
ax4.annotate('Richlite Fretboard (6mm)\n+ Rolled Comfort Edges', xy=(18, 3.5), xytext=(15, 10.5),
             arrowprops=dict(arrowstyle='->', color='#f8fafc', lw=1.2), color='#f8fafc', fontsize=7.5, fontweight='bold')
ax4.annotate('Luminlay 2.5mm\nGlow Side Dot', xy=(-23.2, 3.0), xytext=(-33, 10.5),
             arrowprops=dict(arrowstyle='->', color='#22d3ee', lw=1.2), color='#22d3ee', fontsize=7.5, fontweight='bold')
ax4.annotate('2.2mm Carbon/Cerakote Outer Shell\n(Warm to Touch in 2 Seconds!)', xy=(-16, -11), xytext=(-33, -18),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.5, fontweight='bold')
ax4.annotate('Dual Carbon Spars\n+ Low-Profile Truss Rod', xy=(0, -9.5), xytext=(8, -18),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.2), color='#fbbf24', fontsize=7.5, fontweight='bold')

plt.suptitle('6-STRING "CARBON SPINE" MASTER ENGINEERING BLUEPRINT (METHOD 2 TURNKEY CNC HYBRID — 1:1 MILLIMETER SCALE)', color='#f8fafc', fontsize=14.5, fontweight='bold', y=0.98)
plt.savefig(r'C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\guitar_6string_master_blueprint.png', dpi=180, bbox_inches='tight')
print('Saved 6-string guitar master blueprint successfully')
