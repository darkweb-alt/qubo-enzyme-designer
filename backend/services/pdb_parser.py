import os
import requests
from Bio.PDB import PDBParser

PDB_URL = "https://files.rcsb.org/download/6ILW.pdb"
LOCAL_PDB_PATH = os.path.join(os.path.dirname(__file__), "../data/6ILW.pdb")

def ensure_pdb_exists():
    """Downloads 6ILW.pdb if it doesn't exist or is empty."""
    os.makedirs(os.path.dirname(LOCAL_PDB_PATH), exist_ok=True)
    if not os.path.exists(LOCAL_PDB_PATH) or os.path.getsize(LOCAL_PDB_PATH) == 0:
        print("Downloading 6ILW.pdb from RCSB...")
        response = requests.get(PDB_URL)
        if response.status_code == 200:
            with open(LOCAL_PDB_PATH, "w") as f:
                f.write(response.text)
        else:
            raise Exception("Failed to download 6ILW PDB file.")

def parse_active_site(residue_ids=[87, 156, 189, 243]):
    """
    Parses 6ILW and extracts coordinates for active site residues 
    (e.g., catalytic triad/pocket residues in PETase).
    """
    ensure_pdb_exists()
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("6ILW", LOCAL_PDB_PATH)
    
    extracted_data = []
    for model in structure:
        for chain in model:
            for residue in chain:
                res_id = residue.get_id()[1]
                if res_id in residue_ids:
                    coords = [atom.get_coord().tolist() for atom in residue]
                    extracted_data.append({
                        "res_name": residue.get_resname(),
                        "res_id": res_id,
                        "atom_count": len(coords),
                        "center_coord": [
                            sum(c[0] for c in coords)/len(coords),
                            sum(c[1] for c in coords)/len(coords),
                            sum(c[2] for c in coords)/len(coords)
                        ]
                    })
    return extracted_data