# Onboard Active DSP & Analog Rig Specification: Green Screamer + Keyed NS-1 Noise Gate + NAM Player + Ultra-Low-Latency Wireless + Wi-Fi Control

Yes — **all four systems** fit cleanly inside the `82 mm`-wide 5-axis CNC Spine Core with **zero increase in external dimensions**, turning the guitar into a self-contained, zero-cable rig that outputs a finished `Gate -> Green Screamer -> Neural Amp Modeler (NAM) -> Cab IR` signal both over **1/4" jack** and **uncompressed `< 2.0 ms` wireless**.

---

## 1. Signal Chain Architecture (Why Putting the Gate + Screamer Inside the Guitar Is Actually Superior to External Pedals)

```mermaid
flowchart LR
    PU["Fishman Fluence Modern\n(Raw Dry Humbucker)"] --> SPLIT["Internal Dry Split"]
    SPLIT -->|"Pure Dry Key Trigger"| KEY["NS-1 / Zuul Sidechain\nRMS Envelope Detector"]
    SPLIT -->|"Audio Path"| TS["Analog SMD 'Green Screamer'\n(OPA1678 + 720Hz HPF + Si Clipping)"]
    TS --> VCA["THAT2181 Blackmer VCA\nNoise Suppressor Clamp"]
    KEY -->|"Zero-Lag Gate Control"| VCA
    VCA --> ADC["24-Bit / 96kHz ADC\n(TI PCM3168A / AK4619)"]
    ADC --> NAM["Embedded NAM + Cab IR Engine\n(CM4/CM5 or STM32H7 / RTNeural)"]
    NAM --> DAC["24-Bit Stereo DAC\n(Line / Headphone / 1/4\" Out)"]
    NAM -->|"Digital I2S"| ULL["5.8GHz / 2.4GHz ULL Wireless TX\n(1.8ms Uncompressed Audio to Amp/DAW)"]
    WIFI["Onboard Wi-Fi 6 / BLE\n(WebUI App Control & .NAM Upload)"] <--> NAM
```

### The "4-Cable Method" Advantage Without Any Cables
On a traditional pedalboard, a noise gate placed *after* a Tube Screamer struggles because the Tube Screamer boosts the pickup's noise floor. Pro metal rigs use a **keyed sidechain gate** (like a Boss NS-1X / NS-2 in 4-cable mode or a Fortin Zuul) that listens to the **raw dry guitar pickup** to open and close a VCA located *after* the overdrive pedal.
* Because both circuits live **inside the guitar**, we tap the raw Fishman Fluence output **10 millimeters away** as the **Sidechain Key Trigger**, run the audio through the analog **Green Screamer**, and clamp the noise with a **THAT2181 VCA** right before the **NAM** input.
* **Result:** Dead-silent djent staccato stops even with a maxed-out Green Screamer into a high-gain 5150/Rectifier `.nam` profile!

---

## 2. Circuit-by-Circuit Hardware & Physical Footprint (`Total Board Area: 32 mm × 85 mm`)

The internal electronics bay on the right side of the `82 mm` CNC spine (`Y = 105 mm to 220 mm`) plus the rear cavity pocket provides **`95 mm × 34 mm × 24 mm`** of volume — more than enough for a stacked 2-board module + flat Li-Ion battery:

### Module A: Analog "Green Screamer" + Keyed NS-1 Noise Suppressor Daughterboard (`24 mm × 42 mm × 4 mm` 4-Layer SMD PCB)
1. **Green Screamer Stage (`12 × 18 mm` section):**
   * **Op-Amp:** Texas Instruments **`OPA1678`** (or classic **`JRC4558D`** in `SOIC-8` package) running on an internal `±9V` charge-pump rail (`LT1054`) for huge headroom.
   * **Tone Voicing:** Classic TS808/TS9 `720 Hz` high-pass shelving filter (`0.047 µF` film cap + `4.7 kΩ` resistor) that cuts flubby sub-bass before clipping and pushes the `750 Hz–1.2 kHz` pick-attack midrange, feeding symmetrical `1N4148` silicon clipping diodes.
   * **Metal "Tight Boost" Preset Mode:** Controlled via digital potentiometers (`MCP4261` SPI digipots) from the processor or Wi-Fi app (default metal boost setting: `Drive = 0–10%`, `Tone = 65%`, `Level = 100%`).
2. **NS-1 / Zuul Keyed Noise Suppressor Stage (`18 × 22 mm` section):**
   * **Detector:** Precision full-wave rectifier + dual-time-constant RMS envelope tracker driven directly by the pre-Screamer pickup signal.
   * **Gate VCA:** **`THAT2181C`** (or `SSI2164`) studio-grade Blackmer voltage-controlled amplifier placed *after* the Green Screamer (`-95 dB` attenuation when closed, `< 0.5 ms` opening attack, smooth program-dependent decay).

### Module B: Neural Amp Modeler (`NAM`) + Cab IR + Wi-Fi Control Engine (`30 mm × 55 mm × 6 mm`)
You have **two ways** to implement the onboard NAM engine:

| Approach | Hardware Module | Latency & Performance | Effort Level |
| :--- | :--- | :--- | :--- |
| **Option B1: Zero-Soldering Donor Board (Fastest Prototype)** | Strip the bare `36 × 60 mm` PCB out of an off-the-shelf **M-Vave Tank-Mini / Sonicake Pocket Master / Valeton GP-5** (or **IK Tonex One**) | `< 2.2 ms` latency, loads `.nam` / amp captures + Cab IRs + Bluetooth/USB app control out of the box | **Easiest (15 mins)** — costs **$45–$65**, zero custom firmware coding required! |
| **Option B2: Custom Embedded CM4/CM5 or Radxa Zero 3W (`RK3566`) Module** | **Radxa Zero 3W** (`30 × 65 mm`, Quad-Core Cortex-A55 @ 1.8GHz + NPU + **Onboard Wi-Fi 6 & BLE 5.2**) + **TI `PCM3168A`** 24-bit/96kHz I2S Codec | **`0.67 ms` DSP buffer (`32 samples @ 48kHz`)** running full desktop **`NeuralAmpModelerCore` (Standard WaveNet)** + stereo 2048-tap Cab IR | **Custom Pro Grade** — hosts a built-in **Wi-Fi WebUI (`http://guitar.local`)** so any phone or laptop can drag-and-drop `.nam` files and tweak Screamer/Gate knobs over Wi-Fi with zero app install! |

### Module C: Wireless Audio Transmitter ("Remote Signal Sender") vs. Wi-Fi Control
> [!IMPORTANT]
> **Why We Use Dual-Radio Architecture (Wi-Fi for Control + 5.8 GHz / 2.4 GHz ULL for Live Audio):**
> Standard Wi-Fi (`802.11`) has variable packet jitter (`8–25 ms`), which feels laggy under your picking hand. By pairing **Wi-Fi** (for wireless preset/parameter control & `.nam` file uploads) with a dedicated **Ultra-Low-Latency (`1.8 ms`) Digital RF Audio Transmitter** for the live guitar sound, you get zero-lag playability!

* **Live Guitar Audio Transmitter (`15 × 22 mm`):**
  * **Prototype Shortcut:** Embed the tiny internal transmitter PCB from a **NUX B-8 / Boss WL-20 / Joyo JW-06 (`5.8 GHz`, `24-bit/48kHz`, `< 2.2 ms` latency)** directly onto the guitar's internal output bus, paired with its plug-in receiver on your amp/interface.
  * **Production OEM Chip:** **Nordic `nRF5340 Audio` (`LC3plus` Ultra-Low-Latency)** or **Texas Instruments `CC8531` PurePath Wireless** (`1.6 ms` fixed latency, uncompressed `24-bit/48kHz`).
* **Where the Antenna Goes (Solving Carbon Fiber RF Shielding):**
  * Carbon fiber and aluminum block radio waves if the antenna is buried inside the metal spine.
  * **Solution:** Route the miniature `50 Ω` `U.FL` coaxial pigtail `25 mm` into the pickup cavity and adhere the flat `2.4 / 5.8 GHz` FPC flex antenna **directly underneath the non-conductive plastic Fishman soapbar cover (or under the `6.0 mm` Richlite fretboard heel)**. Richlite (paper-phenolic) and ABS plastic are **100% RF-transparent**, giving full `30-meter` (`100 ft`) line-of-sight range!

---

## 3. Power Budget & Rechargeable USB-C Battery Runtime

| Subsystem | Current Draw (`@ 5V`) | Power |
| :--- | :---: | :---: |
| **Fishman Fluence Modern Humbucker** | `2.5 mA` | `0.01 W` |
| **Analog SMD Green Screamer + Keyed NS-1 Gate** | `18 mA` | `0.09 W` |
| **NAM + Cab IR DSP Engine (Low-Power RT / RK3566 1-Core)** | `240 mA` | `1.20 W` |
| **5.8 GHz ULL Wireless Audio Transmitter (+ Wi-Fi Idle)** | `65 mA` | `0.33 W` |
| **Total Continuous Power Consumption** | **`~325 mA`** | **`~1.63 W`** |

* **Battery Cell:** 1x High-Density **`21700` (`5,000 mAh / 18.5 Wh`)** or flat pouch Li-Ion cell (`65 × 34 × 8 mm`) mounted in the CNC rear spine pocket, wired to a **USB-C PD Charging & Bypass BMS port** next to the 1/4" jack.
* **Total Unplugged Wireless Battery Life:** **`9.5 to 11 Hours`** of continuous playing per charge (and you can play indefinitely while plugged into any USB-C power bank or laptop).

---

## 4. External Controls on the `82 mm` Spine (Zero Clutter)
To keep the minimalist stealth aesthetic intact, you only need **two flush controls** on the right side wall of the `82 mm` spine:
1. **Knurled Rotary Encoder / Push-Push Volume Wheel:** Controls Master Output Volume; double-click to toggle **Bypass (Raw Pickup) vs. Active Rig (`Gate + Screamer + NAM + IR`)**.
2. **3-Way Mini Recessed Preset Toggle (or Capacitive Touch Strip) + Status LED:** Switches instantly between **Preset 1 (Tight Rhythm: NS-1 Gate + Green Screamer + 5150 NAM)**, **Preset 2 (Searing Lead: Screamer + Delay + Lead NAM)**, and **Preset 3 (Crystal Clean NAM)** — while all deep tweaking (`Screamer Drive/Tone`, `Gate Threshold`, and `.nam` file swapping) happens wirelessly over **Wi-Fi (`http://guitar.local`)** from your phone or laptop!
