# RTL-SDR Blog V4 - Complete Setup & Project Guide

Welcome! Your RTL-SDR Blog V4 dongle with antennas is arriving soon. This folder contains everything you need to set up, test, and run interesting radio reception projects.

---

## 📋 Quick Start Checklist

**Before Antennas Arrive:**
- [x] ✅ RTL-SDR Blog custom drivers installed
- [x] ✅ SDR++ receiver software installed
- [x] ✅ Supporting tools installed (rtl_433, SatDump, etc.)
- [x] ✅ Configuration & reference guides prepared

**When Antennas Arrive (15 minutes):**
1. Assemble dipole antenna base with rods
2. Connect coax cable to dongle
3. Plug into MacBook with USB-C adapter
4. Open SDR++ and test FM radio (100 MHz)

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

## 🚀 First 5 Projects to Try

### 1️⃣ **FM Radio Reception** (5 minutes)
Easiest first test - you'll immediately hear audio.

```bash
# Open SDR++
# 1. Click play button
# 2. Tune to 100 MHz
# 3. Enable WFM demodulation
# 4. You should hear FM stations
```

**Expected**: Colored peaks in waterfall = FM stations on air
**Troubleshooting**: If no signals, check drivers installed (see ANTENNA_SETUP_CHECKLIST.md)

---

### 2️⃣ **Weather Satellite Images** (20 minutes)
Decode real-time weather satellite images.

**Equipment needed**:
- Antenna extended to ~1.1m per rod (for 137 MHz)
- Window mount or outdoor placement
- Clear view of sky

**Steps**:
1. Go to https://www.heavens-above.com
2. Find next NOAA-15/18/19 pass for your location
3. Open SDR++
4. Tune to 137.620 MHz (NOAA-15) or 137.912 MHz (NOAA-18)
5. Set gain to 45-50
6. Click Record when satellite rises above horizon
7. Stop when it sets
8. Open **SatDump** → Load recorded file → Select NOAA decoder
9. View decoded weather image!

**Expected**: Weather clouds visible in decoded image
**Duration**: ~10 minutes per pass

---

### 3️⃣ **Aircraft Radar (ADS-B)** (5 minutes)
See live aircraft positions on a map.

```bash
# Make script executable
chmod +x aircraft_radar_setup.sh

# Launch aircraft tracker
./aircraft_radar_setup.sh

# Open browser to: http://localhost:8080
```

**Expected**: 
- Live aircraft appearing on map
- Click aircraft for more info (flight number, altitude, speed)
- 100-300 km range depending on antenna height

**Frequency**: 1090 MHz (ADS-B)
**Antenna**: Any length works, but 30-50 cm optimal

---

### 4️⃣ **Wireless Sensors & IoT** (5 minutes)
Decode temperature sensors, tire sensors, smart devices.

```bash
# Detect all 433 MHz devices broadcasting
rtl_433 -f 433.92M

# Example output:
# Weather station: Temperature 22°C, Humidity 65%
# Tire sensor: Pressure 2.1 bar, Battery OK
```

**Frequency**: 433.92 MHz
**Antenna**: Can be short (~17cm per rod)
**Detects**: Weather stations, TPMS sensors, smart home devices, door bells

---

### 5️⃣ **ISS Packet Radio & SSTV** (live event)
Receive live transmissions from the International Space Station.

**Setup**:
1. Go to https://www.heavens-above.com
2. Find next ISS pass
3. Extend antenna fully (~1.1m per rod)
4. Tune SDR++ to 145.800 MHz
5. Enable NFM demodulation
6. Record during pass
7. Use **Direwolf** to decode packet radio
   - Or decode SSTV images (slow-scan TV)

**Expected**: Live voice from ISS + packet radio digipeater
**Only works**: When ISS passes overhead (check Heavens-Above for times)

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

## 🎯 Next Steps

1. **Read**: ANTENNA_SETUP_CHECKLIST.md (assembly guide)
2. **Read**: FREQUENCY_REFERENCE.md (settings for each band)
3. **When antennas arrive**: Follow physical assembly instructions
4. **Test**: Start with FM radio (easiest first project)
5. **Record**: Try satellite or ISS reception
6. **Explore**: Visit RTL-SDR.com for more project ideas

---

## 📝 Project Log

Use this space to track your projects:

```
Project: FM Radio Reception
Date: [Your date]
Frequency: 100.0 MHz (BBC Radio 1)
Result: ✅ Working perfectly
Notes: Good signal strength, clear audio

Project: Weather Satellite (NOAA-18)
Date: [Your date]
Frequency: 137.912 MHz
Result: ✅ Decoded image successfully
Notes: Extended rods to 1.1m, mounted at window

Project: Aircraft Radar
Date: [Your date]
Frequency: 1090 MHz (ADS-B)
Result: ✅ Tracking aircraft 200km+ away
Notes: Antenna extension affects range significantly
```

---

**Equipment Status**: ✅ Pre-installed & Ready
**Next Action**: Assemble antenna when it arrives
**Support**: See RTL-SDR blog forum if you get stuck

Good luck with your radio reception projects! 📡
