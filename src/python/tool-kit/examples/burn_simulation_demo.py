from cold_gas_toolkit.core.constants import V_t, T_t, R_specific
from cold_gas_toolkit.core.flow import mass_flow_rate
from cold_gas_toolkit.core.sizing import calculate_required_propellant, calculate_total_impulse
from cold_gas_toolkit.core.simulation import simulate_pressure_and_mass_over_time

# --- Mission Parameters ---
Isp = 65                     # s from flow model
thrust = 0.12                # N from thrust model
burn_time = 60               # s

# --- Compute m_dot and m_required ---
m_dot = mass_flow_rate()
I_total = calculate_total_impulse(thrust, burn_time)
m_required = calculate_required_propellant(I_total, Isp)

# --- Run Simulation ---
times, pressures, masses = simulate_pressure_and_mass_over_time(
    m_start=m_required,
    V=V_t,
    T=T_t,
    R=R_specific,
    m_dot=m_dot,
    burn_time=burn_time,
    time_step=0.1
)

# --- Output Summary ---
print("=== Burn Simulation Results ===")
print(f"Start Pressure: {pressures[0]/1e6:.2f} MPa")
print(f"End Pressure:   {pressures[-1]/1e6:.2f} MPa")
print(f"Start Mass:     {masses[0]:.4f} kg")
print(f"End Mass:       {masses[-1]:.4f} kg")
print(f"Steps Simulated: {len(times)}")
