from cold_gas_toolkit.core.constants import (
    P_t, T_t, gamma, R_specific, A_throat, P_0, g0, A_exit, Expansion_ratio
)
from cold_gas_toolkit.core.flow import (
    mass_flow_rate, exit_mach, exit_temperature,
    exit_pressure, exit_velocity
)
from cold_gas_toolkit.core.thrust import (
    calculate_thrust, calculate_isp
)
from cold_gas_toolkit.core.sizing import (
    calculate_total_impulse,
    calculate_required_propellant,
    calculate_tank_volume,
    calculate_delta_v,
)

# --- Design Parameter ---
A_exit = A_throat * Expansion_ratio
burn_time = 60  # seconds
dry_mass = 1.2  # kg (structure, electronics, etc.)
propellant_density = 900  # kg/m³ (approx for CO₂ under pressure)

# --- Flow Calculations ---
m_dot = mass_flow_rate()
M_e = exit_mach(Expansion_ratio, gamma)
T_e = exit_temperature(T_t, M_e, gamma)
P_e = exit_pressure(P_t, M_e, gamma)
v_e = exit_velocity(T_e, gamma, R_specific, M_e)

# --- Performance Calculations ---
thrust = calculate_thrust(m_dot, v_e, P_e, A_exit)
Isp = calculate_isp(v_e)

# --- Sizing Calculations ---
I_total = calculate_total_impulse(thrust, burn_time)
m_propellant = calculate_required_propellant(I_total, Isp)
tank_volume = calculate_tank_volume(m_propellant, propellant_density)
wet_mass = dry_mass + m_propellant
delta_v = calculate_delta_v(Isp, wet_mass, dry_mass)

# --- Output ---
print("=== Cold Gas System Performance ===")
print(f"Thrust:                {thrust:.3f} N")
print(f"Isp:                   {Isp:.2f} s")
print(f"Total Impulse:         {I_total:.2f} N·s")
print(f"Required Propellant:   {m_propellant:.4f} kg")
print(f"Required Tank Volume:  {tank_volume*1e6:.2f} cm³")
print(f"Achievable Δv:         {delta_v:.2f} m/s")

