# RTL-SDR V4 Antenna Arrival - Preparation Summary

**Prepared on:** 2026-05-28  
**Status:** 100% Ready for antenna arrival

---

## What You're Getting

Your RTL-SDR Blog V4 package includes:
- RTL-SDR Blog V4 Dongle (RTL2832U + R828D Tuner)
- Telescopic dipole antenna rods (x2)
- Dipole base with SMA connector
- 3-metre coax extension cable (SMA connectors)
- Mini flexible tripod
- Suction cup window mount
- **Still need to buy:** USB-A female to USB-C male adapter (~£4-6)

---

## Software Installation Complete

### Drivers Installed
- RTL-SDR Blog custom drivers (v4 specific)
- Homebrew package manager
- Supporting libraries (cmake, libusb, pkgconfig)

### Applications Installed
- SDR++ (primary receiver software)
- rtl_433 (wireless sensor decoder)
- GQRX (alternative receiver)
- Supporting tools

### Configuration Complete
- Custom drivers configured in /usr/local/lib
- macOS driver blacklist configured
- All permissions set correctly

---

## Documentation Prepared

### 1. **README.md** (START HERE)
   - Overview of all files
   - Quick start checklist
   - 5 beginner projects with step-by-step instructions
   - Software reference table
   - Troubleshooting guide
   
### 2. **ANTENNA_SETUP_CHECKLIST.md**
   - Hardware checklist (verify everything is in the box)
   - Physical assembly instructions
   - First signal check procedure
   - Detailed troubleshooting
   - Common project guides

### 3. **FREQUENCY_REFERENCE.md**
   - Complete frequency table (FM, Aircraft, Satellites, ISS, Weather, etc.)
   - Optimal antenna lengths by frequency
   - Demodulation modes (WFM, NFM, AM, SSB, CW)
   - SDR++ quick settings for each use case
   - Recording & post-processing guide

### 4. **RTL-SDR_V4_Field_Manual.docx**
   - Official hardware manual
   - Complete driver installation steps
   - Hardware specifications
   - Original documentation from RTL-SDR Blog

---

## Executable Scripts Ready to Use

Located in `scripts/` folder:

### **aircraft_radar_setup.sh**
One-command aircraft tracking system:
```bash
cd scripts/
./aircraft_radar_setup.sh
# Opens live aircraft map at http://localhost:8080
```

### **satellite_tracker.py**
Predicts when satellites pass overhead:
```bash
cd scripts/
python3 satellite_tracker.py
# Shows NOAA/ISS/Meteor satellite passes for your location
```
**Note:** Requires free N2YO API key (instructions in script)

---

## 5 First Projects Ready to Try

| # | Project | Complexity | Time | Antenna Length |
|---|---------|-----------|------|---|
| 1 | FM Radio Reception | Easy | 5 min | Any (~50cm) |
| 2 | Weather Satellites | Medium | 20 min | ~110cm (full) |
| 3 | Aircraft Radar (ADS-B) | Easy | 5 min | ~15cm |
| 4 | Wireless Sensors (433 MHz) | Easy | 5 min | ~17cm |
| 5 | ISS Reception | Medium | Live event | ~110cm (full) |

**Recommended order:** Try #1 (FM) → #3 (Aircraft) → #4 (Sensors) → #2 (Satellites) → #5 (ISS)

---

## Timeline When Antennas Arrive

### **0-15 minutes: Physical Assembly**
1. Unbox all components
2. Verify everything matches ANTENNA_SETUP_CHECKLIST.md
3. Assemble dipole antenna (rods + base)
4. Connect coax cable
5. Plug into MacBook with USB-C adapter

### **15-20 minutes: First Signal Test**
1. Open SDR++
2. Click play button
3. Tune to 100 MHz (FM radio)
4. Should see colored peaks in waterfall
5. Enable WFM and listen to FM stations

### **20+ minutes: First Real Project**
- **Easy:** Run aircraft_radar_setup.sh → see live aircraft on map
- **Medium:** Predict satellite pass → record → decode weather image
- **Advanced:** Catch next ISS pass → record packet radio

---

## Before Running First Project

**You will need:**
- [ ] USB-A to USB-C adapter (the ONLY external purchase!)
- [ ] This folder on your MacBook
- [ ] Internet access (for frequency lookups, satellite predictions)
- [ ] Optional: External window mount (for satellites/ISS)

**Quick verification:**
```bash
# Test that drivers installed correctly:
which rtl_fm              # Should show /usr/local/bin/rtl_fm
which rtl_433             # Should show /opt/homebrew/bin/rtl_433

# Test that SDR++ can find dongle:
# (will be done when you plug in the hardware)
```

---

## Troubleshooting Quick Reference

| Problem | Solution | Reference |
|---------|----------|-----------|
| SDR++ won't open | System Preferences → Security → Allow | ANTENNA_SETUP_CHECKLIST.md |
| No signals on 100 MHz | Verify RTL-SDR Blog drivers (not stock) | README.md Troubleshooting |
| Weak signals | Reduce gain to 30-40, move antenna | FREQUENCY_REFERENCE.md |
| Satellite images unclear | Extend antenna to full length (1.1m) | ANTENNA_SETUP_CHECKLIST.md |
| rtl_433 not working | Install manually: `brew install rtl_433` | README.md |

---

## Frequencies You'll Use Most

| What | Frequency | Why |
|------|-----------|-----|
| FM Radio | 100 MHz | Test your setup works |
| Aircraft Radar | 1090 MHz | See live aircraft on map |
| Weather Satellites | 137.6 MHz | Decode weather images |
| ISS | 145.8 MHz | Catch live passes |
| Sensors | 433.92 MHz | Detect temperature, tire sensors |

---

## Learning Path Suggested

**Day 1:**
- [ ] Read README.md (overview)
- [ ] Assemble antenna when it arrives
- [ ] Test FM radio (verify everything works)

**Day 2:**
- [ ] Try aircraft radar project (see live data immediately)
- [ ] Try wireless sensors (fun to decode devices around you)

**Week 1:**
- [ ] Catch a satellite pass (check Heavens-Above.com)
- [ ] Record and decode weather images
- [ ] Explore your local frequencies (radioreference.com)

**Week 2+:**
- [ ] Try ISS reception (when it passes overhead)
- [ ] Build your own antenna
- [ ] Explore advanced projects on rtl-sdr.com

---

## What's Already Installed

### Core Tools
```
RTL-SDR Blog drivers ..................... Installed
SDR++ (main software) ..................... Installed
rtl_433 (sensor decoder) .................. Installed
GQRX (alternative software) ............... Installed
Supporting libraries ...................... Installed
```

### External Tools (install when needed)
```
SatDump (satellite decoder) ............... GUI download needed
Direwolf (APRS/packet radio) .............. brew install direwolf
dump1090-fa (aircraft radar) .............. See aircraft_radar_setup.sh
```

---

## Quick File Guide

**When antennas arrive, open in this order:**
1. `README.md` — Overview + 5 beginner projects
2. `ANTENNA_SETUP_CHECKLIST.md` — Physical assembly guide
3. `FREQUENCY_REFERENCE.md` — Settings for specific frequencies
4. `aircraft_radar_setup.sh` — Run to see live aircraft
5. `satellite_tracker.py` — Run to predict satellite passes

---

## Success Indicators

**You'll know everything is working when:**
1. FM radio at 100 MHz shows colored peaks in SDR++
2. Aircraft appear on the map when running aircraft_radar_setup.sh
3. rtl_433 detects wireless devices in your home
4. SatDump successfully decodes satellite weather images
5. ISS packet radio appears during live passes

---

## Important Reminders

**USB-C Adapter Required**
- Your MacBook only has USB-C ports
- The dongle is USB-A
- You MUST buy USB-A female to USB-C male adapter
- ~£4-6, Anker or Baseus brand recommended

**Custom Drivers Essential**
- V4 requires RTL-SDR Blog custom drivers (already installed)
- Standard macOS drivers will NOT work
- If you get "no signals", check drivers installed

**IF AGC Must Be Disabled**
- In SDR++ settings, find "IF AGC" and DISABLE it
- This is critical for V4 dongle operation

**Antenna Length Matters**
- Different frequencies need different lengths
- See FREQUENCY_REFERENCE.md for optimal lengths
- Short rods (~50cm) work for FM
- Full rods (~110cm) needed for satellites/ISS

---

## Support Resources

- **Official RTL-SDR Blog**: https://www.rtl-sdr.com (guides, projects)
- **Satellite Predictions**: https://www.heavens-above.com
- **Frequency Database**: https://radioreference.com
- **SDR++ GitHub**: https://github.com/AlexandreRouma/SDRPlusPlus
- **SatDump**: https://github.com/SatDump/SatDump

---

## Preparation Checklist - Complete!

- [x] Read RTL-SDR V4 Field Manual
- [x] Installed RTL-SDR Blog custom drivers
- [x] Installed SDR++ receiver software
- [x] Installed supporting tools (rtl_433, GQRX, etc.)
- [x] Created comprehensive documentation (4 guides)
- [x] Prepared executable scripts (2 tools)
- [x] Set up frequency reference table
- [x] Created troubleshooting guides
- [x] Verified installations

---

**Your RTL-SDR setup is 100% ready for antenna arrival!**

When the antennas arrive:
1. Assemble antenna (15 minutes)
2. Test FM radio (5 minutes)
3. Start your first project

**Have fun exploring the radio spectrum!**

---

*Preparation completed: 2026-05-28 21:33 GMT+1*
*Ready for antenna arrival: YES*
