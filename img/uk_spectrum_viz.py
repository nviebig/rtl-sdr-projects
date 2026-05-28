#!/usr/bin/env python3
"""
UK Frequency Spectrum Visualization - Better Version
Based on Ofcom UKFAT
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# Better organized frequency data with standard UK allocations
spectrum_data = [
    # LF/MF (Low/Medium Frequency)
    ("Maritime Radiobeacon", 190, 285, "#1f77b4"),
    ("AM Broadcast", 526, 1606, "#ff7f0e"),

    # HF (High Frequency / Shortwave) - Amateur bands
    ("160m Amateur", 1800, 2000, "#d62728"),
    ("80m Amateur", 3500, 4000, "#d62728"),
    ("40m Amateur", 7000, 7300, "#d62728"),
    ("20m Amateur", 14000, 14350, "#d62728"),
    ("15m Amateur", 21000, 21450, "#d62728"),
    ("10m Amateur", 28000, 29700, "#d62728"),

    # VHF (Very High Frequency)
    ("Aviation VHF", 108, 137, "#2ca02c"),
    ("FM Broadcast", 88, 108, "#ff0000"),
    ("2m Amateur (144-146)", 144, 146, "#9467bd"),
    ("Maritime VHF", 156, 162, "#17becf"),

    # Lower UHF
    ("PMR/Walkie-talkies", 400, 430, "#bcbd22"),
    ("ISM/433MHz", 433, 435, "#e377c2"),
    ("70cm Amateur", 430, 440, "#9467bd"),

    # Upper UHF / Digital
    ("Digital TV (UHF)", 470, 694, "#8c564b"),
    ("GSM-900", 890, 960, "#e7298a"),
    ("GSM-1800", 1710, 1880, "#e7298a"),

    # Microwave/SHF
    ("UMTS-2100", 2110, 2170, "#66c2a5"),
    ("WiFi 2.4GHz", 2400, 2500, "#fc8d62"),
    ("ISM 5GHz", 5150, 5925, "#8da0cb"),
    ("WiFi 5GHz", 5150, 5850, "#fc8d62"),
    ("Satellites (downlink)", 10500, 12500, "#1b9e77"),
]

# Create figure with two subplots
fig = plt.figure(figsize=(18, 12))

# ===== SUBPLOT 1: Logarithmic Spectrum =====
ax1 = plt.subplot(2, 1, 1)

y_pos = 0
band_heights = {}

for service, freq_min, freq_max, color in spectrum_data:
    log_min = np.log10(freq_min)
    log_max = np.log10(freq_max)
    width = log_max - log_min

    # Draw rectangle
    rect = FancyBboxPatch((log_min, y_pos), width, 0.9,
                          boxstyle="round,pad=0.01",
                          facecolor=color, edgecolor='black',
                          linewidth=1, alpha=0.85)
    ax1.add_patch(rect)

    # Add text label
    mid_pos = (log_min + log_max) / 2
    ax1.text(mid_pos, y_pos + 0.45, f"{service}\n({freq_min:.0f}-{freq_max:.0f}MHz)",
            ha='center', va='center', fontsize=7, weight='bold', color='white')

    y_pos += 1.2

# Formatting
ax1.set_xlim(2, 4.2)  # 100 MHz to ~15 GHz
ax1.set_ylim(-1, y_pos)
ax1.set_xlabel('Frequency (Logarithmic Scale)', fontsize=12, weight='bold')
ax1.set_title('UK Radio Frequency Spectrum (Ofcom UKFAT)', fontsize=14, weight='bold', pad=20)

# X-axis labels
ax1.set_xticks([2, 2.5, 3, 3.5, 4, 4.2])
ax1.set_xticklabels(['100 MHz', '316 MHz', '1 GHz', '3.16 GHz', '10 GHz', '~15 GHz'], fontsize=10)
ax1.set_yticks([])

ax1.grid(axis='x', alpha=0.2, linestyle='--')
ax1.set_axisbelow(True)
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# ===== SUBPLOT 2: Key Bands for RTL-SDR =====
ax2 = plt.subplot(2, 1, 2)

rtl_sdr_bands = [
    ("FM Radio\n88-108 MHz", 88, 108, "#ff0000"),
    ("Aerospace\n108-137 MHz", 108, 137, "#2ca02c"),
    ("2m Amateur\n144-146 MHz", 144, 146, "#9467bd"),
    ("UHF TV\n470-694 MHz", 470, 694, "#8c564b"),
    ("433 ISM\n433-435 MHz", 433, 435, "#e377c2"),
    ("GSM-900\n890-960 MHz", 890, 960, "#e7298a"),
    ("GSM-1800\n1710-1880 MHz", 1710, 1880, "#e7298a"),
    ("WiFi 2.4GHz\n2400-2500 MHz", 2400, 2500, "#fc8d62"),
]

x_pos = 0
for label, freq_min, freq_max, color in rtl_sdr_bands:
    width = freq_max - freq_min
    height = 3

    rect = FancyBboxPatch((x_pos, 0), width, height,
                          boxstyle="round,pad=0.02",
                          facecolor=color, edgecolor='black',
                          linewidth=1.5, alpha=0.85)
    ax2.add_patch(rect)

    # Add text
    ax2.text(x_pos + width/2, height/2, label,
            ha='center', va='center', fontsize=9, weight='bold', color='white')

    x_pos += width + 50

# Formatting
ax2.set_xlim(0, x_pos)
ax2.set_ylim(0, 3.5)
ax2.set_xlabel('Frequency (MHz)', fontsize=12, weight='bold')
ax2.set_title('Common Bands for RTL-SDR Reception', fontsize=12, weight='bold', pad=15)

# Add frequency ruler
ruler_y = -0.5
for freq in range(0, int(x_pos) + 500, 500):
    ax2.plot([freq, freq], [0, -0.2], 'k-', linewidth=0.5)
    if freq % 1000 == 0:
        ax2.text(freq, ruler_y, f"{freq//1000}GHz" if freq >= 1000 else f"{freq}MHz",
                ha='center', fontsize=7)

ax2.set_yticks([])
ax2.set_xticks([])
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/uk_spectrum_clean.png',
           dpi=200, bbox_inches='tight', facecolor='white')
print("✓ Saved: uk_spectrum_clean.png")

# ===== Create a simpler frequency table plot =====
fig2, ax = plt.subplots(figsize=(14, 10))

# Group by frequency range
frequency_groups = {
    'LF (30-300 kHz)': [
        ('Maritime Beacon', '190-285 kHz'),
    ],
    'MF (300 kHz-3 MHz)': [
        ('AM Broadcast', '526-1606 kHz'),
    ],
    'HF (3-30 MHz)': [
        ('Amateur 80m', '3.5-4.0 MHz'),
        ('Amateur 40m', '7.0-7.3 MHz'),
        ('Amateur 20m', '14.0-14.35 MHz'),
        ('Amateur 15m', '21.0-21.45 MHz'),
        ('Amateur 10m', '28.0-29.7 MHz'),
    ],
    'VHF (30-300 MHz)': [
        ('FM Broadcast', '88-108 MHz'),
        ('Aviation', '108-137 MHz'),
        ('2m Amateur', '144-146 MHz'),
        ('Maritime VHF', '156-162 MHz'),
    ],
    'UHF (300 MHz-3 GHz)': [
        ('PMR/Walkie-talkies', '400-430 MHz'),
        ('433 ISM Band', '433-435 MHz'),
        ('70cm Amateur', '430-440 MHz'),
        ('Digital TV', '470-694 MHz'),
        ('GSM-900', '890-960 MHz'),
        ('GSM-1800', '1710-1880 MHz'),
        ('UMTS-2100', '2110-2170 MHz'),
        ('WiFi 2.4GHz', '2400-2500 MHz'),
    ],
    'SHF (3-30 GHz)': [
        ('ISM 5GHz', '5150-5925 MHz'),
        ('WiFi 5GHz', '5150-5850 MHz'),
        ('Satellite Downlink', '10.5-12.5 GHz'),
    ],
}

y_pos = 0
colors = ['#ff7f0e', '#d62728', '#2ca02c', '#17becf', '#8c564b', '#e7298a']
color_idx = 0

for group, bands in frequency_groups.items():
    # Group header
    ax.text(-0.02, y_pos, group, fontsize=11, weight='bold',
           bbox=dict(boxstyle='round', facecolor=colors[color_idx], alpha=0.7, edgecolor='black'))
    y_pos -= 1

    # Bands
    for band_name, band_freq in bands:
        ax.text(0, y_pos, f"  {band_name}", fontsize=9, va='center')
        ax.text(0.6, y_pos, band_freq, fontsize=9, va='center', style='italic')
        y_pos -= 0.6

    y_pos -= 0.4
    color_idx += 1

ax.set_xlim(-0.05, 1)
ax.set_ylim(y_pos, 1)
ax.axis('off')
ax.set_title('UK Frequency Bands Reference (Ofcom UKFAT)', fontsize=14, weight='bold', pad=20)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/uk_frequency_reference.png',
           dpi=200, bbox_inches='tight', facecolor='white')
print("✓ Saved: uk_frequency_reference.png")

print("\n✓ All plots generated successfully!")
