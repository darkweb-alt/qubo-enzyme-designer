import numpy as np

def build_enzyme_qubo(num_residues=4, num_rotamers=3, clash_penalty=100.0):
    """
    Builds a QUBO dictionary for side-chain rotamer packing.
    Variables: x_{i,r} -> Residue i takes rotamer r.
    Total binary variables = num_residues * num_rotamers.
    """
    qubo = {}
    
    # Map variable index for residue i, rotamer r
    def var_index(i, r):
        return i * num_rotamers + r

    total_vars = num_residues * num_rotamers

    # 1. Constraint Term: Exactly one rotamer per residue -> P * (sum(x_ir) - 1)^2
    P = clash_penalty * 2.0
    for i in range(num_residues):
        for r1 in range(num_rotamers):
            idx1 = var_index(i, r1)
            # Linear term: -2 * P
            qubo[(idx1, idx1)] = qubo.get((idx1, idx1), 0.0) - 2.0 * P
            
            for r2 in range(num_rotamers):
                idx2 = var_index(i, r2)
                # Quadratic term: +2 * P (for r1 != r2 or r1 == r2 adds up correctly)
                if idx1 <= idx2:
                    qubo[(idx1, idx2)] = qubo.get((idx1, idx2), 0.0) + 2.0 * P

    # 2. Interaction & Clash Energy Matrix (Simulated pairwise potentials)
    np.random.seed(42) # Reproducible hackathon demo data
    for i in range(num_residues):
        for j in range(i + 1, num_residues):
            for r1 in range(num_rotamers):
                for r2 in range(num_rotamers):
                    idx1 = var_index(i, r1)
                    idx2 = var_index(j, r2)
                    
                    # Simulated energy reward or steric clash penalty
                    # Favorable interactions get negative values, clashes get positive
                    interaction_energy = np.random.uniform(-15.0, 25.0)
                    if r1 == r2:
                        interaction_energy += 10.0 # slight penalty for identical rigid angles
                        
                    if idx1 <= idx2:
                        qubo[(idx1, idx2)] = qubo.get((idx1, idx2), 0.0) + interaction_energy

    return qubo, total_vars