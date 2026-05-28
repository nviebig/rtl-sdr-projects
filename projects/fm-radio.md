# FM Radio Reception

**Difficulty:** Easy | **Time:** 5 minutes | **Recommended First Project**

## Overview
The simplest RTL-SDR project. Verify your hardware works by listening to FM radio broadcasts.

## Equipment
- RTL-SDR V4 dongle
- Antenna (any length, ~50 cm optimal)
- SDR++ software

## Steps

1. **Open SDR++** from Applications folder
2. **Click play button** (top left corner)
3. **Tune to 100 MHz** in the frequency input box
4. **Look at waterfall display** - you should see colored peaks (these are FM stations)
5. **Click on a peak** to tune to a specific station
6. **Enable WFM demodulation** (dropdown menu)
7. **Increase volume** and listen

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No signals/peaks | Check RTL-SDR drivers installed (see docs/ANTENNA_SETUP.md) |
| Only gray noise | Disable IF AGC in SDR++ settings |
| No sound | Enable WFM demodulation, check audio output |
| Wrong frequencies | Verify custom RTL-SDR Blog drivers (not stock macOS) |

## What to Listen For

- **87.5 - 92 MHz** - BBC Radio stations
- **92 - 97.6 MHz** - Independent/commercial stations
- **97.6 - 104.6 MHz** - More commercial stations
- **104.6 - 108 MHz** - Remaining FM stations

## Next Steps

Once FM works, try:
- **Aircraft Radar** - See live aircraft positions
- **Wireless Sensors** - Detect nearby devices
- **Weather Satellites** - Decode satellite images

## Notes

- FM stations broadcast with WFM (Wide Frequency Modulation)
- 200 kHz bandwidth per station
- Good signal strength visible as bright colors in waterfall
- RDS data shows station name/song info if enabled
