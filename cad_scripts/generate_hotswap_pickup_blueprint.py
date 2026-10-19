import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon
import numpy as np

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.0

fig = plt.figure(figsize=(22, 13.5), dpi=220)
fig.patch.set_facecolor('#090d14')

fig.suptitle(
    'TRUE 1:1 MILLIMETER ENGINEERING BLUEPRINT — STRINGS-ON SIDE-SLIDING HOT-SWAP PICKUP CARTRIDGE\n'
    '70.0 x 38.0 mm Pickup Longitudinal Along Strings (X) | Slides 75 mm Out the Left Wall (Z) Under 6 Tensioned Strings | 6-Pin Auto-ID Pogo Dock',
    color='#f8fafc', fontsize=14.5, fontweight='bold', y=0.975
)

gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.15], height_ratios=[1.05, 0.95],
                      left=0.04, right=0.97, top=0.90, bottom=0.05, wspace=0.14, hspace=0.22)

def style_ax(ax, title):
    ax.set_facecolor('#0d131d')
    ax.set_title(title, color='#38bdf8', fontsize=11.5, fontweight='bold', pad=10)
    ax.tick_params(colors='#94a3b8', labelsize=8.5)
    ax.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.6)
    ax.grid(True, which='minor', color='#131c2a', linestyle=':', linewidth=0.4)
    ax.minorticks_on()
    ax.set_xlabel('X — Across Spine Width (mm) [Left = -41 mm, Right = +41 mm]', color='#cbd5e1', fontsize=9)

# ==============================================================================
# PANEL 1: TOP VIEW (X-Y) — PICKUP SLIDING OUT TO THE LEFT UNDER 6 STRINGS
# ==============================================================================
ax1 = fig.add_subplot(gs[0, 0])
style_ax(ax1, '1. TOP VIEW (X-Y) — PICKUP CARTRIDGE SLIDING OUT LEFT WALL UNDER TENSIONED STRINGS')
ax1.set_ylabel('Y — Along Spine Length from Tail (mm)', color='#cbd5e1', fontsize=9)
ax1.set_aspect('equal')
ax1.set_xlim(-125, 62)
ax1.set_ylim(95, 235)

# Draw 82mm Spine Body (X = -41 to +41)
spine_rect = FancyBboxPatch((-41, 100), 82, 130, boxstyle="round,pad=0,rounding_size=6",
                            facecolor='#161c26', edgecolor='#64748b', linewidth=1.8, zorder=2)
ax1.add_patch(spine_rect)

# Draw Side-Entry Dovetail Pocket inside Spine (X = -41 to +36.5, Y = 141.5 to 182.5 -> 41mm wide slot)
pocket_rect = FancyBboxPatch((-41, 141.5), 77.5, 41.0, boxstyle="round,pad=0,rounding_size=3",
                             facecolor='#090d14', edgecolor='#38bdf8', linewidth=1.4, linestyle='--', zorder=3)
ax1.add_patch(pocket_rect)

# Draw the 6 Gold Pogo Pins in the floor of the pocket at X = +33.5 mm (Right internal wall)
for i, py in enumerate(np.linspace(149, 175, 6)):
    ax1.add_patch(Circle((33.5, py), 1.4, facecolor='#fbbf24', edgecolor='#f59e0b', lw=0.8, zorder=5))
ax1.text(33.5, 185.5, '6-Pin Gold\nPogo Block\n(X=+33.5mm)', color='#fbbf24', fontsize=7.5, fontweight='bold', ha='center', zorder=10)

# Draw 4x N52 Neodymium Locking Magnets in Pocket Floor
for (mx, my) in [(-32, 144.5), (-32, 179.5), (28, 144.5), (28, 179.5)]:
    ax1.add_patch(Circle((mx, my), 2.2, facecolor='#94a3b8', edgecolor='#e2e8f0', lw=0.8, zorder=4))

# Draw Pickup Cartridge SLID HALFWAY OUT TO THE LEFT (shifted by dX = -65 mm so user sees it sliding out!)
dx_slide = -65.0
sled_rect = FancyBboxPatch((-36.5 + dx_slide, 142.0), 73.0, 40.0, boxstyle="round,pad=0,rounding_size=4",
                           facecolor='#262f3d', edgecolor='#f59e0b', linewidth=1.8, zorder=6)
ax1.add_patch(sled_rect)

# Draw 70 x 38 mm Humbucker Pickup mounted ON the Sled (Long 70mm axis across X!)
pu_rect = FancyBboxPatch((-35.0 + dx_slide, 143.0), 70.0, 38.0, boxstyle="round,pad=0,rounding_size=4.5",
                         facecolor='#11151c', edgecolor='#cbd5e1', linewidth=1.4, zorder=7)
ax1.add_patch(pu_rect)

# Draw 2 Bobbins & 12 Pole Pieces (6 per coil, spaced 10.2mm across X!)
for cy in [153.5, 170.5]:
    bobbin = FancyBboxPatch((-32.0 + dx_slide, cy - 6.8), 64.0, 13.6, boxstyle="round,pad=0,rounding_size=3.5",
                            facecolor='#1a202c', edgecolor='#475569', lw=0.9, zorder=8)
    ax1.add_patch(bobbin)
    for s in range(6):
        px = -25.5 + s * 10.2 + dx_slide
        ax1.add_patch(Circle((px, cy), 2.1, facecolor='#d4af37', edgecolor='#fef08a', lw=0.7, zorder=9))

# Draw 6 Gold Mating Pads on the Right Edge of the Sled
for py in np.linspace(149, 175, 6):
    ax1.add_patch(Rectangle((34.2 + dx_slide, py - 1.2), 2.2, 2.4, facecolor='#fbbf24', zorder=8))

# Draw ghost outline of Pickup when 100% LOCKED in center (X = -35 to +35)
ghost_pu = FancyBboxPatch((-35.0, 143.0), 70.0, 38.0, boxstyle="round,pad=0,rounding_size=4.5",
                          facecolor='none', edgecolor='#22d3ee', linewidth=1.2, linestyle=':', zorder=5)
ax1.add_patch(ghost_pu)
ax1.text(0, 162, 'LOCKED POSITION\n(Centered Under 6 Strings\nX = -35 to +35 mm)', color='#22d3ee', fontsize=8, ha='center', va='center', fontweight='bold', zorder=9)

# Draw 6 Guitar Strings running vertically along Y (at X = -25.5 to +25.5 mm) OVER the pocket!
for s in range(6):
    sx = -25.5 + s * 10.2
    ax1.plot([sx, sx], [95, 235], color='#e2e8f0', lw=1.8 - s*0.18, zorder=12)
ax1.text(0, 224, '6 Tensioned Strings Stay 100% On (X = -25.5 to +25.5 mm)', color='#f8fafc', fontsize=8.5, fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='#0f172a', edgecolor='#475569'))

# Big Slide Arrow showing horizontal extraction to the Left (-X)
ax1.annotate('', xy=(-108, 162), xytext=(-36, 162),
             arrowprops=dict(arrowstyle='<->', color='#f59e0b', lw=2.5))
ax1.text(-72, 134, 'SLIDES STRAIGHT OUT LEFT WALL (73 x 40 mm Sled)\nZero String Detuning Required!',
         color='#fbbf24', fontsize=8.5, fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#18181b', edgecolor='#f59e0b'))

# Side controls on Right Wall (X = +41 mm)
ax1.add_patch(Rectangle((39.5, 192), 3.5, 18, facecolor='#38bdf8', zorder=10))
ax1.text(44, 201, 'Vol / Push\nBypass', color='#38bdf8', fontsize=7.5, va='center', fontweight='bold')

# ==============================================================================
# PANEL 2: FRONT ELEVATION CROSS-SECTION (X-Z AT Y=162mm) — CLEARANCE UNDER STRINGS
# ==============================================================================
ax2 = fig.add_subplot(gs[0, 1])
style_ax(ax2, '2. CROSS-SECTION AT PICKUP BAY (Y = 162 mm) — 2.8 mm CLEARANCE UNDER TENSIONED STRINGS')
ax2.set_ylabel('Z — Vertical Thickness (mm) [Top=0, Back=-38mm]', color='#cbd5e1', fontsize=9)
ax2.set_aspect('equal')
ax2.set_xlim(-68, 52)
ax2.set_ylim(-44, 18)

# Main 82 x 38 mm CNC 7075 Spine Cross-Section (X = -41 to +41, Z = -38 to 0)
# Notice the Left Wall (X = -41) is OPEN from Z = -16.5 to 0 so the cartridge slides out the left side!
spine_poly = [
    (-41, -16.5), (36.5, -16.5), (36.5, 0), (41, 0),
    (41, -38), (-41, -38)
]
ax2.add_patch(Polygon(spine_poly, closed=True, facecolor='#1e293b', edgecolor='#94a3b8', lw=1.8, zorder=2))

# Solid 2.5mm CNC Aluminum EMI Shield Bulkhead (Z = -16.5 to -19.0 mm)
ax2.add_patch(Rectangle((-41, -19.0), 82, 2.5, facecolor='#334155', edgecolor='#cbd5e1', lw=1.2, zorder=3))
ax2.text(0, -17.75, '2.5 mm SOLID CNC ALUMINUM EMI SHIELD BULKHEAD (Z = -16.5 to -19.0 mm)',
         color='#f8fafc', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=6)

# Dovetail Guide Rails at Z = -16.5 to -13.5 mm
ax2.add_patch(Rectangle((-36.5, -16.5), 71.0, 2.5, facecolor='#475569', edgecolor='#f59e0b', lw=1.2, zorder=4))
ax2.text(0, -15.2, 'CNC Dovetail Carrier Sled (73 x 40 x 2.5 mm) + 4x N52 Magnets',
         color='#fde047', fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=6)

# Pickup Body sitting on Carrier Sled (X = -35 to +35 mm, Z = -14.0 to -1.5 mm)
ax2.add_patch(FancyBboxPatch((-35.0, -14.0), 70.0, 12.5, boxstyle="round,pad=0,rounding_size=2.0",
                             facecolor='#0f172a', edgecolor='#38bdf8', lw=1.6, zorder=5))
ax2.text(0, -7.8, '70.0 x 38.0 x 12.5 mm PICKUP MODULE\n(EMG 81/57 | Fishman Fluence | Bare Knuckle / Lundgren)',
         color='#38bdf8', fontsize=8.5, fontweight='bold', ha='center', va='center', zorder=7)

# 6 Pole Pieces on top of Pickup (Z = -1.5 to -0.8 mm) and 6 Strings at Z = +2.0 mm!
for s in range(6):
    sx = -25.5 + s * 10.2
    ax2.add_patch(Rectangle((sx - 1.8, -1.5), 3.6, 0.8, facecolor='#d4af37', zorder=6))
    ax2.add_patch(Circle((sx, 2.0), 0.75, facecolor='#f8fafc', edgecolor='#38bdf8', lw=1.0, zorder=10))

# Highlight the 2.8 mm Vertical Clearance Gap between Pickup Top (Z=-0.8mm) and Strings (Z=+2.0mm)
ax2.plot([-44, 44], [2.0, 2.0], color='#22d3ee', ls='--', lw=0.9, zorder=8)
ax2.plot([-44, 44], [-0.8, -0.8], color='#f59e0b', ls='--', lw=0.9, zorder=8)
ax2.text(0, 7.5, '6 Tensioned Strings at Z = +2.0 mm -> 2.8 mm Vertical Clearance Over Pickup!\nCartridge Slides Straight Out Left Side (-X) Under the Strings!',
         color='#22d3ee', fontsize=8.5, fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#090d14', edgecolor='#22d3ee'))

# Spring-loaded 6-Pin Gold Pogo Block at Right Wall of Cavity (X = +34.5 to +36.5 mm)
ax2.add_patch(Rectangle((34.0, -16.0), 2.8, 6.0, facecolor='#fbbf24', edgecolor='#f59e0b', lw=1.0, zorder=7))
ax2.text(44, -11.0, '6-Pin Gold\nPogo Dock', color='#fbbf24', fontsize=7.5, fontweight='bold', ha='center')

# Slide-Out Arrow to the Left (-X)
ax2.annotate('', xy=(-65, -8.5), xytext=(-36, -8.5),
             arrowprops=dict(arrowstyle='->', color='#f59e0b', lw=3.0))
ax2.text(-52, -3.0, 'SLIDES OUT\nLEFT SIDE', color='#fbbf24', fontsize=8.5, fontweight='bold', ha='center')

# Lower Rear Bay (Z = -19.0 to -35.5 mm): 2x 18650 Cells + Green Screamer/NS-1 + NAM Engine
ax2.add_patch(Circle((-23, -27.2), 8.2, facecolor='#16a34a', edgecolor='#86efac', lw=1.3, zorder=5))
ax2.add_patch(Circle((-4.5, -27.2), 8.2, facecolor='#16a34a', edgecolor='#86efac', lw=1.3, zorder=5))
ax2.text(-13.7, -27.2, '2x 18650\n(7000 mAh)', color='#fff', fontsize=7, fontweight='bold', ha='center', va='center', zorder=7)

ax2.add_patch(Rectangle((7, -25.5), 27, 4.2, facecolor='#15803d', edgecolor='#4ade80', lw=1.0, zorder=5))
ax2.text(20.5, -23.4, 'Screamer+NS-1+0V Relay', color='#fff', fontsize=6.2, fontweight='bold', ha='center', va='center', zorder=7)

ax2.add_patch(Rectangle((7, -33.5), 27, 5.0, facecolor='#6b21a8', edgecolor='#c084fc', lw=1.0, zorder=5))
ax2.text(20.5, -31.0, 'NAM + Cab IR + WiFi', color='#fff', fontsize=6.5, fontweight='bold', ha='center', va='center', zorder=7)

# Magnetic Rear Carbon Cover (Z = -35.5 to -38.0 mm)
ax2.add_patch(Rectangle((-34, -38.0), 68, 2.5, facecolor='#0f172a', edgecolor='#38bdf8', lw=1.2, zorder=6))
ax2.text(0, -41.5, '2.5 mm Flush Magnetic Carbon Rear Hatch (Tool-Free Access to 18650s & Analog Drive Cards)',
         color='#94a3b8', fontsize=8, fontweight='bold', ha='center')

# ==============================================================================
# PANEL 3: UNIVERSAL CARTRIDGE SLED — HOW SOAPBAR VS. PASSIVE HUMBUCKER FIT
# ==============================================================================
ax3 = fig.add_subplot(gs[1, 0])
style_ax(ax3, '3. ONE UNIVERSAL 73x40mm SLED FITS BOTH ACTIVE SOAPBARS (EMG/FISHMAN) & PASSIVE HUMBUCKERS (BKP)')
ax3.set_ylabel('Y — Cartridge Width (mm)', color='#cbd5e1', fontsize=9)
ax3.set_aspect('equal')
ax3.set_xlim(-82, 82)
ax3.set_ylim(-32, 34)
ax3.set_xlabel('Left: Type A Active Soapbar Sled (70x38mm)   |   Right: Type B Open-Coil Passive Humbucker Sled (68.5x37mm + Trim Bezel)', color='#cbd5e1', fontsize=9)

# LEFT HALF: Sled A (EMG / Fishman 70x38mm Soapbar) centered at X = -41
ax3.add_patch(FancyBboxPatch((-41 - 36.5, -20.0), 73.0, 40.0, boxstyle="round,pad=0,rounding_size=4",
                             facecolor='#1e293b', edgecolor='#38bdf8', lw=1.6))
ax3.add_patch(FancyBboxPatch((-41 - 35.0, -19.0), 70.0, 38.0, boxstyle="round,pad=0,rounding_size=4.5",
                             facecolor='#11151c', edgecolor='#94a3b8', lw=1.5))
ax3.plot([-41 - 28, -41 + 28], [8.5, 8.5], color='#64748b', lw=3.0)
ax3.plot([-41 - 28, -41 + 28], [-8.5, -8.5], color='#64748b', lw=3.0)
ax3.text(-41, 0, 'ACTIVE SOAPBAR (70.0 x 38.0 mm)\nEMG 81 / 85 / 57 / 60\nFishman Fluence Modern / Abasi',
         color='#38bdf8', fontsize=8, fontweight='bold', ha='center', va='center')
ax3.text(-41, -26.5, 'Plugs into Sled via Factory 3-Pin Header | Pin 6 = 10k/22k (Auto 25kOhm + 9V/18V)',
         color='#cbd5e1', fontsize=7.5, ha='center', fontweight='bold')

# 6 Gold Contacts on Right Edge of Sled A
for py in np.linspace(-13, 13, 6):
    ax3.add_patch(Rectangle((-41 + 34.5, py - 1.2), 2.0, 2.4, facecolor='#fbbf24'))

# RIGHT HALF: Sled B (Bare Knuckle / Lundgren / Seymour Duncan 68.5x37mm Open-Coil + Adapter Bezel) centered at X = +41
ax3.add_patch(FancyBboxPatch((41 - 36.5, -20.0), 73.0, 40.0, boxstyle="round,pad=0,rounding_size=4",
                             facecolor='#1e293b', edgecolor='#f59e0b', lw=1.6))
# CNC Adapter Trim Ring (70 x 38 mm outer, 68.5 x 37 mm inner)
ax3.add_patch(FancyBboxPatch((41 - 35.0, -19.0), 70.0, 38.0, boxstyle="round,pad=0,rounding_size=4.5",
                             facecolor='#334155', edgecolor='#f59e0b', lw=1.2))
# Open-Coil Bobbins inside Trim Ring
for cy in [-9.0, 9.0]:
    ax3.add_patch(FancyBboxPatch((41 - 32.0, cy - 7.2), 64.0, 14.4, boxstyle="round,pad=0,rounding_size=4",
                                 facecolor='#090d14', edgecolor='#64748b', lw=1.0))
    for s in range(6):
        px = 41 - 25.5 + s * 10.2
        ax3.add_patch(Circle((px, cy), 2.2, facecolor='#d4af37', edgecolor='#fef08a', lw=0.7))
ax3.text(41, 0, 'PASSIVE HUMBUCKER (68.5 x 37.0 mm)\nBare Knuckle / Lundgren M6 / SD',
         color='#fde047', fontsize=7.8, fontweight='bold', ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.18', facecolor='#0f172a', edgecolor='#f59e0b', alpha=0.92))
ax3.text(41, -26.5, 'CNC Bezel Hides Mounting Ears | Pin 6 = Open (Auto 500kOhm + 0.0V Zero-Battery Relay)',
         color='#cbd5e1', fontsize=7.5, ha='center', fontweight='bold')

for py in np.linspace(-13, 13, 6):
    ax3.add_patch(Rectangle((41 + 34.5, py - 1.2), 2.0, 2.4, facecolor='#fbbf24'))

# ==============================================================================
# PANEL 4: 6-PIN GOLD POGO AUTO-IMPEDANCE & VOLTAGE SWITCHING SCHEMATIC
# ==============================================================================
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor('#0d131d')
ax4.set_title('4. AUTOMATIC 6-PIN POGO-PIN IMPEDANCE & POWER MATRIX (25kOhm+9V/18V ACTIVE vs. 500kOhm+0V PASSIVE)',
              color='#38bdf8', fontsize=11.0, fontweight='bold', pad=10)
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 100)
ax4.axis('off')

# Draw Table / Schematic Blocks inside Panel 4
boxes = [
    (3, 66, 94, 28, '#111c2d', '#38bdf8',
     'PIN 6 AUTO-SENSE ID RESISTOR -> AUTOMATICALLY CONFIGURES THE GUITAR WHEN CARTRIDGE CLICKS IN:\n'
     '• Pin 1: Pickup Hot Output     • Pin 2: Star Ground / Shield     • Pin 3: Voice 2 / Coil-Split\n'
     '• Pin 4: Voice 3 / High-Tilt   • Pin 5: Isolated +9V / +18V Rail • Pin 6: Sense ID Resistor (ID_R to GND)'),
    (3, 35, 45, 27, '#14261c', '#22c55e',
     'WHEN PASSIVE SLED IS INSERTED (Bare Knuckle / Lundgren / SD):\n'
     '• Pin 6 Sense = OPEN (∞ Ohm)\n'
     '• Power Rail (Pin 5) = 0.0V HARD-OFF (Zero Noise)\n'
     '• Load = 500 kOhm Passive Pot + Omron G6K 0.0V Relay\n'
     '• Works 100% WITHOUT BATTERIES or Feeds 1MOhm JFET Buffer'),
    (52, 35, 45, 27, '#231829', '#c084fc',
     'WHEN ACTIVE SLED IS INSERTED (EMG 81/57 or Fishman Fluence):\n'
     '• Pin 6 Sense = 10 kOhm (EMG) or 22 kOhm (Fishman Fluence)\n'
     '• Power Rail (Pin 5) = Ultraclean +9V LDO (or +18V EMG Mode!)\n'
     '• Load = Switched to 25 kOhm Active Load via TI TS5A3159A\n'
     '• Pins 3 & 4 Auto-Map to Fishman Voice 1 / Voice 2 / Voice 3'),
    (3, 4, 94, 27, '#1e1b18', '#f59e0b',
     'WHY THIS BEATS EVERY TRADITIONAL GUITAR:\n'
     '1. Swap pickups in 3 seconds from the left side with strings at 100% full pitch (2.8 mm clearance under strings).\n'
     '2. Both 70x38mm Soapbars (EMG/Fishman) and 68.5x37mm Open-Coil Humbuckers (Bare Knuckle/Lundgren) fit the same slot.\n'
     '3. Zero soldering: EMG/Fishman plug into the sled via stock 3-pin cable; passive pickups clamp into a 4-pin Wago block.')
]

for (bx, by, bw, bh, fc, ec, txt) in boxes:
    ax4.add_patch(FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0,rounding_size=2.5",
                                 facecolor=fc, edgecolor=ec, lw=1.5))
    ax4.text(bx + 2.5, by + bh/2, txt, color='#f8fafc', fontsize=8.3, va='center', ha='left', linespacing=1.42, fontweight='bold')

out_repo = r'C:\work\guitarlane\images\02_cnc_specs_and_blueprints\09_3second_strings_on_hotswap_pickup_cartridge_system.png'
out_art = r'C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\Guitar_Gallery\05d_True_1to1_HotSwap_Pickup_Cartridge_Engineering_Blueprint.png'
plt.savefig(out_repo, dpi=220, facecolor=fig.get_facecolor())
plt.savefig(out_art, dpi=220, facecolor=fig.get_facecolor())
print("Saved exact 1:1 hot-swap engineering blueprint successfully.")
