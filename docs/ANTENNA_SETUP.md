# RTL-SDR V4 Antenna Arrival - Complete Setup Checklist

## 📦 Before the Antennas Arrive

### Hardware Verification Checklist
- [ ] RTL-SDR Blog V4 Dongle
- [ ] Telescopic dipole antenna rods (x2)
- [ ] Dipole base with SMA connector
- [ ] 3-metre coax extension cable (SMA male to SMA female)
- [ ] Mini flexible tripod (gorilla pod style)
- [ ] Suction cup window mount
- [ ] **⚠️ BUY: USB-A female to USB-C male adapter** (£4-6, Anker/Baseus recommended)

### Software Installation Status
- [ ] Homebrew installed
- [ ] RTL-SDR Blog custom drivers (v4 specific)
- [ ] SDR++ - primary receiver software
- [ ] dump1090-fa - aircraft radar decoder
- [ ] rtl_433 - wireless sensor decoder
- [ ] SatDump - satellite image decoder
- [ ] GQRX - alternative software (backup)
- [ ] Direwolf - APRS/packet radio decoder

### System Configuration
- [ ] RTL-SDR drivers blacklist configured
- [ ] macOS Gatekeeper allowed SDR++ access
- [ ] SDR++ configured to use RTL-SDR (librtlsdr) backend

---

## 🔧 Physical Assembly (When Antennas Arrive)

### Step 1: Assemble the Dipole Antenna
1. Take the dipole base with SMA connector
2. Screw the two telescopic dipole rods into the base
3. Extend each rod to appropriate length:
   - **General use**: ~17 cm each
   - **Satellite reception (137 MHz)**: ~53 cm each
   - **Meteor radio**: ~17 cm
   - **ISS reception**: ~53 cm

### Step 2: Connect Coax Cable
1. Connect the 3-metre SMA coaxial cable to the dipole base (SMA male to female)
   - This keeps the dongle away from your laptop
   - Reduces interference and heat exposure

### Step 3: Mount the Dongle
1. Connect USB-A female end of your adapter to the RTL-SDR V4 dongle
2. Plug the USB-C end into your MacBook
3. Place dongle in a stable position:
   - **Desktop**: Use flexible tripod
   - **Satellites**: Use suction cup on window with clear sky view
   - **Rooftop**: Secure with coax tension/cable management

---

## ✅ First Signal Check

1. Open **SDR++** from Applications folder
2. Click the **play button** (top left) to start receiver
3. Tune to **100 MHz** in the frequency box
4. Look for colored peaks in the waterfall display (FM radio stations)
5. Click a peak and enable **WFM** demodulation
6. You should hear audio from the station

### If No Signals Appear:
- [ ] Check dongle is recognized: **System Information → USB**
- [ ] Disable IF AGC in SDR++ settings
- [ ] Restart SDR++ application
- [ ] Check macOS Gatekeeper hasn't blocked the app
- [ ] Verify custom RTL-SDR drivers are installed (not stock macOS drivers)

---

## 🛰️ Common Projects to Try

### 1. Aircraft Radar (ADS-B)
```bash
dump1090-fa --net --interactive
```
Open browser to `localhost:8080` for live aircraft map

### 2. Weather Satellite Images
- Use **SatDump** GUI application
- Tune to NOAA satellites (137-138 MHz)
- Record and decode weather images

### 3. Wireless Sensors
```bash
rtl_433 -f 433.92M
```
Decode weather stations, TPMS tire sensors, smart home devices

### 4. ISS Packet Radio / SSTV
- Use **Direwolf** for APRS decoding
- Predicted passes at **Heavens-Above.com**
- Tune to 145.80 MHz for ISS

### 5. FM Radio + RDS
- Tune to any FM station (88-108 MHz)
- Enable RDS decoder in SDR++
- View station name, artist, song info

---

## 🐛 Troubleshooting Reference

| Problem | Solution |
|---------|----------|
| No signals detected | Verify RTL-SDR Blog custom drivers installed (not stock drivers) |
| Wrong frequencies displayed | Reinstall RTL-SDR drivers + disable IF AGC |
| macOS won't recognize dongle | Run blacklist command; restart |
| SDR++ app won't open | System Preferences → Security → Allow SDR++ |
| Audio crackling/distorted | Reduce gain, move away from WiFi/microwave |
| Signal drops when laptop moves | Check coax cable connection, RF shielding |
| Weak satellite signals | Extend antenna rods to full length, move to window |

---

## 📚 Quick Reference Links

- **SDR++**: https://github.com/AlexandreRouma/SDRPlusPlus (nightly builds)
- **SatDump**: https://github.com/SatDump/SatDump
- **Satellite Passes**: https://www.heavens-above.com
- **Frequency List**: https://radioreference.com (searchable)
- **RTL-SDR Blog**: https://www.rtl-sdr.com (guides & projects)

---

## 📝 Notes

- **Always use the RTL-SDR Blog custom drivers** - standard macOS drivers won't work correctly with V4
- **IF AGC must be disabled** on V4 for proper operation
- **Antenna length matters** - it's tuned for specific frequency ranges
- **Coax quality affects signal** - the included 3m cable is quality-rated
- **Location matters** - higher elevation = better reception

---

**Status**: Equipment ordered and software pre-installed ✅
**Next steps**: When antennas arrive, follow "Physical Assembly" section above.
