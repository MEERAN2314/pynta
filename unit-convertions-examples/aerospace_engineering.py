"""
Aerospace Engineering Unit Conversions
======================================

Real-world unit conversions commonly used in aerospace engineering,
including aircraft design, rocket propulsion, orbital mechanics, and flight operations.

Author: Unifyt Team
Industry: Aerospace Engineering
"""

from unifyt import Quantity, constants
import numpy as np


def print_header(title: str) -> None:
    """Print formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"{title}")
    print(f"{'=' * 70}\n")


def print_result(label: str, value: Quantity, conversions: list = None) -> None:
    """Print conversion result with optional additional units."""
    print(f"{label}: {value}")
    if conversions:
        for unit in conversions:
            print(f"  → {value.to(unit)}")


# ============================================================================
# 1. AIRCRAFT PERFORMANCE
# ============================================================================

def aircraft_performance():
    """Aircraft performance calculations and conversions."""
    print_header("1. AIRCRAFT PERFORMANCE")
    
    # Airspeed conversions (critical for flight operations)
    print("Airspeed Conversions:")
    cruise_speed = Quantity(450, 'knot')
    print_result("Cruise speed", cruise_speed, 
                ['kilometer/hour', 'meter/second', 'mile/hour'])
    
    # Altitude conversions
    print("\nAltitude Conversions:")
    flight_level_350 = Quantity(35000, 'foot')
    print_result("FL350", flight_level_350,
                ['meter', 'kilometer', 'mile'])
    
    # Rate of climb
    print("\nRate of Climb:")
    climb_rate = Quantity(2000, 'foot/minute')
    climb_rate_ms = Quantity(climb_rate.magnitude * 0.00508, 'meter/second')
    print_result("Climb rate", climb_rate_ms,
                ['meter/second', 'foot/minute'])
    
    # Fuel consumption
    print("\nFuel Consumption:")
    fuel_flow = Quantity(2500, 'kilogram/hour')
    print_result("Fuel flow", fuel_flow,
                ['pound/hour', 'kilogram/second'])
    
    # Wing loading
    print("\nWing Loading:")
    aircraft_mass = Quantity(75000, 'kilogram')
    wing_area = Quantity(122, 'meter^2')
    wing_loading_value = aircraft_mass.magnitude / wing_area.magnitude
    wing_loading = Quantity(wing_loading_value, 'kilogram/meter^2')
    print_result("Wing loading", wing_loading,
                ['pound/foot^2'])


# ============================================================================
# 2. ROCKET PROPULSION
# ============================================================================

def rocket_propulsion():
    """Rocket propulsion system conversions."""
    print_header("2. ROCKET PROPULSION")
    
    # Thrust
    print("Engine Thrust:")
    thrust = Quantity(7500000, 'newton')
    print_result("Saturn V F-1 engine thrust", thrust,
                ['meganewton', 'kilonewton', 'pound_force'])
    
    # Specific impulse
    print("\nSpecific Impulse:")
    isp = Quantity(450, 'second')
    exhaust_velocity = isp.magnitude * constants.g.magnitude
    exhaust_vel = Quantity(exhaust_velocity, 'meter/second')
    print(f"Specific impulse: {isp}")
    print_result("Exhaust velocity", exhaust_vel,
                ['kilometer/second', 'mile/hour'])
    
    # Propellant mass flow rate
    print("\nPropellant Flow Rate:")
    mass_flow = Quantity(2500, 'kilogram/second')
    print_result("Mass flow rate", mass_flow,
                ['ton/second', 'pound/second'])
    
    # Chamber pressure
    print("\nCombustion Chamber Pressure:")
    chamber_pressure = Quantity(20, 'megapascal')
    print_result("Chamber pressure", chamber_pressure,
                ['pascal', 'bar', 'psi', 'atmosphere'])


# ============================================================================
# 3. ORBITAL MECHANICS
# ============================================================================

def orbital_mechanics():
    """Orbital mechanics and space mission conversions."""
    print_header("3. ORBITAL MECHANICS")
    
    # Orbital velocity
    print("Orbital Velocities:")
    leo_velocity = Quantity(7800, 'meter/second')
    print_result("LEO orbital velocity", leo_velocity,
                ['kilometer/second', 'kilometer/hour', 'mile/hour'])
    
    escape_velocity = Quantity(11200, 'meter/second')
    print_result("\nEarth escape velocity", escape_velocity,
                ['kilometer/second', 'mile/hour'])
    
    # Orbital altitude
    print("\nOrbital Altitudes:")
    iss_altitude = Quantity(408, 'kilometer')
    print_result("ISS altitude", iss_altitude,
                ['meter', 'mile', 'nautical_mile'])
    
    geo_altitude = Quantity(35786, 'kilometer')
    print_result("\nGEO altitude", geo_altitude,
                ['meter', 'mile'])
    
    # Delta-v budget
    print("\nDelta-V Requirements:")
    leo_to_geo = Quantity(3900, 'meter/second')
    print_result("LEO to GEO transfer", leo_to_geo,
                ['kilometer/second'])
    
    # Orbital period
    print("\nOrbital Period:")
    iss_period = Quantity(92.68, 'minute')
    print_result("ISS orbital period", iss_period,
                ['hour', 'second'])


# ============================================================================
# 4. AERODYNAMICS
# ============================================================================

def aerodynamics():
    """Aerodynamic calculations and conversions."""
    print_header("4. AERODYNAMICS")
    
    # Dynamic pressure
    print("Dynamic Pressure (q):")
    # q = 0.5 * ρ * v²
    air_density = Quantity(1.225, 'kilogram/meter^3')
    velocity = Quantity(250, 'meter/second')
    q_value = 0.5 * air_density.magnitude * velocity.magnitude ** 2
    dynamic_pressure = Quantity(q_value, 'pascal')
    print_result("Dynamic pressure", dynamic_pressure,
                ['kilopascal', 'psi', 'bar'])
    
    # Lift coefficient (dimensionless)
    print("\nLift Coefficient:")
    lift_coeff = 0.45
    print(f"CL = {lift_coeff} (dimensionless)")
    
    # Reynolds number (dimensionless)
    print("\nReynolds Number:")
    reynolds = 5e6
    print(f"Re = {reynolds:.2e} (dimensionless)")
    
    # Mach number
    print("\nMach Number:")
    aircraft_speed = Quantity(850, 'kilometer/hour')
    speed_of_sound = Quantity(343, 'meter/second')
    mach_number = aircraft_speed.to('meter/second').magnitude / speed_of_sound.magnitude
    print(f"Mach {mach_number:.2f}")
    print(f"  Aircraft speed: {aircraft_speed}")
    print(f"  Speed of sound: {speed_of_sound}")


# ============================================================================
# 5. STRUCTURAL LOADS
# ============================================================================

def structural_loads():
    """Structural load calculations for aircraft."""
    print_header("5. STRUCTURAL LOADS")
    
    # Load factor (g-force)
    print("Load Factors:")
    max_load_factor = 9.0  # Fighter jet
    print(f"Maximum load factor: {max_load_factor}g")
    acceleration = max_load_factor * constants.g.magnitude
    accel_qty = Quantity(acceleration, 'meter/second^2')
    print_result("Acceleration", accel_qty,
                ['meter/second^2'])
    
    # Stress
    print("\nStructural Stress:")
    stress = Quantity(400, 'megapascal')
    print_result("Allowable stress (aluminum)", stress,
                ['pascal', 'psi', 'bar'])
    
    # Strain (dimensionless)
    print("\nStrain:")
    strain = 0.002
    print(f"Strain: {strain} (dimensionless)")
    print(f"Strain: {strain * 100}%")
    
    # Bending moment
    print("\nBending Moment:")
    # Moment = Force × Distance
    force = Quantity(50000, 'newton')
    distance = Quantity(2.5, 'meter')
    moment_value = force.magnitude * distance.magnitude
    moment = Quantity(moment_value, 'newton * meter')
    print(f"Bending moment: {moment}")


# ============================================================================
# 6. PROPULSION EFFICIENCY
# ============================================================================

def propulsion_efficiency():
    """Propulsion system efficiency calculations."""
    print_header("6. PROPULSION EFFICIENCY")
    
    # Thrust specific fuel consumption (TSFC)
    print("Thrust Specific Fuel Consumption:")
    tsfc = Quantity(0.5, 'kilogram/hour')  # per newton of thrust
    print(f"TSFC: {tsfc} / newton")
    
    # Propulsive efficiency
    print("\nPropulsive Efficiency:")
    prop_efficiency = 0.85
    print(f"ηp = {prop_efficiency * 100}%")
    
    # Thermal efficiency
    print("\nThermal Efficiency:")
    thermal_efficiency = 0.40
    print(f"ηth = {thermal_efficiency * 100}%")
    
    # Overall efficiency
    overall_efficiency = prop_efficiency * thermal_efficiency
    print(f"\nOverall efficiency: {overall_efficiency * 100:.1f}%")


# ============================================================================
# 7. ATMOSPHERIC CONDITIONS
# ============================================================================

def atmospheric_conditions():
    """Atmospheric condition conversions."""
    print_header("7. ATMOSPHERIC CONDITIONS")
    
    # Standard atmosphere at sea level
    print("Standard Atmosphere (Sea Level):")
    std_pressure = Quantity(101325, 'pascal')
    print_result("Pressure", std_pressure,
                ['kilopascal', 'bar', 'psi', 'atmosphere'])
    
    std_temp = Quantity(15, 'celsius')
    print_result("\nTemperature", std_temp,
                ['kelvin', 'fahrenheit'])
    
    std_density = Quantity(1.225, 'kilogram/meter^3')
    print(f"\nDensity: {std_density}")
    
    # Conditions at cruise altitude (35,000 ft)
    print("\n\nConditions at FL350 (35,000 ft):")
    cruise_pressure = Quantity(23842, 'pascal')
    print_result("Pressure", cruise_pressure,
                ['kilopascal', 'psi', 'atmosphere'])
    
    cruise_temp = Quantity(-54, 'celsius')
    print_result("\nTemperature", cruise_temp,
                ['kelvin', 'fahrenheit'])
    
    cruise_density = Quantity(0.38, 'kilogram/meter^3')
    print(f"\nDensity: {cruise_density}")


# ============================================================================
# 8. RANGE AND ENDURANCE
# ============================================================================

def range_endurance():
    """Aircraft range and endurance calculations."""
    print_header("8. RANGE AND ENDURANCE")
    
    # Range
    print("Aircraft Range:")
    max_range = Quantity(8000, 'nautical_mile')
    print_result("Maximum range", max_range,
                ['kilometer', 'mile'])
    
    # Endurance
    print("\nEndurance:")
    max_endurance = Quantity(12, 'hour')
    print_result("Maximum endurance", max_endurance,
                ['minute', 'second'])
    
    # Fuel capacity
    print("\nFuel Capacity:")
    fuel_capacity = Quantity(120000, 'kilogram')
    print_result("Fuel capacity", fuel_capacity,
                ['ton', 'pound'])
    
    # Specific range
    print("\nSpecific Range:")
    # Distance per unit fuel
    specific_range_value = max_range.to('kilometer').magnitude / fuel_capacity.magnitude
    print(f"Specific range: {specific_range_value:.2f} km/kg")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all aerospace engineering conversion examples."""
    print("\n" + "=" * 70)
    print("AEROSPACE ENGINEERING UNIT CONVERSIONS")
    print("Real-world conversions for aircraft, rockets, and spacecraft")
    print("=" * 70)
    
    aircraft_performance()
    rocket_propulsion()
    orbital_mechanics()
    aerodynamics()
    structural_loads()
    propulsion_efficiency()
    atmospheric_conditions()
    range_endurance()
    
    print("\n" + "=" * 70)
    print("All aerospace engineering conversions completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
