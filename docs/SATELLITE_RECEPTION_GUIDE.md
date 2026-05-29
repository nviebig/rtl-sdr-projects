# Satellite Reception with RTL-SDR - Complete Guide

**RTL-SDR is excellent for receiving satellites!** Despite what you might think, the hardware can't receive high-frequency satellite downlinks (10+ GHz), but it's perfect for the most accessible and rewarding satellite projects.

---

## What You CAN Receive

### 1. NOAA Weather Satellites ⭐ (Most Popular)

**Frequency:** 137.5–138 MHz (VHF)  
**Signal Type:** APT (Automatic Picture Transmission)  
**What You Get:** Real-time weather satellite imagery — clouds, storms, temperature

**Active Satellites:**
- **NOAA-15** — 137.620 MHz
- **NOAA-18** — 137.912 MHz  
- **NOAA-19** — 137.100 MHz
- **Meteor M2-4** — 137.100 MHz (Russian meteorological satellite)

**How It Works:**
1. Satellites pass overhead every 12 hours
2. Each pass lasts ~12 minutes
3. Signal gets stronger as satellite approaches, peaks at zenith, then fades
4. You capture raw APT data
5. Software decodes it into weather maps

**Required Hardware:**
- RTL-SDR dongle (any recent version)
- **Antenna:** Simple dipole or quarter-wave at ~137 MHz (~53 cm)
- Optional: LNA (Low Noise Amplifier) for better signal

**Software to Decode:**
- **WXtoImg** — Most popular, easy to use
- **QSSTV** — Versatile satellite/weather image decoder
- **SatDump** — Modern, open-source, excellent quality

**Difficulty:** ⭐ Beginner (very rewarding)

**Example Output:**
```
Pass Details: NOAA-19 overhead at 14:32 UTC
Maximum Elevation: 87° (nearly zenith)
Duration: 13 minutes

Decoded image shows:
- Cloud formations across UK and Europe
- Ocean temperature patterns (color-coded)
- Storm systems visible as bright white areas
- Detail: ~4 km resolution
```

---

### 2. ISS (International Space Station) ⭐ Popular

**Frequency:** 145.800 MHz (2m amateur radio band)  
**Signal Type:** FM voice transmissions  
**What You Get:** Live conversations between astronauts and ground stations

**Why ISS?**
- Humans are talking on this frequency
- Fastest orbiting object visible to humans (28,000 km/h)
- Passes overhead ~16 times per day
- Most rewarding experience: hearing actual astronaut voices

**How It Works:**
1. ISS crew uses amateur radio to communicate with ground
2. Transmissions are often directed to schools or public events
3. Sometimes open "voice check" transmissions
4. You can hear Russian, American, European astronauts
5. Signal is strong and clear

**Required Hardware:**
- RTL-SDR dongle
- **Antenna:** Simple dipole at ~145 MHz (~50 cm) works great
- Optional: External antenna for better range

**Software:**
- Any SDR software (SDR++, GQRX, CubicSDR)
- No special decoding needed—just listen!
- Optional: frequency scanner to catch transmissions

**Difficulty:** ⭐ Beginner (instant gratification)

**Example:**
```
14:45 UTC - ISS pass beginning
You tune to 145.800 MHz
Static... then suddenly...

"Houston, this is ISS. Copying well. Providing
downlink on 145.800. Standing by for school
contact in... 3... 2... 1..."

Clear, strong signal!
```

---

### 3. Iridium Satellites

**Frequency:** ~1.6 GHz (L-band)  
**Signal Type:** Digital bursts  
**What You Get:** Satellite phone transmissions (technical project)

**How It Works:**
- Network of 66+ low-Earth orbit communication satellites
- Each satellite periodically "flares" with strong signals
- You can detect and triangulate flares
- More technical than NOAA/ISS

**Required Hardware:**
- RTL-SDR (frequency range adequate)
- Directional antenna for better reception
- Software: GFSK demodulation tools

**Difficulty:** ⭐⭐ Intermediate (technical knowledge needed)

---

## What You CAN'T Receive (Yet)

### Geostationary Satellites (10+ GHz)

**Examples:** Weather satellites (GOES, Himawari), Communications, Broadcast  
**Frequency:** 10.5–12.5 GHz (C-band, Ku-band)  
**Why Not:** RTL-SDR hardware maxes out at ~2.5 GHz

**To Receive These, You Need:**
- Specialized receiver or upconverter
- Dish antenna (1–3 meters)
- LNA (very low-noise, <0.5 dB)
- High-gain amplifiers
- Cost: $500–$5000+

**But:** GOES and Himawari also transmit on NOAA APT band (137–138 MHz), so you can still receive their imagery!

---

## Quick Start: Receive NOAA Weather Imagery

### Step 1: Find Satellite Passes
Use online tools to find when NOAA satellites pass overhead:
- [N2YO.com](https://www.n2yo.com/) — Detailed pass predictions
- [Heavens-Above](https://www.heavens-above.com/) — Excellent for visual predictions
- [WXtoImg](https://wxtoimgrestored.xyz/) — Built-in pass predictor

### Step 2: Prepare Hardware
- Build dipole antenna (~53 cm per arm, total ~106 cm)
- Connect to RTL-SDR
- Place antenna outside, pointing up (or track satellite across sky)

### Step 3: Install Software
```bash
# macOS
brew install wxtoimg     # or download from website
brew install gqrx        # SDR receiver software

# Linux
sudo apt install gqrx-sdr wxtoimg

# Windows
Download from wmwxtoimg.com or gqrxsdr.org
```

### Step 4: Receive & Decode
1. Open GQRX or equivalent SDR software
2. Tune to 137.620 MHz (NOAA-15) or 137.912 MHz (NOAA-18)
3. Set mode to **FM**
4. Adjust gain for strongest signal
5. When satellite passes, you'll hear noise pattern
6. Record WAV file (automatic in WXtoImg)
7. Import into WXtoImg
8. Decode → get weather image!

### Step 5: View Results
```
Decode complete!
Image shows: Cloud formations, ocean temperature, storm systems
Resolution: ~4 km per pixel
Timestamp: 2026-05-29 14:32 UTC
```

---

## Performance Expectations

### Signal Quality
| Satellite | Elevation | Signal | Quality |
|-----------|-----------|--------|---------|
| NOAA | >30° | Good | Excellent, full image |
| NOAA | 10–30° | Weak | Partial image, noisy edges |
| NOAA | <10° | Very Weak | Degraded, might lose |
| ISS | >45° | Excellent | Crystal clear voice |
| ISS | 20–45° | Good | Clear, some fading |
| ISS | <20° | Weak | Heavily faded, may not decode |

### Antenna Impact
- **No antenna:** ~50 meter range for ISS (maybe catch signal)
- **Dipole antenna:** ~200+ km range for NOAA, ISS clearly audible
- **Yagi antenna:** ~500+ km range, excellent images
- **LNA + Yagi:** Professional-grade, global reception possible

---

## RTL-SDR Reception Bands Reference

From the VHF/UHF detail plot:

| Frequency | Satellite | Service | RTL-SDR | Antenna |
|-----------|-----------|---------|---------|---------|
| **137–138 MHz** | **NOAA Weather** | Satellite | ✅ Perfect | 53 cm dipole |
| **145.8 MHz** | **ISS** | Amateur Radio | ✅ Perfect | 50 cm dipole |
| 1600 MHz | Iridium | Satellite | ✅ Marginal | Directional |
| 10.5–12.5 GHz | GOES/Himawari | Satellite | ❌ No | Requires equipment |

---

## Real-World Tips

### Best Reception Times
- **NOAA:** Evening passes (satellite + low sun angle = good illumination)
- **ISS:** Just after sunset (satellite still lit, ground dark)
- **Iridium:** Any time (flares appear predictably)

### Antenna Placement
- **Higher is better** (roof, balcony, tall mast)
- **Clear sky view** essential (trees/buildings block signals)
- **Away from electrical noise** (power lines, motors, switching supplies)

### Seasonal Variations
- **Summer:** More passes per day (higher maximum elevations)
- **Winter:** Fewer passes, lower in sky
- **Equinox:** Passes occur at different times

### Troubleshooting
| Problem | Solution |
|---------|----------|
| Weak/no signal | Check antenna height/placement, point towards satellite |
| Noisy image | Improve antenna, add LNA, receive during better passes |
| Can't find passes | Check latitude/longitude in software, verify satellite active |
| ISS not audible | Lower in sky (<20°), move antenna outside, use LNA |

---

## Satellite Tracking Software

### Online (No Installation)
- [N2YO.com](https://www.n2yo.com/) — Real-time 3D tracking
- [Heavens-Above.com](https://www.heavens-above.com/) — Detailed predictions
- [CelesTrak](https://celestrak.org/) — Orbital element database

### Desktop (Recommended for Reception)
- **WXtoImg** — NOAA-focused, excellent image processing
- **GQRX** — General-purpose SDR + built-in frequency tracking
- **CubicSDR** — User-friendly, good for learning
- **SatDump** — Modern, multiple satellite support

### Mobile Apps
- **SatelliteTracker** — iOS/Android, real-time passes
- **ISS Detector** — Specifically for ISS notifications
- **Heavens-Above** — Android app, excellent reference

---

## Going Further

### Medium Difficulty
- **Build a fixed Yagi antenna** — Directional, 3× better range
- **Add LNA amplifier** — Boosts weak signals significantly
- **Receive multiple satellites** — NOAA + Meteor in one pass
- **Auto-tracking setup** — Mechanical antenna rotator follows satellite

### Advanced
- **Satellite imagery analysis** — Extract weather data from images
- **Triangulation** — Use multiple receivers for precise positioning
- **High-resolution imaging** — Build reception system for HRPT (high-res satellite data)
- **Meteor M2 series** — Decode both LRPT (Russian) and APT (compatible)

---

## Hardware Specs for Reference

### RTL2832U + R820T2 (RTL-SDR Blog V4)
- **Frequency Range:** 24 MHz – 1.766 GHz (with modification)
- **VHF/UHF:** Excellent (24 MHz – 1.766 GHz)
- **2m Amateur (145 MHz):** Perfect ✅
- **NOAA Band (137–138 MHz):** Perfect ✅
- **L-band (1.6 GHz):** Marginal (near upper limit)
- **C-band/Ku-band (10+ GHz):** Not supported ❌

### Recommended Upgrades for Satellite Work
1. **LNA Amplifier** — 0.5 dB noise figure minimum (~$30–$100)
2. **Directional Antenna** — Yagi or helix ($50–$200)
3. **Weatherproof Enclosure** — Protect electronics outdoors ($20–$50)
4. **Better Coaxial Cable** — Low-loss (RG-213 or better)

---

## Community & Support

- **Reddit:** r/amateurradio, r/rtlsdr
- **Forums:** ARRL.net, RTL-SDR Blog forums
- **Projects:** NOAA-APT Decoder projects on GitHub
- **Events:** International Observe the Moon Night, Earth Science Week

---

## Summary

**RTL-SDR is perfect for:**
- ✅ NOAA weather satellite imagery (most rewarding)
- ✅ ISS astronaut voice reception (instant gratification)
- ✅ Iridium satellite detection (technical challenge)

**RTL-SDR cannot receive:**
- ❌ High-frequency geostationary satellites (10+ GHz)
- ❌ Commercial satellite broadcasts without specialized equipment

**Next Step:** Try receiving a NOAA pass—it's easier than you think, and the imagery is amazing!

---

**Last Updated:** 2026-05-29  
**Satellite Data Source:** CelesTrak, N2YO  
**RTL-SDR Information:** RTL-SDR Blog official specifications
