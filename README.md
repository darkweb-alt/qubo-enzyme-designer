<div align="center">

<img src="assets/banner.svg" alt="Quantum Bio-Forge banner" width="100%"/>

<br/>

<a href="https://github.com/<your-username>/quantum-bio-forge">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1100&color=A78BFA&center=true&vCenter=true&width=760&lines=Enzyme+design+is+a+combinatorial+problem.;We+turn+it+into+a+QUBO.;Annealing+finds+the+low-energy+conformation.;Built+for+PETase+plastic+degradation." alt="Typing animation"/>
</a>

<br/><br/>

[![Hackathon](https://img.shields.io/badge/Event-Q--Hack%20India%202026-8b5cf6?style=for-the-badge)](https://github.com)
[![Track](https://img.shields.io/badge/Track-Quantum%20Biotech%20%26%20Chemistry-14b8a6?style=for-the-badge)](https://github.com)
[![Team](https://img.shields.io/badge/Team-Monday-3b82f6?style=for-the-badge)](https://github.com)
[![Status](https://img.shields.io/badge/Status-Prototype%20Ready-22c55e?style=for-the-badge)](https://github.com)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Biopython](https://img.shields.io/badge/Biopython-3C873A?style=flat-square)
![D-Wave Ocean](https://img.shields.io/badge/D--Wave_Ocean-1F3A93?style=flat-square)

</div>

---

## ⚡ At a Glance

<div align="center">

| 🧬 Target | 🧮 Model | 🏆 Result | ⏱️ Speed |
|:---:|:---:|:---:|:---:|
| **PETase** (PDB `6ILW`) | **QUBO**, 12 binary variables | **−142.5** vs **+42.0** kcal/mol | **~42 ms** per solve |

</div>

---

## 👥 Team Monday

<div align="center">

| 🧑‍💻 Pitambar Yadav | 🔬 Bhavna S | 🎨 Kowshick Balaji M |
|:---:|:---:|:---:|
| Lead Developer & Quantum Architecture | Biophysical Modeling & Research | System Integration & UI/UX Design |

</div>

---

## 📑 Table of Contents
1. [Problem](#-1-problem-q-hack-india-2026)
2. [Why It Matters](#-2-why-it-matters)
3. [Proposed Solution](#-3-proposed-solution)
4. [Why Quantum?](#%EF%B8%8F-4-why-quantum)
5. [Implementation & Architecture](#%EF%B8%8F-5-implementation-and-architecture)
6. [Minimal Prototype](#-6-minimal-prototype)
7. [Results / Validation](#-7-results--validation)
8. [Getting Started](#%EF%B8%8F-8-getting-started)
9. [Roadmap](#%EF%B8%8F-9-roadmap-round-2--beyond)
10. [References](#-10-references-and-sources)

---

## 🎯 1. Problem (Q-Hack India 2026)

### What problem are you solving?
Enzymes are nature's high-efficiency biological catalysts, but engineering them for industrial or environmental use (such as plastic degradation) is bottlenecked by **combinatorial side-chain packing**.

* The active site, the pocket where substrate binding and catalysis happen, can adopt many amino-acid rotamer combinations: **3^N** for N residues with 3 rotamers each.
* Classical optimizers (Monte Carlo, greedy local search) can get **trapped in high-energy local minima**, leaving steric clashes, unstable conformations, and poor substrate binding.

### 📈 How fast the search space grows

The number of configurations explodes with every residue added (3 rotamers per residue):

```mermaid
xychart-beta
    title "Configurations vs. number of residues (3^N)"
    x-axis "Residues (N)" [2, 4, 6, 8, 10, 12]
    y-axis "Possible configurations" 0 --> 540000
    bar [9, 81, 729, 6561, 59049, 531441]
```

> Our prototype uses **N = 4** (81 states) to validate the pipeline end to end. The same QUBO formulation is what we scale in later rounds.

---

## 💡 2. Why It Matters

### Who faces this problem and why is it important?
* **The global environmental crisis:** Billions of tons of plastic waste (notably PET) accumulate worldwide. Enzymes like **PETase** can degrade PET, but wild-type variants have low catalytic efficiency and high conformational energy barriers.
* **The R&D bottleneck:** Wet-lab directed evolution is expensive, slow, and trial-and-error driven. Computational protein design can speed it up, but only if algorithms can navigate rugged, non-linear energy landscapes. Solving this opens the door to programmable plastic-degrading and carbon-capturing biological agents.

---

## 🚀 3. Proposed Solution

### What are you building?
**Quantum Bio-Forge** is a full-stack computational suite that converts enzyme active-site design into a **QUBO (Quadratic Unconstrained Binary Optimization)** problem.

| Stage | What happens |
|---|---|
| 🧬 **Structural parsing** | Ingests the experimental crystal structure from the Protein Data Bank ([6ILW](https://www.rcsb.org/structure/6ILW)) |
| 📐 **Distance-matrix biophysics** | Computes inter-atomic Euclidean distances between catalytic residues to quantify steric clashes |
| ⚛️ **Annealing optimization** | Encodes packing as a binary quadratic model and solves it with the D-Wave Ocean toolchain to find the minimum-energy conformation |

---

## ⚛️ 4. Why Quantum?

### Why does quantum computing or quantum technology make sense here?
* **Combinatorial scaling:** Conformational search spaces grow exponentially (see the chart above). Greedy and local-search methods scale poorly and stagnate in local minima.
* **Native QUBO fit:** Quantum annealers such as D-Wave's are built to sample low-energy states of Ising/QUBO problems, which is exactly how side-chain packing is formulated. Quantum tunneling lets physical annealers cross narrow energy barriers that trap classical descent.
* **Prototype note:** The current prototype runs D-Wave's **simulated annealing** sampler locally. It is a classical, quantum-inspired solver that validates the QUBO model and pipeline. Running the same model on a physical QPU is the first roadmap item.

---

## ⚙️ 5. Implementation and Architecture

### How is the solution implemented?
Quantum Bio-Forge is a client-server hybrid:

<div align="center">
  <img src="assets/pipeline.svg" alt="Pipeline from PDB 6ILW through Biopython, QUBO and dimod to the Next.js dashboard" width="100%"/>
</div>

<br/>

**Quantum / annealing components:** D-Wave Ocean SDK (`dimod`) for building the binary quadratic model, sampling, and energy-state convergence.

**Classical components:** FastAPI server, Biopython (`Bio.PDB`) geometry parser, and a Next.js / Tailwind CSS research dashboard with a real-time conformational scrubber and annealing-descent curves.

### 🔄 Request flow

```mermaid
sequenceDiagram
    autonumber
    actor U as Researcher
    participant UI as Next.js Dashboard
    participant API as FastAPI Backend
    participant PDB as Biopython (6ILW)
    participant S as dimod Annealer
    U->>UI: Select catalytic residues
    UI->>API: POST /optimize
    API->>PDB: Load structure, read coordinates
    PDB-->>API: Atom positions
    API->>API: Build distance and clash matrix
    API->>API: Formulate QUBO (12 variables)
    API->>S: Sample binary quadratic model
    S-->>API: Lowest-energy state
    API-->>UI: Energies, clashes, descent curve
    UI-->>U: Live scrubber and convergence plot
```

### 🧮 QUBO formulation

* **4 catalytic residues × 3 rotamer states = 12 binary variables** `x_{i,r}`.
* **Linear terms:** self-energy of each rotamer.
* **Quadratic terms:** pairwise steric-clash penalty from the inter-atomic distance matrix.
* **Constraint:** exactly one rotamer per residue, enforced with a penalty term.

$$
E(x) = \sum_{i,r} h_{i,r}\,x_{i,r} + \sum_{(i,r)<(j,s)} J_{ir,js}\,x_{i,r}\,x_{j,s} + P \sum_{i}\Big(\sum_{r} x_{i,r} - 1\Big)^2
$$

<details>
<summary><b>Show a minimal code sketch of the solver step</b></summary>

```python
import dimod
from dwave.samplers import SimulatedAnnealingSampler  # pip install dwave-samplers

# h: linear biases, J: pairwise clash penalties, P: one-hot penalty weight
bqm = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.BINARY)
for residue in residues:
    bqm.add_linear_equality_constraint(
        [(var, 1.0) for var in residue.rotamer_vars],
        constant=-1.0,
        lagrange_multiplier=P,
    )

sampleset = SimulatedAnnealingSampler().sample(bqm, num_reads=200)
best = sampleset.first
print(best.sample, best.energy)
```

</details>

---

## 🧪 6. Minimal Prototype

### What have you actually built?
A functional, end-to-end full-stack web app running locally:

| | Feature | Description |
|:-:|---|---|
| 🖥️ | **Interactive research dashboard** | Clean, research-grade light theme showing pipeline steps, residue targets, and live solver telemetry |
| 🎚️ | **Live conformational scrubber** | A slider that moves through structural transition states in real time, with live energy changes and clash elimination |
| 📉 | **Annealing convergence viewport** | Graphical comparison of classical greedy trapping vs. annealing descent paths |

<!--
Add screenshots after you capture them:
<div align="center">
  <img src="assets/screenshots/dashboard.png" alt="Dashboard" width="90%"/>
</div>
-->

---

## 📊 7. Results / Validation

### What are the results?

<div align="center">
  <img src="assets/convergence.svg" alt="Animated energy descent: greedy search stalls at +42.0 kcal/mol, annealing reaches -142.5 kcal/mol" width="100%"/>
</div>

<br/>

* **Energy minimization:** Eliminated steric clashes across the target catalytic pocket (**TRP 87, SER 156, HIS 189, ASP 243**).
* **Latency:** Average solve time of **~42 ms** for the 12-variable QUBO.

```mermaid
xychart-beta
    title "Final energy reached (kcal/mol), lower is better"
    x-axis ["Classical Greedy", "Annealing (QUBO)"]
    y-axis "Energy (kcal/mol)" -160 --> 60
    bar [42.0, -142.5]
```

| Method | Final Energy | Outcome |
|---|---:|---|
| Classical greedy search | **+42.0 kcal/mol** | 🟠 Trapped in a local minimum |
| Annealing-based QUBO solver | **−142.5 kcal/mol** | 🟢 Reached the global minimum |

> Energies come from the prototype's scoring model (distance-based clash penalties), not a full force field. Advanced scoring is on the roadmap.

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
pip install fastapi uvicorn biopython dimod dwave-samplers numpy
uvicorn main:app --reload --port 8000
```
API docs: `http://localhost:8000/docs`

### 3. Run the frontend
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:3000`.

### 📁 Project structure
```text
quantum-bio-forge/
├── assets/         # README banner, pipeline and chart graphics
├── backend/        # FastAPI server, PDB parsing, QUBO + solver
├── frontend/       # Next.js + Tailwind dashboard
└── README.md
```

---

## 🗺️ 9. Roadmap (Round 2 & Beyond)

```mermaid
timeline
    title Quantum Bio-Forge Roadmap
    Prototype (done) : QUBO formulation : Simulated annealing on 6ILW : Interactive dashboard
    Round 2 : Physical QPU via D-Wave Leap : Hybrid solver jobs
    Scale-up : Multi-residue protein regions : Sub-space decomposition
    Advanced physics : Electrostatics and solvation : Hydrogen-bond networks : HOBO models
```

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

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1500&color=2DD4BF&center=true&vCenter=true&width=520&lines=Built+with+%E2%9A%9B%EF%B8%8F+by+Team+Monday;Q-Hack+India+2026+%7C+Infinitude" alt="Footer"/>

⭐ If this project helped you, consider starring the repo.

</div>