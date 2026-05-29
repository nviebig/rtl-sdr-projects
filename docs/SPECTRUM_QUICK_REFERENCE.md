# UK Spectrum Quick Reference

## Color Palette at a Glance

| Color | Service | Common Bands |
|-------|---------|--------------|
| 🔴 Red | **Broadcasting & Media** | FM (88–108 MHz), TV (470–694 MHz), AM radio |
| 🔴 Pink | **Mobile Communications** | GSM-900, GSM-1800, UMTS, LTE |
| 🟣 Purple | **Amateur Radio** | HF (3.5–29.7 MHz), 2m (144–146 MHz), 70cm (430–440 MHz) |
| 🟢 Green | **Aviation & Maritime** | VHF COM (108–137 MHz), Maritime (156–162 MHz) |
| 🟢 Dark Green | **WiFi & ISM** | 433 MHz ISM, WiFi 2.4 GHz (2.4–2.5 GHz) |
| 🔵 Blue | **Scientific & Industrial** | WiFi 5 GHz (5.15–5.85 GHz), research bands |
| 🟦 Teal | **Satellite** | Satellite (10.5–12.5 GHz) |

---

## RTL-SDR Accessible Bands (9 Total)

| Frequency | Band | Service | Antenna |
|-----------|------|---------|---------|
| 88–108 MHz | **FM Radio** | Broadcasting | 50 cm |
| 108–137 MHz | **Aviation** | Safety-Critical | 50 cm |
| 144–146 MHz | **2m Amateur** | Amateur Radio | 50 cm |
| 433–435 MHz | **433 ISM** | WiFi & ISM | 20 cm |
| 430–440 MHz | **70cm Amateur** | Amateur Radio | 20 cm |
| 470–694 MHz | **UHF TV** | Broadcasting | 30 cm |
| 890–960 MHz | **GSM-900** | Mobile | 15 cm |
| 1710–1880 MHz | **GSM-1800** | Mobile | 10 cm |
| 2400–2500 MHz | **WiFi 2.4GHz** | WiFi & ISM | 5 cm |

---

## Spectrum Density Summary

**Total UK Spectrum Allocated:** 3.4 GHz (9 kHz–12.5 GHz)

### By Service (Bandwidth Ranking)
1. **Satellite** — 2.0 MHz (58%) 🟦 Teal
2. **Scientific & Industrial** — 700 kHz (20%) 🔵 Blue
3. **Mobile Communications** — 330 kHz (10%) 🔴 Pink
4. **Broadcasting & Media** — 245 kHz (7%) 🔴 Red
5. **WiFi & ISM** — 102 kHz (3%) 🟢 Dark Green
6. **Amateur Radio** — 38 kHz (1%) 🟣 Purple
7. **Aviation & Maritime** — 35 kHz (1%) 🟢 Green

### By Frequency Decade
| Range | Bandwidth | Main Use |
|-------|-----------|----------|
| 1–10 kHz | 5 kHz | VLF/LF (scientific) |
| 10–100 kHz | 1 kHz | LF (rare) |
| 100 kHz–1 MHz | 7 kHz | MF (AM radio) |
| 1–10 MHz | 7 kHz | HF (amateur radio) |
| 10–100 MHz | 32 kHz | VHF (FM, aviation) |
| 100 MHz–1 GHz | 381 kHz | UHF (TV, GSM-900) |
| 1–10 GHz | 1.0 MHz | SHF (GSM-1800, WiFi, UMTS) |
| 10–100 GHz | 2.0 MHz | EHF (satellite, microwave) |

---

## Visualization Files Summary

| Plot | Focus | Best For |
|------|-------|----------|
| **Comprehensive Spectrum** | All 18 bands, log scale | Overview, documentation |
| **By Service Category** | Organized by use type | Policy, pattern analysis |
| **Density Analysis** | Bandwidth quantified | Research, capacity planning |
| **RTL-SDR Bands** | What you can receive | Hardware planning |
| **Reference Table** | Complete details | Lookup, project planning |
| **Color Palette** | Legend and meanings | Understanding other plots |

---

## Common Questions

### Q: Why does Satellite have so much more allocation than Amateur Radio?
**A:** Satellite communications needs wider bandwidth for long-distance, high-capacity global links. Amateur radio operates on narrow channels for point-to-point communication.

### Q: Can I receive Satellite bands with RTL-SDR?
**A:** No, RTL-SDR hardware maxes out ~2.5 GHz. Satellite C-band (10.5–12.5 GHz) requires specialized equipment (LNA + higher-frequency tuner).

### Q: Why is most spectrum above 100 MHz?
**A:** Higher frequencies support shorter wavelengths → smaller antennas → more capacity per unit area. Modern applications (mobile, WiFi) dominate high-frequency regions.

### Q: Are these bands exclusive to their service?
**A:** Mostly, but with exceptions. OFCOM issues licenses and sometimes multiple services share bands. The visualizations show primary allocations.

### Q: Can I use the 433 MHz ISM band for my project?
**A:** Yes, ISM (Industrial, Scientific, Medical) bands are unlicensed in most countries. Check local regulations. RTL-SDR can receive but not transmit.

---

## Frequency Selection Tips for RTL-SDR

1. **Start with FM Radio** (88–108 MHz) — Always active, easy to verify
2. **Check local airports** for Aviation band (108–137 MHz)
3. **433 MHz** good for wireless sensors, IoT device discovery
4. **UHF TV** (470–694 MHz) declining but still receives
5. **2.4 GHz WiFi** possible but weak reception without external LNA

---

## Related Resources

- **Visualization Guide:** `docs/VISUALIZATION_GUIDE.md` (detailed descriptions)
- **Frequency Database:** `docs/FREQUENCY_REFERENCE.md` (more complete list)
- **Hardware Setup:** `docs/ANTENNA_SETUP.md` (RTL-SDR installation)
- **OFCOM UKFAT:** https://www.ofcom.org.uk/spectrum/frequencies/uk-fat
- **RTL-SDR Blog:** https://www.rtl-sdr.com (projects and guides)

---

**Keep this page bookmarked for instant spectrum reference!**
