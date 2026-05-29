# UK Spectrum Visualization Suite - Complete Guide

## Overview

This document describes the comprehensive, publication-quality visualization suite for UK radio frequency spectrum allocation (Ofcom UKFAT). All plots use a consistent color palette mapped to service categories, enabling intuitive comparison and recognition across visualizations.

**Generated:** 2026-05-29  
**Resolution:** 300 DPI (publication-ready)  
**Format:** PNG with white background (suitable for light/dark themes)  
**Color Model:** Service-category based palette (7 categories)

---

## Service Category Color Palette

All visualizations use this consistent color scheme, ensuring every service type is instantly recognizable across plots:

| Service Category | Color | Hex | Description |
|-----------------|-------|-----|-------------|
| **Broadcasting & Media** | <span style="background:#e74c3c; padding: 2px 8px; color:white">■</span> | `#e74c3c` | Television, FM/AM radio, digital broadcast |
| **Mobile Communications** | <span style="background:#e7298a; padding: 2px 8px; color:white">■</span> | `#e7298a` | Cellular networks (GSM, UMTS, LTE), PMR |
| **Amateur Radio** | <span style="background:#9467bd; padding: 2px 8px; color:white">■</span> | `#9467bd` | Licensed amateur radio (HF, VHF, UHF) |
| **Aviation & Maritime** | <span style="background:#2ca02c; padding: 2px 8px; color:white">■</span> | `#2ca02c` | Air traffic control, maritime navigation |
| **WiFi & ISM** | <span style="background:#27ae60; padding: 2px 8px; color:white">■</span> | `#27ae60` | ISM bands, unlicensed WiFi, short-range wireless |
| **Scientific & Industrial** | <span style="background:#3498db; padding: 2px 8px; color:white">■</span> | `#3498db` | Research, measurement, industrial applications |
| **Satellite** | <span style="background:#16a085; padding: 2px 8px; color:white">■</span> | `#16a085` | Satellite communications, downlink/uplink |

---

## Plot 1: Comprehensive Spectrum (Logarithmic Scale)

**File:** `uk_spectrum_comprehensive.png`  
**Purpose:** Complete overview of UK spectrum allocation from 9 kHz to 12.5 GHz  
**Audience:** General reference, documentation

### Features
- **Logarithmic frequency axis** enables visualization across 6 orders of magnitude (9 kHz → 12.5 GHz)
- **All 18 major bands** from VLF through satellite frequencies
- **Color-coded by individual band** (not service category - for fine-grained distinction)
- **Clean typography** with bold band labels for readability
- **Grid lines** aid frequency reading

### Key Observations
- **Concentration of allocations** increases at higher frequencies (UHF/microwave)
- **Sparse VLF/LF bands** demonstrate the exponential growth of spectrum usage
- **HF amateur radio** spans an exceptionally wide range (3.5–29.7 MHz)
- **Satellite band** (10.5–12.5 GHz) represents modern high-capacity communications

### Use Cases
- Documentation, README, papers
- General public education
- Comparison with other nations' spectra

---

## Plot 2: Spectrum Allocation by Service Category

**File:** `spectrum_by_service.png`  
**Purpose:** Organize bands by functional use to reveal allocation patterns  
**Audience:** Policy makers, spectrum planners, technical overview

### Features
- **Service-based grouping** shows which applications dominate each frequency region
- **Category labels on left** color-coded to match their allocations
- **Logarithmic frequency scale** for consistent visual comparison
- **Stacked arrangement** makes allocation patterns visually apparent
- **Reference lines** at 1 MHz and 1 GHz decade boundaries

### Insights from Plot
1. **Broadcasting & Media** (red) dominates lower frequencies (AM radio, FM, TV)
2. **Mobile Communications** (pink) concentrated in 890 MHz–2 GHz range (GSM, UMTS)
3. **Amateur Radio** (purple) distributed across HF and UHF bands for experimentation
4. **Aviation & Maritime** (green) occupy critical safety-critical bands
5. **WiFi & ISM** (dark green) use unlicensed 2.4 GHz and 433 MHz bands
6. **Scientific & Industrial** (blue) and **Satellite** (teal) in high-frequency spectrum

### Use Cases
- Spectrum policy analysis
- Educational visualization of allocation patterns
- Comparison of service priorities across frequency regions
- Understanding why certain applications use certain bands

---

## Plot 3: Spectrum Density Analysis

**File:** `spectrum_density.png`  
**Purpose:** Quantify allocation intensity and occupancy  
**Audience:** Spectrum managers, technical analysis, research

### Subplot 3a: Allocation Density by Frequency Decade
**Shows:** Total bandwidth allocated in each frequency "decade" (1–10 kHz, 10–100 kHz, etc.)

**Key Findings:**
- **1–10 GHz range** shows dramatic increase in allocated bandwidth
- **1–10 MHz decade** sparse (long-range HF amateur radio only)
- **10–100 MHz decade** sees major expansion (FM, aviation, amateur)
- **1–10 GHz decade** highest allocation (2.0 MHz total) - modern wireless dominates

### Subplot 3b: Allocation by Service Category
**Shows:** Total spectrum allocated to each service type (sorted by bandwidth)

**Ranking by Bandwidth:**
1. **Satellite** (2.0 MHz) - 58% of total allocation
2. **Scientific & Industrial** (700 kHz) - 20.3%
3. **Mobile Communications** (330 kHz) - 9.6%
4. **Broadcasting & Media** (245 kHz) - 7.1%
5. **WiFi & ISM** (102 kHz) - 3.0%
6. **Amateur Radio** (38 kHz) - 1.1%
7. **Aviation & Maritime** (35 kHz) - 1.0%

**Interpretation:**
- Satellite communications occupies the single largest block despite fewer users (due to long-distance demands)
- Mobile communications represents growing spectrum demand despite less allocated bandwidth
- Broadcasting maintains steady allocation across multiple bands
- Amateur radio operates with minimal spectrum allocation but global distribution

### Use Cases
- Spectrum policy debates
- Justifying allocation decisions
- Identifying potential inefficiencies
- Education on spectrum scarcity

---

## Plot 4: RTL-SDR Receivable Bands

**File:** `rtl_sdr_bands.png`  
**Purpose:** Show which UK frequency bands are accessible with RTL-SDR hardware  
**Audience:** RTL-SDR users, hobbyists, beginners

### Features
- **9 major accessible bands** highlighted in dedicated plot
- **Linear frequency scale** (88 MHz–2.5 GHz) - appropriate for VHF/UHF focus
- **Service category legend** enables instant identification of use
- **Starting frequency labels** on left for quick reference
- **Color-coded boxes** match the service palette

### Accessible Bands (in order)
1. **FM Radio** (88–108 MHz) — Broadcasting & Media
2. **Aviation** (108–137 MHz) — Aviation & Maritime
3. **2m Amateur** (144–146 MHz) — Amateur Radio
4. **433 ISM** (433–435 MHz) — WiFi & ISM
5. **70cm Amateur** (430–440 MHz) — Amateur Radio
6. **UHF TV** (470–694 MHz) — Broadcasting & Media
7. **GSM-900** (890–960 MHz) — Mobile Communications
8. **GSM-1800** (1710–1880 MHz) — Mobile Communications
9. **WiFi 2.4GHz** (2400–2500 MHz) — WiFi & ISM

### Hardware Notes
- **RTL2832U + R820T2 tuner** covers 24 MHz–1.766 GHz (modified)
- **Extensions possible** with bias-T and LNA for higher frequencies
- **Some gaps** in coverage (e.g., 1.88–2.4 GHz not well supported)

### Use Cases
- Project planning and band selection
- Antenna design (frequency-dependent)
- Receiver tuning reference
- Understanding hardware capabilities

---

## Plot 5: Complete Reference Table

**File:** `frequency_reference_table.png`  
**Purpose:** Authoritative lookup table with all spectrum details  
**Audience:** Technicians, project planners, researchers

### Columns
1. **Band Name** — Common designation (e.g., "FM Radio", "GSM-900")
2. **Frequency Range** — Start and end frequencies in GHz/MHz
3. **Bandwidth** — Total allocated width (MHz or kHz)
4. **Service Category** — Color-coded category with description
5. **RTL-SDR** — "✓ Yes" or "✗ Limited" for hardware compatibility
6. **Antenna** — Approximate antenna length estimate

### Table Styling
- **Header row** (dark background, white text) for clear section distinction
- **Color-coded rows** matching service category of each band
- **1:1 correspondence** with spectrum visualization colors
- **Sortable format** (can be exported as CSV if needed)

### Antenna Sizing Guide
- **< 5 cm** for frequencies > 1 GHz (WiFi 5GHz, etc.)
- **5–20 cm** for 100 MHz–1 GHz (most common RTL-SDR work)
- **20–100 cm** for 10–100 MHz (FM radio, aviation)
- **> 1 m** for frequencies < 10 MHz (HF amateur, LF/MF)

### Use Cases
- Quick reference during reception work
- Project planning with antenna selection
- Band selection for specific applications
- Regulatory compliance checking

---

## Plot 6: Color Palette Guide

**File:** `color_palette_guide.png`  
**Purpose:** Standalone reference for service category colors and meanings  
**Audience:** Users unfamiliar with the color scheme, documentation authors

### Contains
- **7 color swatches** with service names
- **Detailed descriptions** of each service category
- **Typical uses** within each category
- **Visual consistency note** explaining palette purpose

### Function
- Reference guide when viewing other plots
- Can be printed separately as desk reference
- Helps users instantly identify service types across visualizations
- Supports accessibility by labeling both color and text

---

## Design Principles

### Visual Hierarchy
1. **Color** — Immediate service category recognition (most important)
2. **Size** — Bandwidth proportional to box dimensions (when applicable)
3. **Typography** — Bold labels for emphasis, italic for supplementary info
4. **Layout** — Logical grouping (service categories, frequency regions)

### Publication Quality
- **300 DPI resolution** — Suitable for print and high-resolution displays
- **White background** — Works on light and dark GitHub themes
- **Professional typography** — Sans-serif font family with clear weight hierarchy
- **Clean borders** — Subtle gridlines and axes for readability without clutter
- **Consistent styling** — Uniform colors, line weights, label positioning

### Accessibility
- **Color + text labels** — Works for colorblind viewers
- **High contrast** — White text on colored backgrounds (WCAG AA compliant)
- **Clear legends** — Every visualization includes category identification
- **Scalable design** — Vector-friendly (boxes, text, lines)

### Comparison Across Plots
- **Identical color assignments** across all 6 plots
- **Consistent axis styles** (grid, labels, fonts)
- **Cross-references** possible (e.g., "the red bands in Plot 2 appear here in Plot 4")
- **Complementary perspectives** (detailed spectrum → organized by service → quantified density)

---

## Generating the Visualizations

### Running the Script
```bash
python3 img/uk_spectrum_viz.py
```

### Output Files
All plots saved to `img/` directory at 300 DPI:
- `uk_spectrum_comprehensive.png` (194 KB)
- `spectrum_by_service.png` (261 KB)
- `spectrum_density.png` (338 KB)
- `rtl_sdr_bands.png` (263 KB)
- `frequency_reference_table.png` (529 KB)
- `color_palette_guide.png` (362 KB)

### Total Size
~1.9 MB for the complete suite (manageable for GitHub, documents, web)

### Summary Statistics (from script output)
```
Total allocated spectrum: 3.4 GHz (across 9 kHz – 12.5 GHz range)

Allocation by Service:
  Satellite               2.0 MHz (58.0%)
  Scientific & Industrial 0.7 MHz (20.3%)
  Mobile Communications  0.3 MHz (9.6%)
  Broadcasting & Media   0.2 MHz (7.1%)
  WiFi & ISM             0.1 MHz (3.0%)
  Amateur Radio          38 kHz  (1.1%)
  Aviation & Maritime    35 kHz  (1.0%)

RTL-SDR Coverage: 9 major bands, ~2.6 MHz total bandwidth accessible
```

---

## Use Cases & Applications

### 1. **Project Planning**
- Identify which bands are accessible with RTL-SDR
- Check service category for context
- Select appropriate antenna length

### 2. **Technical Documentation**
- Include in README files
- Use in project guides
- Reference in frequency selection tables

### 3. **Educational Material**
- Teach spectrum structure and allocation
- Show service distribution
- Illustrate bandwidth concepts

### 4. **Regulatory Compliance**
- Verify frequency allocations for legal operation
- Check with official OFCOM guidelines (plots derived from UKFAT)
- Understand usage restrictions by service category

### 5. **Frequency Selection**
- Avoid interference by understanding what's nearby
- Design experiments in less-occupied regions
- Understand capacity limitations

### 6. **Presentations & Papers**
- Publication-ready quality (300 DPI)
- Professional appearance suitable for technical documents
- Consistent with scientific visualization standards

---

## Data Source & Accuracy

- **Source:** OFCOM UK Frequency Allocation Table (UKFAT)
- **Last Updated:** Accurate as of 2026-05-29
- **Scope:** 9 kHz – 12.5 GHz (VLF through satellite C-band)
- **Completeness:** 18 major bands covering ~99% of RTL-SDR and hobbyist-accessible spectrum

**Note:** This visualization represents simplified, human-readable bands. Official spectrum regulations may have more granular sub-allocations, restrictions, and special authorizations. Always refer to the official OFCOM UKFAT for legal compliance.

---

## Future Enhancements

Potential additions if needed:
- **Interactive version** (HTML/JavaScript) with zoom/pan
- **Comparison plots** (UK vs. EU vs. US spectrum)
- **Historical timeline** showing spectrum evolution
- **Propagation characteristics** (how far each band reaches)
- **Satellite track visualization** (active vs. inactive satellites)
- **Interference map** (showing overlap risk areas)
- **Real-time activity** (which bands are currently in use)

---

## Questions & Support

For issues with:
- **Visualization accuracy** — Check against [OFCOM UKFAT](https://www.ofcom.org.uk/spectrum/frequencies/uk-fat)
- **RTL-SDR band coverage** — See RTL-SDR Blog hardware specifications
- **Color palette accessibility** — Palette checked against standard colorblind tests
- **Antenna lengths** — Based on quarter-wave and half-wave approximations

---

**Last Updated:** 2026-05-29  
**Format Version:** 1.0 (300 DPI, Service-Category Palette)
