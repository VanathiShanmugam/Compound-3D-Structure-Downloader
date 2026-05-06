# Usage:
# python src/download_sdf.py
# Downloads 3D SDF structures from PubChem using SMILES

import os
import requests
import time
import argparse

def download_3d_sdf(name, smiles, output_folder):
    try:
        # Step 1: Get CID
        cid_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/cids/JSON"
        cid_response = requests.get(cid_url)
        cid_response.raise_for_status()
        cid = cid_response.json()["IdentifierList"]["CID"][0]

        # Step 2: Get 3D SDF
        sdf_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{cid}/SDF?record_type=3d"
        sdf_response = requests.get(sdf_url)
        sdf_response.raise_for_status()

        file_path = os.path.join(output_folder, f"{name}.sdf")
        with open(file_path, "wb") as f:
            f.write(sdf_response.content)

        print(f"✅ Downloaded: {name}")

    except Exception as e:
        print(f"❌ Failed: {name} | Error: {e}")


def load_compounds(file_path):
    compounds = {}
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                name, smiles = line.strip().split(",")
                compounds[name] = smiles
    return compounds


def main():
    parser = argparse.ArgumentParser(description="Download 3D SDF structures from PubChem")
    
    parser.add_argument("--input", required=True, help="Path to input file (name,SMILES)")
    parser.add_argument("--output", default="outputs", help="Output folder")

    args = parser.parse_args()

    # Create output folder
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    compounds = load_compounds(args.input)

    print(f"\n🔬 Downloading {len(compounds)} compounds...\n")

    for name, smiles in compounds.items():
        download_3d_sdf(name, smiles, args.output)
        time.sleep(1)

    print("\n🎉 All downloads completed.")


if __name__ == "__main__":
    main()
