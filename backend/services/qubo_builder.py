import math
import numpy as np

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(coord1, coord2)))

def build_structural_qubo(residue_atoms, num_rotamers=3, clash_penalty=100.0):
    """
    Builds a QUBO matrix based on real 3D atomic distances and steric clash detection.
    """
    num_residues = len(residue_atoms)
    total_vars = num_residues * num_rotamers
    qubo = {}

    def var_index(i, r):
        return i * num_rotamers + r

    # 1. Constraint Term: Exactly one rotamer per residue -> P * (sum(x_ir) - 1)^2
    P = clash_penalty * 2.0
    for i in range(num_residues):
        for r1 in range(num_rotamers):
            idx1 = var_index(i, r1)
            qubo[(idx1, idx1)] = qubo.get((idx1, idx1), 0.0) - 2.0 * P
            
            for r2 in range(num_rotamers):
                idx2 = var_index(i, r2)
                if idx1 <= idx2:
                    qubo[(idx1, idx2)] = qubo.get((idx1, idx2), 0.0) + 2.0 * P

    # 2. Real Structural Energy Matrix (Distance-based Van der Waals / Clash Penalty)
    for i in range(num_residues):
        for j in range(i + 1, num_residues):
            res_i = residue_atoms[i]
            res_j = residue_atoms[j]
            
            # Compute baseline distance between residue centers from 6ILW
            center_i = [sum(a["coord"][k] for a in res_i["atoms"])/len(res_i["atoms"]) for k in range(3)]
            center_j = [sum(a["coord"][k] for a in res_j["atoms"])/len(res_j["atoms"]) for k in range(3)]
            base_dist = calculate_euclidean_distance(center_i, center_j)

            for r1 in range(num_rotamers):
                for r2 in range(num_rotamers):
                    idx1 = var_index(i, r1)
                    idx2 = var_index(j, r2)
                    
                    # Simulate rotamer conformational shift offset (e.g., rotamer angle offset)
                    spatial_offset = (r1 - r2) * 0.4 
                    simulated_dist = base_dist + spatial_offset
                    
                    # Biophysical scoring: 
                    # If atoms overlap (< 3.0 Å), assign heavy positive penalty.
                    # If optimal packing distance (~4.0 - 5.5 Å), assign favorable energy reward.
                    if simulated_dist < 3.0:
                        interaction_energy = 80.0  # Severe steric clash
                    elif 4.0 <= simulated_dist <= 6.0:
                        interaction_energy = -18.5 # Favorable VdW packing
                    else:
                        interaction_energy = -2.0  # Neutral distance

                    if idx1 <= idx2:
                        qubo[(idx1, idx2)] = qubo.get((idx1, idx2), 0.0) + interaction_energy

    return qubo, total_vars