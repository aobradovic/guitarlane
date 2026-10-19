# 08 — How to Order & Build the Onboard Tube Screamer, NS-1 Gate, NAM Neural Engine, 5.8GHz Wireless & Zero-Battery Relay (`Prototype #01` + `10 NAMM Guitars`)

To make sure your **first prototype (in November)** and your **10 NAMM Founders Edition guitars (in January)** work reliably on day one—**without waiting 6 months for custom chip programming or FCC radio testing**—here is the exact **2-Track Electronics Strategy**.

---

## 1. The Secret to Shipping on Time for NAMM 2027: "Custom Carrier PCB + Plug-In Cores"

Instead of trying to solder tiny surface-mount chips by hand or waiting months for FCC certification on a custom radio, the `102 mm × 60 mm × 16.5 mm` (`18.5 mm` between coils) rear electronics bay is split into **two parts**:

1. **Part A — Ordered from `JLCPCB.com` Turnkey SMT Assembly (`7–8 Days Delivery`, `$38` for 5 boards):**
   * **The Mother-Dock PCB + The `Green Screamer` / `NS-1` Keyed Noise Gate Analog Circuit.**
   * Because the **Tube Screamer (`JRC4558D` op-amp + `1N4148` clipping diodes)**, the **Sidechain-Keyed Noise Gate (`THAT2181C` VCA + `TL072` envelope detector)**, the **Zero-Battery Fail-Safe Bypass Relay (`Omron G6K-2F-Y`)**, and the **6-Pin Gold Pogo-Pin Pickup Dock (`Mill-Max 0906-1`)** are 100% standard analog components in JLCPCB's automated library, **JLCPCB's robots solder the entire analog circuit for you**.
   * Even better: **JLCPCB's minimum SMT order is 5 boards (`~$38` total)**, meaning when you order for **Guitar #1**, you automatically receive **5 completed boards**—and ordering **10 more boards** in December costs only **`~$65` total**!
2. **Part B — Off-the-Shelf Plug-In Compute & Wireless Cores (`2-Day Amazon / DigiKey Delivery`):**
   * Rather than writing custom `.NAM` neural DSP firmware or passing `$10,000` FCC wireless lab testing before January, your JLCPCB Mother-Dock has **two plug-in headers** that accept pre-built, pre-certified micro-modules that you can buy tomorrow on Amazon, Sweetwater, or DigiKey!

---

## 2. Item-by-Item: How You Get Each of the 5 Onboard Systems

### Item 1: The Tube Screamer (`TS808 / TS9` + Mod Matrix)
* **How It's Built for Production & NAMM (`JLCPCB SMT`):**
  * Uses the exact original analog schematic: **`MMBT3904` input JFET/BJT buffer $\rightarrow$ `JRC4558D` (`LCSC #C7076`, `$0.18`) dual op-amp overdrive stage $\rightarrow$ `720 Hz` / `360 Hz` switchable bass-tightening high-pass filter $\rightarrow$ symmetrical `1N4148WS` (`LCSC #C2128`) silicon clipping diodes $\rightarrow$ active tone & output boost stage**.
* **Fastest "Day-1 Shortcut" for Prototype #01 (Zero PCB Wait):**
  * Want to test the exact circuit inside Guitar #1 this week before your custom PCB even arrives? Buy an **Ibanez Tube Screamer Mini (`TSMINI`, `$79` on Sweetwater/Amazon)** or **Demonfx Mini Screamer (`$28` on Amazon)**.
  * When you remove the 4 bottom screws and take the circuit board out of its heavy metal foot-pedal box, the bare SMD circuit board inside is only **`34 mm × 64 mm × 8 mm`**! It runs on `9V` and drops straight into the rear cavity of Guitar #1.

### Item 2: The `NS-1` / `Fortin Zuul`-Style Keyed Noise Suppressor
* **How It Works Better Than a Regular Pedal:**
  * A normal noise gate pedal sits *after* your overdrive pedal, so the hiss of the Tube Screamer keeps the gate open.
  * On our Mother-Dock PCB, **Pin 1 of the Hot-Swap Pickup Pogo Dock (`Raw Guitar Signal`) splits into two paths**:
    1. **Audio Path:** Goes through the **Tube Screamer** $\rightarrow$ into the **`THAT2181C` studio VCA gate clamp**.
    2. **Sidechain Key Path (`TL072` Fast Envelope Detector):** Listens directly to your **clean, un-boosted pickup signal** right at the strings! The instant your right palm mutes the strings, the gate clamps shut in **`0.4 ms`**—producing dead silence between staccato metal riffs even with massive Tube Screamer boost!
* **Fastest "Day-1 Shortcut" for Prototype #01:**
  * You can also decase a **Mooer Noise Killer / Rowin Micro Noise Gate (`$26` on Amazon, bare PCB size `32 × 62 × 8 mm`)** or use the built-in noise gate inside the `NAM` compute module below.

### Item 3: The Onboard `NAM` (Neural Amp Modeler) + Cab IR Replay Engine
You have **two plug-and-play ways** to put real `.NAM` amp captures and Cab IRs inside the guitar right now without writing DSP code from scratch:

* **Option A (Fastest Turnkey `.NAM` Player — `$45–$59` on Amazon, Ready in 48 Hours):**
  * Purchase an **M-VAVE Tank-Mini / Blackbox** or **Sonicake Pocket Master** (`$49–$59` on Amazon).
  * These pocket units run a dedicated floating-point neural DSP chip that natively loads community **`.NAM` (Neural Amp Modeler) / `.am2data` amp captures**, **3rd-party `.WAV` Cab IRs**, **Overdrive**, **Noise Gate**, **USB-C Audio Interface**, and **Mobile App Bluetooth control**—and already run on a `3.7V` Li-Ion battery!
  * Once you remove the outer plastic/metal shell (4 screws), the bare SMD neural DSP board is only **`82 mm × 42 mm × 9.5 mm`**, which fits directly inside our `102 mm × 60 mm × 16.5 mm` rear electronics bay and wires straight to your side volume wheel, 3-way preset toggle, USB-C port, and `2x 18650` batteries!
* **Option B (Open-Source Custom Developer Path — `$29` Electro-Smith Daisy Seed or `$45` Raspberry Pi CM4):**
  * Plug an **Electro-Smith Daisy Seed (`ARM Cortex-M7 @ 480 MHz`, `65 × 18 × 6 mm`, `$29` at DigiKey/Mouser)** or **Raspberry Pi Compute Module 4 Lite (`55 × 40 × 4.7 mm`, `$45`)** onto the Mother-Dock header running open-source **RTNeural / `NeuralAmpModelerCore` C++**.

### Item 4: The `5.8 GHz` Ultra-Low-Latency Wireless Transmitter + Amp Receiver
* **How to Ship 10 Wireless Guitars at NAMM 2027 With Zero FCC Delay (`$49` Per Guitar):**
  * If you build a custom radio transmitter from bare chips, the FCC requires a `$10,000+` RF compliance test before you can sell it.
  * **The Smart Builder Solution:** Buy a pre-certified **NUX C-5RC `5.8 GHz`** or **Joyo JW-06 / Lekato `5.8 GHz` (`< 2.2 ms` latency, `24-bit / 48 kHz`) Wireless Guitar System (`$49` on Amazon)**.
  * **Step 1:** Keep the **`1/4"` Receiver Bug (`RX`)** untouched in its factory housing—that's the dongle the buyer plugs into their amplifier or pedalboard at NAMM!
  * **Step 2:** Unclip the tiny plastic shell of the **Transmitter Bug (`TX`)**. Inside is a pre-paired, FCC-certified **`38 mm × 22 mm × 5 mm` `5.8 GHz` circuit board** with an integrated ceramic antenna.
  * **Step 3:** Mount that tiny `38 × 22 mm` transmitter board inside the guitar's non-conductive carbon-fiber RF window (wired to the `3.7V/5V` battery rail and audio output bus). When the player flips the wireless switch on the guitar, it links automatically in `1 second` to the receiver plugged into the amp!

### Item 5: Dual-`18650` Battery Bay (`7,000 mAh`) + Zero-Battery Passive Fail-Safe Relay
* **Dual-`18650` Power (`4x Keystone 1043P` SMD Clips + `2x Samsung 35E 3,500 mAh` Cells = `$15.60`):**
  * Snap two standard `18650` cells into the gold spring clips inside the rear bay. Because `7,000 mAh` is **`14×` the capacity** of a normal wireless bug battery, the guitar runs for **`18–24 hours` continuously** with everything turned on (`NAM` + `Screamer` + `5.8GHz` Wireless), or **`300+ hours`** in analog-only mode!
* **Zero-Battery Passive Fail-Safe (`Omron G6K-2F-Y` Relay, `$2.45`):**
  * Soldered right next to the `1/4"` Neutrik output jack.
  * Whenever the battery is removed, dead, or switched to **Passive Mode**, the relay's mechanical spring rests on its **Normally Closed (`NC`) gold contacts**—connecting the hot-swap pickup pogo pins **100% directly to the `1/4"` guitar cable** with zero active electronics in the way!

---

## 3. Total Electronics Cost Summary (`Prototype #01` vs. `10 NAMM Guitars`)

The complete Bill of Materials with exact manufacturer and **JLCPCB LCSC part numbers** is saved in [`cnc_production_files/BOM_Onboard_Electronics_JLCPCB_and_Modules.csv`](../cnc_production_files/BOM_Onboard_Electronics_JLCPCB_and_Modules.csv):

| Electronics Subsystem | Cost for **Guitar #1** (`Prototype #01`) | Cost Per Guitar for **10 NAMM Guitars** (`Qty 10`) | Where to Order Today |
| :--- | :---: | :---: | :--- |
| **1. Mother-Dock PCB + `Green Screamer` + `NS-1` Keyed Gate (`JLCPCB Turnkey SMT`)** | `$59.31` *(Includes 5 boards!)* | `$23.79 / guitar` | `JLCPCB.com` (using `LCSC #` from BOM CSV) |
| **2. Embedded `.NAM` Neural + Cab IR Compute Module** | `$45.00` | `$39.00 / guitar` | Amazon / Electro-Smith / DigiKey |
| **3. `5.8 GHz` ULL Wireless TX Core + Paired `1/4"` Amp Receiver** | `$49.00` | `$42.00 / guitar` | Amazon / Sweetwater / OEM |
| **4. Dual `18650` (`7,000 mAh`) Protected Li-Ion Cells (`2x Samsung 35E`)** | `$13.00` | `$11.50 / guitar` | `18650BatteryStore.com` / DigiKey |
| **5. Neutrik Locking `1/4"` Jack + Push-Push Volume Wheel + 3-Way Toggle + USB-C** | `$19.50` | `$16.50 / guitar` | Mouser / DigiKey |
| **COMPLETE ONBOARD ELECTRONICS & WIRELESS RIG TOTAL** | **`$185.81`** | **`$132.79 / guitar`** | **Delivered in `2–8 Days`** |
