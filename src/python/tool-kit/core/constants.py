# ---- Physical Constants ----
g0 = 9.80665  # This is standard gravity in units [m/s^2]

# ---- Gas Properties (CO₂ for this system) ----
gamma = 1.29            # [-] Specific heat ratio for CO₂
R_specific = 188.9      # [J/kg·K] Specific gas constant for CO₂

# ---- System Conditions ----
P_t = 5.5e6             # [Pa] Total tank pressure (paintball is ~800 psi)
T_t = 300               # [K] Total tank temperature (doinh this at room temp, can change to reflect test environment temp)
P_0 = 0                 # [Pa] Ambient pressure (vacuum for space, [test day pressure] for test environment)

# ---- Geometry ----
d_throat = 1e-3         # [m] Throat diameter (2mm for this)
A_throat = 3.1416 * (d_throat/2)**2  # [m²] Throat area
d_exit = 3e-3  # [m] Exit diameter (4 mm)
A_exit = 3.1416 * (d_exit / 2)**2  # [m²] Exit area

Expansion_ratio = A_exit / A_throat
