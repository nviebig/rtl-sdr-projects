# ISS Reception (Voice, APRS, SSTV)

**Difficulty:** Intermediate | **Time:** 10 minutes per pass | **Special Event**

## Overview
Receive live transmissions from the International Space Station when it passes overhead. Hear astronaut voices, decode packet radio (APRS), or capture slow-scan television (SSTV) images.

## What You Can Receive

| Mode | Frequency | What to Hear |
|------|-----------|------------|
| **Voice** | 145.800 MHz | Live astronaut transmissions |
| **APRS** | 145.825 MHz | Packet radio digipeater data |
| **SSTV** | 145.800 MHz | Slow-scan TV image transmissions |

## Equipment

- RTL-SDR V4 dongle
- **Antenna extended to ~1.1 m per rod** (critical)
- Clear sky view during pass
- SDR++ software
- Direwolf software (APRS decoding)
- SatDump software (SSTV decoding)

## ISS Passes

**Find passes:** https://www.heavens-above.com

Key facts:
- ISS orbits every **~90 minutes**
- Passes over your location **multiple times per day**
- Each pass lasts **3-10 minutes** depending on trajectory
- **Higher elevation = better signal** (aim for >30°)
- Best reception when ISS passes **directly overhead** (90° elevation)

## Steps to Receive Voice

### 1. Find Next Pass
1. Go to https://www.heavens-above.com
2. Click "ISS" in left menu
3. Note **rise time** and **maximum elevation**
4. **Mark time 5 minutes before pass begins**

### 2. Prepare Equipment
- Extend antenna **fully to ~1.1 m per rod**
- Point antenna at sky (omnidirectional works)
- Position yourself near window if indoors
- Test SDR++ opens correctly

### 3. Record Signal
1. Open SDR++
2. **Tune to 145.800 MHz** (ISS downlink frequency)
3. Set **Gain: 40-50**
4. Enable **NFM demodulation** (not WFM!)
5. Click **Record** 1 minute before ISS rises
6. **Listen and record** entire pass
7. Stop recording after ISS sets

### 4. Listen to Recording
- File will be saved as .wav
- Play back to hear astronaut voices
- Listen for call signs (e.g., "NA1SS")
- May hear music/announcements if schoolchildren on board

## Steps to Decode APRS Packet Radio

### 1. Record Signal (same as voice above)

### 2. Decode with Direwolf
```bash
# Install Direwolf
brew install direwolf

# Decode recorded audio
direwolf -r recording.wav
```

### 3. Results
You'll see packet radio digipeater data:
- Station positions
- Call signs
- Beacon information
- Relay data

## Steps to Decode SSTV Images

### 1. Record Signal (same as voice)

### 2. Decode with SatDump
1. Open SatDump software
2. Load .wav file from ISS recording
3. Select **SSTV decoder**
4. Process recording
5. View decoded images

**What you'll see:**
- ISS crew photos
- Earth views from orbital altitude
- Mission patches
- Educational images

## Technical Details

| Parameter | Value |
|-----------|-------|
| **Downlink Frequency** | 145.800 MHz |
| **Uplink Frequency** | 144.490 MHz |
| **Demodulation** | NFM (Narrow FM) |
| **Bandwidth** | 12.5 kHz |
| **Antenna Optimal** | 1.03 m per rod (λ/2 at 145.8 MHz) |
| **Antenna Practical** | 1.1 m per rod (close enough) |
| **Doppler Shift** | ±5 kHz during pass |
| **Gain Setting** | 40-50 |

## ISS Specifics

- **Orbital Period**: 90 minutes
- **Altitude**: ~400 km
- **Inclination**: 51.6°
- **Crew Size**: Typically 3-6 astronauts
- **Activity**: Regular voice contacts, periodic SSTV events

## Tips for Best Reception

- **Highest antenna elevation** = strongest signal
  - >70° elevation = excellent
  - 30-70° elevation = good
  - <30° elevation = weak/difficult

- **Antenna orientation**: Point toward zenith (overhead) for best results

- **Time of pass**: No difference in signal strength

- **Location**: Higher elevation (hills/mountains) = better range

- **Doppler effect**: Frequency shifts ±5 kHz during pass (auto-tracked by SDR++)

## Common Issues

| Problem | Solution |
|---------|----------|
| No signal detected | Check antenna extended, wrong frequency? |
| Weak signal | Increase gain to 50, improve antenna height |
| Signal dropouts | Normal near start/end of pass (low elevation) |
| Only noise | Antenna not extended, or high noise floor |
| Can't hear voices | Try NFM mode (not WFM), check volume |

## What to Listen For

**Common ISS Callsigns:**
- **NA1SS** - NASA ISS
- **W5XA** - Amateur radio experiments
- Various astronaut call signs

**What you might hear:**
- Astronaut greetings ("Hello, this is ISS...")
- Music or announcements
- Telemetry tones
- Other amateur radio operators calling ISS

## Special Events

ISS schedules special **ARISS (Amateur Radio on the ISS)** contacts:
- School contact events
- Educational broadcasts
- Amateur radio nets
- Check: https://www.ariss.org/

These are prime times to hear clear voices from orbit!

## Resources

- **Heavens-Above**: https://www.heavens-above.com (pass predictions)
- **ARISS**: https://www.ariss.org/ (ISS amateur radio info)
- **Direwolf**: https://github.com/wb2osz/direwolf (APRS decoder)
- **SatDump**: https://github.com/SatDump/SatDump (SSTV decoder)

## Notes

- ISS passes at **different times each day** (predictable rotation)
- Some passes will be better than others (elevation dependent)
- Voice contacts sometimes scheduled, sometimes spontaneous
- No special license required to listen (rx-only)
- Perfect first contact with space! 🚀
