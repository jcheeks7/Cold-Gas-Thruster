# Cold Gas Propulsion Toolkit

A modular Python toolkit for modeling, sizing, and simulating cold gas propulsion systems. Designed for aerospace engineers and students to estimate performance, size hardware, and visualize system behavior from first principles.

---

## Features

* **Core Flow Modeling**: Calculates mass flow rate, exit velocity, Mach number, and thrust
* **Sizing Tools**: Computes required propellant mass, total impulse, tank volume, and achievable delta-v
* **Nozzle Design**: Supports Mach-area relationships, exit geometry, and expansion ratio analysis
* **Tank Modeling**: Ideal gas storage, MEOP calculation, and burst pressure estimation
* **Time-Step Simulation**: Models pressure and mass over time with plotting support

---
## Author

Developed by Jaxsen Cheeks — Aerospace Engineering @ Georgia Tech
Toolkit developed for academic and personal propulsion projects.

---

## Future Additions

* Multi-pulse burn simulation
* Streamlit GUI
* Unit testing
* CSV export for test reports

---

## Folder Structure

```
cold-gas-toolkit/
├── core/
│   ├── constants.py          # Global constants (Pt, Tt, gamma, R, etc.)
│   ├── flow.py               # Isentropic flow calculations
│   ├── thrust.py             # Thrust and Isp functions
│   ├── sizing.py             # Impulse, mass, delta-v, and tank volume
│   ├── tank.py               # Ideal gas modeling and burst pressure
│   └── simulation.py         # Time-step simulation of burn
├── examples/
│   ├── full_cold_gas_case.py     # End-to-end flow and sizing demo
│   ├── sizing_demo.py            # Propellant mass and delta-v
│   ├── tank_sizing_demo.py       # Pressure and burst calculations
│   └── plot_burn_simulation.py   # Pressure/mass vs time visualization
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/your-username/cold-gas-toolkit.git
cd cold-gas-toolkit
pip install -r requirements.txt
```

---

## Requirements

* Python 3.7+
* `matplotlib`
* `scipy`

Install manually:

```bash
pip install matplotlib scipy
```

---

## Example Usage

Run a complete mission analysis:

```bash
python examples/full_cold_gas_case.py
```

Run a burn simulation and plot:

```bash
python examples/plot_burn_simulation.py
```

---


## License

MIT License
