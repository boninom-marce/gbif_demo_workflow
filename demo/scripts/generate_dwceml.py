"""
generate_dwceml.py

This script generates Darwin Core (Event Core + Occurrence Core) CSV files
and a minimal EML file from demo acoustic data.

It combines:
1. metadata_extracted.csv -> automatically extracted technical metadata
2. extra_metadata.csv     -> manually added metadata (species, location, date/time)

Usage:
    python scripts/generate_dwceml.py
"""

import pandas as pd
from datetime import datetime
import os

# Paths
metadata_csv = "metadata_extracted.csv"
extra_metadata_csv = "extra_metadata.csv"

dwc_event_csv = "dwc_event.csv"
dwc_occurrence_csv = "dwc_occurrence.csv"
eml_file = "eml.xml"

# Load CSVs
tech_df = pd.read_csv(metadata_csv)
extra_df = pd.read_csv(extra_metadata_csv)

# Merge technical and extra metadata by file_name
df = pd.merge(tech_df, extra_df, on="file_name", how="left")

# Generate eventID for each recording
df['eventID'] = df['file_name'].apply(lambda x: f"event_{x.split('.')[0]}")

# -----------------------------
# Create Event Core
# -----------------------------
# Minimal columns for Event Core: eventID, eventDate, eventTime, decimalLatitude, decimalLongitude, locality
event_df = df[['eventID', 'eventDate', 'eventTime', 'decimalLatitude', 'decimalLongitude', 'locality']].drop_duplicates()
event_df.to_csv(dwc_event_csv, index=False)

# -----------------------------
# Create Occurrence Core
# -----------------------------
occurrence_records = []
for _, row in df.iterrows():
    occurrence_records.append({
        "occurrenceID": f"occ_{row['eventID']}_{row['file_name'].split('.')[0]}",
        "eventID": row["eventID"],
        "scientificName": row.get("scientificName", "Unknown species (demo)"),
        "basisOfRecord": "MachineObservation",
        # For demo, generate a placeholder URL for associatedMedia
        "associatedMedia": f"https://demo.org/media/{row['file_name']}",
        "duration_sec": row.get("duration_seconds", "")
    })

occurrence_df = pd.DataFrame(occurrence_records)
occurrence_df.to_csv(dwc_occurrence_csv, index=False)

# -----------------------------
# Create minimal EML
# -----------------------------
eml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<eml:eml packageId="demo.1.1"
    system="GBIF"
    xmlns:eml="eml://ecoinformatics.org/eml-2.1.1"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="eml://ecoinformatics.org/eml-2.1.1 eml.xsd">

  <dataset>
    <title>Demo dataset: Acoustic recordings and metadata</title>
    <creator>
      <individualName>
        <surName>Demo</surName>
      </individualName>
      <organizationName>INIBIOMA</organizationName>
    </creator>
    <pubDate>{datetime.today().date()}</pubDate>
    <abstract>
      <para>This is a demonstration dataset generated for the GBIF Ebbe Nielsen Challenge.
      It contains example acoustic recordings with basic metadata transformed into Darwin Core
      and EML formats. All data are fictional for demonstration purposes only.</para>
    </abstract>
    <intellectualRights>
      <para>This dataset is for demonstration only and not intended for actual publication.</para>
    </intellectualRights>
  </dataset>
</eml:eml>
"""

with open(eml_file, "w", encoding="utf-8") as f:
    f.write(eml_content)

print(f"Darwin Core and EML files generated:\n- {dwc_event_csv}\n- {dwc_occurrence_csv}\n- {eml_file}")
