from .constants import g0
from math import log

def calculate_total_impulse(thrust, burn_time):
    """
    Parameters:
    - thrust [N]
    - burn_time [s]

    Returns:
    - Total impulse [N·s]
    """
    return thrust * burn_time

def calculate_required_propellant(I_total, Isp):
    """
    Parameters:
    - I_total [N·s]
    - Isp [s]

    Returns:
    - Propellant mass [kg]
    """
    return I_total / (Isp * g0)

def calculate_tank_volume(m_propellant, density):
    """
    Parameters:
    - m_propellant [kg]
    - density [kg/m³]

    Returns:
    - Volume [m³]
    """
    return m_propellant / density

def calculate_delta_v(Isp, m_initial, m_final):
    """
    Parameters:
    - Isp [s]
    - m_initial [kg]
    - m_final [kg]

    Returns:
    - Delta-v [m/s]
    """
    return Isp * g0 * log(m_initial / m_final)
