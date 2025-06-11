from math import sqrt
from .constants import P_t, T_t, gamma, R_specific, A_throat
from scipy.optimize import fsolve

def estimate_mass_flow_rate(P0, T0, A_throat, gamma, R_specific):
    pressure_term = P0 / sqrt(T0)
    flow_term = sqrt(gamma / R_specific)
    expansion_term = ((gamma + 1) / 2) ** (- (gamma + 1) / (2 * (gamma - 1)))
    return A_throat * pressure_term * flow_term * expansion_term

def area_mach_eq(M, expansion_ratio, gamma):
    term1 = 1 / M
    term2 = (2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2)
    exponent = (gamma + 1) / (2 * (gamma - 1))
    return term1 * term2**exponent - expansion_ratio

def exit_mach(expansion_ratio, gamma):
    guess = 2.0  # Supersonic; Can change, <1 is subsonic, >1 supersong; we want this to be supersonic
    M_e, = fsolve(area_mach_eq, guess, args=(expansion_ratio, gamma))
    return M_e

def exit_temperature(T_t, M_e, gamma):
    T_e = T_t / (1 + ((gamma - 1) / 2) * M_e**2)
    return T_e

def exit_pressure(P_t, M_e, gamma):
    P_e = P_t / (1 + ((gamma - 1) / 2) * M_e**2) ** (gamma / (gamma - 1))
    return P_e
from math import sqrt

def exit_velocity(T_e, gamma, R_specific, M_e):
    a_e = sqrt(gamma * R_specific * T_e)  # Speed of sound at exit
    v_e = M_e * a_e
    return v_e
