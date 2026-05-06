# Usage:
# python src/download_sdf.py
# Downloads 3D SDF structures from PubChem using SMILES

import os
import requests
import time

# ==============================
# OUTPUT FOLDER
# ==============================
output_folder = r"C:\Users\vanat\OneDrive\Documents\N.fowleri\3d structs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ==============================
# COMPOUND LIST (Name : SMILES)
# ==============================

compounds = {
    "Thymol": "CC1=CC(=C(C=C1)C(C)C)O",
    "Kaempferol": "C1=CC(=CC=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O",
    "Resveratrol": "C1=CC(=CC=C1C=CC2=CC(=CC(=C2)O)O)O",
    "Silybin": "COC1=C(C=CC(=C1)C2C(OC3=C(O2)C=C(C=C3)C4C(C(=O)C5=C(C=C(C=C5O4)O)O)O)CO)O",
    "Luteolin": "C1=CC(=C(C=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O)O",
    "Heliocide_H2": "CC(C)C1=C2C(=C(C(=C1O)O)C=O)C(=O)C3CC(=CCC3(C2=O)C)CCC=C(C)C",
    "Curcumin": "COC1=C(C=CC(=C1)C=CC(=O)CC(=O)C=CC2=CC(=C(C=C2)O)OC)O",
    "Phytosphingosine_2": "CCCCCCCCCCCCCCC(C(C(CO)N)O)O",
    "Forskolin": "CC(=O)OC1C(C2C(CCC(C2(C3(C1(OC(CC3=O)(C)C=C)C)O)C)O)(C)C)O",
    "Demethoxycurcumin": "COC1=C(C=CC(=C1)C=CC(=O)CC(=O)C=CC2=CC=C(C=C2)O)O",
    "Borneol": "CC1(C2CCC1(C(C2)O)C)C",
    "Andrographolide": "CC12CCC(C(C1CCC(=C)C2CC=C3C(COC3=O)O)(C)CO)O",
    "Apigenin": "C1=CC(=CC=C1C2=CC(=O)C3=C(C=C(C=C3O2)O)O)O",
    "Naringenin": "C1C(OC2=CC(=CC(=C2C1=O)O)O)C3=CC=C(C=C3)O",
    "Carvacrol": "CC1=C(C=C(C=C1)C(C)C)O",
    "Alpha_Terpineol": "CC1=CCC(CC1)C(C)(C)O",
    "Limonene": "CC1=CCC(CC1)C(=C)C",
    "Rosmarinic_acid": "C1=CC(=C(C=C1CC(C(=O)O)OC(=O)C=CC2=CC(=C(C=C2)O)O)O)O",
    "Vanillic_acid": "COC1=C(C=CC(=C1)C(=O)O)O",
    "Caffeic_acid": "C1=CC(=C(C=C1C=CC(=O)O)O)O",
    "Ferulic_acid": "COC1=C(C=CC(=C1)C=CC(=O)O)O",
    "Bisdemethoxycurcumin": "C1=CC(=CC=C1C=CC(=O)CC(=O)C=CC2=CC=C(C=C2)O)O",
    "Allicin": "C=CCSS(=O)CC=C",
    "Eugenol": "COC1=C(C=CC(=C1)CC=C)O",
    "Citral": "CC(=CCCC(=CC=O)C)C",
    "Linalool": "CC(=CCCC(C)(C=C)O)C",
    "Cinnamic_acid": "C1=CC=C(C=C1)C=CC(=O)O",
    "Alpha_bisabolol": "CC1=CCC(CC1)C(C)(CCC=C(C)C)O",
    "Chlorophorin": "CC(=CCCC(=CCC1=C(C=C(C=C1O)C=CC2=C(C=C(C=C2)O)O)O)C)C",
    "Formononetin": "COC1=CC=C(C=C1)C2=COC3=C(C2=O)C=CC(=C3)O",
    "Maackiain": "C1C2C(C3=C(O1)C=C(C=C3)O)OC4=CC5=C(C=C24)OCO5"
}

# ==============================
# FUNCTION TO DOWNLOAD 3D SDF
# ==============================

def download_3d_sdf(name, smiles):
    try:
        # Step 1: Get CID from SMILES
        cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/cids/JSON"
        cid_response = requests.get(cid_url)
        cid_response.raise_for_status()

        cid = cid_response.json()["IdentifierList"]["CID"][0]

        # Step 2: Download 3D SDF
        sdf_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/SDF?record_type=3d"
        sdf_response = requests.get(sdf_url)
        sdf_response.raise_for_status()

        # Save file
        file_path = os.path.join(output_folder, f"{name}.sdf")
        with open(file_path, "wb") as f:
            f.write(sdf_response.content)

        print(f"✅ Downloaded: {name}")

    except Exception as e:
        print(f"❌ Failed: {name} | Error: {e}")


# ==============================
# RUN DOWNLOAD
# ==============================

for compound_name, smiles in compounds.items():
    download_3d_sdf(compound_name, smiles)
    time.sleep(1)  # Avoid server overload

print("\n✔️ All downloads completed.")
