from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.pdb_parser import parse_active_site_atoms
from services.qubo_builder import build_structural_qubo
from services.quantum_solver import solve_qubo

app = FastAPI(title="Quantum Bio-Forge API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Quantum Bio-Forge Backend Online", "target_pdb": "6ILW", "engine": "Structural-Distance QUBO"}

@app.get("/api/optimize")
def run_quantum_optimization():
    try:
        # 1. Parse real atom coordinates from 6ILW PDB file
        residue_atoms = parse_active_site_atoms([87, 156, 189, 243])
        
        # 2. Build QUBO based on actual Euclidean distances and clash penalties
        qubo_dict, total_vars = build_structural_qubo(residue_atoms, num_rotamers=3)
        
        # 3. Solve via simulated quantum annealing
        result = solve_qubo(qubo_dict)
        
        return {
            "residues": [{"res_name": r["res_name"], "res_id": r["res_id"], "atom_count": len(r["atoms"])} for r in residue_atoms],
            "qubo_variables": total_vars,
            "optimization_result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))