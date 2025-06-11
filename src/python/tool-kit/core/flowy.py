from math import sqrt
from .constants import P_t, T_t, gamma, R_specific, A_throat
"Known constants from .constants"
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
    guess = 2.0  # Supersonic
    M_e, = fsolve(area_mach_eq, guess, args=(expansion_ratio, gamma))
    return M_e

