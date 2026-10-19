# Modular Customization, Hot-Swap Pickups, Analog Drive Cartridges & Hardware Upgrade Architecture

To turn the **Carbon Spine (`UNISPAR` / `MONOSPAR`)** into a high-margin, infinitely customizable platform—where a player can order **EMG, Fishman Fluence, Bare Knuckle, Lundgren, Seymour Duncan, or DiMarzio** pickups, swap between **Green Screamer, Precision Drive, Fortin 33, or HM-2** analog circuits, and upgrade bridges, wings, frets, and finishes at purchase or after purchase—every subsystem is engineered around **standardized mechanical envelopes and tool-free electrical interconnects**.

![Modular Customization Ecosystem — Hot-Swap Pickups, Analog Drive Cards & Hardware Upgrades](../images/02_cnc_specs_and_blueprints/08_modular_custom_pickups_drive_cards_and_hardware_upgrades.jpg)

---

## 1. Universal Hot-Swap Pickup Bay (`EMG` + `Bare Knuckle` + `Fishman` + `Lundgren` + `Seymour Duncan`)

### 1.1 The Mechanical Secret: One `71.0 × 39.0 mm` Master Cavity + Precision CNC Adapter Bezels
In the metal guitar world, pickups come in **two different physical footprints**:
1. **Active / Soapbar Footprint (`70.0 × 38.0 mm` rounded rectangle, screwless exterior):** Used by **EMG** (`81`, `85`, `57`, `60`, `81X`, `707`, `808`), **Fishman Fluence Modern / Abasi / Keith Merrow**, and **Seymour Duncan Blackouts** (and optional soapbar covers from Bare Knuckle / Lundgren).
2. **Standard Open-Coil / Covered Passive Humbucker Footprint (`68.5 × 37.0 mm` coil body with side mounting tabs):** Used by **Bare Knuckle Pickups (BKP)** (`Aftermath`, `Ragnarok`, `Juggernaut`, `Nailbomb`, `Warpig`, `Painkiller`), **Lundgren** (`M6`, `M7`, `M8`, `Black Heaven`), **Seymour Duncan** (`Nazgûl`, `Black Winter`, `Distortion`, `Alpha/Omega`), and **DiMarzio** (`D Activator`, `Titan`).

**How our CNC Spine accepts 100% of both without ever modifying the guitar body:**
* **Master CNC Pickup Cavity (`71.0 mm × 39.0 mm × 16.0 mm` deep):** Milled into the `82 mm` spine with two recessed brass `M3` threaded inserts at the standard soapbar/tab spacing plus a flush **6-Pin Gold Pogo-Pin / Quick-Connect Header** mounted in the floor of the cavity.
* **Two Interchangeable CNC Carbon/Titanium Trim Bezels (`2.0 mm` thick):**
  * **Bezel Type A (`Soapbar Flush Bezel`):** Drops directly around any `70 × 38 mm` **EMG** or **Fishman Fluence** soapbar.
  * **Bezel Type B (`Open-Coil / BKP Battle-Worn Adapter Ring`):** A flush `71 × 39 mm` outer / `68.8 × 37.3 mm` inner CNC anodized aluminum or carbon trim ring with hidden countersunk pockets for the passive humbucker's side mounting ears—allowing **any standard Bare Knuckle, Lundgren, Seymour Duncan, or DiMarzio open-coil or battle-worn covered humbucker** to drop straight into the exact same `71 × 39 mm` soapbar pocket with zero gap!

---

### 1.2 The Universal 6-Pin Active/Passive Quick-Connect Header & Auto-Impedance Switch
Whether the customer chooses **Active EMG (`9V`/`18V` at `25 kΩ`)**, **Active Fishman Fluence (`9V` Multi-Voice)**, or **Passive Bare Knuckle / Lundgren (`0V` at `500 kΩ` + Coil-Split)**, every pickup clips onto a small **$4 Universal Carrier Sled** on the underside of the pickup that mates with the spine's 6-pin header:

| Pin | Function | Active EMG (`81` / `57`) | Active Fishman Fluence | Passive Bare Knuckle / Lundgren / SD |
| :---: | :--- | :--- | :--- | :--- |
| **Pin 1** | **Hot Signal Output** | EMG Quick-Connect White | Fluence Hot | North Start (Black/Red) |
| **Pin 2** | **Signal Ground / Shield** | EMG Braid/Ground | Fluence Ground | South Start + Bare Shield |
| **Pin 3** | **Coil-Tap / Voice 2** | EMG `89`/`TW` Dual-Mode | Fluence Voice 2 Select | North Finish + South Finish (Series/Split Link) |
| **Pin 4** | **Voice 3 / High-Freq Tilt** | NC | Fluence Voice 3 (Single Coil) | Passive Capacitive Partial-Split |
| **Pin 5** | **Isolated `+9V` / `+18V` Active Pickup Rail** | `+9V` (or selectable `+18V` boost!) | `+9V` Regulated LDO (`12 mA`) | Disconnected (`0.0V` pure passive) |
| **Pin 6** | **Sense Pin (`ID_R`)** | `10 kΩ` to GND (`Active Mode`) | `22 kΩ` to GND (`Fluence Mode`) | `Open / ∞` (`Passive 500kΩ + 0V Relay Mode`) |

* **Automatic Active vs. Passive Detection (`Pin 6`):**
  * When a **Bare Knuckle, Lundgren, or Seymour Duncan passive pickup** is plugged in (`Pin 6 = Open`), the guitar automatically enables the **`500 kΩ` passive load** and the **`Omron G6K-2F-Y` `0.0V` Zero-Battery Passive Relay**—so the guitar works **100% without batteries** and also feeds the high-impedance `1 MΩ` `OPA1656` JFET buffer when active DSP is turned on.
  * When an **EMG (`81`/`85`/`57`)** or **Fishman Fluence** is plugged in (`Pin 6 = 10kΩ/22kΩ`), the guitar automatically switches input loading to **`25 kΩ` active voicing** and turns on the ultra-clean **`+9V` (or selectable `+18V` EMG headroom mod!) LDO regulator** powered from the Dual-`18650` cells, USB-C bus power, or TRS phantom power—plus we include a secondary snap-in `9V` alkaline backup clip inside the battery bay so even an EMG player can pop in a standard gas-station `9V` battery in an emergency!

---

### 1.3 Supported Factory & Upgrade Pickup Menu (6, 7 & 8-String)

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
