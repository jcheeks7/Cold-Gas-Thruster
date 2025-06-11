import streamlit as st
from math import pi

from cold_gas_toolkit.core.constants import g0, R_specific, gamma
from cold_gas_toolkit.core.flow import (
    mass_flow_rate, exit_mach, exit_temperature,
    exit_pressure, exit_velocity
)
from cold_gas_toolkit.core.thrust import calculate_thrust, calculate_isp
from cold_gas_toolkit.core.sizing import (
    calculate_total_impulse, calculate_required_propellant,
    calculate_delta_v, calculate_tank_volume
)
import matplotlib.pyplot as plt
from cold_gas_toolkit.core.simulation import simulate_pressure_and_mass_over_time
st.title("Cold Gas Thruster Sizing Tool")

# --- User Inputs ---
P_t = st.slider("Tank Pressure (Pa)", 1e6, 8e6, 5.5e6, step=1e5)
T_t = st.slider("Tank Temperature (K)", 250, 400, 300)
d_throat = st.slider("Throat Diameter (mm)", 0.5, 5.0, 1.0) / 1000
expansion_ratio = st.slider("Expansion Ratio (Ae / A*)", 1.0, 10.0, 4.0)
burn_time = st.slider("Burn Time (s)", 1, 120, 60)
dry_mass = st.number_input("Dry Mass (kg)", value=1.2)
density = st.number_input("Propellant Density (kg/m³)", value=900.0)

# --- Derived Geometry ---
A_throat = pi * (d_throat / 2)**2
A_exit = A_throat * expansion_ratio

# --- Flow Calculations ---
m_dot = mass_flow_rate()
M_e = exit_mach(expansion_ratio, gamma)
T_e = exit_temperature(T_t, M_e, gamma)
P_e = exit_pressure(P_t, M_e, gamma)
v_e = exit_velocity(T_e, gamma, R_specific, M_e)
thrust = calculate_thrust(m_dot, v_e, P_e, A_exit)
Isp = calculate_isp(v_e)

# --- Sizing Calculations ---
I_total = calculate_total_impulse(thrust, burn_time)
m_required = calculate_required_propellant(I_total, Isp)
tank_volume = calculate_tank_volume(m_required, density)
wet_mass = dry_mass + m_required
delta_v = calculate_delta_v(Isp, wet_mass, dry_mass)

# --- Output ---
st.subheader("Results")
st.write(f"**Thrust:** {thrust:.3f} N")
st.write(f"**Isp:** {Isp:.2f} s")
st.write(f"**Total Impulse:** {I_total:.2f} N·s")
st.write(f"**Required Propellant:** {m_required:.4f} kg")
st.write(f"**Tank Volume Needed:** {tank_volume*1e6:.2f} cm³")
st.write(f"**Achievable Δv:** {delta_v:.2f} m/s")


# --- Simulation Inputs ---
simulate = st.checkbox("Run Burn Simulation", value=True)

if simulate:
    times, pressures, masses = simulate_pressure_and_mass_over_time(
        m_start=m_required,
        V=tank_volume,
        T=T_t,
        R=R_specific,
        m_dot=m_dot,
        burn_time=burn_time,
        time_step=0.1
    )
    fig, ax1 = plt.subplots()

    ax1.plot(times, [p / 1e6 for p in pressures], color="tab:red", label="Pressure [MPa]")
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Pressure [MPa]", color="tab:red")
    ax1.tick_params(axis="y", labelcolor="tab:red")

    ax2 = ax1.twinx()
    ax2.plot(times, masses, color="tab:blue", label="Mass [kg]")
    ax2.set_ylabel("Mass [kg]", color="tab:blue")
    ax2.tick_params(axis="y", labelcolor="tab:blue")

    fig.tight_layout()
    st.pyplot(fig)
