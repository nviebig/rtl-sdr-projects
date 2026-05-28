# Weather Satellite Image Decoding

**Difficulty:** ⭐⭐ Intermediate | **Time:** 20+ minutes per pass

## Overview
Receive and decode real-time weather satellite imagery. Capture cloud patterns, infrared data, and weather information from polar-orbiting satellites passing overhead.

## Active Satellites (2024+)

| Satellite | Frequency | Status | Inclination |
|-----------|-----------|--------|------------|
| **NOAA-15** | 137.620 MHz | Active ✅ | 98.6° |
| **NOAA-18** | 137.912 MHz | Active ✅ | 99.0° |
| **NOAA-19** | 137.100 MHz | Active ✅ | 99.2° |
| **Meteor M2-4** | 137.100 MHz | Active ✅ | 98.6° |

**Note:** NOAA-17 was decommissioned in 2022. Current operational NOAA satellites are 15, 18, and 19.

## Equipment

- RTL-SDR V4 dongle
- **Antenna extended to ~1.1 m per rod** (critical for 137 MHz band)
- Clear sky view (window mount recommended)
- SatDump software (download from GitHub)
- SDR++ software

## Steps

### 1. Find Satellite Pass
Visit https://www.heavens-above.com:
1. Enter your location
2. Look for NOAA-15, NOAA-18, or NOAA-19
3. Note pass time and maximum elevation
4. **Higher elevation = better signal** (aim for >30°)

### 2. Prepare Equipment
- Extend antenna **fully to ~1.1 m per rod**
- Position antenna pointing at clear sky
- Window mount works well
- Ideally orient antenna perpendicular to satellite path

### 3. Record Signal
1. Open SDR++
2. **Tune to satellite frequency:**
   - NOAA-15: 137.620 MHz
   - NOAA-18: 137.912 MHz
   - NOAA-19: 137.100 MHz
3. Set **Gain: 45-50**
4. Enable **WFM demodulation**
5. Click **Record** button 2 minutes before satellite rises
6. Watch waterfall for signal appearance (rising tone pattern)
7. **Stop recording** when satellite sets

### 4. Decode Image
1. Open **SatDump** software
2. Click **Processor**
3. Load your recorded .wav file
4. Select satellite type (NOAA)
5. Click **Process**
6. Wait for decoding (~30 seconds to 2 minutes)
7. View decoded weather image!

## What You'll See

- **Cloud patterns** visible from orbit
- **Thermal (infrared) imagery** showing temperature
- **Nighttime passes** show city lights and aurora
- **Hurricane/storm structures** clearly visible
- **Sea ice** and polar regions show well
- **Geographic features** like mountains and terrain

## Technical Details

| Parameter | Value |
|-----------|-------|
| **Frequency Band** | 137.0 - 138.0 MHz (NOAA band) |
| **Modulation** | WFM (Wide FM) |
| **Bandwidth** | 38 kHz |
| **Antenna Optimal** | 1.10 m per rod (λ/2 at 137 MHz) |
| **Pass Duration** | ~10-12 minutes |
| **Pass Frequency** | Multiple per day |

## Tips for Best Results

- **Antenna elevation**: Extend fully to 1.1 m
- **Timing**: Record entire visible pass (2 min before rise to 2 min after set)
- **Gain**: 45-50 (adjust if you see only noise)
- **Location**: Higher elevation = better signal
- **Weather**: Clear skies improve reception
- **Time of day**: Daytime passes better for cloud detail

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No signal visible | Extend antenna fully, check pass time |
| Weak/noisy signal | Check satellite elevation angle (>30° better) |
| Decoder produces garbage | Signal too weak - try higher location/antenna |
| Image shows artifacts | Normal with weak signal, try higher passes |
| SatDump won't decode | Check file is full pass recording, try another decoder |

## Software Resources

- **SatDump** (primary): https://github.com/SatDump/SatDump
- **WXtoImg** (alternative, legacy): http://wxtoimg.com/
- **Orbitron** (pass prediction): https://www.stoff.pl/

## Advanced Topics

- **Receiver drift**: Use TCXO discipline to avoid frequency shift
- **Multiple satellites**: NOAA and Meteor at similar frequencies
- **Hyper spectral data**: NOAA carries multiple sensors
- **Real-time decoding**: Use rtlsdr-pipe + SatDump for live decoding

## Notes

- Polar-orbiting satellites pass over your location multiple times per day
- Different satellites cross at different local times
- Pass visibility depends on latitude (better at higher latitudes)
- Winter passes may show snow/ice, summer shows vegetation
