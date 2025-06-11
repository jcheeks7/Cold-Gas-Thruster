from cold_gas_toolkit.core.constants import (
    T_t, R_specific, V_t, P_t
)
from cold_gas_toolkit.core.sizing import (
    calculate_required_propellant
)
from cold_gas_toolkit.core.tank import (
    calculate_meop,
    estimate_burst_pressure,
    ideal_gas_mass
)
from cold_gas_toolkit.core.flow import (
    mass_flow_rate, exit_mach, exit_temperature,
    exit_pressure, exit_velocity
)
from cold_gas_toolkit.core.thrust import (
    calculate_thrust, calculate_isp
)
from cold_gas_toolkit.core.constants import (
    gamma, R_specific, T_t, A_throat, P_t, P_0
)


# --- Example Mission Parameters ---
I_total = 7.5              # N·s total impulse needed
Isp = 65                   # s from our flow model

# --- Step 1: Required propellant mass ---
m_required = calculate_required_propellant(I_total, Isp)

# --- Step 2: Pressure needed to store it ---
MEOP = calculate_meop(m_required)  # Uses default T_t, V_t, R
burst_pressure = estimate_burst_pressure(MEOP, safety_factor=1.5)

# --- Step 3: Check how much gas your current tank can store at P_t ---
m_actual = ideal_gas_mass()  # Uses current tank P_t, T_t, V_t

# --- Output ---
print("=== Tank Sizing Demo ===")
print(f"Required Impulse:         {I_total:.2f} N·s")
print(f"Isp:                      {Isp:.2f} s")
print(f"Required Propellant Mass: {m_required:.4f} kg")
print(f"Tank Volume (V_t):        {V_t*1e6:.2f} cm³")
print(f"MEOP Required:            {MEOP/1e6:.2f} MPa")
print(f"Burst Pressure Estimate:  {burst_pressure/1e6:.2f} MPa")
print(f"Mass Tank Can Store @P_t: {m_actual:.4f} kg")
