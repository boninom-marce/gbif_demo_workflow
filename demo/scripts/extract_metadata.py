"""
extract_metadata.py

This script reads all WAV audio files in the demo/media folder,
extracts technical metadata (duration, sampling rate, bit depth, channels),
and saves a CSV file (metadata_extracted.csv) with the results.

Note:
- GPS coordinates, species name, locality, event date/time, etc., are NOT in WAV files.
  Those should be added manually in a separate CSV file (extra_metadata.csv) to
  comply with Darwin Core and EML standards.
"""

import os
import wave
import csv

# -----------------------------
# Updated paths: relative to script
# -----------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder where the audio files are stored
MEDIA_FOLDER = os.path.join(SCRIPT_DIR, "../media")
# Output CSV file with extracted metadata
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "../metadata_extracted.csv")

def extract_metadata(file_path):
    """
    Extract basic technical metadata from a WAV file.
    
    Parameters:
        file_path (str): Path to the WAV file.
        
    Returns:
        dict: Metadata containing file name, duration (s), sampling rate (Hz), bit depth, channels.
    """
    with wave.open(file_path, "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth() * 8  # in bits
        frame_rate = wav_file.getframerate()
        n_frames = wav_file.getnframes()
        duration = n_frames / float(frame_rate)

    return {
        "file_name": os.path.basename(file_path),
        "duration_seconds": round(duration, 3),
        "sampling_rate_hz": frame_rate,
        "bit_depth": sample_width,
        "channels": channels
    }

def main():
    """
    Main function:
    - Reads all WAV files in MEDIA_FOLDER
    - Extracts metadata
    - Saves results to OUTPUT_FILE as CSV
    """
    if not os.path.exists(MEDIA_FOLDER):
        print(f"Error: Media folder not found: {MEDIA_FOLDER}")
        return

    rows = []
    for file_name in os.listdir(MEDIA_FOLDER):
        if file_name.lower().endswith(".wav"):
            file_path = os.path.join(MEDIA_FOLDER, file_name)
            metadata = extract_metadata(file_path)
            rows.append(metadata)

    # Save CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["file_name", "duration_seconds", "sampling_rate_hz", "bit_depth", "channels"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Metadata extracted and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()


