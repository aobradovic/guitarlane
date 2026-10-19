import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle, Arc

fig, axes = plt.subplots(1, 3, figsize=(22, 11), dpi=180)
fig.patch.set_facecolor('#0d1117')

# ==========================================
# PANEL 1: HUMAN BODY SCALE (Side & Back View of 30" / 760mm Bag on 5'10" / 1780mm Person)
# ==========================================
ax1 = axes[0]
ax1.set_facecolor('#111822')
ax1.set_xlim(-100, 900)
ax1.set_ylim(400, 1900)
ax1.set_aspect('equal')
ax1.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.8)
ax1.minorticks_on()
ax1.grid(True, which='minor', color='#151e2d', linestyle=':', linewidth=0.5)
ax1.tick_params(colors='#94a3b8', labelsize=8)
ax1.set_xlabel(' Dimension (mm)', color='#94a3b8', fontsize=9)
ax1.set_ylabel('Height from Floor (mm) [1780mm = 5 ft 10 in]', color='#94a3b8', fontsize=9)
for s in ax1.spines.values():
    s.set_color('#334155')
ax1.set_title('1. HUMAN SCALE: 30" (760mm) Bag on 5\'10" Person', color='#f8fafc', fontsize=12, fontweight='bold', pad=18)

# Draw Side Profile of 1780mm (5'10") Adult (x=220)
# Torso (hip at y=960, shoulder at y=1480, top of head at y=1780)
ax1.add_patch(FancyBboxPatch((170, 500), 95, 480, boxstyle='round,pad=0,rounding_size=25', facecolor='#1e293b', edgecolor='#64748b', lw=1.5)) # Legs
ax1.add_patch(FancyBboxPatch((155, 950), 135, 530, boxstyle='round,pad=0,rounding_size=35', facecolor='#334155', edgecolor='#94a3b8', lw=1.8)) # Torso
ax1.add_patch(Rectangle((195, 1480), 55, 65, facecolor='#334155', edgecolor='#94a3b8', lw=1.5)) # Neck
ax1.add_patch(Circle((225, 1645), 105, facecolor='#334155', edgecolor='#94a3b8', lw=1.8)) # Head (top at 1750)
ax1.text(222, 1220, '5\'10"\n(1780 mm)\nADULT\nTORSO', color='#cbd5e1', fontsize=8.5, ha='center', va='center', fontweight='bold')

# Draw 30" (760mm tall x 150mm thin) Bag on Back (hip belt at y=940 -> top at y=1700!)
# Notice: With a load-bearing hip belt (like an Arc'teryx/Osprey pack), the bottom sits at y=920 (tailbone/pelvis), so the top is at y=920+760 = 1680mm (BELOW the top of the head at 1780mm!)
bag_side_x = 0
bag_side_y = 920
ax1.add_patch(FancyBboxPatch((bag_side_x, bag_side_y), 150, 760, boxstyle='round,pad=0,rounding_size=18', facecolor='#0f172a', edgecolor='#38bdf8', lw=2.5, zorder=5))

# Internal Side Cross-Section inside the 150mm (5.9") depth!
# Rear 48mm: 18" Laptop (28mm) + 16" MBP (17mm) from y=935 to y=1335
ax1.add_patch(Rectangle((bag_side_x + 100, bag_side_y + 15), 26, 400, facecolor='#581c87', edgecolor='#c084fc', lw=1.2, zorder=6))
ax1.add_patch(Rectangle((bag_side_x + 78, bag_side_y + 15), 18, 356, facecolor='#3b0764', edgecolor='#e9d5ff', lw=1.2, zorder=6))
ax1.text(bag_side_x + 113, bag_side_y + 215, '18" + 16" Laptops\n(400mm tall, 45mm thick)', color='#e9d5ff', fontsize=6.5, ha='center', va='center', rotation=90, zorder=7)

# Front-left: 721mm Guitar Spine (38mm thick at bridge, 20mm thick at neck) running y=935 to y=1656
ax1.add_patch(Polygon([
    (bag_side_x + 15, bag_side_y + 15),
    (bag_side_x + 55, bag_side_y + 15),
    (bag_side_x + 55, bag_side_y + 230),
    (bag_side_x + 38, bag_side_y + 736),
    (bag_side_x + 15, bag_side_y + 736),
], closed=True, facecolor='#1e293b', edgecolor='#38bdf8', lw=1.2, zorder=6))
ax1.text(bag_side_x + 32, bag_side_y + 480, '721mm 1-Piece Guitar Spine', color='#38bdf8', fontsize=6.8, ha='center', va='center', rotation=90, fontweight='bold', zorder=7)

# Upper cavity ABOVE laptops (y=1430 to y=1640): Studio Headphones (95mm deep x 210mm tall)
ax1.add_patch(FancyBboxPatch((bag_side_x + 48, bag_side_y + 510), 92, 210, boxstyle='round,pad=0,rounding_size=10', facecolor='#052e16', edgecolor='#4ade80', lw=1.4, zorder=6))
ax1.text(bag_side_x + 94, bag_side_y + 615, 'Headphones\n(Above Laptops!)', color='#4ade80', fontsize=6.5, ha='center', va='center', rotation=90, fontweight='bold', zorder=7)

# Dimension callouts on Side View
ax1.annotate('', xy=(-35, bag_side_y), xytext=(-35, bag_side_y + 760), arrowprops=dict(arrowstyle='<->', color='#38bdf8', lw=1.8))
ax1.text(-55, bag_side_y + 380, '760 mm (30.0 in) Total Height\n(Sits from Pelvis to Back of Head)', color='#38bdf8', fontsize=8.5, ha='center', va='center', rotation=90, fontweight='bold')

ax1.annotate('', xy=(bag_side_x, bag_side_y - 30), xytext=(bag_side_x + 150, bag_side_y - 30), arrowprops=dict(arrowstyle='<->', color='#38bdf8', lw=1.8))
ax1.text(bag_side_x + 75, bag_side_y - 60, '150 mm\n(5.9 in Thin!)', color='#38bdf8', fontsize=8, ha='center', fontweight='bold')

# Draw Back View of Person Wearing the 340mm (13.4") Wide x 760mm (30") Tall Pack (x=460 to 840)
bx_center = 650
# Shoulders (460mm wide)
ax1.add_patch(FancyBboxPatch((bx_center - 225, 950), 450, 530, boxstyle='round,pad=0,rounding_size=45', facecolor='#334155', edgecolor='#94a3b8', lw=1.5))
ax1.add_patch(Circle((bx_center, 1645), 100, facecolor='#334155', edgecolor='#94a3b8', lw=1.5))
# 340mm x 760mm Pack on Back
ax1.add_patch(FancyBboxPatch((bx_center - 170, 920), 340, 760, boxstyle='round,pad=0,rounding_size=24', facecolor='#0f172a', edgecolor='#38bdf8', lw=2.2, zorder=5))
ax1.text(bx_center, 1300, 'BACK VIEW ON BODY\n340 mm (13.4") Wide\nx\n760 mm (30.0") Tall\n\nNarrower than\nadult shoulders\n(450 mm)!', color='#f8fafc', fontsize=8.5, ha='center', va='center', fontweight='bold', zorder=6)
ax1.plot([bx_center - 250, bx_center + 250], [1750, 1750], color='#f43f5e', linestyle='--', lw=1.2, zorder=7)
ax1.text(bx_center, 1775, 'Top of Head (1750-1780mm) — Bag Does NOT Stick Above Head!', color='#fb7185', fontsize=7.5, ha='center', fontweight='bold')


# ==========================================
# PANEL 2: EXACT INTERNAL FRONT ELEVATION OF THE 30" (760 x 340 x 150 mm) BAG
# ==========================================
ax2 = axes[1]
ax2.set_facecolor('#111822')
ax2.set_xlim(-60, 440)
ax2.set_ylim(-60, 840)
ax2.set_aspect('equal')
ax2.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.8)
ax2.minorticks_on()
ax2.grid(True, which='minor', color='#151e2d', linestyle=':', linewidth=0.5)
ax2.tick_params(colors='#94a3b8', labelsize=8)
ax2.set_xlabel('Width (mm)', color='#94a3b8', fontsize=9)
ax2.set_ylabel('Height (mm)', color='#94a3b8', fontsize=9)
for s in ax2.spines.values():
    s.set_color('#334155')
ax2.set_title('2. INSIDE THE 30" BAG (760 x 340 x 150 mm)', color='#f8fafc', fontsize=12, fontweight='bold', pad=18)

# Outer shell 340 x 760
ax2.add_patch(FancyBboxPatch((20, 0), 340, 760, boxstyle='round,pad=0,rounding_size=26', facecolor='#161f2c', edgecolor='#f8fafc', lw=2.5, zorder=1))

# Rear Laptop Compartment (Bottom 400mm)
ax2.add_patch(Rectangle((43, 18), 294, 400, facecolor='#2e1065', edgecolor='#a855f7', lw=2, linestyle='--', alpha=0.7, zorder=2))
ax2.text(190, 395, 'REAR SLEEVE: 18" LAPTOP (400 x 294 mm)', color='#e9d5ff', fontsize=8, ha='center', fontweight='bold', zorder=3)
ax2.add_patch(Rectangle((66, 18), 248, 356, facecolor='#3b0764', edgecolor='#c084fc', lw=1.5, linestyle=':', alpha=0.6, zorder=2))
ax2.text(190, 355, 'REAR SLEEVE: 16" MACBOOK PRO (356 x 248 mm)', color='#d8b4fe', fontsize=7.5, ha='center', zorder=3)

# Left Padded Channel: 721mm Guitar (6-str or 7-str)
# Total len = 721mm (y=18 to y=739)
gx = 76
gy = 18
y_top = gy + 721
y_nut = y_top - 18
y_24 = y_nut - 486
pts_body = [(gx-41, gy+15), (gx-35, gy), (gx+35, gy), (gx+41, gy+15), (gx+41, gy+90), (gx+28.5, y_24), (gx-28.5, y_24), (gx-41, gy+90)]
ax2.add_patch(Polygon(pts_body, closed=True, facecolor='#1e293b', edgecolor='#38bdf8', lw=1.8, zorder=5))
pts_neck = [(gx-28.5, y_24), (gx+28.5, y_24), (gx+21.5, y_top), (gx-21.5, y_top)]
ax2.add_patch(Polygon(pts_neck, closed=True, facecolor='#0f172a', edgecolor='#38bdf8', lw=1.8, zorder=5))
ax2.add_patch(Rectangle((gx-32, y_24-55), 64, 34, facecolor='#090d16', edgecolor='#f8fafc', lw=1, zorder=6))
ax2.add_patch(Rectangle((gx-32, gy+24), 64, 52, facecolor='#090d16', edgecolor='#38bdf8', lw=1.2, zorder=6))
ax2.text(gx, (y_24+y_top)/2, '1-PIECE 25.5" GUITAR SPINE\n721 mm (28.4") x 82 mm max', color='#38bdf8', fontsize=8, ha='center', va='center', rotation=90, fontweight='bold', zorder=7)

# Detached 3A + 3B Titanium Wings Slot (y=240 to y=460, x=116 to 152)
ax2.add_patch(FancyBboxPatch((114, 235), 38, 220, boxstyle='round,pad=0,rounding_size=6', facecolor='#334155', edgecolor='#cbd5e1', lw=1.5, zorder=5))
ax2.text(133, 345, 'Detached\n3A/3B Wings\n(220x38mm)', color='#f8fafc', fontsize=7, ha='center', va='center', rotation=90, fontweight='bold', zorder=6)

# Upper Right Zone (y=515 to y=735, ABOVE the laptops!): Studio Headphones
ax2.add_patch(FancyBboxPatch((140, 520), 200, 215, boxstyle='round,pad=0,rounding_size=14', facecolor='#052e16', edgecolor='#22c55e', lw=2, zorder=5))
ax2.add_patch(Circle((240, 627), 82, facecolor='none', edgecolor='#4ade80', lw=2, linestyle='--', zorder=6))
ax2.text(240, 627, 'STUDIO HEADPHONES\n210 x 185 x 95 mm\n(Zero overlap with laptops!)', color='#4ade80', fontsize=8, ha='center', va='center', fontweight='bold', zorder=7)

# Middle Right Zone (y=430 to y=508, ABOVE the laptops!): 3x SSD Hard Drives
for i in range(3):
    sx = 140 + i * 68
    ax2.add_patch(FancyBboxPatch((sx, 430), 62, 78, boxstyle='round,pad=0,rounding_size=5', facecolor='#451a03', edgecolor='#f59e0b', lw=1.6, zorder=5))
    ax2.text(sx + 31, 469, f'SSD #{i+1}\n110x60mm', color='#fbbf24', fontsize=7, ha='center', va='center', fontweight='bold', zorder=6)

# Lower Right Zone (y=25 to y=215, in front of lower laptop sleeve): Chargers + Cables
ax2.add_patch(FancyBboxPatch((160, 25), 180, 195, boxstyle='round,pad=0,rounding_size=10', facecolor='#0f172a', edgecolor='#94a3b8', lw=1.5, alpha=0.9, zorder=5))
ax2.text(250, 122, '330W Gaming Brick\n+ 140W MacBook Charger\n+ Audio Interface & Cables\n(180 x 195 mm)', color='#e2e8f0', fontsize=7.5, ha='center', va='center', fontweight='bold', zorder=6)


# ==========================================
# PANEL 3: REAL-WORLD COMMERCIAL 30-INCH (760mm) BACKPACK ARCHETYPES
# ==========================================
ax3 = axes[2]
ax3.set_facecolor('#111822')
ax3.set_xlim(0, 500)
ax3.set_ylim(-60, 840)
ax3.set_aspect('equal')
ax3.grid(True, which='major', color='#1e293b', linestyle='-', linewidth=0.8)
ax3.tick_params(colors='#94a3b8', labelsize=8)
ax3.set_xlabel('Width (mm)', color='#94a3b8', fontsize=9)
for s in ax3.spines.values():
    s.set_color('#334155')
ax3.set_title('3. REAL-WORLD 30" (760mm) BAG CATEGORIES', color='#f8fafc', fontsize=12, fontweight='bold', pad=18)

# Draw 3 silhouettes side by side at y=0 to 760
# 1. Alpine / Technical Monolith Pack (e.g. Arc'teryx Alpha AR 55 / Black Diamond Speed 50 - 760 x 340 x 150)
ax3.add_patch(FancyBboxPatch((25, 0), 130, 760, boxstyle='round,pad=0,rounding_size=20', facecolor='#1e293b', edgecolor='#38bdf8', lw=2))
ax3.text(90, 380, 'STYLE 1:\nALPINE / TECH\nMONOLITH\n(760 x 340 mm)\n\nLike Arc\'teryx\nAlpha / Peak\nDesign 65L,\nbut slimmed to\n150mm (5.9")\ndepth', color='#f8fafc', fontsize=7.5, ha='center', va='center', fontweight='bold')

# 2. Asymmetric Tapered "Teardrop / Scabbard" Pack (340mm wide at base for 18" laptop, tapering to 260mm at top)
pts_taper = [(185, 0), (315, 0), (315, 420), (285, 760), (185, 760)]
ax3.add_patch(Polygon(pts_taper, closed=True, facecolor='#1e293b', edgecolor='#22c55e', lw=2))
ax3.text(245, 380, 'STYLE 2:\nASYMMETRIC\nTAPERED PACK\n\n340mm wide at\nbottom (for 18"\nlaptop), tapers\nto 240mm at top\n(for guitar neck\n+ headphones)', color='#4ade80', fontsize=7.5, ha='center', va='center', fontweight='bold')

# 3. Roll-Top / Expandable Collar Pack (550mm in Laptop Mode -> Unrolls to 760mm in Guitar Mode!)
ax3.add_patch(FancyBboxPatch((345, 0), 130, 540, boxstyle='round,pad=0,rounding_size=15', facecolor='#1e293b', edgecolor='#f59e0b', lw=2))
ax3.add_patch(FancyBboxPatch((350, 540), 120, 220, boxstyle='round,pad=0,rounding_size=12', facecolor='#451a03', edgecolor='#fbbf24', lw=2, linestyle='--'))
ax3.text(410, 270, 'STYLE 3:\nCONVERTIBLE\nROLL-TOP\n\n21" (540mm)\nin daily Laptop\nMode', color='#f8fafc', fontsize=7.5, ha='center', va='center', fontweight='bold')
ax3.text(410, 650, 'Unrolls to\n30" (760mm)\nwhen carrying\nGuitar!', color='#fbbf24', fontsize=7.5, ha='center', va='center', fontweight='bold')

plt.suptitle('30-INCH (760 x 340 x 150 mm) SINGLE-BAG ENGINEERING — HUMAN SCALE, INTERNAL STACKING & 3 BAG STYLES', color='#f8fafc', fontsize=13.5, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(r'C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\bag_30_inch_engineering_scale.png', dpi=180)
print('Saved 30-inch bag CAD successfully')
