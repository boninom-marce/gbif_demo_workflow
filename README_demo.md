# Demo workflow

This demo illustrates, on a reduced scale, the process of transforming raw acoustic data into curated, interoperable datasets suitable for publication and integration with GBIF.

## Contents

- `media/` — 10 example audio files (.wav, 1 s each, ~2.5 MB) used for demonstration (can be replaced by other environmental data)
- `scripts/` — scripts to extract basic metadata and generate DwC/EML-ready tables (`extract_metadata.py`, `generate_dwceml.py`)
- `metadata_extracted.csv` — automatically extracted metadata from audio files
- `extra_metadata.csv` — manually added metadata (species, location, date/time)
- Output files after running the scripts: `dwc_event.csv`, `dwc_occurrence.csv`, `eml.xml`

## How to run the demo

1. **Check dependencies**
   - Python 3.8+
   - Required libraries (installed via `requirements.txt`):  
     `pandas`, `wave`, `datetime`

2. **Inspect the input**
   - Raw audio files are located in `media/`
   - Technical metadata is generated automatically by `extract_metadata.py`
   - Manual/contextual metadata is provided in `extra_metadata.csv`

3. **Run the scripts**
   1. Execute `extract_metadata.py` (inside `scripts/`) to generate `metadata_extracted.csv` containing duration, sampling rate, bit depth, and number of channels for each audio file.
   2. Execute `generate_dwceml.py` (inside `scripts/`) to merge `metadata_extracted.csv` with `extra_metadata.csv` and produce:
      - `dwc_event.csv` — simplified Darwin Core Event table
      - `dwc_occurrence.csv` — simplified Darwin Core Occurrence table
      - `eml.xml` — minimal EML metadata file

4. **Inspect the outputs**
   - All output files are written to the repository root (`/`).
   - These files illustrate the structure expected for integration with IPT/GBIF.

## Notes

- This demo uses audio files for clarity, but the workflow is designed to handle other types of environmental data such as sensor CSVs, camera trap images, or video.
- Real deployments would use larger volumes of data and more detailed metadata.
- The scripts are intended as **illustrative examples**, not production-ready tools.
- URLs for associated media are placeholders (`https://demo.org/media/{file_name}`) and can be replaced with Zenodo/Wikimedia Commons links in real datasets.
