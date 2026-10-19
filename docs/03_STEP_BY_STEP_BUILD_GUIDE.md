# Step-by-Step Build & Execution Guide: 6-String "Carbon Spine" Guitar (Method 2 — Turnkey 5-Axis CNC)

This guide walks you step-by-step from ordering parts to holding the finished, playable **6-String "Carbon Spine" Prototype** (`721 mm / 28.38"` total length, `82 mm / 3.23"` bare spine width, smooth `R6–R8 mm` rounded bullnose & beveled edges) with **zero carbon layup molds, zero hand-sanding, and ~90 minutes of hands-on assembly**.

---

## Phase 1: Order the Off-The-Shelf Hardware & Reinforcement Parts First (Days 1–3)

> [!IMPORTANT]
> **Always order your hardware before sending files to the CNC machine shop.** Having the physical Hipshot bridge, Fishman pickup, truss rod, and carbon spars on your desk lets you verify the exact millimeter dimensions with a $20 digital caliper before the CNC shop cuts metal.

### 1.1 Hardware & Materials Shopping Checklist (6-String Prototype)

| Step | Component | Exact Model / Part Number | Qty | Est. Cost | Direct Supplier Link |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | **Headless Floating Tremolo + CNC Headpiece** | **Hipshot** 6-String Headless Tremolo (`4HV060B`, Black, `10.5 mm` pitch) + **LowPro CNC 6-String Headpiece** (`43 mm` width) | 1 set | $345 | https://hipshotproducts.com/collections/guitar-headless |
| **2** | **Bridge Humbucker (100% Zero-Battery Compatible)** | **Lundgren M6** / **Bare Knuckle Ragnarok** / **Seymour Duncan Black Winter** Passive Ceramic Soapbar (`70 × 38 mm`, 4-conductor) — works **100% passively with zero batteries**, or feeds the onboard active DSP rig | 1 set | $149–$199 | https://www.sweetwater.com/store/detail/BlkWint6Brg--seymour-duncan-black-winter-bridge-humbucker-pickup-black |
| **3** | **Side Controls, Zero-Battery Relay & Locking Jack** | **Neutrik** `NJ3FP6C-BAG` TRS Locking Jack + **Bourns** `500kΩ/10kΩ` Dual-Gang Push-Push Volume Wheel + **Omron `G6K-2F-Y`** Normally-Closed `0.0V` True-Bypass Relay + **Taiway** 3-Way Mini Toggle + Waterproof **USB-C** Port | 1 set | $38 | https://www.mouser.com/ProductDetail/Omron-Electronics/G6K-2F-Y-DC5 |
| **4** | **Dual-Action Spoke-Wheel Truss Rod** | **StewMac Hot Rod** Low-Profile Dual-Action Spoke-Wheel Truss Rod (`440 mm / 17.3"` length, `6.0 × 9.5 mm` channel) | 1 pc | $26 | https://www.stewmac.com/luthier-tools-and-supplies/supplies/truss-rods/stewmac-hot-rod-low-profile-truss-rods/ |
| **5** | **Internal Carbon Fiber Neck Spars** | **Rock West Composites / DragonPlate** Pultruded Unidirectional Carbon Bar (`4.0 mm × 10.0 mm × 600 mm` / `0.157" × 0.393"`) | 2 pcs | $28 | https://www.rockwestcomposites.com/browse/rectangular-bar-strips |
| **6** | **Fretboard Blank & Stainless Jumbo Frets** | **Richlite Black Diamond** Fingerboard Blank (`6.0 × 70 × 520 mm`) + **Jescar** `FW57110-S` Stainless Steel Jumbo Fretwire (24+1 pre-radiused `16"` lengths) | 1 set | $58 | https://www.stewmac.com/tonewoods/electric-guitar-bodies-and-necks-and-wood/electric-guitar-fingerboards/richlite-fingerboard-blank/ |
| **7** | **Glowing Side Dots** | **Luminlay** `SGY-25` or `SGB-25` Super-Luminova Side Dot Rod (`2.5 mm` diameter, Cyan/Green glow) | 1 rod | $16 | https://www.luminlay.com/productsens.html |
| **8** | **Quick-Release Wing Pins (For 3A & 3B)** | **McMaster-Carr / Ganter GN 817.6** M6 Captive Quarter-Turn Retractable Indexing Plunger (`6 mm` hardened pin, red anodized knob) | 2 pcs | $32 | https://www.mcmaster.com/spring-plungers/retractable-spring-plungers/ |
| **9** | **Strap Lock Button & Warm Leg Grip Strip** | **Schaller S-Locks** (Black/Ruthenium, 1 pair) + **McMaster-Carr** `2.0 mm` Black Adhesive-Backed Santoprene Rubber Strip (`60A` durometer) | 1 set | $34 | https://www.mcmaster.com/santoprene-rubber/ |
| **10** | **Aerospace Structural Epoxy** | **3M Scotch-Weld DP420 Black** Two-Part Toughened Structural Epoxy (`50 mL` cartridge + mixing nozzle) | 1 tube | $36 | https://www.mcmaster.com/epoxy-adhesives/3m-structural-adhesives/ |
| **11** | **Onboard Active Rig + Dual-18650 Battery System** *(Optional Drop-In Module — see [`docs/05_ONBOARD_NAM_SCREAMER_WIRELESS_SPEC.md`](05_ONBOARD_NAM_SCREAMER_WIRELESS_SPEC.md))* | **Keystone `1048`** Dual-`18650` Holder + **2x Samsung `35E` (`7,000 mAh`)** Cells + **TI `BQ25895` / `TPS2121`** USB-C/TRS Power Mux + **Analog SMD Green Screamer + `THAT2181C` NS-1 Gate PCB** + **Radxa Zero 3W / Daisy Seed NAM Module** + **`5.8 GHz` ULL Wireless TX** | 1 kit | $139 | See [`docs/05_ONBOARD_NAM_SCREAMER_WIRELESS_SPEC.md`](05_ONBOARD_NAM_SCREAMER_WIRELESS_SPEC.md) |

---

## Phase 2: Verify Measurements & Export the 5 CNC `.STEP` Files (Days 8–10)

Once the parts above arrive, take 15 minutes with digital calipers to confirm 4 critical dimensions in your 3D CAD file (Fusion 360 / SolidWorks / FreeCAD / Onshape) before exporting the `.STEP` (`AP214`) files:

1. **Truss Rod Slot (`6.15 mm` wide × `9.65 mm` deep × `442 mm` long):** Adds `+0.15 mm` clearance around your `6.0 × 9.5 mm` spoke-wheel truss rod so it drops in effortlessly without binding.
2. **Carbon Spar Slots (Two slots, each `4.10 mm` wide × `10.10 mm` deep × `560 mm` long):** Centered at `X = ±8.5 mm` on either side of the truss rod. The `+0.10 mm` (`0.004"`) clearance leaves the ideal `0.05 mm` bondline for 3M DP420 epoxy.
3. **Pickup, Bridge & Rear Electronics/Battery Bay Cavities (`38.0 mm` Lower Spine Depth):**
   * **Top Soapbar Pickup Route:** `70.6 mm × 38.6 mm × 14.0 mm` deep (`R5.0 mm` corner radii), centered at `Y = 162 mm` from the tail, leaving a solid **`2.5 mm` CNC aluminum EMI shield bulkhead** between the pickup and the rear electronics bay.
   * **Rear Electronics + Dual-`18650` Battery Bay (`Y = 128 mm` to `Y = 235 mm` on the back of the spine):** `66.0 mm` wide × `107.0 mm` long × **`20.0 mm` deep**, split into:
     - **Left Bay (`39 × 72 × 20 mm`):** Holds the **Keystone `1048` Dual-`18650` battery cradle** (`7,000 mAh` total, tool-free pop-in/out).
     - **Right/Lower Bay (`62 × 55 × 20 mm`):** Holds the stacked **Analog Green Screamer + NS-1 Sidechain Gate PCB** (`52 × 34 mm`) and **NAM Neural Amp + Cab IR + Wi-Fi 6 + 5.8 GHz Wireless Module** (`65 × 30 mm`), plus a `2.5 mm` stepped magnetic recess for the flush carbon rear access hatch (`6x N52` magnets).
   * **Hipshot Tremolo Route:** Verify the top baseplate recess (`66.5 × 56.5 mm`), the through-block slot (`45 × 18 mm`), and the rear 3-spring cavity (`48 × 72 × 22 mm` deep at `Y = 30–118 mm`).
4. **Smooth Rounded & Beveled Outer Edges (No Pointy Corners):**
   * Apply a **`35° × 8.0 mm` forearm comfort bevel** on the right-side top transition of the `82 mm` spine (`Y = 140 mm` to `Y = 250 mm`).
   * Apply a continuous **`R6.0 mm` (`1/4"`) bullnose fillet** around the entire outer perimeter of the `82 mm` spine and a **`R8.0 mm` full bullnose roundover** on the **3A Upper Horn** and **3B Lower Leg Rail**.
   * Add **`4.0 mm` steel dowel pin alignment holes** (2 holes in the neck core matching 2 blind holes in the underside of the Richlite fretboard) so the fretboard self-aligns to within `±0.02 mm` when glued.

### Export 6 Separate `.STEP` Files for Quoting:
* `Part_01_Spine_Core_7075_or_6061.step` — Full `703 mm × 82 mm × 38 mm` hollow-lattice spine core with rear battery/DSP bay
* `Part_02_Top_Skin_3mm_Carbon.step` — `3.0 mm` flat carbon fiber top plate (`195 × 78 mm`) with pickup & bridge cutouts
* `Part_03_Neck_Back_Shell_Carbon.step` — `2.2 mm` contoured warm-touch carbon/G10 neck back shell (`486 mm` long)
* `Part_04_Rear_Tuner_UGuard_Ti_or_7075.step` — `82 × 42 × 23 mm` rounded rear U-guard (`R14 mm` outer corners)
* `Part_05_Wings_3A_and_3B.step` — Smooth teardrop **3A Upper Horn** + curved **3B Lower Leg Rail**
* `Part_06_Rear_Magnetic_Battery_DSP_Cover_Carbon.step` — `2.5 mm` flush CNC carbon rear hatch (`109 × 68 mm`) for instant tool-free access to the `2x 18650` batteries and electronics

---

## Phase 3: Upload to Turnkey CNC Factories & Order (Days 11–25)

You will upload your `.STEP` files to **one CNC metal/carbon portal** and (optionally) **one luthier CNC fretboard shop** so the parts arrive ready to bolt/glue together.

### 3.1 Where to Upload the Metal & Carbon Parts (`Part_01` through `Part_06`)
* **Recommended Instant-Quote Portals:**
  1. **RapidDirect** (https://www.rapiddirect.com/) — Best pricing for `700 mm+` 5-axis CNC aluminum, titanium, and carbon fiber plate; upload `.STEP` files directly for instant DFM check.
  2. **JLCCNC** (https://jlccnc.com/) — Lowest cost for 1-off CNC 6061/7075 prototypes with matte black anodizing.
  3. **PCBWay CNC** (https://www.pcbway.com/rapid-prototyping/manufacture/) — Offers both 5-axis CNC 7075-T6, Grade-5 Titanium (`TC4`), CNC-machined 3K matte carbon fiber sheet, and turnkey SMD PCB assembly (`PCBA`) for the onboard Green Screamer + NS-1 Gate board under one roof.

### 3.2 Copy-Paste Manufacturing Spec Notes for Your CNC Quote
When uploading `Part_01` through `Part_06`, paste these exact notes into the **"Special Instructions / Engineering Notes"** box:

```text
1. GENERAL TOLERANCES: ISO 2768-f (Fine), ±0.05 mm on all mating dovetail slots, dowel pin holes, and neck reinforcement channels.
2. EDGE ROUNDING: Machine all 3D perimeter bullnose fillets (R6.0 mm to R14.0 mm) and 35-degree comfort bevels with ball-nose finishing stepover <= 0.15 mm so zero manual sanding is required.
3. SURFACE FINISH (Part_01 Spine Core): Fine glass-bead blast (Ra 1.6 um) followed by Matte Black Type III Hard Anodize (or Cerakote H-146 Graphite Black on neck back area). Leave the 25x25 mm thermal pad boss inside the rear DSP bay bare/anodized flat for thermal interface pad contact.
4. SURFACE FINISH (Part_04 U-Guard & Part_05 3A/3B Wings): Fine glass-bead blast (Ra 1.6 um) clear satin finish on Grade-5 Titanium (Ti-6Al-4V) or Matte Titanium-Grey Anodized 7075-T6.
5. THREAD TAPPING: Pre-tap all M3, M4, and M6 holes per CAD thread callouts prior to anodizing.
```

### 3.3 Getting the Richlite Fretboard Pre-Slotted, Pre-Radiused & Rolled
If you do not want to slot or radius the fretboard yourself, send your Richlite blank (or order turnkey) from a luthier CNC shop such as **CNCCraft** (https://www.cnccraft.co.uk/) or a local CNC luthier service with these specs:
* **Scale Length:** `25.5"` (`647.7 mm`) with **Zero-Fret** slot at `0.00 mm` + **24 Fret Slots** (`0.58 mm / 0.023"` slot width × `1.8 mm` depth).
* **Radius & Edges:** `16"` (`406.4 mm`) fretboard radius with **`1.5 mm` CNC-rolled comfort edges** along both sides and `2.5 mm` side-dot holes drilled at frets `3, 5, 7, 9, 12 (double), 15, 17, 19, 21, 24 (double)`.

---

## Phase 4: Pre-Assembly Dry Fit & Fretboard Prep (30 Minutes)

When your box of finished CNC parts arrives on your workbench:

1. **Test-Fit Without Glue (5 Mins):**
   * Drop the `440 mm` spoke-wheel truss rod into the center slot of `Part_01_Spine_Core` and the two `4 × 10 mm` carbon spars into the flanking slots. Verify they sit `0.1 mm` below flush.
   * Slide the **3A Upper Horn** and **3B Lower Leg Rail** into the side dovetail receptacles and click the two **M6 red quarter-turn spring plungers** in. Verify they lock rock-solid with zero play.
2. **Press Frets & Side Dots into the Richlite Fretboard (25 Mins):**
   * Dab a tiny drop of thin CA glue (`StewMac #10`) into the `2.5 mm` side holes, insert the **Luminlay** cyan rod, snip flush with flush-cutters, and lightly buff smooth with a 600-grit foam pad.
   * Press the 24 pre-radiused **Jescar `FW57110-S` stainless steel jumbo frets** (plus the slightly taller `FW58118-S` stainless zero-fret at position `0`) into the CNC-blind-ended fret slots using a small arbor press or dead-blow fretting hammer. Because the slots are CNC-milled with `1.5 mm` rolled edges, the frets seat at uniform height immediately.

---

## Phase 5: Structural Bonding of the Spine (30 Minutes Active + 24h Cure)

> [!CAUTION]
> **Never let epoxy touch the moving threads or bar of the truss rod.** Wrap the main body of the dual-action truss rod in a single layer of thin plumber's PTFE (Teflon) tape or Kapton tape before setting it into its channel, leaving only the outer anchor blocks bare.

1. **Prep Bonding Surfaces (5 Mins):**
   * Wipe the internal carbon spar slots, the top face of the CNC spine core, the two `4 × 10 mm` carbon spars, and the underside of the Richlite fretboard with **99% Isopropyl Alcohol** on a lint-free cloth.
2. **Bond the Carbon Spars, Top Skin & Neck Shell (15 Mins):**
   * Attach the static mixing nozzle to your **3M Scotch-Weld DP420 Black** cartridge (`60-minute` working time — no need to rush).
   * Apply a thin bead into the two `4 × 10 mm` spar channels and press the **two pultruded carbon fiber spars** fully into place.
   * Place the PTFE-wrapped **dual-action truss rod** into the center channel (with the spoke-wheel adjustment nut facing the 24th-fret heel recess).
   * Apply a thin, even film of DP420 to the underside of the **`2.2 mm` warm-touch carbon neck back shell** and the **`3.0 mm` carbon top skin** (over the bridge/pickup section) and press them onto their CNC registration ledges.
3. **Drop On & Clamp the Fretboard (10 Mins):**
   * Insert the two `4.0 mm` steel alignment dowel pins into the neck core.
   * Spread a thin, uniform layer of DP420 across the top of the neck core and carbon spars (staying `3 mm` away from the center truss rod slot).
   * Press the **Richlite fretboard** down onto the two alignment pins — it will lock into exact alignment with the neck edges automatically.
   * Apply 6 padded trigger clamps (or wrap tightly with silicone luthiery binding bands) along the neck, wipe away any tiny epoxy squeeze-out immediately with a cotton swab dipped in isopropyl alcohol, and let cure undisturbed for **24 hours at room temperature**.

---

## Phase 6: Bolt-On Hardware, Zero-Battery + Active Rig Wiring & Final Setup (30 Minutes)

After 24 hours, remove the clamps. Your structural spine is now a single monolithic aerospace beam.

1. **Bolt On the Headpiece, Bridge & Titanium U-Guard (10 Mins):**
   * Screw the **CNC LowPro 6-String Headpiece** into the pre-tapped M4 holes at the top of the neck (`Y = 703 mm`) right behind the zero-fret.
   * Drop the **Hipshot 6-String Headless Tremolo** into the bridge cavity, attach the **3 rear tension springs** to the spring claw inside the back cavity, and thread in the claw adjustment screws.
   * Bolt the **CNC Grade-5 Titanium Rear U-Guard** into the rear of the spine using its 4 flush M4 socket-head screws. Confirm the guard extends `12 mm` past the barrel tuners and `4 mm` below them.
2. **Install Pickup, Zero-Battery Fail-Safe Relay & Optional Dual-`18650` Active Rig (10 Mins):**
   * Feed the **high-gain passive ceramic soapbar humbucker** (`Lundgren M6` / `Bare Knuckle Ragnarok` / `Black Winter`) cable through the `4 mm` hole in the `2.5 mm` aluminum EMI shield bulkhead into the rear electronics bay.
   * Mount the 4 flush right-side controls (`Bourns` dual-gang push-push volume wheel, 3-way preset toggle switch, waterproof `USB-C` port, and `Neutrik NJ3FP6C-BAG` TRS locking jack).
   * **How the 3-Mode Zero-Battery Fail-Safe Works Automatically:**
     - **With Zero Batteries Installed (100% Passive Mode):** The **Omron `G6K-2F-Y` Normally-Closed (`0.0V`) gold-contact mechanical relay** defaults to its passive closed position—routing the passive soapbar pickup directly through the `500 kΩ` pot deck to the `1/4"` jack with zero battery power required.
     - **With Zero Batteries + USB-C or TRS Cable Power:** Plugging in any `5V` USB-C cable (or `9V–12V` TRS phantom power) automatically powers the **Green Screamer + NS-1 Keyed Gate + NAM Engine + Wireless TX** via the `TI TPS2121` power mux even if the `18650` battery cradle is completely empty.
     - **With 2x `18650` Cells Installed (`14–22 Hours` Untethered Wireless/DSP):** Pop two rechargeable `18650` cells into the **Keystone `1048`** cradle and snap the **magnetic carbon rear hatch (`Part_06`)** shut. Push the volume thumbwheel in/out at any time to toggle between **Active NAM + Screamer + NS-1 Gate** and **100% Passive Analog True-Bypass**.
3. **Apply Leg Grip Strip, Attach Wings & String Up (10 Mins):**
   * Peel the 3M backing off the **`2.0 mm` Santoprene rubber strip** and press it into the flush CNC recess along the outer edge of the **3B Lower Leg Rail**.
   * Click the **3A Upper Horn** and **3B Lower Leg Rail** into the spine dovetails with the two **red captive quarter-turn pins**.
   * Install a set of `.010–.046` (or `.009–.042`) guitar strings through the Hipshot tail barrels, lock the strings at the top CNC headpiece with a 3mm hex key, tune to pitch using the protected rear barrel tuners, and set saddle height to **`0.9 mm` (high E) / `1.2 mm` (low E)** at the 12th fret.

---

## Visual Reference Blueprints & Renders in Repository

* **[1:1 Millimeter CNC Blueprint (With Dual-18650, Screamer, NS-1 Gate, NAM & Zero-Battery Relay)](../images/02_cnc_specs_and_blueprints/01_master_1to1_mm_cnc_blueprint.png)**
* **[Underside Dual-18650 Battery + NAM/Screamer/NS-1 Cutaway & Side Controls Macro](../images/02_cnc_specs_and_blueprints/07_onboard_battery_nam_screamer_cutaway_and_controls.jpg)**
* **[Exploded Method 2 CNC Bonding Stack & 12th-Fret Cross-Section](../images/02_cnc_specs_and_blueprints/03_cnc_narrow_spine_exploded_and_12th_fret_section.jpg)**
* **[Internal CNC Lattice & Carbon Spar Placement Cutaway](../images/02_cnc_specs_and_blueprints/02_cnc_spec_assembled_and_internal_lattice_cutaway.jpg)**
* **[Uncropped Workbench DSLR Photo (Smooth Rounded & Beveled Edges)](../images/01_dslr_and_rounded_edges/01_dslr_workbench_wide_uncropped.jpg)**
* **[Interactive 360° 3D WebGL Model Viewer](../viewer/carbon_spine_3d_interactive.html)**

![Underside Dual-18650 Battery + NAM/Screamer/NS-1 Cutaway & Side Controls](../images/02_cnc_specs_and_blueprints/07_onboard_battery_nam_screamer_cutaway_and_controls.jpg)

![Exploded Method 2 CNC Bonding Stack & 12th-Fret Cross-Section](../images/02_cnc_specs_and_blueprints/03_cnc_narrow_spine_exploded_and_12th_fret_section.jpg)


