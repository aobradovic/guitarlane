# 07 — How to Build It, Exact Costs, Week-by-Week Schedule & NAMM 2027 Launch Playbook

*Prepared: October 19, 2026 | Target Event: **The 2027 NAMM Show (January 26–30, 2027 — Anaheim Convention Center, CA)** | Time Remaining: **14 Weeks (101 Days)***

---

## 1. Can You Build & Demo This at NAMM 2027?

**YES — 100%.** Because we engineered this guitar around **Method 2 (Turnkey 5-Axis CNC Billet + Pre-Cured Autoclave Carbon Plates + Off-the-Shelf Bridge/Pickups)**, you have **zero mold-making lead time** and **zero wood-drying or paint-booth curing delays**:
* **CNC Machining Lead Time (`RapidDirect` / `JLCCNC` / `PCBWay`):** **10 to 14 business days** from uploading the files in `cnc_production_files/` to FedEx/DHL delivery at your door.
* **Turnkey PCB Assembly (`JLCPCB` / `PCBWay`):** **7 to 10 business days** for the 6-pin pogo-pin dock, passive fail-safe relay motherboard, and the 4 M.2 overdrive/gate daughterboards.
* **Final Bench Assembly Time:** **~2.5 hours per guitar** (bonding the carbon spars and Richlite fretboard with `3M™ Scotch-Weld™ DP420` epoxy, bolting on the Hipshot bridge, Titanium U-Guard, and `3A`/`3B` wings, and sliding in the pickup cartridge).

With **14 full weeks** between **today (October 19, 2026)** and **NAMM 2027 Opening Day (January 26–28, 2027)**, you can complete your first working prototype by **late November 2026**, build 2–3 final show-floor guitars in **December 2026**, and still have **3.5 full weeks of buffer in January 2027** for setup, fret dress, preset voicing, and demo video production.

---

## 2. How to Make It (5-Vendor Turnkey Manufacturing Playbook)

You do **not** need a machine shop, luthiery saws, or soldering equipment. Five specialized online suppliers manufacture and finish every component to `±0.05 mm` (`ISO 2768-f`) tolerances and ship them to your desk for bolt-together assembly:

### Vendor 1: 5-Axis CNC Metal & Carbon Fiber Parts (`RapidDirect.com`, `JLCCNC.com`, or `PCBWay.com`)
Upload the exact 1:1 millimeter files from [`cnc_production_files/`](../cnc_production_files/) and specify these materials and finishes:
1. **`Part_01_Spine_Core_7075_T6.stl`**
   * **Material:** Aerospace Aluminum `7075-T6`
   * **Surface Finish:** Fine Glass-Bead Blast (`Ra 1.2 μm`) + **Type III Hard Anodize Matte Stealth Black** (or **Cerakote H-146 Graphite Black**).
   * **Tapped Threads (Callout on Quote):** `M4 × 0.7` threads for Rear U-Guard & Neck/Bridge mounts; `M5 × 0.8` for quarter-turn wing pins.
2. **`Part_04_Rear_Tuner_UGuard_Ti_G5.stl`**
   * **Material:** Grade-5 Titanium (`Ti-6Al-4V`)
   * **Surface Finish:** Fine Glass-Bead Blast Satin Natural Titanium (`Ra 1.2 μm`).
3. **`Part_05A_Upper_Horn_Wing_3A_Ti_or_7075.stl` & `Part_05B_Lower_Leg_Rail_3B_Ti_or_7075.stl`**
   * **Material:** Grade-5 Titanium (`Ti-6Al-4V`) or `7075-T6` Matte Black Anodized Aluminum.
4. **`Part_07_Universal_HotSwap_Pickup_Sled.stl` (Order 4x–6x Sleds so you can pre-mount 4 different pickups for NAMM!)**
   * **Material:** `7075-T6` Black Anodized Aluminum (`73.0 × 40.0 × 2.5 mm`).
5. **`Part_02_Top_Skin_3mm_Carbon.stl`, `Part_03_Neck_Back_Shell_Carbon.stl`, `Part_06_Rear_Magnetic_Hatch_Carbon.stl` & `Master_2D_CNC_Profiles_1to1_mm.dxf`**
   * **Material:** Quasi-Isotropic Pre-Cured Autoclave Toray `T700/T800` Solid Carbon Fiber Plate (`3.0 mm` top skin, `2.5 mm` rear hatch, `2.2 mm` neck shell) in **100% Matte Clear Coat (`5 GU` dead-flat sheen)**.

### Vendor 2: Fretboard, Stainless Frets & Carbon Neck Spars (`Richlite` / `LMI` / `StewMac` + `DragonPlate.com`)
1. **Fretboard:** Order a CNC-radiused (`16"` or `12"–16"` compound radius), pre-slotted **`25.5"` (`647.7 mm`) scale, 24-fret + Zero-Fret Richlite "Black Diamond" Fretboard** trimmed to `43.0 mm → 57.0 mm × 6.0 mm`.
2. **Fretwire & Side Dots:** `25x` Pre-cut, pre-radiused **Jescar `FW57110-S` Stainless Steel Jumbo Frets** + **`2.5 mm` Super-Blue Luminlay** side dots.
3. **Internal Neck Spars & Truss Rod:** `2x` Pultruded Unidirectional Carbon Fiber Bars (`4.0 mm × 10.0 mm × 460 mm` from `DragonPlate.com`, `$14` each) + `1x` `440 mm` Low-Profile Dual-Action Spoke-Wheel Truss Rod (`$18`).

### Vendor 3: Off-the-Shelf Bridge, Locks & Hardware (`Hipshot Products` / `ABM` / `McMaster-Carr`)
1. **Bridge & Headpiece:** **Hipshot 6-String Headless Tremolo System** (or **Hipshot 6-String Fixed Headless Hardtail**) + **LowPro 6-String Headless String Lock** in Satin Black (`~$245` direct OEM/builder price).
2. **Quick-Release Pins & Magnets (`McMaster-Carr`):**
   * `2x` Captive Stainless Spring-Loaded Quarter-Turn Ball-Lock / Cam-Lock Pins (`Ø6 mm` shank) with Red Anodized Knobs for the `3A`/`3B` wings.
   * `24x` `Ø6 mm × 3 mm` Grade `N52` Nickel-Plated Neodymium Magnets (for the pickup bay and magnetic rear hatch).
   * `1x` Strip of `4.0 mm` Black `60A` Santoprene® Rubber for the `3B` lower leg rest edge.

### Vendor 4: Hot-Swap Pickups for Your 3-Second NAMM Demo (`EMG`, `Fishman`, `Bare Knuckle`, `Seymour Duncan`)
Bolt each pickup onto its own `Part_07` CNC Dovetail Sled with its `R_ID` sense resistor soldered across Pins 5–6 so you can swap all 4 live at NAMM in 3 seconds:
1. **Sled #1:** **EMG 81** (Brushed Black Chrome Active Soapbar — `R_ID = 10 kΩ`)
2. **Sled #2:** **Fishman Fluence Modern Ceramic** (Black Soapbar — `R_ID = 22 kΩ`)
3. **Sled #3:** **Bare Knuckle Ragnarok / Aftermath** (Battle-Worn Passive Humbucker in CNC Adapter Bezel — `R_ID = 100 kΩ`)
4. **Sled #4:** **Seymour Duncan Black Winter / Lundgren M6** (Open-Coil Passive Humbucker — `R_ID = 100 kΩ`)

### Vendor 5: Turnkey PCBs & Embedded `NAM` Engine (`JLCPCB.com` / `Electro-Smith Daisy` / `Raspberry Pi CM4`)
* **Fastest Path for NAMM 2027 Prototype:**
  * Instead of writing bare-metal DSP firmware from scratch before January, mount an **Electro-Smith Daisy Seed (`ARM Cortex-M7 @ 480 MHz`, `$29`)** or a **Raspberry Pi Compute Module 4 Lite (`Quad-Core Cortex-A72 @ 1.5 GHz` running headless Elk Audio OS + `NeuralAmpModelerCore` C++ engine, `$45`)** directly onto your `JLCPCB` carrier motherboard inside the rear cavity!
  * Order the Mother-Dock PCB (with the `6-pin Mill-Max 0906-1` spring pogo-pin block, `Omron G6K-2F-Y` zero-battery fail-safe bypass relay, `2x 18650` holder, and `M.2 Key-E` socket) + the 4 swappable analog overdrive daughterboards (`Green Screamer`, `Precision Drive`, `Fortin 33 + Gate`, `HM-2W`) fully populated by **JLCPCB Turnkey SMT Assembly** in 8 days for **under `$140` total (for 5 boards of each)**.

---

## 3. How Much Does It Cost? (Complete Bill of Materials Breakdown)

Here is the real-world cost breakdown across **three tiers**: building **1 single prototype**, building a **3-guitar NAMM 2027 Show Bundle** (recommended because CNC setup charges drop by ~45% when ordering 3 units at once), and **Batch Production (`Qty 50`)**:

| Subsystem / Part | `Qty 1` Single Prototype | `Qty 3` NAMM Show Bundle *(Per Guitar)* | `Qty 50` Production Batch *(Per Guitar)* | Lead Time |
| :--- | :---: | :---: | :---: | :---: |
| **1. `7075-T6` CNC Spine Core (`Part_01`, Anodized Black)** | `$420` | `$245` | `$115` | `10–12 days` |
| **2. Grade-5 Titanium Rear Tuner U-Guard (`Part_04`)** | `$115` | `$75` | `$38` | `10–12 days` |
| **3. Detachable `3A` & `3B` Wings (`Part_05A/B`, Ti or 7075)** | `$165` | `$105` | `$48` | `10–12 days` |
| **4. CNC Carbon Plates (`Part_02` Top, `Part_03` Neck, `Part_06` Hatch)** | `$175` | `$120` | `$62` | `8–10 days` |
| **5. Universal Hot-Swap Pickup Sled (`Part_07` + Pogo/N52)** | `$38` | `$22` | `$9` | `8–10 days` |
| **6. Richlite Fretboard + 24 Jescar SS Frets + Carbon Spars + Truss Rod** | `$145` | `$125` | `$74` | `5–7 days` |
| **7. Hipshot 6-String Headless Bridge + String Lock Headpiece** | `$265` | `$235` | `$155` | `In stock (5 days)` |
| **8. Primary Pickup (`Fishman Fluence` or `EMG` or `Bare Knuckle`)** | `$135` | `$120` | `$78` | `In stock (3 days)` |
| **9. Onboard Electronics (`NAM` Module + `Screamer/NS-1` PCB + `5.8GHz` TX + `2x 18650`)** | `$185` | `$135` | `$72` | `8–10 days` |
| **10. Adhesives (`3M DP420`), Quarter-Turn Pins, Neutrik Jack, Strings** | `$45` | `$30` | `$18` | `2–3 days` |
| **TOTAL COST PER COMPLETE GUITAR** | **`$1,688`** | **`$1,212 / guitar`** (`$3,636` for 3) | **`$669 / guitar`** | **~2.5 Weeks** |

### Optional NAMM 2027 Demo Accessories Budget:
* **Extra Hot-Swap Pickup Cartridges (`3x` extra pre-loaded sleds so you have all 4 brands on the table: `EMG 81`, `Fishman Modern`, `Bare Knuckle Ragnarok`, `SD Black Winter`):** **`+$460` total**
* **All 4 Swappable M.2 Analog Drive Daughterboards (`5 pcs` of each from JLCPCB SMT):** **`+$115` total**
* **Custom `30"` (`760 mm`) Stealth Dual-Laptop + Guitar Spine Backpack Prototype (Cut & sewn by a tactical gear sample maker or modified `30"` hard-shell pack with CNC laser-cut EVA foam inserts):** **`+$280 – $420`**

---

## 4. When & How: Week-by-Week Countdown to NAMM 2027 (`Oct 19, 2026 → Jan 28, 2027`)

| Weeks | Target Dates | Milestone & Action Items |
| :--- | :--- | :--- |
| **Week 1–2** | **Oct 19 – Nov 1, 2026** | **Lock Orders & Quotes:**<br>• Upload `cnc_production_files/*.stl` & `.dxf` to **RapidDirect** & **JLCCNC** for instant DFM review and order Prototype #1 (or all 3 NAMM units).<br>• Order Hipshot 6-string headless bridge, Richlite pre-slotted fretboard, Jescar `57110-S` stainless frets, `DragonPlate` carbon spars, and pickups (`EMG`, `Fishman`, `Bare Knuckle`).<br>• File USPTO Intent-to-Use (`Section 1(b)`) trademark application (`$350` in Class 015) for your chosen brand name (**VEXOR**, **SPINEFORGE**, **EXOSPIN**, or **VANTASPINE**) so your mark is legally protected before showing at NAMM. |
| **Week 3–4** | **Nov 2 – Nov 15, 2026** | **PCB Fabrication & Fretboard Prep:**<br>• Submit Mother-Dock PCB & M.2 `Green Screamer` / `NS-1` / `Fortin 33` Gerber & BOM files to **JLCPCB Turnkey SMT**.<br>• Press & dress the 24 stainless frets into the Richlite fretboard (`R1.5 mm` rolled edges) while CNC metal parts are in transit. |
| **Week 5–6** | **Nov 16 – Nov 29, 2026** | **CNC Parts Delivery & Prototype #1 Dry-Fit (`Thanksgiving Week`):**<br>• Receive `7075-T6` spine core, Grade-5 Titanium U-Guard, `3A`/`3B` wings, carbon skins, and hot-swap sleds.<br>• Perform dry-fit verification of the side-sliding pickup cartridge (`H7/g6` dovetail slide + 6-pin pogo contact + `2.80 mm` string clearance) and quarter-turn wing pins. |
| **Week 7–8** | **Nov 30 – Dec 13, 2026** | **Bonding, Electronics Integration & First String-Up:**<br>• Bond `2x` carbon spars, fretboard, and `2.2 mm` warm-touch carbon neck shell to the `7075-T6` spine using `3M™ Scotch-Weld™ DP420` (`24h` full cure).<br>• Install Mother-Dock PCB, `NAM` module, `2x 18650` battery cradle, and Hipshot bridge.<br>• String up Prototype #1 with `10–46` strings and test all 3 modes (Active `NAM` + Wireless, Analog `Screamer` + `NS-1`, and Zero-Battery Passive Relay). |
| **Week 9–11** | **Dec 14 – Jan 3, 2027** | **Build NAMM Show Units #2 & #3 + Custom Backpack Foam Insert:**<br>• Assemble the remaining show guitars (e.g., 1 Bead-Blasted Titanium Wing model + 1 Stealth Black DLC model) and laser-cut the custom EVA foam divider for the `30"` Dual-Laptop + Guitar Backpack. |
| **Week 12–13** | **Jan 4 – Jan 17, 2027** | **Burn-In Testing, `NAM` Preset Capture & Marketing Reel:**<br>• Load custom studio `NAM` captures (5150 III, Dual Rectifier, Mesa Mark IIC+) onto the onboard neural engine.<br>• Shoot 60-second macro demo videos showing the **3-Second Strings-On Pickup Swap** (`EMG` → `Bare Knuckle`) and pulling the guitar + 2 laptops out of one backpack. |
| **Week 14** | **Jan 18 – Jan 25, 2027** | **Final Pack & Travel to Anaheim, CA:**<br>• Pack guitars, 4 pickup cartridges, 4 M.2 drive cards, headphone amp/FRFR monitor, and QR-code pre-order cards. |
| **SHOW TIME** | **Jan 26 – Jan 30, 2027** | **THE 2027 NAMM SHOW (Anaheim Convention Center):**<br>• **Jan 26–27:** Media & Creator Preview Days.<br>• **Jan 28–30:** Main Exhibition Floor Open. |

---

## 5. Three Ways to Demo at NAMM 2027 (Even as a New Independent Brand)

1. **Strategy A: Official NAMM "New Exhibitor / Boutique Builder Pod" (`~$1,800 – $2,800`)**
   * NAMM offers compact `5'×5'` or `8'×8'` turnkey tabletop/kiosk pods in the Boutique Guitar / Luthiery zone specifically for first-time innovative instrument makers. Contact NAMM Trade Show Sales immediately (`namm.org/thenammshow/exhibit`)—late-stage pod reallocations happen in October/November.
2. **Strategy B: Partner / Co-Demo inside a Component Supplier's Booth (`$0 Booth Cost`)**
   * Because your guitar is a **live, interactive showcase for pickup & hardware brands**—allowing players to hear an **EMG 81**, a **Fishman Fluence Modern**, a **Bare Knuckle Ragnarok**, and a **Seymour Duncan Black Winter** swapped inside the **exact same guitar in 3 seconds without loosening strings**—pickup, bridge (`Hipshot`), and amp-modeler brands love having a centerpiece demo instrument in their booth or private demo room.
3. **Strategy C: The "Backpack Guerilla + Hotel Demo Suite" Play (`Highest ROI for Creators & Press`)**
   * Book a suite at the **Anaheim Marriott or Hilton** (50 yards from the Hall D guitar entrance) for high-volume FRFR amp demos with guitar YouTubers (Ola Englund, Agufish, Keith Merrow, Rhett Shull, etc.), AND walk the NAMM floor wearing the sleek **`30"` Matte Black Backpack**.
   * When talking to artists, press, or dealers on the floor, unzip the bag, pull out the `82 mm` Carbon Spine alongside your two laptops, snap on the `3A`/`3B` Titanium wings in 5 seconds, plug headphones directly into the guitar's onboard `NAM` + `Green Screamer` engine, and swap an `EMG` for a `Bare Knuckle` in 3 seconds right in front of their eyes. That visual hook is tailor-made to go viral at NAMM 2027.
