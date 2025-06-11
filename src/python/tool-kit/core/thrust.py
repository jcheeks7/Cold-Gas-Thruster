from .constants import P_0
from .constants import g0

def calculate_thrust(m_dot, v_e, P_e, A_exit):
    momentum = m_dot * v_e
    pressure = (P_e - P_0) * A_exit
    return momentum + pressure

def calculate_isp(v_e):
    return v_e / g0
