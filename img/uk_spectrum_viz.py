#!/usr/bin/env python3
"""
UK Frequency Spectrum Visualization - Clean, Readable Version (Optimized)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ===== PLOT 1: Detailed Spectrum =====
fig, ax = plt.subplots(figsize=(16, 11))

spectrum_bands = [
    ("VLF\n9-14 kHz", 9, 14, "#1a1a4d", 0),
    ("LF\n190-285 kHz", 190, 285, "#2a2a8d", 1),
    ("MF\n526-1606 kHz\nAM Radio", 526, 1606, "#ff9500", 2),
    ("HF (3.5-29.7 MHz)\nAmateur Radio", 3500, 29700, "#d62728", 3),
    ("FM\n88-108 MHz", 88, 108, "#ff0000", 4),
    ("Aviation\n108-137 MHz", 108, 137, "#2ca02c", 5),
    ("2m Amateur\n144-146 MHz", 144, 146, "#9467bd", 6),
    ("Maritime\n156-162 MHz", 156, 162, "#17becf", 7),
    ("PMR\n400-430 MHz", 400, 430, "#ffbb00", 8),
    ("433 ISM", 433, 435, "#ff69b4", 9),
    ("70cm Amateur\n430-440 MHz", 430, 440, "#9467bd", 10),
    ("Digital TV\n470-694 MHz", 470, 694, "#8c564b", 11),
    ("GSM-900\n890-960 MHz", 890, 960, "#e7298a", 12),
    ("GSM-1800\n1710-1880 MHz", 1710, 1880, "#e74c3c", 13),
    ("UMTS-2100\n2110-2170 MHz", 2110, 2170, "#e67e22", 14),
    ("WiFi 2.4GHz\n2400-2500 MHz", 2400, 2500, "#27ae60", 15),
    ("WiFi 5GHz\n5150-5850 MHz", 5150, 5850, "#3498db", 16),
    ("Satellite\n10.5-12.5 GHz", 10500, 12500, "#16a085", 17),
]

for label, freq_min, freq_max, color, y_pos in spectrum_bands:
    if freq_max > 10000:
        log_min = np.log10(freq_min)
        log_max = np.log10(freq_max)
        x_pos = log_min
        width_plot = log_max - log_min
    else:
        x_pos = freq_min
        width_plot = freq_max - freq_min

    rect = FancyBboxPatch((x_pos, y_pos - 0.35), width_plot, 0.7,
                          boxstyle="round,pad=0.02", facecolor=color,
                          edgecolor='black', linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)

    mid_pos = x_pos + width_plot / 2
    ax.text(mid_pos, y_pos, label, ha='center', va='center',
           fontsize=10, weight='bold', color='white', family='monospace')

ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-1, 18)
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(['1 kHz', '10 kHz', '100 kHz', '1 MHz', '10 MHz', '100 MHz'],
                   fontsize=10, weight='bold')
ax.set_yticks([])
ax.set_xlabel('Frequency (Log Scale)', fontsize=12, weight='bold', labelpad=15)
ax.set_title('UK Radio Frequency Spectrum - Ofcom UKFAT', fontsize=14, weight='bold', pad=20)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(axis='x', alpha=0.2, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/uk_spectrum_clean.png',
           dpi=150, bbox_inches='tight', facecolor='white')
print("✓ Saved: uk_spectrum_clean.png")
plt.close()

# ===== PLOT 2: RTL-SDR Bands =====
fig, ax = plt.subplots(figsize=(16, 8))

rtl_bands = [
    ("FM Radio\n88-108 MHz", 88, 108, "#ff0000"),
    ("Aviation\n108-137 MHz", 108, 137, "#2ca02c"),
    ("2m Amateur\n144-146 MHz", 144, 146, "#9467bd"),
    ("433 ISM\n433-435 MHz", 433, 435, "#ff69b4"),
    ("UHF TV\n470-694 MHz", 470, 694, "#8c564b"),
    ("GSM-900\n890-960 MHz", 890, 960, "#e7298a"),
    ("GSM-1800\n1710-1880 MHz", 1710, 1880, "#e74c3c"),
    ("WiFi 2.4GHz\n2400-2500 MHz", 2400, 2500, "#27ae60"),
]

for i, (label, freq_min, freq_max, color) in enumerate(rtl_bands):
    y_pos = 7 - i
    width = freq_max - freq_min
    
    rect = FancyBboxPatch((freq_min, y_pos - 0.35), width, 0.7,
                          boxstyle="round,pad=0.01", facecolor=color,
                          edgecolor='black', linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    
    mid = freq_min + width / 2
    ax.text(mid, y_pos, label, ha='center', va='center',
           fontsize=11, weight='bold', color='white', family='monospace')

ax.set_xlim(0, 2700)
ax.set_ylim(-0.5, 8)
ax.set_xticks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500])
ax.set_xticklabels(['0', '250', '500', '750', '1000', '1250', '1500', '1750', '2000', '2250', '2500 MHz'],
                   fontsize=9, weight='bold', rotation=45, ha='right')
ax.set_yticks([])
ax.set_xlabel('Frequency (MHz)', fontsize=12, weight='bold', labelpad=15)
ax.set_title('RTL-SDR Common Bands (VHF/UHF)', fontsize=14, weight='bold', pad=20)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(axis='x', alpha=0.2, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/rtl_sdr_bands.png',
           dpi=150, bbox_inches='tight', facecolor='white')
print("✓ Saved: rtl_sdr_bands.png")
plt.close()

# ===== PLOT 3: Reference Table =====
fig, ax = plt.subplots(figsize=(14, 10))

frequency_data = [
    ["Band", "Frequency", "Usage", "RTL-SDR", "Antenna"],
    ["FM Radio", "88-108 MHz", "Broadcast", "Yes", "50 cm"],
    ["Aviation", "108-137 MHz", "Air Traffic", "Yes", "50 cm"],
    ["2m Amateur", "144-146 MHz", "Amateur Radio", "Yes", "50 cm"],
    ["433 ISM", "433-435 MHz", "Sensors", "Yes", "20 cm"],
    ["UHF TV", "470-694 MHz", "Digital TV", "Yes", "30 cm"],
    ["70cm Amateur", "430-440 MHz", "Amateur Radio", "Yes", "20 cm"],
    ["GSM-900", "890-960 MHz", "Mobile", "Yes", "15 cm"],
    ["GSM-1800", "1710-1880 MHz", "Mobile", "Yes", "10 cm"],
    ["UMTS-2100", "2110-2170 MHz", "3G/Mobile", "Yes", "8 cm"],
    ["WiFi 2.4GHz", "2400-2500 MHz", "WiFi", "Yes", "5 cm"],
    ["WiFi 5GHz", "5150-5850 MHz", "WiFi", "Limited", "3 cm"],
    ["Satellites", "10.5-12.5 GHz", "Downlink", "No", "Dish"],
]

colors = []
for i, row in enumerate(frequency_data):
    if i == 0:
        colors.append(['#333333'] * 5)
    elif row[3] == "Yes":
        colors.append(['#d4edda'] * 5)
    elif row[3] == "Limited":
        colors.append(['#fff3cd'] * 5)
    else:
        colors.append(['#f8d7da'] * 5)

table = ax.table(cellText=frequency_data, cellLoc='center', loc='center',
                cellColours=colors, colWidths=[0.15, 0.2, 0.25, 0.15, 0.15])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.2)

for i in range(5):
    table[(0, i)].set_text_props(weight='bold', color='white', fontsize=11)

for i in range(len(frequency_data)):
    for j in range(5):
        cell = table[(i, j)]
        cell.set_linewidth(1.5)
        cell.set_edgecolor('black')

ax.axis('off')
ax.set_title('UK Frequency Bands - RTL-SDR Reference\nGreen=Good for RTL-SDR | Yellow=Limited | Red=Not Suitable',
            fontsize=13, weight='bold', pad=20)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/frequency_table.png',
           dpi=150, bbox_inches='tight', facecolor='white')
print("✓ Saved: frequency_table.png")
plt.close()

print("\n✓ All plots generated (150 DPI) - readable and optimized!")
