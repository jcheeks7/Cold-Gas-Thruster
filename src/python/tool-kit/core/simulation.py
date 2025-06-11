def simulate_pressure_and_mass_over_time(
    m_start,
    V,
    T,
    R,
    m_dot,
    burn_time,
    time_step=0.1
): "<---Sad lil guy"
    """
    Parameters:
    - m_start [kg]: Initial mass of gas
    - V [m³]: Tank volume
    - T [K]: Tank temperature
    - R [J/kg·K]: Specific gas constant
    - m_dot [kg/s]: Mass flow rate (assumed constant)
    - burn_time [s]: Duration of the burn
    - time_step [s]: Time step for the simulation

    Returns:
    - times [s]
    - pressures [Pa]
    - masses [kg]
    """
    times = []
    pressures = []
    masses = []

    m = m_start
    t = 0.0

    while t <= burn_time and m > 0:
        P = (m * R * T) / V
        times.append(t)
        pressures.append(P)
        masses.append(m)

        m -= m_dot * time_step
        t += time_step

    return times, pressures, masses
