# Onboard Active DSP & Battery-Free Passive Fail-Safe Specification: Green Screamer + Keyed NS-1 Noise Gate + NAM Player + Wireless/Wi-Fi + Zero-Battery True Bypass

All four onboard systems (**Analog Green Screamer**, **Keyed NS-1/Zuul Noise Suppressor**, **Neural Amp Modeler [`NAM`] + Cab IR**, and **5.8 GHz Ultra-Low-Latency Wireless + Wi-Fi 6**) fit cleanly inside the `20 mm`-deep lower cavity underneath the pickup (`Y = 116 mm to 212 mm`) alongside a **quick-swap Dual-18650 (`7,000 mAh`) battery cradle** — AND the guitar is engineered with a **Normally-Closed Zero-Power Mechanical Relay + High-Gain Passive Soapbar Pickup** so it **works 100% without batteries at any time**.

![Underside Dual-18650 Battery Bay, NAM/Screamer/Gate Board & Side Control Panel](../images/02_cnc_specs_and_blueprints/07_onboard_battery_nam_screamer_cutaway_and_controls.jpg)

---

## 1. How the Guitar Runs 100% WITHOUT Batteries (3 Battery-Free Operating Modes)

> [!IMPORTANT]
> **Critical Design Rule:** An active-only pickup (like a standard 9V-only pickup) goes completely dead if the battery dies or is removed for an international flight. To guarantee the guitar **always works with zero batteries installed**, we use a **High-Gain Passive Ceramic Soapbar Humbucker** (e.g., **Lundgren M6 Soapbar**, **Bare Knuckle Ragnarok Soapbar**, or **Seymour Duncan Black Winter / Nazgûl Soapbar** in a `70 × 38 mm` matte-black housing) paired with a **Normally-Closed (`NC`) Mechanical Bypass Relay (`Omron G6K-2F-Y`)**.

```mermaid
flowchart LR
    PU["High-Gain Passive Ceramic Humbucker\n(Lundgren M6 / BKP / Duncan Soapbar)"] --> RELAY_IN["Omron G6K-2F-Y\nNormally-Closed Fail-Safe Relay"]
    
    RELAY_IN -->|"NO POWER / BATTERIES REMOVED\n(0.0V Default Resting Contact)"| VOL_PASSIVE["Passive 500kΩ Master Volume\n(Dual-Gang Pot Deck A)"]
    VOL_PASSIVE --> JACK["Neutrik 1/4\" Locking TRS Jack\n(100% Passive Guitar Output!)"]

    RELAY_IN -->|"POWER PRESENT (Batteries, USB-C, or TRS)\n& Active Rig Engaged"|BUF["Ultra-Low-Noise JFET Buffer\n(1MΩ Input Impedance)"]
    BUF -->|"Pure Dry Key Trigger"| KEY["NS-1 / Zuul Sidechain\nRMS Envelope Detector"]
    BUF -->|"Audio Path"| TS["Analog SMD 'Green Screamer'\n(OPA1678 + 720Hz HPF + Si Clipping)"]
    TS --> VCA["THAT2181 Blackmer VCA\nNoise Suppressor Clamp"]
    KEY -->|"Zero-Lag Gate Control"| VCA
    VCA --> NAM["Embedded NAM + Cab IR Engine\n(24-Bit / 96kHz Codec + ARM NEON)"]
    NAM --> VOL_ACTIVE["Active Output Level\n(Dual-Gang Pot Deck B)"]
    VOL_ACTIVE --> JACK
    NAM -->|"Digital I2S"| ULL["5.8GHz ULL Wireless TX\n(1.8ms Uncompressed Audio)"]
```

### The 3 Ways to Play With Zero Batteries Installed in the Cradle:
1. **Mode A — 100% Passive Analog Guitar Mode (`0 Batteries` + Standard `1/4"` Guitar Cable):**
   * When the `18650` battery cradle is empty (or the batteries run down to `0%`, or you pull/click the Push-Push Volume Wheel to **Passive Bypass**), the **`Omron G6K-2F-Y` gold-clad mechanical relay** requires `0.0 mW` to rest on its **Normally-Closed (NC)** contacts.
   * This routes the passive soapbar humbucker through Deck A of the `500 kΩ` volume thumbwheel straight to the `1/4"` Neutrik output jack via pure copper traces — zero electronics in the signal path.
2. **Mode B — Battery-Free Full DSP Mode Over USB-C (`0 Batteries` + USB-C Cable):**
   * Even with the `18650` batteries completely removed from the guitar (saving `95 grams` of weight), plugging any **USB-C cable** from a laptop, phone, tablet, or USB power bank into the side USB-C port automatically powers the **Green Screamer + NS-1 Gate + NAM Engine + 5.8 GHz Wireless** via an onboard **TI `TPS2121` Power-Path Multiplexer** (and streams 24-bit digital audio straight to your DAW over USB-C at the same time).
3. **Mode C — Battery-Free Full DSP Mode Over `1/4"` TRS "Phantom Power" Guitar Cable (`0 Batteries` + TRS Cable):**
   * The **Neutrik `NJ3FP6C-BAG`** jack is wired as a stereo **TRS** socket: **Tip** = Guitar Audio Output, **Ring** = `9V–12V DC` Phantom Power Input (protected by a Schottky bridge diode so plugging in a normal mono TS guitar cable safely shorts Ring to Ground without harm), **Sleeve** = Ground.
   * With a simple passive TRS power injector box on your pedalboard or desk, your regular guitar cable powers the entire onboard **Green Screamer + NS-1 Gate + NAM** rig indefinitely with **zero batteries inside the guitar**.

---

## 2. Internal Spatial Layout Inside the `82.0 × 38.0 mm` CNC Spine (1:1 Millimeter Allocation)

![1:1 Millimeter CNC Blueprint — Integrated Batteries, Green Screamer, NS-1 Gate, NAM & Wireless](../images/02_cnc_specs_and_blueprints/01_master_1to1_mm_cnc_blueprint.png)

In the lower spine section between the 24th fret (`Y = 217 mm`) and the Hipshot tremolo (`Y = 86 mm`), the spine is **`82.0 mm` wide × `38.0 mm` thick**:
* **Top `15.5 mm` (`Z = 0.0 to -15.5 mm`):** Houses the `3.0 mm` carbon top skin, the **`70 × 38 × 14 mm` Soapbar Humbucker**, the **`5.8 GHz / Wi-Fi` FPC antenna** tucked beneath the non-conductive plastic pickup bezel, and a `2.5 mm` solid CNC aluminum electromagnetic shield bulkhead (`Z = -13.0 to -15.5 mm`) that isolates the pickup from any digital switching noise.
* **Bottom `20.0 mm` (`Z = -15.5 to -35.5 mm`, covered by a `2.5 mm` Flush Magnetic Carbon Rear Access Hatch):** Split longitudinally into two isolated CNC compartments:
  1. **Left Compartment — Dual-`18650` Quick-Swap Battery Bay (`X = -37.0 to -1.0 mm`, `Y = 118 to 190 mm` = `72 × 36 × 20 mm`):**
     * Holds **2x Protected `18650` Li-Ion Cells** (`Ø 18.5 × 65.2 mm` each, e.g., **Samsung `35E` or Molicel `M35A`**, `2 × 3,500 mAh = 7,000 mAh / 25.9 Wh` in parallel `1S2P` configuration) inside gold-plated spring clips + a 5-LED fuel gauge bar.
     * You can charge the cells internally at `30W` via the side **USB-C port**, swap in two fresh `18650` cells in 5 seconds via the magnetic carbon backplate, or pop both cells out to fly or play battery-free.
  2. **Right Compartment — Active Analog + NAM DSP Stack (`X = +1.0 to +37.0 mm`, `Y = 118 to 212 mm` = `94 × 36 × 20 mm`):**
     * **Upper Board (`Z = -17.5 to -24.0 mm`, `32 × 66 mm` 4-Layer Shielded SMD PCB):**
       * **Omron `G6K-2F-Y` Zero-Power Passive Bypass Relay** + **TI `TPS2121` Auto-Switching Power Mux** (`Battery` / `USB-C` / `TRS Ring DC`).
       * **JFET High-Impedance Input Buffer (`OPA1656`)** splitting the dry pickup signal immediately into the **NS-1 / Zuul Keyed Sidechain RMS Detector** and the **Analog SMD "Green Screamer"** (`OPA1678` + `720 Hz` mid-hump high-pass filter + `1N4148` symmetrical silicon clipping + `MCP4261` digital pots) followed by the **`THAT2181C` Blackmer VCA Noise Suppressor Clamp**.
     * **Lower Board (`Z = -26.0 to -34.0 mm`, `32 × 66 mm`):**
       * **Embedded `NAM` (Neural Amp Modeler) + Cab IR + Wi-Fi 6 Compute Module** (`Radxa Zero 3W` / `RPi CM4/CM5` or donor `NAM` pocket engine) + **TI `PCM3168A` 24-bit/96kHz Audio Codec**, thermally coupled via a `1.5 mm` silicone pad to the internal CNC aluminum bulkhead for silent fanless cooling.
     * **Upper Heel RF Window (`Y = 193 to 214 mm`):**
       * **`5.8 GHz` Ultra-Low-Latency (`1.8 ms`) Uncompressed Wireless Audio Transmitter** (`TI CC8531` / `Nordic nRF5340` or embedded `NUX B-8 / Boss WL-20` TX module).

---

## 3. Side-Wall Ergonomic Control Panel (`X = +41.0 mm`, Right Spine Edge)

1. **Recessed Knurled Dual-Gang Volume Thumbwheel + Push-Push Switch (`Y = 164–182 mm`):**
   * Controls output volume in both Active and Passive modes.
   * **Push-Push Click:** Mechanically switches between **Active Rig Mode (`Gate -> Screamer -> NAM -> Cab IR + Wireless`)** and **100% Passive True-Bypass Mode** (and automatically drops to Passive True-Bypass if batteries are removed and no USB-C/TRS power is connected).
2. **3-Way Preset Toggle Switch + Cyan/Green RGB LED (`Y = 143–154 mm`):**
   * **Up (`RHYTHM`):** Tight Metal Chug (`NS-1 Keyed Gate [Hard]` + `Green Screamer [Drive 5%, Tone 65%, Level 100%]` + `5150 / Dual Rec NAM` + `4x12 V30 Cab IR`).
   * **Center (`LEAD`):** Liquid Shred Lead (`NS-1 Gate [Soft]` + `Green Screamer [Drive 35%]` + `High-Gain Lead NAM` + `Stereo Delay` + `Cab IR`).
   * **Down (`CLEAN`):** Crystal Acoustic/Clean (`Screamer Bypassed` + `Boutique Clean Tube Amp NAM` + `Chorus/Reverb`).
3. **Waterproof USB-C Port (`Y = 122–133 mm`):**
   * **30W Fast Battery Charging**, **Battery-Free Bus Power**, **24-Bit/96kHz Class-Compliant USB-C Audio Interface** (record straight into your laptop DAW with one USB-C cable), and `.nam` profile loading.
4. **Flush Neutrik `NJ3FP6C-BAG` Locking `1/4"` TRS Jack (`Y = 96–112 mm`):**
   * Works with any standard mono `1/4"` guitar cable (in both Active and Battery-Free Passive modes) or a stereo TRS cable for battery-free phantom power.
