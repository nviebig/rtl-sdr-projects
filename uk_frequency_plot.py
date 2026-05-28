#!/usr/bin/env python3
"""
UK Frequency Allocation Table Visualization
Based on Ofcom UKFAT data
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# UK Frequency Allocations (MHz ranges)
# Based on Ofcom UK Frequency Allocation Table
uk_allocations = [
    # VLF
    ("VLF Navigation", 9, 14, "darkblue"),

    # LF
    ("Maritime/Aero Radiobeacon", 190, 285, "navy"),
    ("AM Radio", 526, 1606, "blue"),

    # MF
    ("Maritime", 1606, 2850, "lightblue"),

    # HF (Shortwave)
    ("Amateur Radio (HF)", 1800, 30000, "orange"),

    # VHF
    ("FM Radio", 88, 108, "red"),
    ("Air Traffic Control", 108, 136, "darkgreen"),
    ("Maritime VHF", 156, 162, "lightgreen"),
    ("Amateur Radio (2m)", 144, 146, "gold"),

    # UHF
    ("Digital TV/UHF TV", 470, 694, "purple"),
    ("PMR/Walkie-talkies", 400, 430, "magenta"),
    ("ISM/Microwave", 433.05, 434.79, "pink"),
    ("Amateur Radio (70cm)", 430, 440, "yellow"),
    ("Mobile/4G/5G", 694, 960, "red"),
    ("GSM 900", 890, 960, "darkred"),
    ("GSM 1800", 1710, 1880, "crimson"),

    # Cellular/Mobile
    ("UMTS 2100", 2110, 2170, "darkred"),
    ("WiFi 2.4 GHz", 2400, 2500, "green"),
    ("Amateur Radio (23cm)", 1240, 1325, "lightgreen"),

    # Higher bands
    ("ISM 5 GHz", 5150, 5925, "lightblue"),
    ("WiFi 5 GHz", 5150, 5850, "cyan"),
    ("Satellites", 10500, 12500, "navy"),
    ("Millimeter Wave (5G)", 26000, 40000, "gray"),
]

fig, ax = plt.subplots(figsize=(16, 10))

# Plot allocations
y_pos = 0
colors_used = {}
y_labels = []
y_ticks = []

for service, freq_min, freq_max, color in uk_allocations:
    width = freq_max - freq_min
    rect = Rectangle((freq_min, y_pos), width, 0.8,
                     facecolor=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    ax.add_patch(rect)

    # Add label
    mid_freq = (freq_min + freq_max) / 2
    if width > 500:  # Only label if band is wide enough
        ax.text(mid_freq, y_pos + 0.4, service,
               ha='center', va='center', fontsize=8, weight='bold', color='white')

    y_labels.append(service[:25])  # Truncate long names
    y_ticks.append(y_pos + 0.4)
    y_pos += 1

# Styling
ax.set_xlim(0, 40000)
ax.set_ylim(-1, y_pos)
ax.set_xlabel('Frequency (MHz)', fontsize=14, weight='bold')
ax.set_ylabel('Services', fontsize=14, weight='bold')
ax.set_title('UK Frequency Allocation Table (Ofcom UKFAT)', fontsize=16, weight='bold')

# X-axis formatting
ax.set_xticks([0, 100, 500, 1000, 2000, 5000, 10000, 20000, 40000])
ax.set_xticklabels(['0 MHz', '100 MHz', '500 MHz', '1 GHz', '2 GHz', '5 GHz',
                    '10 GHz', '20 GHz', '40 GHz'])

# Y-axis
ax.set_yticks([])

# Grid
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add frequency bands as reference lines
band_references = [
    (88, "VHF FM", "red"),
    (470, "UHF TV", "purple"),
    (2400, "WiFi 2.4GHz", "green"),
    (5000, "WiFi 5GHz", "cyan"),
]

for freq, label, color in band_references:
    ax.axvline(x=freq, color=color, linestyle=':', alpha=0.5, linewidth=1)
    ax.text(freq, y_pos - 0.5, label, rotation=90, fontsize=8, alpha=0.7)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/uk_frequency_allocation.png', dpi=150, bbox_inches='tight')
print("Plot saved to: uk_frequency_allocation.png")

# Also create a log-scale version for better visualization of small bands
fig2, ax2 = plt.subplots(figsize=(16, 10))

y_pos = 0
for service, freq_min, freq_max, color in uk_allocations:
    width = freq_max - freq_min
    rect = Rectangle((np.log10(freq_min), y_pos),
                     np.log10(freq_max) - np.log10(freq_min), 0.8,
                     facecolor=color, edgecolor='black', linewidth=0.5, alpha=0.8)
    ax2.add_patch(rect)

    # Add label
    mid_freq = np.log10(np.sqrt(freq_min * freq_max))
    if width > 50:
        ax2.text(mid_freq, y_pos + 0.4, service,
                ha='center', va='center', fontsize=8, weight='bold', color='white')

    y_pos += 1

ax2.set_xlim(0, 5)  # log10(100000) ≈ 5
ax2.set_ylim(-1, y_pos)
ax2.set_xlabel('Frequency (logarithmic scale, MHz)', fontsize=14, weight='bold')
ax2.set_ylabel('Services', fontsize=14, weight='bold')
ax2.set_title('UK Frequency Allocation Table - Log Scale (Ofcom UKFAT)', fontsize=16, weight='bold')

# X-axis formatting for log scale
ax2.set_xticks([0, 1, 2, 3, 4, 5])
ax2.set_xticklabels(['1 MHz', '10 MHz', '100 MHz', '1 GHz', '10 GHz', '100 GHz'])
ax2.set_yticks([])
ax2.grid(axis='x', alpha=0.3, linestyle='--')
ax2.set_axisbelow(True)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/uk_frequency_allocation_log.png', dpi=150, bbox_inches='tight')
print("Log-scale plot saved to: uk_frequency_allocation_log.png")

plt.show()
