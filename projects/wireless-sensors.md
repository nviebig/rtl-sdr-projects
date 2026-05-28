# Wireless Sensor Decoding

**Difficulty:** Easy | **Time:** 5 minutes

## Overview
Decode wireless sensor broadcasts from devices around you. Detect weather stations, tire pressure monitors (TPMS), smart home devices, doorbells, and more.

## Quick Start

```bash
rtl_433 -f 433.92M
```

You'll see real-time decoding of wireless devices broadcasting nearby.

## Equipment

- RTL-SDR V4 dongle
- Antenna (short, ~17 cm works fine)
- `rtl_433` tool (included)

## What You Can Detect

| Device Type | Frequency | Notes |
|-------------|-----------|-------|
| **Weather Stations** | 433.92 MHz | Temperature, humidity, wind |
| **TPMS** (tire sensors) | 433.92 MHz | Vehicle tire pressure |
| **Smart Home** | 433.92 MHz | Wireless doorbells, locks, outlets |
| **Personal Weather** | 433.92 MHz | Standalone sensors |
| **Remote Controls** | Various | Garage doors, gates, etc. |
| **Baby Monitors** | Various | Older wireless monitors |

## Basic Usage

### Simple Decoding
```bash
# Scan 433.92 MHz (most common ISM band)
rtl_433 -f 433.92M
```

### Advanced Options
```bash
# Increase verbosity
rtl_433 -f 433.92M -vvv

# Dump raw signals
rtl_433 -f 433.92M -r <filename>

# Multiple frequencies
rtl_433 -f 868M -f 915M

# Save to file for analysis
rtl_433 -f 433.92M > output.txt
```

## Output Interpretation

Example output:
```
Flex-868 (Wireless Weather Station) decoding enabled
Weather Station: Indoor  Temp 22.3 °C, Humidity 65 % 
TPMS (Tire Pressure):  Pressure 2.08 bar, Status OK
```

Breaking down:
- **Device type**: What kind of sensor
- **Channel/ID**: Which specific device
- **Readings**: Temperature, pressure, etc.
- **Status**: Battery level, signal strength

## Configuration

### Antenna
- **Frequency**: 433.92 MHz (most common)
- **Antenna Length**: ~17 cm (λ/4 at 433 MHz)
- **Can be indoors**: Short range is fine for nearby devices
- **Gain**: 30-40 (adjust if no signals)

### Common Frequencies (ISM Band)
- **433.92 MHz** - Most common in EU/UK/Russia
- **915 MHz** - North America
- **868 MHz** - European variant
- **2.4 GHz** - WiFi, Zigbee (needs special receiver)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No devices detected | Check frequency (433.92 MHz is most common) |
| Few devices found | Might not have many wireless sensors nearby |
| Garbled output | Reduce gain, check frequency accuracy |
| Device not recognized | May be proprietary/encrypted, try `-vvv` for raw data |

## Advanced Analysis

### Signal Recording
```bash
# Record raw IQ data
rtl_433 -f 433.92M -r filename.iq
```

### Frequency Scanning
```bash
# Find active frequencies
rtl_433 -s 433000000 -e 434000000
```

### Specific Device Type
```bash
# Only decode specific devices
rtl_433 -f 433.92M -R 40  # Only Ecowitt devices
```

## Privacy Note

This tool can decode wireless signals from nearby devices. Always respect privacy laws in your jurisdiction.

## Resources

- **rtl_433 Documentation**: https://github.com/merbanan/rtl_433
- **Device Database**: https://github.com/merbanan/rtl_433/tree/master/src/devices
- **ISM Band Info**: https://en.wikipedia.org/wiki/ISM_band

## Notes

- Most consumer IoT uses 433.92 MHz or 915 MHz
- Open-source decoders may not recognize proprietary formats
- Signal range typically 30-100 meters indoors
- Can detect devices multiple rooms away
