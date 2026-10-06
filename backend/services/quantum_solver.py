import dimod

def solve_qubo(qubo_dict):
    """
    Solves the QUBO using D-Wave's Simulated Annealer sampler.
    Returns the optimal binary configuration and energy score.
    """
    sampler = dimod.SimulatedAnnealer()
    response = sampler.sample_qubo(qubo_dict, num_reads=100)
    
    # Get the best sample (lowest energy)
    best_sample = response.first.sample
    best_energy = response.first.energy
    
    return {
        "solution": best_sample,
        "energy": float(best_energy),
        "samples_evaluated": len(response.record)
    }