# Antenna Configuration Guide

## Dipole Antenna Basics

The included telescopic dipole antenna is tuned for multi-band operation. Optimal performance requires proper rod extension for your target frequency.

## Antenna Length Calculations

### General Formula
```
Optimal length = wavelength / 2 = speed of light / (2 × frequency)
               = 300 MHz·m / (2 × frequency_MHz)
               = 150 / frequency_MHz meters
```

For dipole, each rod should be **λ/4** (quarter wavelength).

## Recommended Lengths by Application

| Application | Frequency | Each Rod Length | Notes |
|------------|-----------|-----------------|-------|
| **FM Radio** | 100 MHz | ~75 cm | Can use shorter (~50 cm) |
| **Aircraft (ADS-B)** | 1090 MHz | ~13.7 cm | Very short |
| **ISS/Satellites** | 145.8 MHz | ~51 cm | Standard amateur config |
| **Weather Satellites** | 137.6 MHz | ~55 cm | Slightly longer for 137 MHz |
| **Wireless Sensors** | 433.92 MHz | ~17 cm | Very short, easy to extend |
| **Amateur VHF** | 146 MHz | ~51 cm | Same as ISS |
| **General Purpose** | Multi-band | **110 cm** | Full extension, works decently on all bands |

## Configuration by Frequency Band

### VHF Band (137-174 MHz)
- **Best for:** Weather satellites, ISS, amateur radio
- **Optimal rod length:** 1.1 m per rod (full extension)
- **Why:** Half-wavelength dipole at ~145 MHz
- **Performance:** Excellent across 137-174 MHz range

### Aircraft Band (1090 MHz)
- **Best for:** Aircraft radar (ADS-B)
- **Optimal rod length:** ~13.7 cm per rod
- **Why:** λ/4 at 1090 MHz
- **Performance:** Much shorter needed for UHF frequencies

### ISM Band (433 MHz)
- **Best for:** Wireless sensors, remote controls, IoT
- **Optimal rod length:** ~17 cm per rod
- **Why:** λ/4 at 433.92 MHz
- **Performance:** Good signal on wireless devices

### FM Radio (88-108 MHz)
- **Best for:** Broadcast FM listening
- **Optimal rod length:** 75-80 cm per rod
- **Why:** Longer waves = longer antenna
- **Performance:** Can use shorter (~50 cm) for casual listening

## Performance vs. Frequency

```
Frequency (MHz) | Each Rod Length | Application
50              | 150 cm          | LF/Maritime (too long for telescope)
100             | 75 cm           | FM Radio
137.6           | 55 cm           | Weather Satellites
145.8           | 51 cm           | ISS/Amateur VHF
433.92          | 17 cm           | Wireless Sensors
1090            | 14 cm           | Aircraft Radar
2400            | 6.2 cm          | WiFi/Cellular (not recommended)
```

## Practical Antenna Tips

### For Multi-Band Use (General Purpose)
**Extend to full length (1.1 m per rod)**
- Works reasonably on ALL bands 137-1090 MHz
- Best compromise for multiple projects
- Small efficiency loss on each band
- Recommended for beginners

### For Single-Band Optimization
**Use specific length for your target frequency**
- Maximum efficiency on one frequency
- Significantly better reception
- Requires manual adjustment
- Recommended for advanced users

### Antenna Gain vs. Frequency
```
Lower frequencies  → Longer antenna = more gain
Higher frequencies → Shorter antenna possible but different gain pattern
```

## Mounting Configurations

### Vertical Monopole (Most Common)
- **Setup:** Antenna pointing straight up
- **Pattern:** Omnidirectional in horizontal plane
- **Best for:** Mobile objects (aircraft, satellites)
- **Height:** Higher is always better

### Horizontal Dipole
- **Setup:** Antenna pointing horizontally
- **Pattern:** Figure-8 pattern perpendicular to antenna
- **Best for:** Ground stations at specific azimuth
- **Use case:** Directional reception if needed

### Angled/Tilted Dipole
- **Setup:** Antenna at 45° angle
- **Pattern:** Combination of above
- **Best for:** Satellites at various elevations
- **Practical:** Often naturally occurs with tripod mounting

## Impedance & Matching

- **Antenna impedance:** 50 Ohms (matched to dongle)
- **Coax cable:** 50 Ohm SMA
- **No matching network needed** for basic applications
- **All coax connections:** SMA male-to-female

## Signal Strength Optimization

### Factors Affecting Reception (in order of importance)

1. **Antenna elevation** (~5 dB impact)
   - Higher = better signal
   - 100m elevation vs. 10m = ~10× range improvement

2. **Antenna height above obstacles** (~3 dB)
   - Clear view of sky critical
   - Trees/buildings block signals

3. **Antenna length (at frequency)** (~2 dB)
   - Proper length = resonance = max gain
   - Off-frequency = reduced gain

4. **Antenna orientation** (~1-2 dB)
   - Vertical best for omnidirectional
   - Minor effect with dipole

5. **Coax quality** (~0.5-1 dB)
   - Included cable is good quality
   - Longer cable = more loss

### The 5-8-5 Rule
- Optimal frequency = best
- ±5 MHz away = slight loss (0.5 dB)
- ±10 MHz away = noticeable loss (1-2 dB)
- ±20 MHz away = significant loss (3+ dB)

## Coax Cable Tips

- **Included cable:** 3 meters, SMA connectors
- **Quality:** RG58 equivalent (good for this application)
- **Keep away from:** High-power transmitters, noisy equipment
- **Connector care:** Keep SMA connectors clean/dry

## Connector Types

- **SMA (SubMiniature A):** Used on V4 dongle
  - Reversible (male/female)
  - Threaded connection
  - 50 Ohm impedance

- **Included cable:** SMA male ↔ SMA female
  - Perfect for V4 dongle
  - 3 meters length standard
  - Can add extensions with adapters

## Advanced: Resonance Curves

Dipole antenna gain vs. frequency (example):

```
Frequency (MHz):  100   120   140   150   160   180
Gain (dBi):      +2.0  +2.5  +2.8  +2.9  +2.8  +2.5
Status:           Fair  Good  Excellent Excellent Good  Fair
```

- Peak performance at resonant frequency (147.5 MHz for 1.1m rods)
- Usable bandwidth: ±30 MHz from resonance (gain loss <1 dB)
- Wider bandwidth than you'd expect due to dipole design

## Notes

- These are guidelines; actual performance varies by local environment
- Experiment with different lengths to find best results
- **Radio rule of thumb:** Higher = Better (always try higher antenna location)
- Frequency accuracy: ±1% (±1.4 MHz at 145 MHz) acceptable
