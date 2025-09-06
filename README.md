# Reproducible Workflow for Publishing Interoperable Biodiversity Datasets

**Summary**  
This repository documents a reproducible workflow for transforming raw local data into curated, interoperable datasets published and linked to GBIF.

---

## Requirements

### Hardware / Storage
- Local storage: NAS or server with RAID protection.  
  *Suggested minimum for pilot: 10–20 TB (scalable).*
- Work server (can be the same NAS/PC) with:
  - Python 3.8+  
  - R 4.x (optional)

### External Repositories
- Hugging Face (for large curated datasets, media, and environmental measurements)  
- Zenodo or Wikimedia Commons (for selected media examples)  
- Public code repository (GitHub/GitLab)

### Recommended Software
- **Python libraries:** `pandas`, `pygbif`, `soundfile`/`librosa`  
- **Metadata tools:** EML editor or CSV templates  
- **Data publishing:** GBIF IPT (local instance or national node)

---

## Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt

```
---

## Step-by-step workflow (input → process → output)

### Step 1 — Backup and version control (preservation)
- Deposit raw files (e.g., `.wav`, `.csv` from sensors) in NAS folder structure with unique naming convention (e.g., `site_date_sensor_type.ext`).  
- Register minimum metadata in a control sheet (`control.csv`) including: file ID, site, coordinates, date/time, device, person responsible, proposed license, quality notes.  
- Maintain local backups and a versioning folder (`/versions`) to ensure preservation and traceability.

---

### Step 2 — Curation and metadata enrichment (process)
- Complete metadata in the control sheet using standards:  
  - **Darwin Core** (Events/Occurrences)  
  - **Audubon Core** (associatedMedia)  
  - **Environmental metadata:** EML or CF conventions for netCDF/time series.  
- Run Python/R scripts to:  
  - Validate fields  
  - Normalize coordinates and dates  
  - Extract audio duration  
  - Calculate basic indicators (e.g., RMS level per file)  
- Output: a master normalized metadata file (`master_metadata.csv/tsv`) plus a `media_metadata.json` linking multimedia files to IDs.

---

### Step 3 — Media publication (media hosting)
- Select representative examples or curated packages for upload to **Hugging Face**, **Zenodo** (DOI) or **Wikimedia Commons** (stable URL).  
- Provide metadata (author, license, description, dataset link).  
- Record resulting URL/DOI/PID in the `master_metadata.csv`.  
- ⚠️ Upload only curated/representative subsets to public free repositories (not necessarily the entire raw dataset initially).

---

### Step 4 — Packaging for GBIF
- Generate two data tables:  
  - **Event core:** eventID, eventDate, samplingProtocol, location, environmental measurements.  
  - **Occurrence core:** species records derived from acoustic analysis (or manual IDs), linked to eventID and pointing associatedMedia to the hosted URL/DOI.  
- Create dataset metadata (EML/IPT) describing methodology, temporal/spatial coverage, responsibilities, and licenses.

---

### Step 5 — Dataset publication
- Publish curated dataset to **CONICET Digital** or an **IPT** (Integrated Publishing Toolkit) managed by INIBIOMA/national GBIF node.  
- Ensure that `associatedMedia` fields point to Hugging Face/Zenodo/Wikimedia URLs for GBIF indexing.  
- Register DOI/identifier and document release in GitHub with changelog.

---

### Step 6 — Documentation and reproducibility (output)
- This GitHub repository includes:  
  - Example scripts (`extract_metadata.py`, `generate_dwceml.py`)  
  - CSV/EML templates  
  - This `README.md` with tutorial step-by-step instructions  
  - Flowchart of the workflow  
- **Demo dataset and media** are included at the root.  
    - `media/` — example audio files  
    - `metadata_extracted.csv` — automatically extracted metadata from audio files  
    - `extra_metadata.csv` — manually added metadata (species, location, date/time)  
- Users can run main.py to reproduce the workflow end-to-end.

---

## License
Specify the license for code and data (e.g., MIT for scripts, CC-BY 4.0 for metadata, CC0/CC-BY-SA for media).


