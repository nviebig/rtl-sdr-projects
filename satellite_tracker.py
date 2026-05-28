#!/usr/bin/env python3
"""
RTL-SDR Satellite Pass Predictor & Scheduler
Fetches predicted passes for NOAA weather satellites and ISS
Alerts when passes are happening (useful for recording/decoding)
"""

import requests
import json
from datetime import datetime, timedelta
import subprocess
import sys

# Your location (update these with your coordinates)
LATITUDE = 51.5074   # London, UK (example)
LONGITUDE = -0.1278
ELEVATION = 20       # meters above sea level

# Common satellites to track
SATELLITES = {
    "ISS (ZARYA)": {
        "norad_id": 25544,
        "frequency": 145.800,
        "mode": "NFM",
        "type": "manned"
    },
    "NOAA-15": {
        "norad_id": 25338,
        "frequency": 137.620,
        "mode": "WFM",
        "type": "weather"
    },
    "NOAA-18": {
        "norad_id": 28654,
        "frequency": 137.912,
        "mode": "WFM",
        "type": "weather"
    },
    "NOAA-19": {
        "norad_id": 33591,
        "frequency": 137.100,
        "mode": "WFM",
        "type": "weather"
    },
    "METEOR M2-4": {
        "norad_id": 57167,
        "frequency": 137.100,
        "mode": "WFM",
        "type": "weather"
    }
}

def get_satellite_passes(norad_id, days_ahead=5):
    """Fetch predicted passes from N2YO API (requires free API key)"""
    try:
        # Note: N2YO free tier limited to 10 API calls/hour
        # Sign up at: https://www.n2yo.com/api/
        api_key = "YOUR_N2YO_API_KEY"  # Get free key from n2yo.com

        url = f"https://api.n2yo.com/rest/v1/satellite/passes/{norad_id}/{LATITUDE}/{LONGITUDE}/{ELEVATION}/{days_ahead}/&apiKey={api_key}"

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️  API Error {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error fetching passes: {e}")
        return None

def print_passes(satellite_name, sat_info):
    """Pretty print upcoming passes"""
    print(f"\n🛰️  {satellite_name}")
    print(f"   Frequency: {sat_info['frequency']} MHz | Mode: {sat_info['mode']}")
    print(f"   NORAD ID: {sat_info['norad_id']}")

    passes = get_satellite_passes(sat_info['norad_id'])

    if not passes or 'passes' not in passes:
        print("   ⚠️  No passes predicted or API unavailable")
        return

    if not passes['passes']:
        print("   No visible passes in the next 5 days")
        return

    for i, pass_data in enumerate(passes['passes'][:3], 1):  # Show next 3 passes
        rise_time = datetime.fromtimestamp(pass_data['risetime'])
        culmination_time = datetime.fromtimestamp(pass_data['maxtime'])
        set_time = datetime.fromtimestamp(pass_data['settime'])
        elevation = pass_data['maxelev']

        time_until = (rise_time - datetime.now()).total_seconds() / 3600

        print(f"\n   Pass #{i}:")
        print(f"     Rise: {rise_time.strftime('%Y-%m-%d %H:%M:%S')} (in {time_until:.1f}h)")
        print(f"     Max:  {culmination_time.strftime('%H:%M:%S')} @ {elevation}° elevation")
        print(f"     Set:  {set_time.strftime('%H:%M:%S')}")

        # Alert if pass is within next hour
        if 0 < time_until < 1:
            print(f"     🚀 PASS STARTING IN {int(time_until*60)} MINUTES!")

def main():
    print("=" * 60)
    print("  RTL-SDR Satellite Pass Predictor")
    print("=" * 60)
    print(f"  Location: {LATITUDE}°, {LONGITUDE}° @ {ELEVATION}m elevation")
    print(f"  Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    for sat_name, sat_info in SATELLITES.items():
        print_passes(sat_name, sat_info)

    print("\n" + "=" * 60)
    print("  Setup Instructions:")
    print("=" * 60)
    print("  1. Sign up for free N2YO API key: https://www.n2yo.com/api/")
    print("  2. Replace 'YOUR_N2YO_API_KEY' in this script")
    print("  3. Update LATITUDE/LONGITUDE to your location")
    print("  4. Run this script periodically to plan recording sessions")
    print("\n  Recording Checklist:")
    print("  ☐ Open SDR++ 5 minutes before pass")
    print("  ☐ Tune to satellite frequency")
    print("  ☐ Set gain to 45-50")
    print("  ☐ Enable WAV recording")
    print("  ☐ Hit 'Record' when satellite rises above horizon")
    print("  ☐ Stop recording when satellite sets")
    print("  ☐ Open SatDump to decode recorded IQ data")
    print("=" * 60)

if __name__ == "__main__":
    main()
