# Compound 3D Structure Downloader

### A Computational Tool for Automated Retrieval of 3D Molecular Structures

---

## Highlights

* Batch download of **3D SDF structures** using SMILES
* Integration with PubChem REST API
* Automated CID retrieval from SMILES
* Command-line interface (CLI) for flexible usage
* Reproducible and scalable workflow

---

## Abstract

Retrieving 3D molecular structures is a critical step in computational drug discovery, molecular docking, and structural bioinformatics workflows.

This project presents a **Python-based automation tool** that retrieves **3D SDF structures** of chemical compounds directly from the PubChem database using SMILES notation.

The tool converts SMILES into PubChem Compound IDs (CIDs) and downloads corresponding 3D structures in SDF format, enabling efficient preparation of ligands for downstream computational analysis.

---

## Objectives

* Automate retrieval of 3D molecular structures
* Convert SMILES to PubChem CID
* Enable batch processing of multiple compounds
* Provide a reusable CLI-based tool
* Support reproducible computational workflows

---

## Methodology

### 1. Input Processing

* Accepts compound data in the format:

  ```
  Compound_Name,SMILES
  ```
* Reads input from a user-provided file

---

### 2. CID Retrieval

* Uses PubChem REST API to:

  * Convert SMILES → CID
* Ensures accurate compound identification

---

### 3. Structure Download

* Fetches **3D SDF structures** using CID
* Saves structures locally

---

### 4. Output Generation

* Each compound saved as:

  ```
  outputs/Compound_Name.sdf
  ```
* Ensures organized storage of structures

---

### 5. Rate Limiting

* Includes delay between requests
* Prevents server overload and ensures stable execution

---

## 📁 Project Structure

```bash id="bzwb0r"
compound-3d-structure-downloader/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── download_sdf.py
│
├── examples/
│   └── compounds.txt
│
└── outputs/   (auto-generated)
```

---

## Reproducibility

### Installation

```bash id="w1ntno"
git clone https://github.com/your-username/compound-3d-structure-downloader.git
cd compound-3d-structure-downloader
pip install -r requirements.txt
```

---

### Input Format

Create a file like:

```txt id="i3h1p3"
Thymol,CC1=CC(=C(C=C1)C(C)C)O
Resveratrol,C1=CC(=CC=C1C=CC2=CC(=CC(=C2)O)O)O
Curcumin,COC1=C(C=CC(=C1)C=CC(=O)CC(=O)C=CC2=CC(=C(C=C2)O)OC)O
```

---

### Run the Tool

```bash id="b8cvw5"
python src/download_sdf.py --input examples/compounds.txt --output outputs
```

---

## Output

* 3D molecular structures in **SDF format**
* Stored in:

  ```
  outputs/
  ```

---

## Applications

* Molecular docking studies
* Drug discovery pipelines
* Ligand preparation
* Structural bioinformatics
* Virtual screening workflows

---

## Limitations

* Depends on availability of compounds in PubChem
* Requires valid SMILES input
* Network-dependent (API calls)

---

## Future Work

* Support CSV/Excel input formats
* Parallel downloading for faster execution
* Integration with docking pipelines
* Web interface or API deployment

---

## Author

**Vanathi Shanmugam**
Bioinformatics | Genomics | Machine Learning

🔗 LinkedIn: https://www.linkedin.com/in/vanathi-shanmugam-26127928a

---

## License

This project is intended for academic and research purposes.
