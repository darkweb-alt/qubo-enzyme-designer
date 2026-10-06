<div align="center">

# ⚛️ QUANTUM BIO-FORGE v1.0
### Quantum-Directed Enzyme Active-Site Optimization Engine

[![Hackathon](https://img.shields.io/badge/Event-Q--Hack%20India%202026%20by%20Infinitude-purple?style=flat-square)](https://github.com)
[![Track](https://img.shields.io/badge/Track-Quantum%20Biotech%20%26%20Chemistry-emerald?style=flat-square)](https://github.com)
[![Team](https://img.shields.io/badge/Team-Monday-blue?style=flat-square)](https://github.com)
[![Status](https://img.shields.io/badge/Status-Prototype%20Ready-success?style=flat-square)](https://github.com)

*Solving combinatorial protein design bottlenecks using QUBO formulation, annealing-based optimization, and structural biophysics.*

</div>

---

## 👥 Team Monday

| Member | Role |
|---|---|
| **Pitambar Yadav** | Lead Developer & Quantum Architecture |
| **Bhavna S** | Biophysical Modeling & Research |
| **Kowshick Balaji M** | System Integration & UI/UX Design |

---

## 📑 Table of Contents
1. [Problem](#-1-problem-q-hack-india-2026)
2. [Why It Matters](#-2-why-it-matters)
3. [Proposed Solution](#-3-proposed-solution)
4. [Why Quantum?](#%EF%B8%8F-4-why-quantum)
5. [Implementation & Architecture](#%EF%B8%8F-5-implementation-and-architecture)
6. [Minimal Prototype](#-6-minimal-prototype)
7. [Results / Validation](#-7-results--validation)
8. [Getting Started](#-8-getting-started)
9. [Roadmap](#%EF%B8%8F-9-roadmap-round-2--beyond)
10. [References](#-10-references-and-sources)

---

## 🎯 1. Problem (Q-Hack India 2026)

### What problem are you solving?
Enzymes are nature's high-efficiency biological catalysts, but engineering them for industrial or environmental applications (such as plastic degradation) is bottlenecked by **combinatorial side-chain packing**.

* The active site, the localized pocket where substrate binding and catalysis occur, can be configured in many different amino-acid rotamer combinations (**3^N** for N residues with 3 rotamers each). The count explodes as more residues are included.
* Classical optimization approaches (Monte Carlo, greedy local search) can get **trapped in high-energy local minima**, resulting in steric clashes, unstable conformations, and poor substrate binding.

---

## 💡 2. Why It Matters

### Who faces this problem and why is it important?
* **The global environmental crisis:** Billions of tons of plastic waste (notably polyethylene terephthalate, PET) accumulate worldwide. Enzymes like **PETase** can degrade PET, but wild-type variants have low catalytic efficiency and high conformational energy barriers.
* **The R&D bottleneck:** Wet-lab directed evolution is expensive, slow, and trial-and-error driven. Computational protein design can accelerate enzyme engineering, but only if algorithms can efficiently navigate rugged, non-linear energy landscapes. Solving this opens doors to programmable plastic-degrading and carbon-capturing biological agents.

---

## 🚀 3. Proposed Solution

### What are you building?
**Quantum Bio-Forge** is a full-stack computational suite that converts enzyme active-site design into a **QUBO (Quadratic Unconstrained Binary Optimization)** problem.

* **Structural parsing:** Ingests experimental protein crystal structures from the Protein Data Bank (PDB: [6ILW](https://www.rcsb.org/structure/6ILW)).
* **Distance-matrix biophysics:** Computes inter-atomic Euclidean distances between catalytic residues to quantify steric clashes.
* **Annealing-based optimization:** Encodes the packing problem as a binary quadratic model and solves it with the D-Wave Ocean annealing toolchain to locate the minimum-energy conformation.

---

## ⚛️ 4. Why Quantum?

### Why does quantum computing or quantum technology make sense here?
* **Combinatorial scaling:** Protein conformational search spaces grow exponentially. Greedy and local-search methods scale poorly and can stagnate in local minima.
* **Native QUBO fit:** Quantum annealers (such as D-Wave's) are purpose-built to sample low-energy states of Ising/QUBO problems, which is exactly how side-chain packing is formulated. Quantum tunneling lets physical annealers cross narrow energy barriers that trap classical descent.
* **Prototype note:** The current prototype uses D-Wave's **simulated annealing** sampler running locally. It is a classical, quantum-inspired solver that validates the QUBO formulation and pipeline. Running the same model unchanged on a physical QPU is the first roadmap item.

---

## ⚙️ 5. Implementation and Architecture

### How is the solution implemented?
Quantum Bio-Forge is a client-server hybrid:

```text
[ RCSB PDB: 6ILW ]
        ↓  (Biopython coordinates)
[ FastAPI Backend (Python) ]
        ↓  (Euclidean distance & clash matrix)
[ QUBO Formulation: 12 binary variables + one-hot constraints ]
        ↓  (D-Wave dimod simulated annealing sampler)
[ Next.js + Tailwind CSS Command Center (interactive frontend) ]
```

**Quantum / annealing components:** D-Wave Ocean SDK (`dimod`) for binary quadratic model construction, sampling, and energy-state convergence.

**Classical components:** FastAPI server, Biopython (`Bio.PDB`) spatial-geometry parser, and a Next.js / Tailwind CSS research dashboard with a real-time conformational scrubber and annealing-descent curves.

**QUBO formulation (summary):**
* 4 catalytic residues × 3 rotamer states = **12 binary variables** `x_{i,r}`.
* Linear terms: self-energy of each rotamer.
* Quadratic terms: pairwise steric-clash penalty derived from the inter-atomic distance matrix.
* Constraint: exactly one rotamer per residue, enforced with a penalty term `P · (Σ_r x_{i,r} − 1)²`.

---

## 🧪 6. Minimal Prototype

### What have you actually built?
A functional, end-to-end full-stack web application running locally:

1. **Interactive research dashboard:** a clean, research-grade light-theme interface showing pipeline steps, residue targets, and live solver telemetry.
2. **Live conformational scrubber:** a slider to move through structural transition states in real time, with live energy changes and clash elimination.
3. **Annealing convergence viewport:** a graphical comparison of classical greedy trapping versus annealing descent paths.

---

## 📊 7. Results / Validation

### What are the results?
* **Energy minimization:** Eliminated steric clashes across the target catalytic pocket (**TRP 87, SER 156, HIS 189, ASP 243**).
* **Benchmark (prototype run):**

| Method | Final Energy | Outcome |
|---|---|---|
| Classical greedy search | +42.0 kcal/mol | Trapped in local minimum |
| Annealing-based QUBO solver | −142.5 kcal/mol | Reached global minimum |

* **Latency:** Average solve time of **~42 ms** for the 12-variable QUBO.

> Energies are in the prototype's scoring model (distance-based clash penalties), not a full force field. Advanced scoring is on the roadmap.

---

## 🛠️ 8. Getting Started

### Prerequisites
* Python 3.10+
* Node.js 18+ and npm

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/quantum-bio-forge.git
cd quantum-bio-forge
```

### 2. Run the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install fastapi uvicorn biopython dimod dwave-neal numpy
uvicorn main:app --reload --port 8000
```
API docs will be available at `http://localhost:8000/docs`.

### 3. Run the frontend
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:3000` in your browser.

### Project structure
```text
quantum-bio-forge/
├── backend/        # FastAPI server, PDB parsing, QUBO + solver
├── frontend/       # Next.js + Tailwind dashboard
└── README.md
```

---

## 🗺️ 9. Roadmap (Round 2 & Beyond)

1. **Physical QPU integration:** move from local simulated annealing to hybrid jobs on D-Wave quantum annealing hardware via the Leap cloud API.
2. **Full protein scaling:** expand from 4 active-site residues to multi-residue regions using parallel sub-space decomposition.
3. **Advanced biophysical scoring:** add electrostatics, solvation energy, and hydrogen-bond networks via higher-order optimization (HOBO) models.

---

## 📚 10. References and Sources

* **Protein Data Bank:** [RCSB PDB 6ILW, PETase crystal structure](https://www.rcsb.org/structure/6ILW)
* **D-Wave Ocean SDK:** [dimod documentation](https://docs.ocean.dwavesys.com/)
* **Biopython:** [Bio.PDB module](https://biopython.org/)
* **Foundational research:** combinatorial side-chain optimization and protein design frameworks.

---

<div align="center">

**Built with ⚛️ by Team Monday for Q-Hack India 2026**

</div>