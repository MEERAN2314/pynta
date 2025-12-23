"""Physical and mathematical constants with units."""

from pynta.quantity import Quantity
import math

# Mathematical constants
pi = math.pi
e = math.e
golden_ratio = (1 + math.sqrt(5)) / 2

# Physical constants (CODATA 2018 values)

# Speed of light in vacuum
speed_of_light = Quantity(299792458, 'meter/second')
c = speed_of_light

# Planck constant
planck = Quantity(6.62607015e-34, 'joule * second')
h = planck
hbar = Quantity(1.054571817e-34, 'joule * second')

# Gravitational constant
gravitational_constant = Quantity(6.67430e-11, 'meter^3 / kilogram / second^2')
G = gravitational_constant

# Elementary charge
elementary_charge = Quantity(1.602176634e-19, 'coulomb')
e_charge = elementary_charge

# Electron mass
electron_mass = Quantity(9.1093837015e-31, 'kilogram')
m_e = electron_mass

# Proton mass
proton_mass = Quantity(1.67262192369e-27, 'kilogram')
m_p = proton_mass

# Neutron mass
neutron_mass = Quantity(1.67492749804e-27, 'kilogram')
m_n = neutron_mass

# Avogadro constant
avogadro = Quantity(6.02214076e23, '1/mole')
N_A = avogadro

# Boltzmann constant
boltzmann = Quantity(1.380649e-23, 'joule/kelvin')
k_B = boltzmann

# Gas constant
gas_constant = Quantity(8.314462618, 'joule/mole/kelvin')
R = gas_constant

# Stefan-Boltzmann constant
stefan_boltzmann = Quantity(5.670374419e-8, 'watt/meter^2/kelvin^4')
sigma = stefan_boltzmann

# Electric constant (permittivity of free space)
electric_constant = Quantity(8.8541878128e-12, 'farad/meter')
epsilon_0 = electric_constant

# Magnetic constant (permeability of free space)
magnetic_constant = Quantity(1.25663706212e-6, 'henry/meter')
mu_0 = magnetic_constant

# Standard acceleration of gravity
standard_gravity = Quantity(9.80665, 'meter/second^2')
g = standard_gravity

# Atmospheric pressure at sea level
standard_atmosphere = Quantity(101325, 'pascal')
atm = standard_atmosphere

# Absolute zero
absolute_zero = Quantity(0, 'kelvin')

# Astronomical constants

# Astronomical unit
astronomical_unit = Quantity(1.495978707e11, 'meter')
AU = astronomical_unit

# Light year
light_year = Quantity(9.4607304725808e15, 'meter')
ly = light_year

# Parsec
parsec = Quantity(3.0856775814913673e16, 'meter')
pc = parsec

# Solar mass
solar_mass = Quantity(1.98847e30, 'kilogram')
M_sun = solar_mass

# Earth mass
earth_mass = Quantity(5.97217e24, 'kilogram')
M_earth = earth_mass

# Earth radius (mean)
earth_radius = Quantity(6.371e6, 'meter')
R_earth = earth_radius

# Atomic and nuclear constants

# Bohr radius
bohr_radius = Quantity(5.29177210903e-11, 'meter')
a_0 = bohr_radius

# Rydberg constant
rydberg = Quantity(10973731.568160, '1/meter')
R_inf = rydberg

# Fine structure constant (dimensionless)
fine_structure = 7.2973525693e-3
alpha = fine_structure

# Atomic mass unit
atomic_mass_unit = Quantity(1.66053906660e-27, 'kilogram')
u = atomic_mass_unit
amu = atomic_mass_unit

# Useful conversion factors

# Electron volt to joules
eV_to_J = 1.602176634e-19

# Calorie to joules
cal_to_J = 4.184

# BTU to joules
BTU_to_J = 1055.06

# Horsepower to watts
hp_to_W = 745.7

# Dictionary of all constants for easy access
CONSTANTS = {
    # Mathematical
    'pi': pi,
    'e': e,
    'golden_ratio': golden_ratio,
    
    # Physical
    'c': c,
    'h': h,
    'hbar': hbar,
    'G': G,
    'e_charge': e_charge,
    'm_e': m_e,
    'm_p': m_p,
    'm_n': m_n,
    'N_A': N_A,
    'k_B': k_B,
    'R': R,
    'sigma': sigma,
    'epsilon_0': epsilon_0,
    'mu_0': mu_0,
    'g': g,
    'atm': atm,
    
    # Astronomical
    'AU': AU,
    'ly': ly,
    'pc': pc,
    'M_sun': M_sun,
    'M_earth': M_earth,
    'R_earth': R_earth,
    
    # Atomic
    'a_0': a_0,
    'R_inf': R_inf,
    'alpha': alpha,
    'u': u,
}


def get_constant(name: str) -> Quantity:
    """
    Get a physical constant by name.
    
    Args:
        name: Name of the constant
        
    Returns:
        Quantity representing the constant
        
    Raises:
        KeyError: If constant not found
        
    Examples:
        >>> c = get_constant('c')
        >>> print(c)
        299792458 meter/second
    """
    if name in CONSTANTS:
        return CONSTANTS[name]
    raise KeyError(f"Constant '{name}' not found")


def list_constants() -> list:
    """
    List all available constants.
    
    Returns:
        List of constant names
    """
    return sorted(CONSTANTS.keys())
