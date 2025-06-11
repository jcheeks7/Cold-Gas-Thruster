from cold_gas_toolkit.core.constants import R_specific, T_t, V=Tank_volume, P

# 1. Estimate gas mass using ideal gas law
def ideal_gas_mass(P, V, T=T_t, R=R_specific):
    """
    Parameters:
    - P: Pressure [Pa]
    - V: Volume [m³]
    - T: Temperature [K] (default: T_t)
    - R: Specific gas constant [J/kg·K] (default: CO₂)

    Returns:
    - Mass [kg]
    """
    return (P * V) / (R * T)


# 2. Required pressure to store desired gas mass
def calculate_meop(m_required, V, T=T_t, R=R_specific):
    """
    Parameters:
    - m_required: Mass of gas [kg]
    - V: Volume [m³]
    - T: Temperature [K] (default: T_t)
    - R: Specific gas constant [J/kg·K] (default: CO₂)

    Returns:
    - MEOP [Pa]
    """
    return (m_required * R * T) / V


# 3. Estimate burst pressure with margin
def estimate_burst_pressure(MEOP, safety_factor=1.5):
    """
    Parameters:
    - MEOP: Max expected pressure [Pa]
    - safety_factor: Multiplier for safety (default: 1.5)

    Returns:
    - Burst pressure [Pa]
    """
    return MEOP * safety_factor
