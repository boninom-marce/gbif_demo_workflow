"""
main.py

This script runs the full demo workflow in order:
1. Extract metadata from WAV files (extract_metadata.py)
2. Generate Darwin Core and EML outputs (generate_dwceml.py)

Usage:
    python main.py
"""

import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, "scripts", script_name)
    print(f"\n>>> Running {script_name} ...")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error while running {script_name}:\n{result.stderr}")
        sys.exit(1)
    else:
        print(result.stdout)

def main():
    print("=== Demo workflow started ===")
    run_script("extract_metadata.py")
    run_script("generate_dwceml.py")
    print("\n=== Demo workflow completed successfully! ===")
    print("Generated files:")
    print("- metadata_extracted.csv")
    print("- dwc_event.csv")
    print("- dwc_occurrence.csv")
    print("- eml.xml")

if __name__ == "__main__":
    main()
