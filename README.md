# Cold Gas Propulsion System

A hands-on cold gas thruster project designed and built for fun. This repository includes the full design lifecycle: research, system modeling, simulation, documentation, CAD, and hardware test planning.

---

## 🚀 Project Overview

Cold gas propulsion is a simple, safe, and cost-effective technology for small spacecraft attitude and trajectory control. This system uses a compressed gas CO₂ expelled through a nozzle to generate thrust via Newton's Third Law.

This project models, simulates, and prepares for the physical implementation of a cold gas thruster, including hardware, controls, and testing protocols.

---

## 🚧 Current Progress🚧:

✅Literature Review <br>
✅Concept Design <br>
✅Design Choice Review <br>
✅Schematics <br>
✅Material Ordered <br>
✅Material Recieved <br>
✅Tool Kit <br>
✅Simulation (Toolkit & CFD) <br>
✅CAD <br>
✅Build <br>
✅Results <br>

---

## 📁 Repository Structure

```
cold-gas-propulsion/
├── docs/                  # Documentation and visual references
│   ├── CAD/               # SolidWorks and STEP files
│   ├── testing/           # Test plans, safety protocols
│   ├── schematics/        # System-level architecture diagrams (P&ID's, etc...)
│   ├── images/            # Graphics for README and LaTeX report
│   └── report/            # LaTeX project report (main.tex, sample.bib)
│
├── src/                   # Source code for simulation and analysis
│   └── python/            # System Simulation and Control Baord
│
├── data/                  # Experimental data, logs, CSV or .mat files
├── results/               # Output plots and figures
├── .gitignore
├── LICENSE
└── README.md              # You're here
```

---

## 🧠 Features

* Ideal gas and isentropic nozzle flow models
* Time-step tank pressure & mass simulation
* CAD-compatible tank layout and plumbing
* Full LaTeX technical report with citations
* P\&ID and testing documentation

---

## 🛠 Tools Used

* **Python** — Data simulation and valve control
* **SolidWorks / Fusion 360** — 3D modeling
* **LaTeX** — technical documentation
* **GitHub** — version control and publishing

---

## 📄 LaTeX Report

Location: [`docs/report/`](docs/report/)

To compile:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Includes:

* Literature survey (cold gas, CubeSat trends)
* Design rationale and equations
* Simulation results and plots
* Safety and testing methodology

---

## 📸 Showcase

*(Coming soon)*

* Annotated CAD screenshots
* Plot samples from simulation
* Build photos & test rig shots

---

## ✅ Future Work

*Nozzle Parameter Expirementation
*Toolkit Expansion

---

## 📜 License

[MIT License](LICENSE) — feel free to fork, remix, and learn from this project.

---

## 👨‍🚀 Author

Developed by Jaxsen Cheeks, a Georgia Tech aerospace engineering undergrad, for summer propulsion research and small satellite systems experience.

For questions, collabs, or feedback, feel free to reach out!
* jcheeks7@gatech.edu
* linkedin.com/jaxsenc
