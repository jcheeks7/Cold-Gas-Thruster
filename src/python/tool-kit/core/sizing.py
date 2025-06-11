from .constants import g0

def calculate_total_impulse(thrust, burn_time):
    "Total impulse [N·s] given thrust [N] and burn time [s]."
    return thrust * burn_time

def calculate_required_propellant(I_total, Isp):
    "Required propellant mass [kg] given total impulse [N·s] and Isp [s]."
    return I_total / (Isp * g0)

def calculate_tank_volume(m_propellant, propellant_density):
    "Tank volume [m³] given propellant mass [kg] and density [kg/m³]."
    return m_propellant / propellant_density

def calculate_delta_v(Isp, m_initial, m_final):
    "Delta-v [m/s] using rocket equation."
    from math import log
    return Isp * g0 * log(m_initial / m_final)

