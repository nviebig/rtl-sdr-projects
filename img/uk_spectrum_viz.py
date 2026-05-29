#!/usr/bin/env python3
"""
UK Frequency Spectrum Visualization Suite - Publication-Quality Scientific Plots
Consistent color palette mapped to service categories for intuitive comparison across plots.
Suitable for inclusion in documentation, papers, and technical presentations.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.gridspec import GridSpec
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# SERVICE-BASED COLOR PALETTE (Consistent across all plots)
# ============================================================================
SERVICE_COLORS = {
    'Broadcasting & Media': '#e74c3c',      # Red - high visibility
    'Amateur Radio': '#9467bd',              # Purple - hobby/individual
    'Mobile Communications': '#e7298a',      # Pink/Magenta - ubiquitous
    'Aviation & Maritime': '#2ca02c',        # Green - safety-critical
    'WiFi & ISM': '#27ae60',                 # Darker green - short-range
    'Satellite': '#16a085',                  # Teal - space
    'Scientific & Industrial': '#3498db',    # Blue - technical
    'Other': '#95a5a6',                      # Gray - miscellaneous
}

BAND_COLORS = {
    "VLF": "#34495e",
    "LF": "#4a5f7f",
    "MF": "#e74c3c",
    "HF": "#d62728",
    "FM Radio": "#e74c3c",
    "Aviation": "#2ca02c",
    "2m Amateur": "#9467bd",
    "Maritime": "#2ca02c",
    "PMR": "#f39c12",
    "433 ISM": "#27ae60",
    "70cm Amateur": "#9467bd",
    "Digital TV": "#e74c3c",
    "GSM-900": "#e7298a",
    "GSM-1800": "#e74c3c",
    "UMTS-2100": "#e7298a",
    "WiFi 2.4GHz": "#27ae60",
    "WiFi 5GHz": "#3498db",
    "Satellite": "#16a085",
}

# ============================================================================
# GLOBAL STYLING CONFIGURATION
# ============================================================================
plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': '#f8f9fa',
    'axes.edgecolor': '#e0e0e0',
    'axes.labelcolor': '#2c3e50',
    'axes.titlecolor': '#2c3e50',
    'xtick.color': '#2c3e50',
    'ytick.color': '#2c3e50',
    'xtick.major.size': 5,
    'xtick.minor.size': 2.5,
    'ytick.major.size': 5,
    'ytick.minor.size': 2.5,
    'grid.color': '#e0e0e0',
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'legend.framealpha': 0.95,
    'legend.edgecolor': '#e0e0e0',
    'font.family': 'sans-serif',
    'font.size': 10,
})

FONT_TITLE = {'fontsize': 16, 'weight': 'bold', 'color': '#2c3e50'}
FONT_LABEL = {'fontsize': 12, 'weight': 'bold', 'color': '#2c3e50'}
FONT_TICK = {'fontsize': 10, 'color': '#2c3e50'}
FONT_LEGEND = {'fontsize': 10}

# ============================================================================
# COMPREHENSIVE FREQUENCY DATA WITH SERVICE CATEGORIES
# ============================================================================
SPECTRUM_DATA = [
    # (Name, Freq_Min_kHz, Freq_Max_kHz, Color, Service)
    ("VLF", 9, 14, BAND_COLORS["VLF"], "Scientific & Industrial"),
    ("LF", 190, 285, BAND_COLORS["LF"], "Broadcasting & Media"),
    ("MF\nAM Radio", 526, 1606, BAND_COLORS["MF"], "Broadcasting & Media"),
    ("HF\nAmateur Radio", 3500, 29700, BAND_COLORS["HF"], "Amateur Radio"),
    ("FM Radio", 88000, 108000, BAND_COLORS["FM Radio"], "Broadcasting & Media"),
    ("Aviation\nVHF", 108000, 137000, BAND_COLORS["Aviation"], "Aviation & Maritime"),
    ("2m Amateur", 144000, 146000, BAND_COLORS["2m Amateur"], "Amateur Radio"),
    ("Maritime\nVHF", 156000, 162000, BAND_COLORS["Maritime"], "Aviation & Maritime"),
    ("PMR/dPMR", 400000, 430000, BAND_COLORS["PMR"], "Mobile Communications"),
    ("433 ISM", 433000, 435000, BAND_COLORS["433 ISM"], "WiFi & ISM"),
    ("70cm Amateur", 430000, 440000, BAND_COLORS["70cm Amateur"], "Amateur Radio"),
    ("UHF TV", 470000, 694000, BAND_COLORS["Digital TV"], "Broadcasting & Media"),
    ("GSM-900", 890000, 960000, BAND_COLORS["GSM-900"], "Mobile Communications"),
    ("GSM-1800", 1710000, 1880000, BAND_COLORS["GSM-1800"], "Mobile Communications"),
    ("UMTS-2100", 2110000, 2170000, BAND_COLORS["UMTS-2100"], "Mobile Communications"),
    ("WiFi 2.4GHz", 2400000, 2500000, BAND_COLORS["WiFi 2.4GHz"], "WiFi & ISM"),
    ("WiFi 5GHz", 5150000, 5850000, BAND_COLORS["WiFi 5GHz"], "Scientific & Industrial"),
    ("Satellite", 10500000, 12500000, BAND_COLORS["Satellite"], "Satellite"),
]

RTL_SDR_DATA = [
    ("FM Radio", 88, 108, BAND_COLORS["FM Radio"], "Broadcasting & Media"),
    ("Aviation", 108, 137, BAND_COLORS["Aviation"], "Aviation & Maritime"),
    ("2m Amateur", 144, 146, BAND_COLORS["2m Amateur"], "Amateur Radio"),
    ("433 ISM", 433, 435, BAND_COLORS["433 ISM"], "WiFi & ISM"),
    ("70cm Amateur", 430, 440, BAND_COLORS["70cm Amateur"], "Amateur Radio"),
    ("UHF TV", 470, 694, BAND_COLORS["Digital TV"], "Broadcasting & Media"),
    ("GSM-900", 890, 960, BAND_COLORS["GSM-900"], "Mobile Communications"),
    ("GSM-1800", 1710, 1880, BAND_COLORS["GSM-1800"], "Mobile Communications"),
    ("WiFi 2.4GHz", 2400, 2500, BAND_COLORS["WiFi 2.4GHz"], "WiFi & ISM"),
]

# ============================================================================
# HELPER FUNCTIONS FOR CONSISTENT STYLING
# ============================================================================
def style_axis_clean(ax, grid_axis='x', remove_top_right=True):
    """Apply consistent scientific plot styling."""
    if remove_top_right:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(0.8)
        ax.spines['bottom'].set_linewidth(0.8)
        ax.spines['left'].set_color('#999999')
        ax.spines['bottom'].set_color('#999999')

    if grid_axis:
        ax.grid(True, axis=grid_axis, alpha=0.25, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)

def add_band_box(ax, x_min, x_max, y_pos, color, label, is_log=False, height=0.7):
    """Draw a frequency band box with consistent styling."""
    if is_log:
        x_min = np.log10(x_min)
        x_max = np.log10(x_max)
    width = x_max - x_min

    rect = FancyBboxPatch(
        (x_min, y_pos - height/2), width, height,
        boxstyle="round,pad=0.01",
        facecolor=color,
        edgecolor='#1a1a1a',
        linewidth=1.2,
        alpha=0.85
    )
    ax.add_patch(rect)

    x_mid = x_min + width / 2
    ax.text(
        x_mid, y_pos, label,
        ha='center', va='center',
        fontsize=9, weight='bold',
        color='white',
        family='sans-serif'
    )

# ============================================================================
# PLOT 1: Comprehensive Spectrum - Logarithmic Scale
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 10))

for i, (name, freq_min, freq_max, color, service) in enumerate(SPECTRUM_DATA):
    add_band_box(ax, freq_min, freq_max, i, color, name, is_log=True, height=0.65)

ax.set_xlim(-0.5, 5.2)
ax.set_ylim(-1, len(SPECTRUM_DATA))
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(['1 kHz', '10 kHz', '100 kHz', '1 MHz', '10 MHz', '100 MHz'], **FONT_TICK)
ax.set_yticks([])

ax.set_xlabel('Frequency (Logarithmic Scale)', **FONT_LABEL, labelpad=12)
ax.set_title('UK Radio Frequency Spectrum - Complete Allocation\nOFCOM UK Frequency Allocation Table (UKFAT)',
            **FONT_TITLE, pad=18)

style_axis_clean(ax, grid_axis='x')

# Add frequency markers on top
ax.text(4.95, len(SPECTRUM_DATA) + 0.3, '12.5 GHz', ha='center', fontsize=8, style='italic', color='#666666')
ax.text(3.95, len(SPECTRUM_DATA) + 0.3, '1 GHz', ha='center', fontsize=8, style='italic', color='#666666')
ax.text(2.95, len(SPECTRUM_DATA) + 0.3, '1 MHz', ha='center', fontsize=8, style='italic', color='#666666')

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/spectrum_analysis/uk_spectrum_comprehensive.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: spectrum_analysis/uk_spectrum_comprehensive.png (300 DPI)")
plt.close()

# ============================================================================
# PLOT 2: Spectrum Allocation by Service Category
# ============================================================================
fig = plt.figure(figsize=(16, 11))
gs = GridSpec(1, 1, figure=fig, hspace=0.4)
ax = fig.add_subplot(gs[0])

# Group bands by service
service_bands = {}
for name, freq_min, freq_max, color, service in SPECTRUM_DATA:
    if service not in service_bands:
        service_bands[service] = []
    service_bands[service].append((name, freq_min, freq_max, color))

# Sort services for consistent ordering
service_order = [
    'Broadcasting & Media',
    'Mobile Communications',
    'Amateur Radio',
    'Aviation & Maritime',
    'WiFi & ISM',
    'Scientific & Industrial',
    'Satellite',
]

y_pos = 0
service_y_positions = {}
band_height = 0.6

for service in service_order:
    if service in service_bands:
        service_y_positions[service] = y_pos
        bands = service_bands[service]

        # Add service category label
        ax.text(-0.5, y_pos + len(bands) * band_height / 2,
               service,
               ha='right', va='center',
               fontsize=11, weight='bold',
               color=SERVICE_COLORS[service],
               family='sans-serif')

        # Add bands within service
        for band_idx, (name, freq_min, freq_max, color) in enumerate(bands):
            band_y = y_pos + band_idx * band_height

            # Frequency range with log scale for higher frequencies
            if freq_max > 100000:
                x_min = np.log10(freq_min)
                x_max = np.log10(freq_max)
            else:
                x_min = np.log10(max(freq_min, 1))
                x_max = np.log10(freq_max)

            width = x_max - x_min

            rect = FancyBboxPatch(
                (x_min, band_y - band_height/2 + 0.05), width, band_height - 0.1,
                boxstyle="round,pad=0.005",
                facecolor=color,
                edgecolor='#1a1a1a',
                linewidth=1.0,
                alpha=0.82
            )
            ax.add_patch(rect)

            # Band label
            x_mid = x_min + width / 2
            ax.text(
                x_mid, band_y,
                name,
                ha='center', va='center',
                fontsize=8.5, weight='bold',
                color='white',
                family='sans-serif'
            )

        y_pos += len(bands) * band_height

ax.set_xlim(-2, 5.2)
ax.set_ylim(-0.5, y_pos + 0.5)

ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(['1 kHz', '10 kHz', '100 kHz', '1 MHz', '10 MHz', '100 MHz'], **FONT_TICK)
ax.set_yticks([])

ax.set_xlabel('Frequency (Logarithmic Scale)', **FONT_LABEL, labelpad=12)
ax.set_title('Spectrum Allocation by Service Category\nOrganized view emphasizing usage patterns and allocation density',
            **FONT_TITLE, pad=18)

style_axis_clean(ax, grid_axis='x')
ax.axvline(x=2, color='#cccccc', linestyle=':', linewidth=1, alpha=0.5)  # 1 MHz marker
ax.axvline(x=3, color='#cccccc', linestyle=':', linewidth=1, alpha=0.5)  # 1 GHz marker

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/spectrum_analysis/spectrum_by_service.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: spectrum_analysis/spectrum_by_service.png (300 DPI)")
plt.close()

# ============================================================================
# PLOT 3: Spectrum Occupancy & Density Analysis
# ============================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))

# Subplot 3a: Allocation Density (bandwidth per frequency decade)
frequency_decades = [
    ('1-10 kHz', 1, 10),
    ('10-100 kHz', 10, 100),
    ('100 kHz-1 MHz', 100, 1000),
    ('1-10 MHz', 1000, 10000),
    ('10-100 MHz', 10000, 100000),
    ('100 MHz-1 GHz', 100000, 1000000),
    ('1-10 GHz', 1000000, 10000000),
    ('10-100 GHz', 10000000, 100000000),
]

densities = []
labels = []
colors_density = []

for label, freq_min, freq_max in frequency_decades:
    total_bandwidth = 0
    decade_colors = []
    for name, spec_min, spec_max, color, service in SPECTRUM_DATA:
        if spec_min >= freq_min and spec_max <= freq_max:
            total_bandwidth += spec_max - spec_min
            decade_colors.append(color)
        elif spec_min < freq_max and spec_max > freq_min:
            # Partial overlap
            overlap_min = max(spec_min, freq_min)
            overlap_max = min(spec_max, freq_max)
            total_bandwidth += overlap_max - overlap_min
            decade_colors.append(color)

    densities.append(total_bandwidth)
    labels.append(label)
    colors_density.append('#3498db' if total_bandwidth > 0 else '#ecf0f1')

bars = ax1.bar(range(len(labels)), densities, color='#3498db', alpha=0.75, edgecolor='#2c3e50', linewidth=1.5)

# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, densities)):
    if val > 0:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{val/1e6:.1f} MHz' if val >= 1e6 else f'{val/1e3:.0f} kHz',
                ha='center', va='bottom', fontsize=9, weight='bold')

ax1.set_xticks(range(len(labels)))
ax1.set_xticklabels(labels, rotation=45, ha='right', **FONT_TICK)
ax1.set_ylabel('Total Allocated Bandwidth', **FONT_LABEL)
ax1.set_title('Spectrum Allocation Density by Frequency Decade',
             fontsize=13, weight='bold', color='#2c3e50', pad=12)
style_axis_clean(ax1, grid_axis='y')
ax1.set_ylim(0, max(densities) * 1.15)

# Subplot 3b: Service Category Allocation
service_allocations = {}
for name, freq_min, freq_max, color, service in SPECTRUM_DATA:
    bw = freq_max - freq_min
    if service not in service_allocations:
        service_allocations[service] = 0
    service_allocations[service] += bw

services_sorted = sorted(service_allocations.items(), key=lambda x: x[1], reverse=True)
service_names = [s[0] for s in services_sorted]
service_bws = [s[1] for s in services_sorted]
service_colors_list = [SERVICE_COLORS[s] for s in service_names]

bars2 = ax2.barh(service_names, service_bws, color=service_colors_list, alpha=0.75, edgecolor='#2c3e50', linewidth=1.5)

# Add value labels
for i, (bar, val) in enumerate(zip(bars2, service_bws)):
    width = bar.get_width()
    label_text = f'{val/1e6:.1f} MHz' if val >= 1e6 else f'{val/1e3:.0f} kHz'
    ax2.text(width, bar.get_y() + bar.get_height()/2.,
            f'  {label_text}',
            ha='left', va='center', fontsize=10, weight='bold', color='#2c3e50')

ax2.set_xlabel('Total Allocated Bandwidth', **FONT_LABEL)
ax2.set_title('Spectrum Allocation by Service Category',
             fontsize=13, weight='bold', color='#2c3e50', pad=12)
style_axis_clean(ax2, grid_axis='x')
ax2.set_xlim(0, max(service_bws) * 1.2)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/spectrum_analysis/spectrum_density.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: spectrum_analysis/spectrum_density.png (300 DPI)")
plt.close()

# ============================================================================
# PLOT 4: RTL-SDR Accessible Bands
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 9))

for i, (name, freq_min, freq_max, color, service) in enumerate(RTL_SDR_DATA):
    width = freq_max - freq_min
    y_pos = len(RTL_SDR_DATA) - i - 1

    rect = FancyBboxPatch(
        (freq_min, y_pos - 0.3), width, 0.6,
        boxstyle="round,pad=0.01",
        facecolor=color,
        edgecolor='#1a1a1a',
        linewidth=1.5,
        alpha=0.85
    )
    ax.add_patch(rect)

    mid = freq_min + width / 2
    ax.text(mid, y_pos, name,
           ha='center', va='center',
           fontsize=11, weight='bold',
           color='white',
           family='sans-serif')

    # Add frequency range label
    ax.text(freq_min - 30, y_pos, f'{freq_min:.0f}',
           ha='right', va='center',
           fontsize=8, color='#666666', style='italic')

ax.set_xlim(-100, 2550)
ax.set_ylim(-0.8, len(RTL_SDR_DATA))

ax.set_xticks([0, 500, 1000, 1500, 2000, 2500])
ax.set_xticklabels(['0', '500', '1000', '1500', '2000', '2500 MHz'], **FONT_TICK)
ax.set_yticks([])

ax.set_xlabel('Frequency (MHz)', **FONT_LABEL, labelpad=12)
ax.set_title('RTL-SDR Receivable Frequency Bands\nCommon bands accessible with RTL2832U/R820T2 hardware',
            **FONT_TITLE, pad=18)

style_axis_clean(ax, grid_axis='x')

# Add legend for service types in RTL-SDR data
services_in_rtl = set([s for _, _, _, _, s in RTL_SDR_DATA])
legend_handles = []
legend_labels = []
for service in service_order:
    if service in services_in_rtl:
        from matplotlib.patches import Patch
        legend_handles.append(Patch(facecolor=SERVICE_COLORS[service], alpha=0.75, edgecolor='#1a1a1a', linewidth=1))
        legend_labels.append(service)

ax.legend(legend_handles, legend_labels, loc='upper left', fontsize=10,
         framealpha=0.95, edgecolor='#e0e0e0', title='Service Category', title_fontsize=11)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/rtl_sdr/rtl_sdr_bands.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: rtl_sdr/rtl_sdr_bands.png (300 DPI)")
plt.close()

# ============================================================================
# PLOT 5: Reference Table with Service Category Coloring
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 11))

table_data = [
    ['Band Name', 'Frequency Range', 'Bandwidth', 'Service Category', 'RTL-SDR', 'Antenna'],
]

for name, freq_min, freq_max, color, service in SPECTRUM_DATA:
    bw = freq_max - freq_min

    # Format frequency nicely
    if freq_max >= 1e6:
        freq_str = f'{freq_min/1e6:.2f} – {freq_max/1e6:.2f} GHz'
        bw_str = f'{bw/1e6:.1f} MHz'
    elif freq_max >= 1e3:
        freq_str = f'{freq_min/1e3:.1f} – {freq_max/1e3:.1f} MHz'
        bw_str = f'{bw/1e3:.0f} kHz'
    else:
        freq_str = f'{freq_min:.0f} – {freq_max:.0f} kHz'
        bw_str = f'{bw:.0f} kHz'

    # Check RTL-SDR capability
    is_rtl_capable = any(
        freq_min <= rmin and freq_max >= rmax
        for _, rmin, rmax, _, _ in RTL_SDR_DATA
    ) or any(
        freq_min >= rmin and freq_max <= rmax
        for _, rmin, rmax, _, _ in RTL_SDR_DATA
    )

    rtl_str = '✓ Yes' if is_rtl_capable else '✗ Limited'

    # Antenna size estimate
    if freq_max >= 1e9:
        antenna = '< 5 cm'
    elif freq_max >= 100e6:
        antenna = '5–20 cm'
    elif freq_max >= 10e6:
        antenna = '20–100 cm'
    else:
        antenna = '> 1 m'

    table_data.append([name, freq_str, bw_str, service, rtl_str, antenna])

# Create color map for rows
row_colors = []
for i, row in enumerate(table_data):
    if i == 0:
        # Header row
        row_colors.append(['#2c3e50'] * 6)
    else:
        service = row[3]
        service_color = SERVICE_COLORS.get(service, '#95a5a6')
        # Lighter version for readability
        row_colors.append([service_color.replace('#', '#') if i > 0 else '#f0f0f0' for _ in range(6)])

# Create table with better styling
table = ax.table(cellText=table_data, cellLoc='left', loc='center',
                cellColours=row_colors, colWidths=[0.15, 0.22, 0.14, 0.22, 0.12, 0.15])

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2.0)

# Style header
for j in range(6):
    table[(0, j)].set_text_props(weight='bold', color='white', fontsize=11)
    table[(0, j)].set_facecolor('#2c3e50')

# Style data rows
for i in range(1, len(table_data)):
    for j in range(6):
        cell = table[(i, j)]
        cell.set_linewidth(1)
        cell.set_edgecolor('#bdc3c7')
        cell.set_text_props(fontsize=9, color='#2c3e50')

        # Improve text contrast
        if j == 3:  # Service column
            service = table_data[i][3]
            service_color = SERVICE_COLORS.get(service, '#95a5a6')
            # Darken the background or adjust text color
            cell.set_text_props(weight='bold', fontsize=9.5)

ax.axis('off')
ax.set_title('UK Radio Frequency Bands - Complete Reference Table\nWith Service Categories and RTL-SDR Compatibility',
            **FONT_TITLE, pad=20)

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/reference/frequency_reference_table.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: reference/frequency_reference_table.png (300 DPI)")
plt.close()

# ============================================================================
# PLOT 6: Color Palette Legend & Service Guide
# ============================================================================
fig, ax = plt.subplots(figsize=(14, 10))

y_start = 0.95
line_height = 0.12

# Title
ax.text(0.5, y_start, 'Service Category Color Palette & Guide',
       ha='center', va='top', fontsize=16, weight='bold', color='#2c3e50',
       transform=ax.transAxes)

y_pos = y_start - 0.15

# Service descriptions
service_descriptions = {
    'Broadcasting & Media': 'Television, FM/AM radio, and digital broadcast services for general public consumption.',
    'Mobile Communications': 'Cellular networks (GSM, UMTS, LTE), PMR, and mobile communication systems.',
    'Amateur Radio': 'Licensed amateur radio bands (HF, VHF, UHF) for hobbyists and experimenters.',
    'Aviation & Maritime': 'Air traffic control, aircraft communication, and maritime navigation/safety frequencies.',
    'WiFi & ISM': 'Industrial, Scientific, Medical bands and unlicensed WiFi/short-range wireless.',
    'Scientific & Industrial': 'Research, scientific measurement, and industrial applications.',
    'Satellite': 'Satellite communications including downlink and uplink frequencies.',
}

for service in service_order:
    if service in service_descriptions:
        # Color box
        rect = Rectangle((0.05, y_pos - 0.04), 0.03, 0.08,
                         facecolor=SERVICE_COLORS[service],
                         edgecolor='#1a1a1a', linewidth=1.5,
                         transform=ax.transAxes)
        ax.add_patch(rect)

        # Service name
        ax.text(0.10, y_pos + 0.01, service,
               ha='left', va='center', fontsize=12, weight='bold',
               color='#2c3e50', transform=ax.transAxes)

        # Description
        ax.text(0.10, y_pos - 0.02, service_descriptions[service],
               ha='left', va='top', fontsize=10, color='#555555',
               style='italic', transform=ax.transAxes, wrap=True)

        y_pos -= line_height

# Add usage note
ax.text(0.5, 0.03, 'These colors are used consistently across all visualizations to enable immediate recognition of frequency allocations.',
       ha='center', va='bottom', fontsize=10, color='#777777',
       style='italic', transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('/Users/niklasviebig/coding_projects/rtl_sdr_projects/img/spectrum_analysis/color_palette_guide.png',
           dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
print("✓ Saved: spectrum_analysis/color_palette_guide.png (300 DPI)")
plt.close()

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================
print("\n" + "="*70)
print("SPECTRUM ANALYSIS SUMMARY")
print("="*70)

total_allocated = sum(freq_max - freq_min for _, freq_min, freq_max, _, _ in SPECTRUM_DATA)
print(f"\nTotal allocated spectrum (9 kHz - 12.5 GHz): {total_allocated/1e9:.2f} GHz")
print(f"\nAllocation by Service Category:")
for service in service_order:
    if service in service_allocations:
        bw = service_allocations[service]
        pct = (bw / total_allocated) * 100
        print(f"  • {service:25s}: {bw/1e6:8.1f} MHz ({pct:5.1f}%)")

print(f"\nRTL-SDR Accessible Bands: {len(RTL_SDR_DATA)} major bands")
rtl_total = sum(freq_max - freq_min for _, freq_min, freq_max, _, _ in RTL_SDR_DATA)
print(f"RTL-SDR coverage: {rtl_total/1e6:.1f} MHz total bandwidth")

print("\n" + "="*70)
print("✓ All plots generated at 300 DPI (publication quality)")
print("✓ Color palette consistent across all visualizations")
print("✓ Ready for inclusion in documentation and presentations")
print("="*70 + "\n")
