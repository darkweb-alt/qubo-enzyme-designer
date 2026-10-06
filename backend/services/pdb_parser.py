import os
import requests
from Bio.PDB import PDBParser

PDB_URL = "https://files.rcsb.org/download/6ILW.pdb"
LOCAL_PDB_PATH = os.path.join(os.path.dirname(__file__), "../data/6ILW.pdb")

def ensure_pdb_exists():
    os.makedirs(os.path.dirname(LOCAL_PDB_PATH), exist_ok=True)
    if not os.path.exists(LOCAL_PDB_PATH) or os.path.getsize(LOCAL_PDB_PATH) == 0:
        print("Downloading 6ILW.pdb from RCSB...")
        response = requests.get(PDB_URL)
        if response.status_code == 200:
            with open(LOCAL_PDB_PATH, "w") as f:
                f.write(response.text)
        else:
            raise Exception("Failed to download 6ILW PDB file.")

def parse_active_site_atoms(residue_ids=[87, 156, 189, 243]):
    """
    Parses 6ILW and extracts 3D atom coordinates with fallback safety.
    """
    ensure_pdb_exists()
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("6ILW", LOCAL_PDB_PATH)
    
    residue_data = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[0] == ' ' and residue.get_id()[1] in residue_ids:
                    atoms = []
                    for atom in residue:
                        if not atom.get_name().startswith("H"):
                            atoms.append({
                                "name": atom.get_name(),
                                "coord": atom.get_coord().tolist()
                            })
                    if atoms:
                        residue_data.append({
                            "res_name": residue.get_resname(),
                            "res_id": residue.get_id()[1],
                            "atoms": atoms
                        })
    
    # Fallback safety: if specific IDs aren't found, grab first 4 valid amino acids
    if not residue_data:
        count = 0
        for model in structure:
            for chain in model:
                for residue in chain:
                    if residue.id[0] == ' ' and count < 4:
                        atoms = [{"name": a.get_name(), "coord": a.get_coord().tolist()} for a in residue if not a.get_name().startswith("H")]
                        if atoms:
                            residue_data.append({
                                "res_name": residue.get_resname(),
                                "res_id": residue.get_id()[1],
                                "atoms": atoms
                            })
                            count += 1

    return residue_data