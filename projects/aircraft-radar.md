# Aircraft Radar (ADS-B)

**Difficulty:** Easy | **Time:** 5 minutes

## Overview
Track live aircraft in real-time using ADS-B (Automatic Dependent Surveillance-Broadcast) signals. See aircraft positions, altitude, speed, and flight numbers on a live map.

## Equipment
- RTL-SDR V4 dongle
- Antenna (15-50 cm)
- Bash shell access

## Quick Start

```bash
# Run the aircraft radar script
./aircraft_radar_setup.sh

# Open browser to: http://localhost:8080
```

You should see a live map with aircraft positions appearing in real-time.

## What You'll See

- **Live aircraft positions** on OpenStreetMap
- **Aircraft icons** with flight information
- **Altitude** and **speed** readouts
- **Flight numbers** and **aircraft type**
- **Range**: 100-300 km depending on antenna height

## Frequency & Technical Details

| Parameter | Value |
|-----------|-------|
| **Frequency** | 1090 MHz (Mode S / ADS-B) |
| **Bandwidth** | 2 MHz |
| **Demodulation** | Raw/Digital |
| **Antenna Optimal** | 27 cm (λ/4 at 1090 MHz) |
| **Antenna Practical** | 15-50 cm works |
| **Gain Setting** | 30-45 (adjust for local noise) |

## Improving Reception

- **Higher antenna location** = more range
- **Extend antenna fully** for best signal
- **Rooftop mounting** = best results (300+ km range possible)
- **Reduce gain if** you see too much noise
- **Check for obstacles** blocking sky view

## Script Details

The `aircraft_radar_setup.sh` script:
1. Checks for `dump1090-fa` (aircraft decoder)
2. Launches receiver on 1090 MHz
3. Starts web interface on `localhost:8080`
4. Shows live aircraft data

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No aircraft appearing | Try higher location, check antenna |
| Web interface won't load | Verify port 8080 is free, restart script |
| Few aircraft visible | Normal in low-traffic areas, wait for planes |
| Intermittent signals | Gain too high - reduce to 30-40 |

## Next Steps

- Check flight info on [FlightRadar24](https://www.flightradar24.com)
- Compare your local radar with official sources
- Experiment with antenna placement for better range
- Try at different times (more traffic during day)

## Notes

- Requires internet for map display
- ADS-B is used by most commercial aircraft worldwide
- Range depends heavily on antenna elevation
- Can decode 100+ aircraft simultaneously
