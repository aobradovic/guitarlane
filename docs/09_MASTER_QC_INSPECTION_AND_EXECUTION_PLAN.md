# 09 — Master Quality Control (QC), Incoming Caliper Inspection, Assembly & NAMM 2027 Execution Plan

---

## 📂 Exact Folder Locations on Your Computer

All of your engineering files, 1:1 CNC `.STL` & `.DXF` production files, copy-paste order sheets, interactive 3D app, and documentation are stored in **two mirrored folders** on your computer (and backed up on GitHub at **[https://github.com/aobradovic/guitarlane.git](https://github.com/aobradovic/guitarlane.git)**):

### 1. Your Primary Working & Git Repository Folder (Cleanest Path):
* **Main Project Folder:** `C:\work\guitarlane`
  * **1:1 CNC `.STL`, `.DXF`, BOM & Order Sheet Folder:** `C:\work\guitarlane\cnc_production_files`
  * **All Engineering, Build, Electronics & QC Manuals:** `C:\work\guitarlane\docs`
  * **Interactive 3D App & `.STL` Inspector:** `C:\work\guitarlane\viewer\carbon_spine_3d_interactive.html`
  * **All Blueprints & DSLR Renders:** `C:\work\guitarlane\images`
  * **CAD & QC Verification Scripts:** `C:\work\guitarlane\cad_scripts`

### 2. Your Local Browseable Gallery Mirror Folder:
* **Gallery Folder:** `C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\Guitar_Gallery`
  * **CNC Production Subfolder:** `C:\Users\aobra\.gemini\antigravity-cli\brain\12f3c50d-00e5-4801-8eda-5dbb0241fd14\Guitar_Gallery\CNC_Production_Files`

---

## 🛠️ Master 5-Stage Quality Control (QC) & Inspection Plan

Use this step-by-step QC protocol for **Guitar #00 (Your November Prototype)** and for **Serial `#01/10` through `#10/10` (Your January NAMM 2027 Founders Edition Batch)**.

---

### STAGE 1: Pre-Order Digital CAD & RFQ File QC (Before Submitting to CNC)

Before clicking "Submit Order" on RapidDirect / JLCCNC / PCBWay, verify these 6 items:

| QC ID | Check Description | Target / Specification | Verification Method | Pass / Fail |
| :---: | :--- | :--- | :--- | :---: |
| **QC-1.1** | **CAD Unit Scale Check** | All 8 `.STL` & `.DXF` files set to **`Millimeters (mm)`** | Drag `.STL` into `carbon_spine_3d_interactive.html` or vendor quote page | `[ ] PASS` |
| **QC-1.2** | **Part 01 Spine Bounding Box** | **`703.0 × 82.0 × 38.0 mm`** (`±0.1 mm`) | Verify on vendor 3D preview screen | `[ ] PASS` |
| **QC-1.3** | **Part 04 Ti U-Guard Bounding Box** | **`82.0 × 42.0 × 23.0 mm`** (`Ti-6Al-4V` Grade 5) | Verify on vendor 3D preview screen | `[ ] PASS` |
| **QC-1.4** | **Part 05A / 05B Wings Dimensions** | `3A`: **`210 × 76 × 12 mm`** \| `3B`: **`205 × 98 × 14 mm`** | Verify on vendor 3D preview screen | `[ ] PASS` |
| **QC-1.5** | **Part 07 Pickup Sled Quantity** | **`73.0 × 40.0 × 2.5 mm`** — Order **`4 pcs`** for Proto #1 (`20 pcs` for 10 NAMM batch) | Verify line-item quantity on quote | `[ ] PASS` |
| **QC-1.6** | **Thread & Tolerance Remarks** | Copy-pasted notes from `CNC_ORDER_SHEET_COPY_PASTE.txt` (`ISO 2768-f`, `M4×0.7`, `M5×0.8`) | Verify Remarks field on each line item | `[ ] PASS` |

---

### STAGE 2: Incoming CNC Part Inspection (Digital Caliper QC Upon Delivery)

**Tools Needed:** Standard `$25` Digital Caliper (`0.01 mm` resolution), `M4 × 0.7` and `M5 × 0.8` screws, and a straightedge ruler.

When the box from the CNC shop arrives, measure these **12 Critical-to-Quality (CTQ) dimensions** before applying any glue or assembling hardware:

| QC ID | Part Name | Dimension to Measure with Digital Calipers | Nominal Target | Allowed Tolerance | Measured (`mm`) | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **QC-2.1** | `Part_01` Spine Core | Total Lower Body Spine Width (`Y = 0` to `219 mm`) | **`82.00 mm`** | `±0.05 mm` (`81.95–82.05`) | `_______` | `[ ]` |
| **QC-2.2** | `Part_01` Spine Core | Nut / Zero-Fret Neck Width (`Y = 703 mm`) | **`43.00 mm`** | `±0.05 mm` (`42.95–43.05`) | `_______` | `[ ]` |
| **QC-2.3** | `Part_01` Spine Core | 24th-Fret Neck Heel Width (`Y = 237 mm`) | **`57.00 mm`** | `±0.05 mm` (`56.95–57.05`) | `_______` | `[ ]` |
| **QC-2.4** | `Part_01` Spine Core | Core Depth (Before `3.0 mm` Top Skin & `2.5 mm` Hatch) | **`32.50 mm`** *(or `38.00 mm` full stack)* | `±0.05 mm` | `_______` | `[ ]` |
| **QC-2.5** | `Part_01` Spine Core | Left-Side Open Pickup Cartridge Exit Window Width (`Y = 141.5–182.5`) | **`41.00 mm`** | `+0.05 / -0.00 mm` | `_______` | `[ ]` |
| **QC-2.6** | `Part_01` + `Part_07` | **Dry-Fit Side-Slide Pickup Sled Test:** Slide `Part_07` (`40.00 mm` wide) horizontally into `Part_01` left slot | **`0.025–0.05 mm` clearance** | Smooth zero-rattle slide (`H7/g6`) | `_______` | `[ ]` |
| **QC-2.7** | `Part_01` Spine Core | Carbon Spar Channels (`2x` slots along neck) | **`4.10 × 10.10 mm`** | `+0.05 / -0.00 mm` (Test-fit `4×10` spars) | `_______` | `[ ]` |
| **QC-2.8** | `Part_01` Spine Core | Central Spoke-Wheel Truss Rod Channel | **`6.10 × 9.20 mm`** | `+0.05 / -0.00 mm` (Test-fit truss rod) | `_______` | `[ ]` |
| **QC-2.9** | `Part_01` Spine Core | Rear Electronics Bay Internal Pocket (`2x 18650` + `NAM` + `Screamer`) | **`102.0 × 60.0 × 16.5 mm`** (`18.5 mm` inter-coil) | `±0.10 mm` (Test-fit `2x 18650` cells + hatch) | `_______` | `[ ]` |
| **QC-2.10** | `Part_04` Ti U-Guard | Rear U-Guard Width & `4x M4` Bolt Alignment to `Part_01` Tail | **`82.00 mm`** | Thread all `4x M4×0.7` bolts in by hand | `_______` | `[ ]` |
| **QC-2.11** | `Part_05A` & `05B` | **Dry-Fit Wing Dovetail & Quarter-Turn Pin Lock Test** | Zero play when locked | Insert `3A` & `3B` tabs; click `Ø6 mm` pins | `_______` | `[ ]` |
| **QC-2.12** | All Parts | **Surface Finish & Edge Radius Tactile Check** | `R6.0 mm` outer bullnose; `Ra 0.8–1.2 μm` satin | Run bare hand along all edges; zero burrs | `_______` | `[ ]` |

---

### STAGE 3: Structural Bonding, Scale Geometry & Fretwork QC

Perform these checks during and after the **90-minute structural assembly** (`3M™ Scotch-Weld™ DP420 Black` epoxy):

| QC ID | Inspection Step | Exact Target Specification | How to Verify | Status |
| :---: | :--- | :--- | :--- | :---: |
| **QC-3.1** | **Pre-Glue Dry Clamp Rehearsal** | `Part_02` Carbon Top Skin, `2x` Carbon Spars, `Part_03` Warm-Touch Neck Shell, and Richlite Fretboard align flush with `Part_01` | Dry-clamp with 6 padded cam clamps before mixing epoxy | `[ ] PASS` |
| **QC-3.2** | **Truss Rod Silicone Masking Check** | **CRITICAL:** Ensure zero `3M DP420` epoxy enters the truss rod adjustment nut or channel | Apply a thin strip of masking tape over top of truss rod slot before spreading epoxy on spar walls | `[ ] PASS` |
| **QC-3.3** | **Scale Length Verification (`25.5"` / `647.70 mm`)** | • Zero-Fret center to 12th-Fret crown center = **`323.85 mm` (`±0.05 mm`)**<br>• Zero-Fret center to High-E Saddle center = **`647.70 mm` (`±0.20 mm`)** | Measure with precision steel machinist rule before epoxy sets (`40 min` working time) | `[ ] PASS` |
| **QC-3.4** | **Fret Levelness & Rolled Edge Check** | • Fret-to-fret height variance **`< 0.02 mm`** (`0.0008"`)<br>• Fretboard & fret ends rolled to smooth **`R1.5 mm`** | Check across every 3-fret group from Fret 1 to Fret 24 using a 4-edge Fret Rocker tool | `[ ] PASS` |
| **QC-3.5** | **Neck Relief Under Full `10–46` String Tension (`105.4 lbs`)** | Net forward relief at 8th–12th fret = **`0.040 – 0.100 mm`** (`0.0015"–0.004"`) | Hold string down at 1st and 24th fret; measure gap at 10th fret with feeler gauge | `[ ] PASS` |
| **QC-3.6** | **String Action Height at 12th Fret** | • **Low E (6th String):** **`1.30 – 1.50 mm`**<br>• **High E (1st String):** **`0.90 – 1.10 mm`** (Zero fret buzz on any fret 1–24) | Measure from top of 12th stainless fret crown to bottom of string | `[ ] PASS` |

---

### STAGE 4: Hot-Swap Pickup Cartridge, Onboard `Screamer`/`NS-1`/`NAM` & Zero-Battery Relay QC

**Tools Needed:** Digital Multimeter (`Ω` and `DC Volts`), guitar cable, amplifier/FRFR speaker, and headphones.

| QC ID | Subsystem Under Test | Test Procedure & Pass Criteria | Target Reading | Status |
| :---: | :--- | :--- | :---: | :---: |
| **QC-4.1** | **Strings-On Pickup Slide Clearance** | With all 6 strings tuned to standard pitch (`E-A-D-G-B-E`), slide `Part_07` Pickup Cartridge in and out of the left side slot 10 times | **`2.80 mm` vertical gap** (`Zero` pole-piece contact with strings during slide!) | `[ ] PASS` |
| **QC-4.2** | **Magnetic Snap & Pogo Contact Resistance** | Measure resistance from pickup solder pad on sled to Mother-Dock PCB pad across all 6 gold pogo pins (`Pins 1–6`) | **`< 0.08 Ω`** per pin; **`+23.2 N` (`5.2 lbs`)** crisp magnetic snap lock | `[ ] PASS` |
| **QC-4.3** | **Auto-Impedance & Active Power Switching (`Pin 6` `R_ID`)** | • Insert **Active Cartridge (`EMG 81` / `Fishman`, `R_ID = 10k/22k`)** $\rightarrow$ Verify `Pin 5` turns ON `+9.0V` and input load = `25 kΩ`<br>• Insert **Passive Cartridge (`Bare Knuckle`, `R_ID = 100k`)** $\rightarrow$ Verify `Pin 5` shuts OFF to `0.0V` (`Zero` battery drain) and load = `500 kΩ` | Measure `Pin 5` voltage with multimeter on both cartridges | `[ ] PASS` |
| **QC-4.4** | **Zero-Battery Fail-Safe Bypass Relay (`Mode 1`)** | **Remove both `18650` batteries completely.** Plug standard `1/4"` guitar cable into Neutrik jack with a passive pickup cartridge installed | **100% clean passive guitar output** (`< 0.1 Ω` from Pickup Hot to `1/4"` Tip via `Omron G6K` NC relay contacts) | `[ ] PASS` |
| **QC-4.5** | **Analog `Green Screamer` + `NS-1` Keyed Gate (`Mode 2`)** | Engage Analog Drive mode. Chug palm-muted open Low-E power chords and stop suddenly | Classic mid-humped `TS808` tighten boost; gate clamps shut in **`< 0.5 ms`** with **`< -95 dBu`** dead silence | `[ ] PASS` |
| **QC-4.6** | **Onboard `NAM` Neural Amp + Cab IR (`Mode 3`)** | Plug studio headphones or FRFR monitor directly into guitar; flip 3-Way Preset Toggle (`Clean / Rhythm / Lead`) | Instant glitch-free switching between 3 `.NAM` + Cab IR captures | `[ ] PASS` |
| **QC-4.7** | **`5.8 GHz` Wireless Link & EMI Shielding Check** | Plug paired `5.8 GHz` Receiver into amp `10 meters` away; play high-gain Lead preset while touching/moving guitar | **`< 2.2 ms` latency**, zero dropouts, **zero digital whine or RF hum** into pickup coils (`>82 dB` bulkhead isolation) | `[ ] PASS` |
| **QC-4.8** | **USB-C Fast Charging & BMS Thermal Check** | Plug USB-C charger into side port for 30 minutes | `5V @ 2A` charging LED active; battery temp stays **`< 36°C`** | `[ ] PASS` |

---

### STAGE 5: Final Weight, Balance & Cosmetics Sign-Off (Before Packing for NAMM 2027)

| QC ID | Final Check | Target Specification | Measured Value | Sign-Off |
| :---: | :--- | :--- | :---: | :---: |
| **QC-5.1** | **Bare Travel Spine Weight (With `2x 18650`)** | **`1,856 g ± 45 g`** (`4.09 lbs ± 0.10 lbs`) | `_______ g` | `[ ] PASS` |
| **QC-5.2** | **Full Stage Weight (With `3A` & `3B` Wings Attached)** | **`2,046 – 2,121 g ± 50 g`** (`4.51 – 4.68 lbs`) | `_______ g` | `[ ] PASS` |
| **QC-5.3** | **Standing Strap Balance & Seated Thigh Grip** | Zero neck dive on strap (`CoG` at 12th fret); zero sliding on thigh at `30°` neck angle | Visual & hands-free balance test | `[ ] PASS` |
| **QC-5.4** | **`30"` Dual-Laptop Backpack Fit Check** | Bare `721 × 82 × 38 mm` spine + detached `3A`/`3B` wings + `18"` laptop + `16"` MacBook Pro zip shut cleanly with zero string contact | Zip bag closed & inspect | `[ ] PASS` |

---

## 🚀 Complete 10-Step Master Execution Plan (`Today → NAMM 2027`)

1. **Step 1 (Today — Oct 19, 2026):** Run automated CAD/DFM QC (`python cad_scripts/run_qc_audit.py` — already verified `100% PASS`).
2. **Step 2 (Oct 19–22, 2026):** Upload the 8 files in `C:\work\guitarlane\cnc_production_files` to **RapidDirect / JLCCNC** using `CNC_ORDER_SHEET_COPY_PASTE.txt` (`Qty 1` for Prototype #01, plus `4x` `Part_07` Pickup Sleds).
3. **Step 3 (Oct 22–25, 2026):** Order off-the-shelf hardware for Guitar #1 (`Hipshot` 6-string headless bridge + headpiece, `Richlite` pre-slotted 24-fret board + `Jescar 57110-S` stainless frets, `DragonPlate` `4×10 mm` carbon spars, `EMG 81`, `Fishman Fluence Modern`, `Bare Knuckle Ragnarok`, and `SD Black Winter`).
4. **Step 4 (Oct 25–30, 2026):** Order the onboard electronics (`JLCPCB` Mother-Dock + `Screamer/NS-1` SMT board using `BOM_Onboard_Electronics_JLCPCB_and_Modules.csv`, plus the plug-in `.NAM` core, `5.8 GHz` wireless pair, and `2x Samsung 35E 18650` cells).
5. **Step 5 (Nov 12–16, 2026):** Receive CNC parts for Guitar #1 $\rightarrow$ **Run Stage 2 Incoming Caliper QC (`QC-2.1` to `QC-2.12`)**.
6. **Step 6 (Nov 20–22, 2026):** Assemble Guitar #1 (`2.5 hours`) $\rightarrow$ **Run Stage 3, 4 & 5 QC (`QC-3.1` to `QC-5.4`)** and play-test for 7 days.
7. **Step 7 (Dec 1, 2026 — Go/No-Go Decision):** Click **"Re-Order `Qty 10`"** on RapidDirect/JLCCNC (adding the `"NAMM 2027 FOUNDERS EDITION — #01 OF 10"` laser engraving callout on `Part_04`) and order 10 sets of hardware/electronics (`$10,560` total).
8. **Step 8 (Dec 22–28, 2026):** Receive all 10 CNC guitar kits $\rightarrow$ Run incoming caliper QC on every spine core and pickup sled.
9. **Step 9 (Jan 2–18, 2027):** Assemble, string up, and run **Stage 3–5 QC Sign-Off Sheets** on all 10 numbered Founders Edition guitars (`#01/10` to `#10/10`).
10. **Step 10 (Jan 26–30, 2027 — THE 2027 NAMM SHOW, Anaheim, CA):** Demo Guitar #00 live out of the `30"` Dual-Laptop Backpack (performing the 3-second strings-on pickup swap from `EMG` to `Bare Knuckle`) and sell the 10 numbered Founders Edition guitars (`$29,990 – $34,990` gross revenue).
