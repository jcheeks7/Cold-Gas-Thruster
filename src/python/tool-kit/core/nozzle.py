from math import sqrt

def estimate_mass_flow_rate(P0, T0, A_throat, gamma, R_specific):
    """
    Input parameters:
    - P0 (Pa): Total (stagnation) pressure
    - T0 (K): Total (stagnation) temperature
    - A_throat (m^2): Nozzle throat area
    - gamma: Heat capacity ratio (e.g., 1.29 for CO2)
    - R_specific (J/kg·K): Specific gas constant for your propellant

    Returns:
    - mdot (kg/s)
    """
    pressure_term = P0 / sqrt(T0)
    flow_term = sqrt(gamma / R_specific)
    expansion_term = ((gamma + 1) / 2) ** (- (gamma + 1) / (2 * (gamma - 1)))
    
    return A_throat * pressure_term * flow_term * expansion_term

def estimate_exit_mach(
