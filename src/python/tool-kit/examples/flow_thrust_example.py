from cold_gas_toolkit.core.constants import (
    P_t, T_t, gamma, R_specific, A_throat
)
from cold_gas_toolkit.core.flow import (
    mass_flow_rate, exit_mach, exit_temperature,
    exit_pressure, exit_velocity
)
from cold_gas_toolkit.core.thrust import (
    calculate_thrust, calculate_isp
)

expansion_ratio = 4.0  # Ae / A* 
A_exit = A_throat * expansion_ratio  # Exit area

# --- FLOW CALCULATIONS MAPPING---
m_dot = mass_flow_rate()
M_e = exit_mach(expansion_ratio, gamma)
T_e = exit_temperature(T_t, M_e, gamma)
P_e = exit_pressure(P_t, M_e, gamma)
v_e = exit_velocity(T_e, gamma, R_specific, M_e)

# --- PERFORMANCE CALCULATIONS ---
F = calculate_thrust(m_dot, v_e, P_e, A_exit)
Isp = calculate_isp(v_e)

# --- OUTPUT ---
print("=== Cold Gas System Output ===")
print(f"Mass Flow Rate:       {m_dot:.6f} kg/s")
print(f"Exit Mach Number:     {M_e:.3f}")
print(f"Exit Temp:            {T_e:.2f} K")
print(f"Exit Pressure:        {P_e:.2f} Pa")
print(f"Exit Velocity:        {v_e:.2f} m/s")
print(f"Thrust:               {F:.3f} N")
print(f"Specific Impulse:     {Isp:.2f} s")
