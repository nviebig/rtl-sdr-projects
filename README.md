# RTL-SDR Blog V4 - Complete Setup & Project Guide

A comprehensive guide for setting up the RTL-SDR Blog V4 software-defined radio on macOS. Includes installation instructions, frequency reference tables, antenna configurations, and ready-to-use scripts for common radio reception projects.

Perfect for beginners and experienced radio enthusiasts interested in exploring the radio spectrum.

---

## 📋 Quick Start

**Hardware Setup:**
1. Install RTL-SDR Blog custom drivers (see `ANTENNA_SETUP_CHECKLIST.md`)
2. Install SDR++ receiver software
3. Assemble antenna and connect dongle
4. Open SDR++ and tune to 100 MHz (FM radio test)

**Get Started Immediately:**
- See `README.md` below for 5 beginner projects
- See `ANTENNA_SETUP_CHECKLIST.md` for hardware assembly
- See `FREQUENCY_REFERENCE.md` for frequency database

---

## 📁 Files in This Folder

| File | Purpose |
|------|---------|
| **ANTENNA_SETUP_CHECKLIST.md** | Hardware assembly + physical setup guide |
| **FREQUENCY_REFERENCE.md** | Complete frequency list + optimal settings |
| **satellite_tracker.py** | Auto-predict satellite passes for recording |
| **aircraft_radar_setup.sh** | One-command launch for live aircraft tracking |
| **RTL-SDR_V4_Field_Manual.docx** | Official hardware manual & driver installation |

---

## 🚀 5 Beginner Projects

### 1️⃣ **FM Radio Reception** (⭐ Easiest)
The simplest first test - verify hardware works by listening to FM radio.

**Steps:**
1. Open SDR++
2. Click play button (top left)
3. Tune to **100 MHz**
4. Enable **WFM** demodulation
5. Click on colored peaks to tune to stations

**Expected:** Colored peaks in waterfall display = active FM stations
**Antenna:** Any length works (~50 cm optimal)
**Troubleshooting:** No signals? Check custom RTL-SDR drivers installed

### 2️⃣ **Weather Satellite Images** (⭐⭐ Intermediate)
Decode real-time weather satellite imagery.

**Requires:**
- Antenna extended to ~1.1 m per rod (for 137 MHz band)
- Clear sky view (window mount recommended)
- SatDump software (download from GitHub)

**Steps:**
1. Check satellite passes: https://www.heavens-above.com
2. Tune SDR++ to satellite frequency:
   - NOAA-15: 137.620 MHz
   - NOAA-18: 137.912 MHz
   - NOAA-19: 137.100 MHz
3. Set gain 45-50, enable WFM
4. Click Record button when satellite rises
5. Stop recording when satellite sets (~10 min)
6. Open **SatDump** → Load .wav file → Decode
7. View decoded weather image

**Duration:** ~10 minutes per satellite pass
**Result:** Cloud/weather imagery from orbit

### 3️⃣ **Aircraft Radar (ADS-B)** (⭐ Easy)
Track live aircraft positions in real-time.

**Quick start:**
```bash
./aircraft_radar_setup.sh
# Opens live map at http://localhost:8080
```

**Features:**
- Real-time aircraft positions
- Altitude, speed, flight number
- 100-300 km range (depends on antenna location)

**Frequency:** 1090 MHz (Mode S ADS-B)
**Antenna:** Any length works (~15-50 cm)

### 4️⃣ **Wireless Sensors** (⭐ Easy)
Detect home weather stations, tire sensors, and IoT devices.

```bash
rtl_433 -f 433.92M
```

**Detects:**
- Weather station sensors (temperature, humidity)
- Vehicle tire pressure monitors (TPMS)
- Smart home devices
- Wireless doorbells

**Frequency:** 433.92 MHz
**Antenna:** Short (~17 cm per rod)

### 5️⃣ **ISS Reception** (⭐⭐ Intermediate)
Receive transmissions from the International Space Station.

**Requires:**
- ISS pass prediction (https://www.heavens-above.com)
- Extended antenna (~1.1 m per rod)
- Clear view of sky during pass window

**What to receive:**
- Voice transmissions (145.800 MHz)
- APRS packet radio (145.825 MHz)
- SSTV slow-scan images (145.80 MHz)

**Tools:** Direwolf (APRS decoder), SatDump (SSTV decoder)
**Duration:** Only works during ISS passes (~10 min windows)

---

## 🔧 Software Reference

| Tool | Purpose | Install | Quick Start |
|------|---------|---------|-------------|
| **SDR++** | Main receiver GUI | Pre-installed | Open from Applications |
| **rtl_433** | Wireless sensor decoder | `brew install rtl_433` | `rtl_433 -f 433.92M` |
| **SatDump** | Satellite image decoder | Manual DL from github | GUI application |
| **Direwolf** | APRS/Packet radio | `brew install direwolf` | `direwolf -c sdr.conf` |
| **GQRX** | Alternative receiver | Pre-installed | Open from Applications |
| **dump1090** | Aircraft radar | See aircraft_radar_setup.sh | Run provided script |

---

## 📡 Antenna Setup by Frequency

| Use Case | Frequency | Rod Length | Tips |
|----------|-----------|-----------|------|
| **FM Radio** | 88-108 MHz | ~50cm each | Any setup works |
| **Weather Satellites** | 137-138 MHz | ~110cm each | Window mount + clear sky |
| **ISS** | 145.8 MHz | ~110cm each | Must catch live pass |
| **Amateur Radio** | 144-146 MHz | ~110cm each | Lots of activity |
| **Wireless Sensors** | 433.92 MHz | ~17cm each | Can be indoors |
| **Aircraft (ADS-B)** | 1090 MHz | ~15cm each | High location better |

**General rule**: Longer rod = better signal for lower frequencies

---

## ⚠️ Important Setup Notes

### Custom Drivers Required
**The V4 requires RTL-SDR Blog custom drivers** - standard macOS drivers will NOT work. These are already installed.

Verify:
```bash
which rtl_fm  # Should show /usr/local/bin/rtl_fm
```

### IF AGC Must Be Disabled
In SDR++ settings, disable **IF AGC** - it doesn't work correctly on the V4.

### USB-C Adapter
You'll need: **USB-A female to USB-C male adapter** (£4-6, Anker/Baseus brand)
- This is the ONLY external purchase required
- Everything else is in the box

### Coax Cable Tips
- Use the included 3m SMA coax cable
- Keeps the dongle away from your laptop (reduces heat/interference)
- Always route cables away from WiFi/USB 3.0 sources

---

## 🐛 Troubleshooting

**No signals appear in SDR++?**
- Check that RTL-SDR drivers are installed: `which rtl_fm`
- Disable IF AGC in SDR++ settings
- Restart SDR++ application
- Check System Information → USB that dongle is recognized

**Weak signals / lots of noise?**
- Reduce gain in SDR++ (try 30-40 instead of 50)
- Move antenna away from WiFi/USB 3.0 devices
- Try different mounting location
- Check coax cable connection

**Satellite reception not working?**
- Verify antenna rods extended to full length (~1.1m per rod)
- Mount antenna pointing at clear sky (window mount best)
- Check pass timing at https://www.heavens-above.com
- Extend antenna length for lower frequencies

---

## 📚 External Resources

- **Heavens-Above**: https://www.heavens-above.com (satellite pass predictions)
- **RTL-SDR Blog**: https://www.rtl-sdr.com (guides, projects, forum)
- **SDR++**: https://github.com/AlexandreRouma/SDRPlusPlus
- **SatDump**: https://github.com/SatDump/SatDump
- **Frequency Database**: https://radioreference.com
- **Amateur Radio Repeaters**: https://www.rptrs.net

---

## 🎯 Getting Started

1. **Setup:** Follow `ANTENNA_SETUP_CHECKLIST.md` for hardware and driver installation
2. **Reference:** Use `FREQUENCY_REFERENCE.md` for frequency database and antenna lengths
3. **First Test:** Start with FM radio reception (easiest, immediate results)
4. **Next:** Try aircraft radar or wireless sensors
5. **Advanced:** Record satellite passes and decode images
6. **Explore:** Visit [RTL-SDR Blog](https://www.rtl-sdr.com) for more projects

---

## 📚 File Guide

- **`README.md`** (this file) — Overview and 5 starter projects
- **`ANTENNA_SETUP_CHECKLIST.md`** — Hardware assembly and driver installation
- **`FREQUENCY_REFERENCE.md`** — Complete frequency database with optimal settings
- **`PREPARATION_SUMMARY.md`** — Setup checklist and troubleshooting
- **`aircraft_radar_setup.sh`** — One-command ADS-B aircraft tracker
- **`satellite_tracker.py`** — Predict satellite passes (requires N2YO API key)

---

## ⚠️ Important Notes

- **Custom Drivers Required**: V4 requires RTL-SDR Blog custom drivers, not stock macOS drivers
- **IF AGC**: Must be disabled in SDR++ settings for proper V4 operation
- **Antenna Length**: Varies by frequency (see FREQUENCY_REFERENCE.md)
- **USB-C Adapter**: Needed for MacBook connection (USB-A dongle to USB-C)

---

## 🔗 Resources

- **[RTL-SDR Blog](https://www.rtl-sdr.com)** — Official guides and projects
- **[Heavens-Above](https://www.heavens-above.com)** — Satellite pass predictions
- **[RadioReference](https://radioreference.com)** — Frequency database
- **[SDR++](https://github.com/AlexandreRouma/SDRPlusPlus)** — Main receiver software
- **[SatDump](https://github.com/SatDump/SatDump)** — Satellite image decoder

---

**Happy exploring! 📡**
