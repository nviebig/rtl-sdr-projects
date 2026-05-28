#!/bin/bash

# RTL-SDR Aircraft Radar (ADS-B) Setup & Launch Script
# Decodes aircraft ADS-B signals and displays live radar map
# Open browser to http://localhost:8080 to view live aircraft

echo "RTL-SDR Aircraft Radar Setup"
echo "=================================="

# Check if dump1090-fa is installed
if ! command -v dump1090-fa &> /dev/null; then
    echo "dump1090-fa not found. Installing..."
    brew install dump1090-mutability || brew install dump1090-fa
fi

if ! command -v dump1090-fa &> /dev/null; then
    echo "dump1090-fa installation may have failed."
    echo "   Try: brew search dump1090"
    exit 1
fi

echo "dump1090-fa found"
echo ""
echo "Starting ADS-B aircraft tracking..."
echo "Frequency: 1090 MHz"
echo "Mode: ADS-B (1090 MHz ES)"
echo ""
echo "Open your browser: http://localhost:8080"
echo "   You should see a map with live aircraft positions"
echo ""
echo "Tuning Tips:"
echo "   - Antenna: Fully extended telescopic rods (~50cm each)"
echo "   - Gain: 45-50 (adjust if too much noise)"
echo "   - Location: Higher elevation = more range"
echo "   - Expected range: 100-300 km depending on altitude"
echo ""
echo "Press Ctrl+C to stop"
echo "=================================="
echo ""

# Launch dump1090-fa with network output
# --net: Enable network output (web interface)
# --net-bind-address 127.0.0.1: Bind to localhost only (security)
# --interactive: Show aircraft in terminal while running
dump1090-fa --net --net-bind-address 127.0.0.1 --interactive

# Fallback to mutability version if fa not available
# dump1090-mutability --net --net-bind-address 127.0.0.1 --interactive
