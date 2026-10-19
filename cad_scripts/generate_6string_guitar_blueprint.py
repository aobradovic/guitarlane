import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle
import numpy as np

fig = plt.figure(figsize=(25, 15.5), dpi=180)
fig.patch.set_facecolor('#0a0e17')

gs = fig.add_gridspec(2, 3, width_ratios=[1.25, 1.05, 1.15], height_ratios=[1.22, 1.0], hspace=0.24, wspace=0.20)

def style_ax(ax, title, subtitle=''):
    ax.set_facecolor('#0f1623')
    ax.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.7)
    ax.minorticks_on()
    ax.grid(True, which='minor', color='#141d2b', linestyle=':', linewidth=0.4)
    ax.tick_params(colors='#94a3b8', labelsize=8)
    for s in ax.spines.values():
        s.set_color('#334155')
    ax.set_title(title, color='#f8fafc', fontsize=11.2, fontweight='bold', pad=18)
    if subtitle:
        ax.text(0.5, 1.015, subtitle, transform=ax.transAxes, color='#38bdf8', fontsize=8.5, ha='center', fontweight='bold')

def cubic_bezier(p0, p1, p2, p3, n=25):
    t = np.linspace(0, 1, n)[:, None]
    pts = ((1-t)**3)*np.array(p0) + 3*((1-t)**2)*t*np.array(p1) + 3*(1-t)*(t**2)*np.array(p2) + (t**3)*np.array(p3)
    return pts.tolist()

def smooth_spine_polygon(x_off=0.0):
    y_upper = np.linspace(160, 217, 25)
    t = (y_upper - 160) / (217 - 160)
    w_half = 28.5 + (41.0 - 28.5) * 0.5 * (1 + np.cos(np.pi * t))
    right_curve = [(x_off + w, y) for w, y in zip(w_half, y_upper)]
    left_curve = [(x_off - w, y) for w, y in zip(w_half[::-1], y_upper[::-1])]
    pts = [(x_off - 35, 16), (x_off + 35, 16), (x_off + 41, 24)] + right_curve + left_curve + [(x_off - 41, 24)]
    return pts

def smooth_3a_wing_pts():
    c1 = cubic_bezier((-25.5, 272), (-42, 285), (-72, 350), (-88, 406), 24)
    c2 = cubic_bezier((-88, 406), (-92, 420), (-103, 416), (-101, 400), 16)
    c3 = cubic_bezier((-101, 400), (-96, 340), (-74, 260), (-48, 220), 24)
    c4 = cubic_bezier((-48, 220), (-38, 206), (-32, 208), (-27.5, 215), 12)
    return [(-27.5, 215), (-25.5, 272)] + c1 + c2 + c3 + c4

def smooth_3b_wing_pts():
    c1 = cubic_bezier((40, 14), (92, 16), (138, 70), (135, 146), 28)
    c2 = cubic_bezier((135, 146), (133, 182), (126, 206), (122, 214), 16)
    c3 = cubic_bezier((122, 214), (116, 222), (109, 218), (111, 206), 12)
    c4 = cubic_bezier((111, 206), (116, 186), (120, 168), (121, 146), 16)
    c5 = cubic_bezier((121, 146), (123, 82), (84, 36), (40, 34), 28)
    return c1 + c2 + c3 + c4 + c5

def draw_6string_top(ax, with_wings=True):
    y_nut = 703.0
    y_24 = 217.0
    nut_w = 43.0
    heel_w = 57.0

    # 1. Smooth S-Curve & Beveled Spine Body (y=16 to y=217)
    pts_spine = smooth_spine_polygon(0.0)
    ax.add_patch(Polygon(pts_spine, closed=True, facecolor='#161f30', edgecolor='#e2e8f0', lw=1.8, zorder=4))
    pts_bevel = [(x*0.91, y) for x, y in pts_spine]
    ax.add_patch(Polygon(pts_bevel, closed=True, facecolor='none', edgecolor='#475569', lw=0.9, linestyle='--', zorder=4.5))

    # 2. Pillowed R14mm Rounded CNC Titanium Rear U-Guard (y=0 to y=32)
    ax.add_patch(FancyBboxPatch((-41, 0), 82, 32, boxstyle='round,pad=0,rounding_size=10', facecolor='#475569', edgecolor='#38bdf8', lw=2.0, zorder=6))
    ax.add_patch(FancyBboxPatch((-31, 10), 62, 24, boxstyle='round,pad=0,rounding_size=5', facecolor='#0f1623', edgecolor='#38bdf8', lw=1.2, zorder=6.5))

    # 3. Neck & Richlite Fretboard (y=217 to y=703)
    pts_neck = [(-heel_w/2, y_24), (heel_w/2, y_24), (nut_w/2, y_nut), (-nut_w/2, y_nut)]
    ax.add_patch(Polygon(pts_neck, closed=True, facecolor='#0b0f17', edgecolor='#cbd5e1', lw=1.6, zorder=5))

    # 4. 24 Stainless Frets + Zero-Fret at y_nut=703
    for f in range(0, 25):
        fy = y_nut - 648.0 * (1.0 - 2.0**(-f/12.0))
        fw = nut_w + (heel_w - nut_w) * ((y_nut - fy) / (y_nut - y_24))
        lw = 1.6 if f == 0 else 0.75
        col = '#38bdf8' if f == 0 else '#94a3b8'
        ax.plot([-fw/2 + 1, fw/2 - 1], [fy, fy], color=col, lw=lw, zorder=6)
        if f in [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]:
            prev_fy = y_nut - 648.0 * (1.0 - 2.0**(-(f-1)/12.0))
            mid_y = (fy + prev_fy)/2.0
            mid_w = nut_w + (heel_w - nut_w) * ((y_nut - mid_y) / (y_nut - y_24))
            ax.add_patch(Circle((-mid_w/2 + 2.2, mid_y), 1.5, facecolor='#22d3ee', edgecolor='none', zorder=8))

    # 5. Rounded CNC LowPro String Lock Headpiece (y=703 to y=721)
    ax.add_patch(FancyBboxPatch((-nut_w/2, y_nut), nut_w, 18, boxstyle='round,pad=0,rounding_size=4', facecolor='#334155', edgecolor='#38bdf8', lw=1.6, zorder=7))

    # 6. Single High-Gain Soapbar Humbucker (Fishman Fluence Modern: 70mm x 38mm, centered at y=162)
    ax.add_patch(FancyBboxPatch((-35, 143), 70, 38, boxstyle='round,pad=0,rounding_size=5', facecolor='#090d14', edgecolor='#f8fafc', lw=1.5, zorder=7))
    ax.text(0, 162, 'FISHMAN FLUENCE\n+ RF ANTENNA WINDOW', color='#94a3b8', fontsize=6.0, ha='center', va='center', fontweight='bold', zorder=8)

    # 7. Hipshot 6-String Headless Tremolo Bridge (y=28 to y=86, width=66mm)
    ax.add_patch(FancyBboxPatch((-33, 28), 66, 58, boxstyle='round,pad=0,rounding_size=4', facecolor='#1e293b', edgecolor='#38bdf8', lw=1.5, zorder=7))
    for s in range(6):
        sx = -26.25 + s * 10.5
        nx = -17.5 + s * 7.0
        ax.add_patch(FancyBboxPatch((sx - 4.2, 48), 8.4, 18, boxstyle='round,pad=0,rounding_size=1.5', facecolor='#334155', edgecolor='#cbd5e1', lw=0.8, zorder=8))
        ax.add_patch(Rectangle((sx - 3.5, 13), 7.0, 15, facecolor='#0f172a', edgecolor='#94a3b8', lw=0.9, zorder=8))
        ax.plot([nx, sx], [712, 55], color='#e2e8f0', lw=0.6 + (5-s)*0.15, alpha=0.85, zorder=9)

    # Tremolo Arm
    ax.plot([29, 38, 22], [58, 125, 195], color='#cbd5e1', lw=2.8, solid_capstyle='round', zorder=10)

    # Right Side-Wall Integrated Control Panel (4 Controls)
    ax.add_patch(Rectangle((37, 164), 5.5, 18, facecolor='#f59e0b', edgecolor='#f8fafc', lw=1, zorder=8))
    ax.add_patch(Rectangle((38, 143), 4.5, 11, facecolor='#a855f7', edgecolor='#f8fafc', lw=1, zorder=8))
    ax.add_patch(Rectangle((38, 122), 4.5, 11, facecolor='#38bdf8', edgecolor='#f8fafc', lw=1, zorder=8))
    ax.add_patch(Rectangle((38, 96), 4.5, 16, facecolor='#22c55e', edgecolor='#f8fafc', lw=1, zorder=8))

    if with_wings:
        ax.add_patch(Polygon(smooth_3a_wing_pts(), closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.8, zorder=3))
        ax.add_patch(Circle((-31, 245), 4.5, facecolor='#ef4444', edgecolor='#f8fafc', lw=1, zorder=9))
        ax.add_patch(Circle((-95, 412), 4.0, facecolor='#94a3b8', edgecolor='#f8fafc', lw=1, zorder=9))

        ax.add_patch(Polygon(smooth_3b_wing_pts(), closed=True, facecolor='#334155', edgecolor='#38bdf8', lw=1.8, zorder=3))
        grip_pts = cubic_bezier((85, 18), (128, 52), (140, 140), (124, 212), 30)
        gx, gy = zip(*grip_pts)
        ax.plot(gx, gy, color='#22c55e', lw=3.8, solid_capstyle='round', zorder=8)
        ax.add_patch(Circle((46, 24), 4.5, facecolor='#ef4444', edgecolor='#f8fafc', lw=1, zorder=9))


# ==========================================
# PANEL 1 (Left): ASSEMBLED TOP VIEW
# ==========================================
ax1 = fig.add_subplot(gs[:, 0])
style_ax(ax1, '1. TOP VIEW — SMOOTH BEVELED & ROUNDED SPINE + ONBOARD RIG', 'Total Length: 721 mm (28.38") | Spine: 82 mm (3.23") | R6–R8mm Roundovers')
ax1.set_xlim(-142, 178)
ax1.set_ylim(-48, 765)
ax1.set_aspect('equal')
draw_6string_top(ax1, with_wings=True)

ax1.annotate('CNC LowPro String Lock\n+ Stainless Zero-Fret (43mm)', xy=(-21.5, 708), xytext=(-135, 708),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#f8fafc', fontsize=8, fontweight='bold')
ax1.annotate('Smooth Teardrop 3A Horn\n(R8mm Bullnose Edge, Zero Spikes)', xy=(-95, 410), xytext=(-138, 480),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')
ax1.annotate('Red Quarter-Turn Pin #1\n(Push & Twist 90° to Detach)', xy=(-31, 245), xytext=(-138, 315),
             arrowprops=dict(arrowstyle='->', color='#ef4444', lw=1.2), color='#fca5a5', fontsize=8, fontweight='bold')
ax1.annotate('1. Master Vol + Push-Push Bypass', xy=(42.5, 173), xytext=(58, 285),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.2), color='#fbbf24', fontsize=7.8, fontweight='bold')
ax1.annotate('2. 3-Way Preset Toggle (Rhythm/Lead/Clean)', xy=(42.5, 148), xytext=(58, 260),
             arrowprops=dict(arrowstyle='->', color='#a855f7', lw=1.2), color='#c084fc', fontsize=7.8, fontweight='bold')
ax1.annotate('3. USB-C 30W Charge + DAW Audio Port', xy=(42.5, 127), xytext=(58, 235),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.8, fontweight='bold')
ax1.annotate('4. Flush Neutrik Locking 1/4" Jack', xy=(42.5, 104), xytext=(58, 210),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.2), color='#4ade80', fontsize=7.8, fontweight='bold')
ax1.annotate('Smooth C-Curve 3B Leg Rail\n(R8mm Roundover + 2mm Santoprene Grip)', xy=(134, 130), xytext=(48, -32),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.2), color='#4ade80', fontsize=8, fontweight='bold')
ax1.annotate('Pillowed R14mm Titanium U-Guard\n(Shields Tuners from Leg Contact)', xy=(-20, 4), xytext=(-138, -32),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=8, fontweight='bold')


# ==========================================
# PANEL 2 (Center): BARE SPINE vs. INTERNAL CNC LATTICE + BATTERIES + GREEN SCREAMER + NS-1 + NAM + WIRELESS
# ==========================================
ax2 = fig.add_subplot(gs[:, 1])
style_ax(ax2, '2. BARE SPINE (LEFT) & ONBOARD BATTERY + DSP BAY (RIGHT)', 'Includes Dual-18650 (7,000 mAh) + Green Screamer + NS-1 Gate + NAM + 5.8GHz TX')
ax2.set_xlim(-148, 148)
ax2.set_ylim(-48, 765)
ax2.set_aspect('equal')

def draw_shifted_spine(ax, x_off, xray=False, title_tag=''):
    y_nut, y_24 = 703.0, 217.0
    nut_w, heel_w = 43.0, 57.0
    pts_spine = smooth_spine_polygon(x_off)
    ax.add_patch(Polygon(pts_spine, closed=True, facecolor='#161f30' if not xray else '#090d14', edgecolor='#e2e8f0' if not xray else '#38bdf8', lw=1.6, zorder=4))

    ax.add_patch(FancyBboxPatch((x_off-41, 0), 82, 32, boxstyle='round,pad=0,rounding_size=10', facecolor='#475569', edgecolor='#38bdf8', lw=1.8, zorder=7))
    ax.add_patch(FancyBboxPatch((x_off-31, 10), 62, 24, boxstyle='round,pad=0,rounding_size=5', facecolor='#0f1623', edgecolor='#38bdf8', lw=1.0, zorder=7.2))

    pts_neck = [(x_off-heel_w/2, y_24), (x_off+heel_w/2, y_24), (x_off+nut_w/2, y_nut), (x_off-nut_w/2, y_nut)]
    ax.add_patch(Polygon(pts_neck, closed=True, facecolor='#0b0f17', edgecolor='#cbd5e1' if not xray else '#38bdf8', lw=1.5, zorder=5))

    if not xray:
        for f in range(0, 25):
            fy = y_nut - 648.0 * (1.0 - 2.0**(-f/12.0))
            fw = nut_w + (heel_w - nut_w) * ((y_nut - fy) / (y_nut - y_24))
            ax.plot([x_off-fw/2+1, x_off+fw/2-1], [fy, fy], color='#64748b', lw=0.7, zorder=6)
        ax.add_patch(FancyBboxPatch((x_off-35, 143), 70, 38, boxstyle='round,pad=0,rounding_size=5', facecolor='#090d14', edgecolor='#f8fafc', lw=1.3, zorder=7))
        ax.add_patch(FancyBboxPatch((x_off-33, 28), 66, 58, boxstyle='round,pad=0,rounding_size=4', facecolor='#1e293b', edgecolor='#38bdf8', lw=1.3, zorder=7))
        for s in range(6):
            sx = x_off - 26.25 + s * 10.5
            ax.add_patch(Rectangle((sx - 3.5, 13), 7.0, 15, facecolor='#0f172a', edgecolor='#94a3b8', lw=0.8, zorder=8))
    else:
        ax.add_patch(Rectangle((x_off-3, 222), 6, 468, facecolor='#f59e0b', alpha=0.85, zorder=6))
        ax.add_patch(Rectangle((x_off-13.5, 212), 4.5, 480, facecolor='#38bdf8', alpha=0.9, zorder=6))
        ax.add_patch(Rectangle((x_off+9.0, 212), 4.5, 480, facecolor='#38bdf8', alpha=0.9, zorder=6))
        for yc in range(232, 660, 36):
            ax.add_patch(FancyBboxPatch((x_off-20, yc), 5, 24, boxstyle='round,pad=0,rounding_size=2', facecolor='#1e293b', edgecolor='#38bdf8', lw=0.6, zorder=6))
            ax.add_patch(FancyBboxPatch((x_off+15, yc), 5, 24, boxstyle='round,pad=0,rounding_size=2', facecolor='#1e293b', edgecolor='#38bdf8', lw=0.6, zorder=6))

        # 2. LEFT UNDERSIDE BAY: DUAL-18650 RECHARGEABLE BATTERY CRADLE (2x 3,500mAh = 7,000mAh)
        ax.add_patch(FancyBboxPatch((x_off-37.5, 118), 36.5, 72, boxstyle='round,pad=0,rounding_size=3', facecolor='#064e3b', edgecolor='#22c55e', lw=1.5, zorder=6.5))
        ax.add_patch(FancyBboxPatch((x_off-35.5, 121), 15.5, 65, boxstyle='round,pad=0,rounding_size=2', facecolor='#10b981', edgecolor='#ecfdf5', lw=0.9, zorder=7))
        ax.add_patch(FancyBboxPatch((x_off-18.5, 121), 15.5, 65, boxstyle='round,pad=0,rounding_size=2', facecolor='#10b981', edgecolor='#ecfdf5', lw=0.9, zorder=7))
        ax.text(x_off-27.7, 153.5, '18650\n3500mAh', color='#022c22', fontsize=5.2, ha='center', va='center', fontweight='bold', rotation=90, zorder=8)
        ax.text(x_off-10.7, 153.5, '18650\n3500mAh', color='#022c22', fontsize=5.2, ha='center', va='center', fontweight='bold', rotation=90, zorder=8)

        # 3. RIGHT-CENTER UNDERSIDE BAY: GREEN SCREAMER + KEYED NS-1 GATE PCB + NAM NEURAL DSP MODULE
        ax.add_patch(FancyBboxPatch((x_off+1.0, 118), 36.5, 72, boxstyle='round,pad=0,rounding_size=3', facecolor='#1e1b4b', edgecolor='#a855f7', lw=1.5, zorder=6.5))
        ax.add_patch(Rectangle((x_off+3.0, 121), 15.0, 66, facecolor='#15803d', edgecolor='#86efac', lw=1.0, zorder=7))
        ax.text(x_off+10.5, 154, 'GREEN SCREAMER\n+ NS-1 KEY GATE', color='#f0fdf4', fontsize=5.0, ha='center', va='center', fontweight='bold', rotation=90, zorder=8)
        ax.add_patch(Rectangle((x_off+19.5, 121), 16.0, 66, facecolor='#312e81', edgecolor='#c084fc', lw=1.0, zorder=7))
        ax.text(x_off+27.5, 154, 'NAM + CAB IR\n+ WI-FI 6 DSP', color='#f3e8ff', fontsize=5.0, ha='center', va='center', fontweight='bold', rotation=90, zorder=8)

        # 4. UPPER HEEL RF WINDOW BAY (y=192 to 214): 5.8GHz ULL Wireless Audio Sender + FPC Antenna
        ax.add_patch(FancyBboxPatch((x_off-24, 193), 48, 20, boxstyle='round,pad=0,rounding_size=3', facecolor='#0c4a6e', edgecolor='#38bdf8', lw=1.4, zorder=6.8))
        ax.text(x_off, 203, '5.8GHz ULL WIRELESS TX\n+ RF ANTENNA (1.8ms)', color='#e0f2fe', fontsize=5.2, ha='center', va='center', fontweight='bold', zorder=8)

        # 5. Rear 3-Spring Tremolo Cavity
        ax.add_patch(FancyBboxPatch((x_off-24, 42), 48, 70, boxstyle='round,pad=0,rounding_size=3', facecolor='#090d14', edgecolor='#f59e0b', lw=1.4, linestyle='--', zorder=6))
        for sx in [-14, 0, 14]:
            ax.plot([x_off+sx, x_off+sx], [48, 106], color='#fbbf24', lw=1.6, zorder=7)

    ax.add_patch(FancyBboxPatch((x_off-nut_w/2, y_nut), nut_w, 18, boxstyle='round,pad=0,rounding_size=4', facecolor='#334155', edgecolor='#38bdf8', lw=1.4, zorder=7))
    ax.text(x_off, 738, title_tag, color='#f8fafc', fontsize=8.5, ha='center', fontweight='bold')

draw_shifted_spine(ax2, -62, xray=False, title_tag='BARE TRAVEL STICK\n(82mm Max Width)')
draw_shifted_spine(ax2, 62, xray=True, title_tag='X-RAY INTERNAL VIEW\n(Batteries + NAM + Screamer + TX)')

ax2.annotate('', xy=(-62-41, -18), xytext=(-62+41, -18), arrowprops=dict(arrowstyle='<->', color='#38bdf8', lw=1.5))
ax2.text(-62, -34, '82 mm (3.23 in)', color='#38bdf8', fontsize=8.5, ha='center', fontweight='bold')

ax2.annotate('2x Carbon I-Beams\n+ Dual-Action Truss Rod', xy=(62, 490), xytext=(0, 560),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.2, ha='center', fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='#0f172a', edgecolor='#38bdf8'))
ax2.annotate('5.8GHz ULL Wireless TX\n(Under RF-Transparent Heel)', xy=(62, 203), xytext=(0, 380),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.3), color='#38bdf8', fontsize=7.2, ha='center', fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='#0c4a6e', edgecolor='#38bdf8'))
ax2.annotate('2x 18650 Battery Bay\n(7,000 mAh / 10h–18h Runtime)', xy=(62-28, 155), xytext=(0, 290),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.3), color='#4ade80', fontsize=7.2, ha='center', fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='#064e3b', edgecolor='#22c55e'))
ax2.annotate('Green Screamer + NS-1 Gate\n+ NAM Neural Engine Bay', xy=(62+22, 135), xytext=(62, -34),
             arrowprops=dict(arrowstyle='->', color='#a855f7', lw=1.3), color='#c084fc', fontsize=7.5, ha='center', fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', facecolor='#1e1b4b', edgecolor='#a855f7'))


# ==========================================
# PANEL 3 (Top-Right): SIDE PROFILE ELEVATION
# ==========================================
ax3 = fig.add_subplot(gs[0, 2])
style_ax(ax3, '3. SIDE PROFILE ELEVATION (STACKED PICKUP & BATTERY/DSP BAY)', 'Top 15mm: Pickup | Bottom 20mm (z=-16 to -36mm): 2x 18650 Batteries + NAM + Screamer')
ax3.set_xlim(-20, 750)
ax3.set_ylim(-75, 110)
ax3.set_aspect('equal')

pts_side_body = [(22, 0), (703, 0), (703, -12.5), (400, -14.0), (250, -16.0), (215, -38.0), (22, -38.0)]
ax3.add_patch(Polygon(pts_side_body, closed=True, facecolor='#1e293b', edgecolor='#f8fafc', lw=1.8, zorder=4))

pts_carbon_back = [(703, -10.3), (400, -11.8), (250, -13.8), (250, -16.0), (400, -14.0), (703, -12.5)]
ax3.add_patch(Polygon(pts_carbon_back, closed=True, facecolor='#38bdf8', edgecolor='none', zorder=6))

ax3.add_patch(Rectangle((217, 0), 486, 6.0, facecolor='#090d14', edgecolor='#38bdf8', lw=1.4, zorder=5))
ax3.add_patch(Polygon([(703, 0), (721, 0), (721, 9.5), (703, 11.0)], closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=1.5, zorder=6))

ax3.add_patch(Rectangle((143, -13), 38, 17, facecolor='#090d14', edgecolor='#f8fafc', lw=1.4, zorder=6))

# UNDERSIDE BATTERY + NAM + GREEN SCREAMER + NS-1 GATE BAY (x=116 to x=212, depth z=-16 to -36mm)
ax3.add_patch(Rectangle((116, -36), 96, 19.5, facecolor='#064e3b', edgecolor='#22c55e', lw=1.5, zorder=6.5))
ax3.plot([116, 212], [-37.5, -37.5], color='#ef4444', lw=2.5, zorder=8)

ax3.add_patch(Rectangle((28, -32), 58, 41, facecolor='#334155', edgecolor='#38bdf8', lw=1.4, zorder=6))
ax3.add_patch(Rectangle((12, -16), 18, 12, facecolor='#090d14', edgecolor='#fbbf24', lw=1.4, zorder=7))

pts_side_uguard = [(0, 2), (32, 2), (32, -4), (8, -4), (8, -22), (32, -22), (32, -28), (0, -28)]
ax3.add_patch(Polygon(pts_side_uguard, closed=True, facecolor='#475569', edgecolor='#38bdf8', lw=1.8, zorder=8))

ax3.plot([55, 703], [9.5, 7.5], color='#4ade80', lw=1.2, zorder=9)

ax3.annotate('CNC Titanium U-Guard\nShields Tuners', xy=(4, -25), xytext=(-10, -68),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.5, fontweight='bold')
ax3.annotate('20mm Deep Lower Bay:\n2x 18650 + NAM + Screamer', xy=(164, -36), xytext=(155, -68),
             arrowprops=dict(arrowstyle='->', color='#22c55e', lw=1.3), color='#4ade80', fontsize=7.5, fontweight='bold')
ax3.annotate('2.2mm Warm-Touch Carbon\nNeck Shell (18.5->20mm)', xy=(480, -13), xytext=(440, -68),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.5, fontweight='bold')
ax3.annotate('0.9mm Ultra-Low Action\nOver 24 Stainless Jumbo Frets', xy=(450, 8), xytext=(380, 45),
             arrowprops=dict(arrowstyle='->', color='#4ade80', lw=1.2), color='#4ade80', fontsize=8, fontweight='bold')


# ==========================================
# PANEL 4 (Bottom-Right): LOWER SPINE CROSS-SECTION AT PICKUP (82.0 x 38.0 mm)
# ==========================================
ax4 = fig.add_subplot(gs[1, 2])
style_ax(ax4, '4. SPINE CROSS-SECTION AT PICKUP BAY (82.0 x 38.0 mm)', 'Shows How Pickup, 2x 18650 Batteries, Green Screamer, NS-1 Gate & NAM Stack Inside 38mm')
ax4.set_xlim(-48, 48)
ax4.set_ylim(-42, 12)
ax4.set_aspect('equal')

ax4.add_patch(FancyBboxPatch((-41.0, -38.0), 82.0, 38.0, boxstyle='round,pad=0,rounding_size=6.0', facecolor='#334155', edgecolor='#38bdf8', lw=2.2, zorder=3))
ax4.add_patch(FancyBboxPatch((-39.0, -3.0), 78.0, 3.0, boxstyle='round,pad=0,rounding_size=1.5', facecolor='#0f172a', edgecolor='#cbd5e1', lw=1.2, zorder=4))

ax4.add_patch(FancyBboxPatch((-35.0, -13.0), 70.0, 16.0, boxstyle='round,pad=0,rounding_size=2.5', facecolor='#090d14', edgecolor='#f8fafc', lw=1.6, zorder=6))
ax4.text(0, -5.0, 'FISHMAN FLUENCE SOAPBAR PICKUP (70 x 14 mm)\n+ RF-TRANSPARENT 5.8GHz ANTENNA SLOT', color='#e2e8f0', fontsize=6.5, ha='center', va='center', fontweight='bold', zorder=7)

ax4.add_patch(Rectangle((-37.0, -15.5), 74.0, 2.5, facecolor='#475569', edgecolor='#94a3b8', lw=1.0, zorder=5))

ax4.add_patch(Rectangle((-37.0, -35.5), 36.0, 20.0, facecolor='#090d14', edgecolor='#22c55e', lw=1.4, zorder=5))
ax4.add_patch(Circle((-28.0, -25.5), 9.0, facecolor='#10b981', edgecolor='#ecfdf5', lw=1.4, zorder=6))
ax4.add_patch(Circle((-10.0, -25.5), 9.0, facecolor='#10b981', edgecolor='#ecfdf5', lw=1.4, zorder=6))
ax4.text(-28.0, -25.5, '18650\nCell #1', color='#022c22', fontsize=6.0, ha='center', va='center', fontweight='bold', zorder=7)
ax4.text(-10.0, -25.5, '18650\nCell #2', color='#022c22', fontsize=6.0, ha='center', va='center', fontweight='bold', zorder=7)

ax4.add_patch(Rectangle((1.0, -35.5), 36.0, 20.0, facecolor='#090d14', edgecolor='#a855f7', lw=1.4, zorder=5))
ax4.add_patch(Rectangle((3.0, -24.0), 32.0, 6.5, facecolor='#15803d', edgecolor='#86efac', lw=1.2, zorder=6))
ax4.text(19.0, -20.7, 'GREEN SCREAMER + NS-1 GATE PCB', color='#f0fdf4', fontsize=5.3, ha='center', va='center', fontweight='bold', zorder=7)
ax4.add_patch(Rectangle((3.0, -34.0), 32.0, 8.0, facecolor='#312e81', edgecolor='#c084fc', lw=1.2, zorder=6))
ax4.text(19.0, -30.0, 'NAM DSP + CAB IR + WI-FI / 5.8GHz', color='#f3e8ff', fontsize=5.3, ha='center', va='center', fontweight='bold', zorder=7)

ax4.add_patch(Rectangle((-36.0, -38.0), 72.0, 2.5, facecolor='#0f172a', edgecolor='#ef4444', lw=1.5, zorder=7))
ax4.text(0, -40.5, 'Flush Magnetic Quick-Swap Rear Access Cover (72 x 2.5 mm)', color='#fca5a5', fontsize=7.0, ha='center', fontweight='bold')

for s in range(6):
    sx = -24.0 + s * 9.6
    ax4.add_patch(Circle((sx, 5.5), 0.65 - s*0.06, facecolor='#4ade80', edgecolor='#fff', lw=0.5, zorder=9))

ax4.annotate('R6.0mm Rounded\nBullnose Edge', xy=(-40, -6), xytext=(-47, 7),
             arrowprops=dict(arrowstyle='->', color='#38bdf8', lw=1.2), color='#38bdf8', fontsize=7.2, fontweight='bold')
ax4.annotate('Side USB-C &\nVolume Wheel', xy=(41, -18), xytext=(32, 7),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=1.2), color='#fbbf24', fontsize=7.2, fontweight='bold')

plt.suptitle('6-STRING "CARBON SPINE" MASTER CNC BLUEPRINT — INTEGRATED BATTERIES, GREEN SCREAMER, NS-1 GATE, NAM & WIRELESS (1:1 MM SCALE)', color='#f8fafc', fontsize=13.5, fontweight='bold', y=0.98)
out1 = r'C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\guitar_6string_master_blueprint.png'
out2 = r'C:\work\guitarlane\images\02_cnc_specs_and_blueprints\01_master_1to1_mm_cnc_blueprint.png'
plt.savefig(out1, dpi=180, bbox_inches='tight')
plt.savefig(out2, dpi=180, bbox_inches='tight')
print('Saved clean 6-string guitar master blueprint')
