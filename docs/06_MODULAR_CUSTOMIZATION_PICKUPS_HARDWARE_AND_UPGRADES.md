# Modular Customization, Hot-Swap Pickups, Analog Drive Cartridges & Hardware Upgrade Architecture

To turn the **Carbon Spine (`UNISPAR` / `MONOSPAR`)** into a high-margin, infinitely customizable platform—where a player can order **EMG, Fishman Fluence, Bare Knuckle, Lundgren, Seymour Duncan, or DiMarzio** pickups, swap between **Green Screamer, Precision Drive, Fortin 33, or HM-2** analog circuits, and upgrade bridges, wings, frets, and finishes at purchase or after purchase—every subsystem is engineered around **standardized mechanical envelopes and tool-free electrical interconnects**.

![Modular Customization Ecosystem — Hot-Swap Pickups, Analog Drive Cards & Hardware Upgrades](../images/02_cnc_specs_and_blueprints/08_modular_custom_pickups_drive_cards_and_hardware_upgrades.jpg)

---

## 1. True 3-Second "Strings-On" Hot-Swap Pickup Cartridge System (`EMG` + `Fishman` + `Bare Knuckle` + `Lundgren` + `Seymour Duncan`)

Yes—not only is it 100% possible, our **82 mm CNC aluminum-and-carbon spine** is the ideal structure on earth to do it properly because the CNC billet holds **`±0.02 mm` tolerances** that wooden guitars cannot hold.

To make swapping between an **active EMG 81**, a **multi-voice Fishman Fluence Modern**, and a **passive Bare Knuckle Ragnarok / Lundgren M6** effortless **without loosening the strings and without touching a soldering iron**, the system solves **three engineering problems** simultaneously:
1. **Mechanical Extraction With Strings At Full Tension:** A **Left-Side Sliding Dovetail Cartridge Drawer** (or **Top Drop-In Magnetic Pogo Sled**) that slides/snaps in beneath the strings in **3 seconds**.
2. **Footprint Unification (`Soapbar` vs. `Open-Coil Humbucker`):** One standardized **`74.0 × 41.0 mm` CNC Carrier Sled** with two interchangeable top bezels so both screwless active soapbars (`EMG` / `Fishman`, `70 × 38 mm`) and tabbed passive humbuckers (`Bare Knuckle` / `Lundgren` / `Seymour Duncan`, `68.5 × 37 mm`) use the exact same cartridge base.
3. **Automatic Electrical Impedance & Voltage Switching (`25 kΩ + 9V/18V` Active vs. `500 kΩ + 0V` Passive):** A 6-pin gold **Mill-Max Pogo-Pin Array** with an **Auto-Sense ID Pin (`Pin 6`)** that automatically reconfigures the guitar's pot impedance, power rail, and `0.0V` passive fail-safe relay the instant a cartridge clicks in.

![3-Second Strings-On Hot-Swap Pickup Cartridge System](../images/02_cnc_specs_and_blueprints/09_3second_strings_on_hotswap_pickup_cartridge_system.jpg)

---

### 1.1 Two Mechanical Hot-Swap Loading Options (Zero String Detuning Required)

Because a traditional pickup has mounting tabs underneath the strings, you normally have to slacken or remove your strings to swap pickups. Our CNC spine eliminates that with two mechanical options:

* **Option 1A (Recommended — `3-Second Side-Slide Dovetail Cartridge`):**
  * The left wall of the `82 mm` spine at the bridge pickup position (`Y = 142 mm` to `Y = 183 mm`) has a precision CNC **dovetail cartridge slot (`71.0 mm` deep × `41.0 mm` wide × `15.5 mm` tall)**.
  * Even with all 6 strings tuned to full concert pitch (`0.9–1.2 mm` action), there is **`2.8 mm` of vertical clearance** between the top of the pickup face and the underside of the strings.
  * You simply press a flush release button on the left side of the spine and **slide the entire pickup cartridge straight out to the left side from underneath the strings**, then slide your next pickup cartridge (`EMG`, `Fishman`, or `Bare Knuckle`) straight in until the **4x `N52` neodymium magnets + ball-detent lock** click home!
* **Option 1B (`Top Drop-In Magnetic Pogo Sled` — Lowest Part Count):**
  * The `71.0 × 39.0 mm` top pickup pocket has `4x Ø6×3 mm N52` neodymium magnets (`3.2 kg` total pull force) and a **6-Pin Gold Pogo-Pin Block** in the floor. With strings loosened by 2 turns (or using the Hipshot tremolo arm depressed slightly), you lift the pickup sled straight out the top with two fingers and drop the next pickup sled in.

---

### 1.2 How One Universal `$6` Carrier Sled Fits `EMG`, `Fishman`, `Bare Knuckle`, `Lundgren` & `Seymour Duncan`

In the metal guitar world, pickups come in **two different physical footprints**:
1. **Active / Soapbar Footprint (`70.0 × 38.0 mm` rounded rectangle, screwless exterior):** Used by **EMG** (`81`, `85`, `57`, `60`, `81X`, `707`, `808`), **Fishman Fluence Modern / Abasi / Keith Merrow**, and **Seymour Duncan Blackouts** (and optional soapbar covers from Bare Knuckle / Lundgren).
2. **Standard Open-Coil / Covered Passive Humbucker Footprint (`68.5 × 37.0 mm` coil body with side mounting tabs):** Used by **Bare Knuckle Pickups (BKP)** (`Aftermath`, `Ragnarok`, `Juggernaut`, `Nailbomb`, `Warpig`, `Painkiller`), **Lundgren** (`M6`, `M7`, `M8`, `Black Heaven`), **Seymour Duncan** (`Nazgûl`, `Black Winter`, `Distortion`, `Alpha/Omega`, `Jupiter`), and **DiMarzio** (`D Activator`, `Titan`).

**How the Universal Pickup Cartridge Sled unifies every pickup brand on earth:**
* Each pickup mounts once onto a **`2.5 mm` thick CNC Anodized Aluminum / Carbon Carrier Sled** (costing `~$6` to machine; players can keep 3 or 4 sleds loaded with their favorite pickups):
  * **Sled Top A (`Soapbar Carrier`):** Fits any `70 × 38 mm` **EMG** or **Fishman Fluence** soapbar. On the underside of the sled is a pre-installed **3-Pin EMG / Fishman Quick-Connect header**—so you literally plug your stock EMG or Fishman pickup straight into the sled with its factory cable!
  * **Sled Top B (`Open-Coil / BKP Adapter Bezel Carrier`):** Features a flush `71 × 39 mm` outer / `68.8 × 37.3 mm` inner CNC trim ring with recessed pockets underneath for a passive humbucker's brass mounting ears, plus a **4-conductor spring-clamp terminal block (`Wago 2060` SMD)** so you can attach any **Bare Knuckle, Lundgren, Seymour Duncan, or DiMarzio** pickup in 60 seconds without soldering!
  * **Built-In Thumbwheel Height Micro-Adjusters:** Two low-profile knurled brass thumbwheels built into the sled let you pre-set the exact pickup height (`2.0 mm` for active EMG/Fishman close to strings; `3.2 mm` for passive Bare Knuckle/Lundgren) once on each sled, so every time you swap cartridges, the height is already dialed in!

---

### 1.3 The Electrical Problem & Solution: How One Guitar Automatically Switches Between `EMG` (`25 kΩ + 9V/18V`), `Fishman` (`Multi-Voice`), and `Bare Knuckle` (`500 kΩ + 0V Zero-Battery`)

Why can't normal guitars hot-swap between **EMG / Fishman** and **Bare Knuckle / Seymour Duncan**?
Because **active pickups (`EMG` / `Fishman`) require a `25 kΩ` volume pot and `+9V` (or `+18V`) DC power**, whereas **passive pickups (`Bare Knuckle` / `Lundgren` / `Seymour Duncan`) require a `500 kΩ` volume pot and `0.0V` (putting a passive pickup on a `25 kΩ` EMG pot kills 95% of its output and treble!)**.

**Our 6-Pin Mill-Max Gold Pogo-Pin Interface (`Mill-Max 821-22-006-10-000101`) solves this 100% automatically via `Pin 6` (`Auto-ID Sense`):**

| Pogo Pin | Function | Active EMG Sled (`81` / `85` / `57` / `81X`) | Active Fishman Fluence Sled (`Modern` / `Merrow` / `Abasi`) | Passive Sled (`Bare Knuckle` / `Lundgren` / `Seymour Duncan`) |
| :---: | :--- | :--- | :--- | :--- |
| **Pin 1** | **Hot Signal Output** | EMG Pin 3 (White Output) | Fluence Hot Output | North Start (Hot) |
| **Pin 2** | **Star Ground / Shield** | EMG Pin 2 (Ground/Shield) | Fluence Ground + Shield | South Start + Bare Shield |
| **Pin 3** | **Voice 2 / Coil-Split** | EMG `89`/`TW` Dual-Coil Select | **Fluence Voice 2** (Passive Alnico Voice) | Series Link (North Finish + South Finish for **Coil-Split**) |
| **Pin 4** | **Voice 3 / High-Freq Tilt** | NC | **Fluence Voice 3** (Single-Coil / HFT) | Passive Capacitive Partial-Split Network |
| **Pin 5** | **Isolated `+9V` / `+18V` Active Pickup Power** | **`+9V`** (or switchable **`+18V` EMG headroom rail**!) | **`+9V` Ultraclean LDO** (`TPS7A20`, `12 mA`) | **Hard-Disconnected (`0.0V`)** |
| **Pin 6** | **Auto-ID Sense Resistor (`ID_R` to GND)** | **`10 kΩ` resistor** built into EMG Sled | **`22 kΩ` resistor** built into Fishman Sled | **`Open / ∞` (No resistor)** on Passive Sled |

#### What Happens Automatically Inside the Guitar When You Snap In a Cartridge:
1. **Snap in a `Bare Knuckle` / `Lundgren` / `Seymour Duncan` Passive Cartridge (`Pin 6 = Open`):**
   * The **`Omron G6K-2F-Y` Normally-Closed (`0.0V`) mechanical relay** routes the pickup through the **`500 kΩ` passive volume pot deck** (in passive/zero-battery mode) and sets the active JFET buffer input impedance to **`1.0 MΩ`** (when using onboard `Green Screamer + NS-1 + NAM`).
   * The `+9V`/`+18V` pickup power rail on `Pin 5` is completely shut off (`0.0 mA`), and the **3-way toggle / push-push switch** controls **Full Humbucker vs. Inner Coil-Split**.
   * **Works 100% with ZERO batteries installed!**
2. **Snap in an `EMG 81 / 85 / 57` Active Cartridge (`Pin 6 = 10 kΩ`):**
   * The comparator detects the `10 kΩ` sense resistor on `Pin 6`, turns on the ultra-low-noise **`+9V` (or WebUI-selectable `+18V` for the famous EMG 18V headroom mod!) regulator** on `Pin 5`, and switches the input load to the exact **`25 kΩ` active EMG load impedance** via a solid-state analog switch (`TI TS5A3159A`, `0.8 Ω` $R_{ON}$).
3. **Snap in a `Fishman Fluence Modern` Cartridge (`Pin 6 = 22 kΩ`):**
   * The comparator detects the `22 kΩ` sense resistor, supplies regulated **`+9V` (`12 mA`)** on `Pin 5`, sets the **`25 kΩ` Fluence load impedance**, and automatically maps `Pin 3` and `Pin 4` so you can switch between **Fluence Voice 1 (`Modern Active High Output`)**, **Voice 2 (`Crisp Passive Fluidity`)**, and **Voice 3 (`Single-Coil`)**!

---

### 1.4 Supported Hot-Swap Pickup Cartridges (6, 7 & 8-String)

| Brand | Popular Metal Models Supported | Type | Custom Shop Upgrade Price |
| :--- | :--- | :--- | :---: |
| **Seymour Duncan** *(Base Tier)* | `Black Winter`, `Nazgûl`, `Distortion (SH-6)`, `Jupiter (Wes Hauch)`, `Pegasus` | Passive (`100% Zero-Battery Ready`) | **Included (Base)** |
| **EMG Pickups** | `EMG 81`, `EMG 57` (Brushed Black Chrome / Gold / Stainless), `EMG 85`, `EMG 81X` (`9V` or `18V` selectable), `707`/`808` | Active (`3-Pin Quick-Connect`) | **+$40 – $65** |
| **Fishman Fluence** | `Fluence Modern Ceramic`, `Fluence Modern Alnico`, `Keith Merrow Custom`, `Tosin Abasi`, `Matt Heafy` | Active Multi-Voice (`3 Voices`) | **+$50 – $75** |
| **Bare Knuckle Pickups (BKP)** | `Ragnarok`, `Aftermath`, `Juggernaut`, `Miracle Man`, `Warpig`, `Nailbomb`, `Polymath` (Open-Coil, Carbon Fiber, or Battle-Worn Etched Titanium covers) | Hand-Wound UK Passive (`Zero-Battery Ready`) | **+$140 – $190** |
| **Lundgren Guitar Pickups** | `Model M6 / M7 / M8` (Meshuggah spec), `Black Heaven`, `The One` | Hand-Wound Swedish Passive (`Zero-Battery Ready`) | **+$150 – $195** |
| **DiMarzio** | `D Activator`, `Titan` (Jake Bowen), `Crunch Lab`, `Occult Classic` | Passive (`Zero-Battery Ready`) | **+$20 – $40** |

---

## 2. Customizable Analog Overdrive, Boost & Noise Suppressor System

Instead of soldering a fixed overdrive circuit onto the main motherboard, the **Analog Preamp + Noise Gate section** is engineered in **two customizable layers**:
1. **Swappable M.2-Style Analog Drive Cartridges (`22 × 60 mm` gold-finger daughterboards)** that snap into the rear electronics bay in 10 seconds with one thumbscrew.
2. **Digitally Controlled Analog Component Matrix (`CD4053` / `ADG1412` analog switches + `MCP4261` digital pots)** on the Universal Screamer Pro card so players can customize clipping diodes, bass tight-cut frequencies, and gate release curves live from the Wi-Fi WebUI!

### 2.1 Swappable Analog Overdrive Daughterboard Cartridges (Hardware Upgrades)

| Cartridge ID | Circuit Topology | Key Analog Components | Voicing & Metal Use Case | Upgrade Price |
| :--- | :--- | :--- | :--- | :---: |
| **Card 01 (Standard): `Green Screamer Pro (TS808 / TS9 /Keeley Mod)`** | Classic `720 Hz` mid-hump overdrive with switchable clipping & bass cut | `OPA1656` / `JRC4558D` + Symmetric `1S1588` Silicon, Asymmetric `SD1` Silicon, `LED` Crunch, or Clean Boost (`No Diode`) | Classic tight metal boost (`Drive = 0`, `Level = 10`, `Tone = 6`) in front of `5150` / `Dual Rectifier` / `Soldano` | **Included** |
| **Card 02: `Precision Horizon Drive` (`Apex` Style)** | Variable 6-position input `Attack` bass-cut filter + active `Bright` sheen | `OPA1652` + 6-pole switched film capacitor high-pass matrix (`90 Hz` to `850 Hz`) + dual MOSFET/Schottky clipping | Modern djent / progressive metal (`7-string` & `8-string` low `F#`/`E` clarity without mud) | **+$59** |
| **Card 03: `Grind / 33 Brutal Boost` (`Fortin` Style)** | `+22 dB` aggressive upper-mid/high-frequency pre-emphasis shelving boost | Discrete low-noise JFET + op-amp frequency-shaping boost with custom girth/grind EQ | Extreme downtuned chug (`Drop A` / `Drop E`), Meshuggah-style percussive pick attack | **+$49** |
| **Card 04: `Swedish Chainsaw HM-2W` (`Left Hand Wrath`)** | Dual-gyrator `85 Hz` ("Bottom") & `1.1 kHz` ("Treble") active resonant EQ + hard clipping | Quad op-amp active gyrator EQ + hard-clipped silicon diode array | Old-school Stockholm death metal (`Entombed` / `Bloodbath`) or blended parallel grit | **+$69** |
| **Card 05: `Silver Centaur Clean/Mid Boost` (`Klon` Charge-Pump `18V`)** | Internal `+18V` / `-9V` charge-pump headroom boost with dual-gang clean/dirty blend | `TC1044S` `18V` rail + germanium/Schottky clipping + clean-blend summing network | Liquid shred leads, edge-of-breakup prog cleans, huge `18V` analog headroom | **+$65** |

### 2.2 Built-In Customizable Parameters on the Standard `Green Screamer + NS-1 Keyed Gate` Card
Even without swapping physical cards, the standard **Card 01 (`Green Screamer Pro + NS-1 Keyed Gate`)** includes an onboard **Analog Mod Matrix** controllable from your phone/laptop over Wi-Fi (`http://guitar.local`):
* **4 Selectable Clipping Modes (Real Analog Relays/Switches):**
  1. `808 Classic` — Symmetric `2x 1S1588` silicon diodes (smooth, classic mid-focus)
  2. `Asymmetric Screamer` — `3x` silicon diodes (`2+1`, warmer, higher output, tube-like even harmonics)
  3. `Turbo Red LED` — `2x` red `3 mm` LEDs (`3.6V` forward voltage — huge open volume boost and crunch)
  4. `Pure Clean Boost` — Diodes lifted completely out of the feedback loop (`+20 dB` clean op-amp mid-boost)
* **4 Selectable Input Bass-Cut ("Tightness") Capacitors (`Attack` Switch):**
  * `Fat (0.1 µF -> 220 Hz)` \| `Classic TS (0.047 µF -> 720 Hz)` \| `Tight 7-String (0.022 µF -> 1.1 kHz)` \| `Djent Razor (0.01 µF -> 1.8 kHz)`
* **NS-1 / Zuul Keyed Noise Suppressor Customization:**
  * **Key Source:** `Pure Dry Pickup Sidechain Key` (recommended — never chokes sustain when you roll back Drive) vs. `Post-Screamer Track`.
  * **Threshold:** `-75 dBu` to `-15 dBu`
  * **Release Curve:** `Fast Chug (8 ms — staccato djent stops)` vs. `Natural Lead Decay (85 ms — smooth fadeout)`

---

## 3. Complete Hardware, Material & Finish Customization Catalog

Because the **Carbon Spine** is built from **6 modular CNC parts** bolted together around a central core, every single piece of hardware is interchangeable and can be sold as **Factory Custom Shop Options** or **Aftermarket Drop-In Upgrade Kits**:

### 3.1 Bridge & Headpiece Upgrades

| Option | Model / Specification | Weight | Price Tier |
| :--- | :--- | :---: | :---: |
| **Bridge Option A (Touring Rock-Solid Hardtail)** | **Hipshot `41100B` Fixed Headless Hardtail** (`10.5 mm` pitch, machined brass/steel saddles, zero spring cavity needed — frees up room for a **Quad-`18650` `14,000 mAh / 40-hour` battery pack!**) | `195 g` | **-$60 (Credit) or Base** |
| **Bridge Option B (Standard Floating Tremolo)** | **Hipshot `4HV060B` Floating Headless Tremolo** with Zero-Point return stop | `320 g` | **Included (Pro Base)** |
| **Bridge Option C (Ultralight Aerospace Titanium Bridge)** | **Custom CNC Grade-5 Titanium (`Ti-6Al-4V`) Saddles & Baseplate** with DLC (Diamond-Like Carbon) black coating and ceramic bearings | `185 g` | **+$220** |
| **Individual Mono-Rail Saddles (Multiscale 6/7/8)** | **ABM `3810` / Hipshot Solo** individual headless tuner bridges for fanned-fret (`25.5"–27.0"` / `26.5"–28.0"`) builds | `210 g` | **+$85** |

### 3.2 Detachable `3A` Upper Horn, `3B` Leg Rail & Rear `U-Guard` Material Tiers

Because the **`3A` Upper Horn**, **`3B` Lower Leg Rail**, and **Rear `U-Guard`** attach via standardized `16.0 mm` CNC dovetail sockets and `M4`/`M6` bolts, customers can mix-and-match or buy extra wing sets:

| Material Tier | Construction & Finish | Weight (`3A+3B+UGuard`) | Upgrade Price |
| :--- | :--- | :---: | :---: |
| **Tier 1: `7075-T6` Stealth Aluminum (Standard)** | 5-axis CNC `7075-T6` billet, glass-bead blasted + **Type III Matte Obsidian Black** or **Satin Titanium Grey** hard anodize | `215 g` | **Included (Base)** |
| **Tier 2: Solid 3K / Forged Carbon Fiber Ultralight** | CNC-milled from `8.0 mm` solid autoclaved `3K` Twill Matte Carbon or Forged Carbon plate — **cuts wing weight by 45%!** | `118 g` | **+$140** |
| **Tier 3: Grade-5 Aerospace Titanium (`Ti-6Al-4V`)** | 5-axis CNC solid Grade-5 Titanium in **Raw Bead-Blasted Satin**, **PVD Gold**, **DLC Black**, or **Heat-Anodized Purple/Blue Damascus** | `325 g` | **+$280** |
| **Ergonomic Wing Geometry Options** | **Shape 1:** `Standard Teardrop 3A + C-Rail 3B` \| **Shape 2:** `Classical V-Thigh Rest 3B` \| **Shape 3:** `Full-Body Silhouette Aero Wings` | Varies | **+$95 / extra wing set** |

### 3.3 Fretboard, Fretwire, Scale Length & Neck Profile Customization

| Category | Standard Spec | Custom Shop Upgrade Options | Upgrade Price |
| :--- | :--- | :--- | :---: |
| **Fretboard Material** | **Richlite Black Diamond** (100% humidity-proof, jet black) | **A-Grade Macassar Ebony**, **Pale Moon Ebony**, **Roasted Birdseye Maple**, or **Solid Woven Carbon Composite** | **+$60 – $140** |
| **Fretwire Spec** | **Jescar `FW57110-S`** Stainless Steel Jumbo (`2.79 × 1.45 mm`) | **Jescar `FW58118-S` Extra-Jumbo Stainless**, **Jescar `EVO Gold`** (nickel-free gold alloy), or **True Temperament** curved frets | **+$35 – $180** |
| **Side & Face Inlays** | **`2.5 mm` Cyan Luminlay** side dots (sterile no-inlay face) | **Green Luminlay (`SGY-25`)**, **Fiber-Optic LED Side Dots** (powered by onboard `18650` with switchable color!), or **Titanium Offset Ring Face Inlays** | **+$45 – $120** |
| **Neck Thickness Profile** | **`18.5 mm -> 20.0 mm` Modern Thin C/D** | **`17.0 -> 19.0 mm` Wizard Ultra-Thin**, **`19.5 -> 21.0 mm` Asymmetric Enduro/Trapezoid**, or **`20.5 -> 22.0 mm` Chunky C** (just a `.STEP` swap before CNC milling!) | **$0 – $50** |
| **Spine & Hardware Colorways** | **Matte Stealth Obsidian Black** + Raw Titanium accents | **Satin Gunmetal Grey**, **Matte Oxblood Crimson**, **Arctic Storm White Cerakote**, **OD Tactical Green**, or **Raw Brushed 7075 Aluminum** | **+$75 – $125** |

---

## 4. Recommended Tiered Product Lineup & Pricing Strategy (High-Margin Upsell Model)

By designing a **single CNC spine core** that accepts all of these modular options, you can offer **3 distinct product tiers** from the exact same CNC CAD files:

1. **Tier 1 — `"PURE ANALOG EDITION"` (`$1,699` Retail / `~$980` DIY Build Cost):**
   * Comes with **Passive Bare Knuckle / Seymour Duncan** (or **Active EMG 81 / Fishman**) pickup in the universal hot-swap bay + **Passive `500 kΩ` / `0.0V` True-Bypass Harness**.
   * Rear electronics bay ships empty (or with a single `9V` clip for EMGs) — making the guitar **featherlight (`1.75 kg / 3.85 lbs`)**, **100% battery-free** (with passive pickups), and **pre-wired to accept the Drop-In `NAM + Screamer + Wireless + Dual-18650` Upgrade Kit (`$299`) at any time in the future!**
2. **Tier 2 — `"STAGE WIRELESS & NAM PRO EDITION"` (`$2,199` Retail / `~$1,276` Build Cost):**
   * Includes the full onboard **Dual-`18650` (`7,000 mAh`) Battery Cradle**, **3-Mode Zero-Battery Fail-Safe Relay**, **Card 01 (`Green Screamer Pro + NS-1 Keyed Gate`)**, **Onboard `NAM` Neural Amp + Cab IR Engine**, and **`5.8 GHz` (`1.8 ms`) Wireless Transmitter + Receiver Pedal**.
3. **Tier 3 — `"TITANIUM CUSTOM SHOP FOUNDER'S EDITION"` (`$2,899+` Retail):**
   * Customer-selected **Bare Knuckle Battle-Worn / Lundgren M6 / EMG 57-66** pickup, **Grade-5 Titanium `3A`/`3B` Wings & `U-Guard`**, **2 Analog Drive Cartridges** (`Green Screamer Pro` + `Precision Horizon Drive` or `Fortin 33`), and the **Path B Carbon Tube Capsule + Dual-Laptop Nomad Backpack**.
