import matplotlib.pyplot as plt
from cold_gas_toolkit.core.constants import V_t, T_t, R_specific
from cold_gas_toolkit.core.flow import mass_flow_rate
from cold_gas_toolkit.core.sizing import calculate_required_propellant, calculate_total_impulse
from cold_gas_toolkit.core.simulation import simulate_pressure_and_mass_over_time

# --- Inputs ---
Isp = 65
thrust = 0.12
burn_time = 60

m_dot = mass_flow_rate()
I_total = calculate_total_impulse(thrust, burn_time)
m_required = calculate_required_propellant(I_total, Isp)

# --- Simulate ---
times, pressures, masses = simulate_pressure_and_mass_over_time(
    m_start=m_required,
    V=V_t,
    T=T_t,
    R=R_specific,
    m_dot=m_dot,
    burn_time=burn_time,
    time_step=0.1
)

# --- Plot ---
fig, ax1 = plt.subplots()

ax1.set_title("Cold Gas Tank Burn Simulation")
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Pressure [MPa]", color="tab:red")
ax1.plot(times, [p / 1e6 for p in pressures], color="tab:red", label="Pressure")
ax1.tick_params(axis="y", labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.set_ylabel("Mass [kg]", color="tab:blue")
ax2.plot(times, masses, color="tab:blue", label="Mass")
ax2.tick_params(axis="y", labelcolor="tab:blue")

fig.tight_layout()
plt.grid(True)
plt.show()
