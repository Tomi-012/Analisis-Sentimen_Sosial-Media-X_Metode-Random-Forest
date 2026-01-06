"""
Script untuk install Playwright (Browser Automation untuk crawling X.com)
Jalankan script ini SATU KALI untuk setup.
"""

import subprocess
import sys

print("="*60)
print("SETUP PLAYWRIGHT UNTUK CRAWLING X.COM")
print("="*60)

# Step 1: Install playwright library
print("\n[1/2] Installing playwright library...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
    print("✓ Playwright library installed")
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# Step 2: Install browser (chromium)
print("\n[2/2] Installing Chromium browser...")
try:
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    print("✓ Chromium browser installed")
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("✓ SETUP SELESAI!")
print("Sekarang Anda bisa menjalankan: python RANDOM_FOREST.py")
print("="*60)
