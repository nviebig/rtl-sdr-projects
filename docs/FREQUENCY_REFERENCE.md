# RTL-SDR Frequency Reference Guide

## Common Frequencies (MHz)

### FM Radio & Audio
| Service | Frequency (MHz) | Bandwidth | Mode |
|---------|---|---|---|
| FM Radio | 88.0 - 108.0 | 200 kHz | WFM |
| AM Radio | 0.5 - 1.7 | 10 kHz | AM |
| VHF Radio (UK) | 145.0 - 147.0 | 12.5 kHz | NFM |

### Aircraft
| Service | Frequency (MHz) | Notes |
|---------|---|---|
| ADS-B (Aircraft radar) | 1090.0 | Essential for aircraft tracking |
| VOR Navigation | 108.0 - 118.0 | Automatic direction finding |
| ILS (Landing) | 108.0 - 112.0 | Instrument landing system |
| ATIS (Info) | 118.0 - 135.0 | Aircraft airport information |

### Satellites
| Satellite | Frequency (MHz) | Purpose | Status |
|---|---|---|---|
| **NOAA-15** | 137.620 | Weather imaging | Active |
| **NOAA-18** | 137.912 | Weather imaging | Active |
| **NOAA-19** | 137.100 | Weather imaging | Active |
| **ISS** | 145.800 | Packet radio/SSTV | Active when overhead |
| **Meteor M 2-4** | 137.100 | Weather imaging | Active |

### ISS (International Space Station)
- **Voice**: 145.80 MHz (FM, NFM demod)
- **Packet Radio (APRS)**: 145.825 MHz
- **SSTV**: 145.80 MHz (slow-scan TV images)
- **Passes**: Check https://www.heavens-above.com

### Meteor Radio
- **Frequency**: 137.100 MHz
- **Bandwidth**: Wide (need good antenna)
- **Software**: SatDump
- **Output**: Weather satellite imagery

### Maritime
| Service | Frequency (MHz) | Mode |
|---|---|---|
| Marine VHF | 156.0 - 174.0 | NFM |
| Marine SSB | 2.0 - 30.0 | SSB (lower band) |
| AIS (Ships) | 161.975, 162.025 | Digital |

### Weather & Environmental
| Service | Frequency (MHz) | Type |
|---|---|---|
| Weather Stations | 433.05 - 434.79 | RTTY |
| Amateur Radio | 144.0 - 146.0 (2m band) | CW, SSB, FM |
| TPMS (Tire Sensors) | 433.05 - 433.95 | OOK |
| Smart Home | 433.92, 868.0 | Various |

### Special Interest
| Service | Frequency (MHz) | Notes |
|---|---|---|
| Amateur Satellites | 145.800 - 146.000 | Varies by satellite |
| Space Station Repeater | 145.800 | Listening only |
| Fire/Police (UK) | 380.0 - 470.0 | Digital encrypted |
| Broadcast TV (old) | 470.0 - 790.0 | DVB-T signals |

---

## Optimal Antenna Configuration

### Dipole Rod Lengths by Frequency

**Frequency** | **Wavelength** | **Full Wave** | **Half Wave (optimal)** | **Quarter Wave**
---|---|---|---|---
**100 MHz** (FM) | 3.0m | 3.0m | **1.5m** | 0.75m
**137 MHz** (Satellites) | 2.19m | 2.19m | **1.1m** | 0.55m
**145.8 MHz** (ISS) | 2.06m | 2.06m | **1.03m** | 0.51m
**433.92 MHz** (Sensors) | 0.69m | 0.69m | **0.35m** | 0.17m

**Note**: Extend telescopic rods to ~1.5m (60cm each) for best multi-band reception

---

## Demodulation Modes

| Mode | Use Case | Bandwidth |
|---|---|---|
| **WFM** | FM radio broadcast | 200 kHz |
| **NFM** | Amateur radio, aviation | 12.5-25 kHz |
| **AM** | AM radio, some aviation | 10 kHz |
| **SSB** | Amateur radio, maritime | 3 kHz |
| **CW** | Morse code | 500 Hz |
| **RAW** | Digital signals (rtl_433 etc.) | Varies |

---

## SDR++ Quick Settings

### For Aircraft Tracking (ADS-B)
- Frequency: 1090 MHz
- Demodulation: RAW
- Gain: 45-50
- External tool: dump1090-fa
- Output: Live aircraft map

### For FM Radio
- Frequency: 88-108 MHz
- Demodulation: WFM
- Gain: 30-40
- RDS: Enable for station info

### For Satellites
- Frequency: 137-138 MHz (NOAA)
- Demodulation: WFM
- Gain: 45-50
- Antenna: Fully extended (~1.1m per rod)
- Recording: Enable WAV export
- Post-process: SatDump decoder

### For ISS
- Frequency: 145.800 MHz
- Demodulation: NFM
- Gain: 40-50
- Antenna: Fully extended
- Note: Only active when ISS passes overhead

### For Wireless Sensors (433 MHz)
- Use rtl_433 command-line tool (easier than SDR++)
- Frequency: 433.92 MHz
- Detects: Weather stations, tire sensors, smart home devices

---

## Recording & Post-Processing

### Record IQ Data (SDR++)
1. Click "Record" button (tape icon)
2. Tune to frequency of interest
3. Let run while satellite/signal passes
4. Stop and save as .wav or .iq

### Decode Weather Satellites
```bash
# Using SatDump
# 1. Record IQ data from 137.5 MHz (NOAA satellite)
# 2. Open SatDump GUI
# 3. Load recorded file
# 4. Select "NOAA" decoder
# 5. Process to get weather image
```

### Decode Aircraft (ADS-B)
```bash
dump1090-fa --net --interactive
# Open browser: localhost:8080
```

### Decode Wireless Sensors
```bash
rtl_433 -f 433.92M
# Decodes temperature sensors, TPMS, smart devices
```

---

## Important Notes

1. **Antenna matching**: Different frequencies need different antenna lengths
2. **Gain settings**: Too much gain = noise; too little = weak signals
3. **IF AGC disabled**: Required for V4 dongle in SDR++
4. **Recording duration**: Satellites pass for ~10 minutes
5. **Signal strength**: Waterfall display shows SNR (colored = good, gray = noise)
6. **Local interference**: Check for WiFi (2.4/5 GHz), microwaves, cordless phones

---

Last updated: 2026-05-28 | V4 Dongle Specific
