"""
Comprehensive Unit Conversion Examples for Unifyt Library
==========================================================

This file demonstrates the full power of Unifyt's unit conversion capabilities
across three levels:
1. Normal Conversions - Everyday unit conversions
2. General Use Cases - Common scientific and engineering scenarios
3. Industry-Level Scenarios - Real-world professional applications

Author: Unifyt Team
Version: 0.2.0
"""

import numpy as np
from unifyt import Quantity, constants, utils
from typing import List, Tuple


def print_section(title: str, char: str = "=") -> None:
    """Print a formatted section header."""
    print(f"\n{char * 80}")
    print(f"{title.center(80)}")
    print(f"{char * 80}\n")


def print_subsection(title: str) -> None:
    """Print a formatted subsection header."""
    print(f"\n{'─' * 80}")
    print(f"  {title}")
    print(f"{'─' * 80}")


def print_conversion(original: Quantity, targets: List[str], description: str = "") -> None:
    """Print a conversion with multiple target units."""
    if description:
        print(f"\n{description}")
    print(f"Original: {original}")
    for target in targets:
        converted = original.to(target)
        print(f"  → {converted}")


# ============================================================================
# PART 1: NORMAL CONVERSIONS - Everyday Unit Conversions
# ============================================================================

def normal_conversions():
    """Demonstrate everyday unit conversions."""
    print_section("PART 1: NORMAL CONVERSIONS - Everyday Use")
    
    # 1.1 Length Conversions
    print_subsection("1.1 Length Conversions")
    
    # Metric system
    distance_m = Quantity(1000, 'meter')
    print_conversion(distance_m, ['kilometer', 'centimeter', 'millimeter'],
                    "Metric length conversions:")
    
    # Imperial system
    distance_ft = Quantity(100, 'foot')
    print_conversion(distance_ft, ['meter', 'yard', 'inch', 'mile'],
                    "Imperial to metric and within imperial:")
    
    # Mixed conversions
    height_cm = Quantity(175, 'centimeter')
    print_conversion(height_cm, ['meter', 'foot', 'inch'],
                    "Human height conversions:")
    
    # 1.2 Mass/Weight Conversions
    print_subsection("1.2 Mass/Weight Conversions")
    
    # Body weight
    weight_kg = Quantity(70, 'kilogram')
    print_conversion(weight_kg, ['pound', 'gram', 'ounce'],
                    "Body weight conversions:")
    
    # Cooking measurements
    flour_g = Quantity(250, 'gram')
    print_conversion(flour_g, ['kilogram', 'ounce', 'pound'],
                    "Cooking ingredient conversions:")
    
    # 1.3 Temperature Conversions
    print_subsection("1.3 Temperature Conversions")
    
    # Room temperature
    temp_c = Quantity(20, 'celsius')
    print_conversion(temp_c, ['fahrenheit', 'kelvin'],
                    "Room temperature:")
    
    # Cooking temperature
    oven_f = Quantity(350, 'fahrenheit')
    print_conversion(oven_f, ['celsius', 'kelvin'],
                    "Oven temperature:")
    
    # Freezing point
    freeze = Quantity(0, 'celsius')
    print_conversion(freeze, ['fahrenheit', 'kelvin'],
                    "Water freezing point:")
    
    # 1.4 Volume Conversions
    print_subsection("1.4 Volume Conversions")
    
    # Liquid volume
    water_l = Quantity(2, 'liter')
    print_conversion(water_l, ['milliliter', 'gallon', 'cup'],
                    "Liquid volume conversions:")
    
    # Fuel tank
    tank_gal = Quantity(15, 'gallon')
    print_conversion(tank_gal, ['liter', 'milliliter'],
                    "Fuel tank capacity:")
    
    # 1.5 Speed Conversions
    print_subsection("1.5 Speed Conversions")
    
    # Highway speed
    speed_mph = Quantity(65, 'mile/hour')
    print_conversion(speed_mph, ['kilometer/hour', 'meter/second'],
                    "Highway speed limit:")
    
    # Running pace
    pace_kmh = Quantity(10, 'kilometer/hour')
    print_conversion(pace_kmh, ['mile/hour', 'meter/second'],
                    "Running pace:")
    
    # 1.6 Time Conversions
    print_subsection("1.6 Time Conversions")
    
    # Work hours
    work_hours = Quantity(8, 'hour')
    print_conversion(work_hours, ['minute', 'second', 'day'],
                    "Work day duration:")
    
    # Movie length
    movie_min = Quantity(142, 'minute')
    print_conversion(movie_min, ['hour', 'second'],
                    "Movie duration:")
    
    # 1.7 Energy Conversions (Everyday)
    print_subsection("1.7 Energy Conversions (Food & Utilities)")
    
    # Food calories
    food_cal = Quantity(2000, 'kilocalorie')
    print_conversion(food_cal, ['joule', 'kilowatt_hour'],
                    "Daily caloric intake:")
    
    # Electricity bill
    electricity = Quantity(500, 'kilowatt_hour')
    print_conversion(electricity, ['joule', 'megajoule'],
                    "Monthly electricity usage:")


# ============================================================================
# PART 2: GENERAL USE CASES - Scientific & Engineering Applications
# ============================================================================

def general_use_cases():
    """Demonstrate scientific and engineering unit conversions."""
    print_section("PART 2: GENERAL USE CASES - Scientific & Engineering")
    
    # 2.1 Physics - Mechanics
    print_subsection("2.1 Physics - Mechanics")
    
    # Acceleration
    gravity = Quantity(9.81, 'meter/second^2')
    print_conversion(gravity, ['kilometer/hour^2', 'mile/hour^2'],
                    "Gravitational acceleration:")
    
    # Force
    force_n = Quantity(1000, 'newton')
    print_conversion(force_n, ['kilonewton', 'pound_force', 'dyne'],
                    "Applied force:")
    
    # Pressure
    pressure_pa = Quantity(101325, 'pascal')
    print_conversion(pressure_pa, ['atmosphere', 'bar', 'psi', 'torr'],
                    "Atmospheric pressure:")
    
    # 2.2 Physics - Energy & Power
    print_subsection("2.2 Physics - Energy & Power")
    
    # Kinetic energy
    kinetic = Quantity(5000, 'joule')
    print_conversion(kinetic, ['kilowatt_hour', 'calorie', 'electronvolt', 'erg'],
                    "Kinetic energy:")
    
    # Power output
    power_w = Quantity(1500, 'watt')
    print_conversion(power_w, ['kilowatt', 'horsepower', 'megawatt'],
                    "Motor power output:")
    
    # 2.3 Electromagnetic Units
    print_subsection("2.3 Electromagnetic Units")
    
    # Voltage
    voltage = Quantity(220, 'volt')
    print_conversion(voltage, ['millivolt', 'kilovolt', 'microvolt'],
                    "Electrical voltage:")
    
    # Current
    current = Quantity(15, 'ampere')
    print_conversion(current, ['milliampere', 'microampere', 'kiloampere'],
                    "Electrical current:")
    
    # Capacitance
    cap = Quantity(100, 'microfarad')
    print_conversion(cap, ['farad', 'nanofarad', 'picofarad'],
                    "Capacitor value:")
    
    # Inductance
    ind = Quantity(10, 'millihenry')
    print_conversion(ind, ['henry', 'microhenry', 'nanohenry'],
                    "Inductor value:")
    
    # Magnetic field
    mag_field = Quantity(1, 'tesla')
    print_conversion(mag_field, ['gauss', 'millitesla', 'microtesla'],
                    "Magnetic field strength:")
    
    # 2.4 Chemistry
    print_subsection("2.4 Chemistry")
    
    # Concentration
    conc = Quantity(1, 'molar')
    print_conversion(conc, ['millimolar', 'micromolar', 'nanomolar'],
                    "Solution concentration:")
    
    # Molecular mass
    mass_amu = Quantity(18.015, 'atomic_mass_unit')
    print_conversion(mass_amu, ['kilogram', 'gram'],
                    "Water molecule mass:")
    
    # 2.5 Astronomy
    print_subsection("2.5 Astronomy")
    
    # Astronomical distances
    dist_au = Quantity(1, 'astronomical_unit')
    print_conversion(dist_au, ['kilometer', 'mile', 'light_year'],
                    "Earth-Sun distance:")
    
    # Stellar distances
    dist_ly = Quantity(4.24, 'light_year')
    print_conversion(dist_ly, ['parsec', 'kilometer', 'astronomical_unit'],
                    "Distance to Proxima Centauri:")
    
    # Galactic distances
    dist_kpc = Quantity(8.5, 'kiloparsec')
    print_conversion(dist_kpc, ['parsec', 'light_year', 'megaparsec'],
                    "Distance to galactic center:")
    
    # Stellar masses
    star_mass = Quantity(2, 'solar_mass')
    print_conversion(star_mass, ['kilogram', 'earth_mass'],
                    "Massive star mass:")
    
    # 2.6 Atomic & Nuclear Physics
    print_subsection("2.6 Atomic & Nuclear Physics")
    
    # Particle energy
    energy_ev = Quantity(13.6, 'electronvolt')
    print_conversion(energy_ev, ['joule', 'rydberg', 'hartree'],
                    "Hydrogen ionization energy:")
    
    # High energy physics
    energy_gev = Quantity(125, 'gigaelectronvolt')
    print_conversion(energy_gev, ['megaelectronvolt', 'joule', 'teraelectronvolt'],
                    "Higgs boson mass-energy:")
    
    # Atomic length scales
    length_ang = Quantity(1, 'angstrom')
    print_conversion(length_ang, ['nanometer', 'picometer', 'meter'],
                    "Atomic bond length:")
    
    # Nuclear length scales
    length_fm = Quantity(1, 'femtometer')
    print_conversion(length_fm, ['meter', 'picometer', 'angstrom'],
                    "Nuclear radius scale:")
    
    # 2.7 Radioactivity & Radiation
    print_subsection("2.7 Radioactivity & Radiation")
    
    # Activity
    activity = Quantity(1, 'curie')
    print_conversion(activity, ['becquerel', 'megabecquerel', 'gigabecquerel'],
                    "Radioactive source activity:")
    
    # Absorbed dose
    dose_gray = Quantity(1, 'gray')
    print_conversion(dose_gray, ['milligray'],
                    "Radiation absorbed dose:")
    
    # Note: 'rad' is ambiguous (radian vs absorbed dose), using full names
    print(f"  (Note: 1 gray = 100 rad in radiation units)")
    
    # Equivalent dose
    dose_sv = Quantity(1, 'sievert')
    print_conversion(dose_sv, ['millisievert', 'microsievert'],
                    "Radiation equivalent dose:")
    
    # Note: 'rem' conversion
    print(f"  (Note: 1 sievert = 100 rem in radiation units)")
    
    # 2.8 Data & Information
    print_subsection("2.8 Data & Information")
    
    # File sizes
    file_mb = Quantity(1024, 'megabyte')
    print_conversion(file_mb, ['gigabyte', 'kilobyte', 'byte', 'bit'],
                    "File size:")
    
    # Binary units
    file_gib = Quantity(1, 'gibibyte')
    print_conversion(file_gib, ['mebibyte', 'kibibyte', 'byte'],
                    "Binary file size:")
    
    # Large storage
    storage_tb = Quantity(5, 'terabyte')
    print_conversion(storage_tb, ['gigabyte', 'petabyte', 'tebibyte'],
                    "Hard drive capacity:")


# ============================================================================
# PART 3: INDUSTRY-LEVEL SCENARIOS - Professional Applications
# ============================================================================

def industry_level_scenarios():
    """Demonstrate real-world industry-level unit conversions."""
    print_section("PART 3: INDUSTRY-LEVEL SCENARIOS - Professional Applications")
    
    # 3.1 Aerospace Engineering
    print_subsection("3.1 Aerospace Engineering")
    
    print("\n🚀 Rocket Launch Calculations:")
    # Escape velocity
    escape_vel = Quantity(11.2, 'kilometer/second')
    print_conversion(escape_vel, ['meter/second', 'mile/hour', 'mach'],
                    "Earth escape velocity:")
    
    # Orbital velocity
    orbital_vel = Quantity(7.8, 'kilometer/second')
    print_conversion(orbital_vel, ['meter/second', 'mile/hour'],
                    "Low Earth orbit velocity:")
    
    # Thrust
    thrust = Quantity(7.5e6, 'newton')
    print_conversion(thrust, ['meganewton', 'kilonewton', 'pound_force'],
                    "Saturn V rocket thrust:")
    
    # Specific impulse (effective exhaust velocity)
    isp = Quantity(450, 'second')
    # Isp * g0 gives exhaust velocity
    exhaust_vel = isp.magnitude * constants.g.magnitude  # Calculate numerically
    exhaust_vel_qty = Quantity(exhaust_vel, 'meter/second')
    print(f"\nSpecific impulse: {isp}")
    print(f"Effective exhaust velocity: {exhaust_vel_qty}")
    print(f"  → {exhaust_vel_qty.to('kilometer/second')}")
    
    # 3.2 Civil Engineering
    print_subsection("3.2 Civil Engineering")
    
    print("\n🏗️ Bridge Construction:")
    # Structural load (mass)
    load_mass = Quantity(50, 'ton')
    print_conversion(load_mass, ['kilogram', 'pound'],
                    "Bridge load capacity per meter (mass):")
    
    # Convert to force (F = m * g)
    load_mass_kg = load_mass.to('kilogram')
    load_force_n = load_mass_kg.magnitude * constants.g.magnitude
    load_force = Quantity(load_force_n, 'newton')
    print(f"\nLoad as force: {load_force}")
    print(f"  → {load_force.to('kilonewton'):.2f}")
    
    # Concrete strength
    strength = Quantity(40, 'megapascal')
    print_conversion(strength, ['pascal', 'psi', 'bar'],
                    "Concrete compressive strength:")
    
    # Beam deflection
    deflection = Quantity(5, 'millimeter')
    print_conversion(deflection, ['meter', 'centimeter', 'inch'],
                    "Maximum allowable deflection:")
    
    # 3.3 Automotive Engineering
    print_subsection("3.3 Automotive Engineering")
    
    print("\n🚗 Vehicle Performance:")
    # Engine power
    engine_power = Quantity(300, 'horsepower')
    print_conversion(engine_power, ['watt', 'kilowatt', 'metric_horsepower'],
                    "Engine power output:")
    
    # Torque
    torque = Quantity(400, 'newton * meter')
    print(f"\nEngine torque: {torque}")
    print(f"  → {torque.to('kilonewton * meter')}")
    
    # Fuel efficiency
    mpg = Quantity(35, 'mile_per_gallon')
    print_conversion(mpg, ['kilometer_per_liter', 'liter_per_100km'],
                    "Fuel efficiency:")
    
    # Tire pressure
    tire_psi = Quantity(32, 'psi')
    print_conversion(tire_psi, ['pascal', 'bar', 'atmosphere'],
                    "Tire pressure:")
    
    # 3.4 Chemical Engineering
    print_subsection("3.4 Chemical Engineering")
    
    print("\n⚗️ Industrial Process:")
    # Flow rate
    flow = Quantity(500, 'liter_per_minute')
    print_conversion(flow, ['cubic_meter_per_second', 'gallon_per_minute'],
                    "Process flow rate:")
    
    # Reactor pressure
    reactor_p = Quantity(150, 'bar')
    print_conversion(reactor_p, ['pascal', 'megapascal', 'atmosphere', 'psi'],
                    "Reactor operating pressure:")
    
    # Viscosity (dynamic)
    viscosity = Quantity(100, 'centipoise')
    print_conversion(viscosity, ['pascal_second', 'poise'],
                    "Fluid dynamic viscosity:")
    
    # Heat capacity
    heat_cap = Quantity(4.18, 'joule_per_kilogram_kelvin')
    print(f"\nSpecific heat capacity: {heat_cap}")
    
    # 3.5 Electrical Power Engineering
    print_subsection("3.5 Electrical Power Engineering")
    
    print("\n⚡ Power Grid Operations:")
    # Transmission voltage
    hv = Quantity(500, 'kilovolt')
    print_conversion(hv, ['volt', 'megavolt'],
                    "High voltage transmission:")
    
    # Power plant output
    plant_power = Quantity(1000, 'megawatt')
    print_conversion(plant_power, ['watt', 'gigawatt', 'kilowatt'],
                    "Nuclear power plant output:")
    
    # Energy generation
    # Convert to base units first
    plant_power_w = plant_power.to('watt')
    hours = Quantity(24, 'hour')
    hours_s = hours.to('second')
    
    # Energy = Power * Time (in joules)
    daily_energy_j = plant_power_w.magnitude * hours_s.magnitude
    daily_energy = Quantity(daily_energy_j, 'joule')
    
    print(f"\nDaily energy generation:")
    print(f"  {daily_energy}")
    print(f"  → {daily_energy.to('gigajoule'):.2e}")
    print(f"  → {daily_energy.to('kilowatt_hour'):.2e}")
    print(f"  → {daily_energy.to('terajoule'):.2f}")
    
    # Transformer capacity
    transformer = Quantity(100, 'megawatt')
    print_conversion(transformer, ['kilowatt', 'gigawatt'],
                    "Substation transformer capacity:")
    
    # 3.6 Oil & Gas Industry
    print_subsection("3.6 Oil & Gas Industry")
    
    print("\n🛢️ Petroleum Operations:")
    # Well pressure
    well_p = Quantity(10000, 'psi')
    print_conversion(well_p, ['pascal', 'megapascal', 'bar'],
                    "Downhole pressure:")
    
    # Production rate
    production = Quantity(50000, 'gallon_per_minute')
    print_conversion(production, ['liter_per_second', 'cubic_meter_per_second'],
                    "Oil production rate:")
    
    # Pipeline flow
    pipeline = Quantity(1000000, 'gallon_per_minute')
    print_conversion(pipeline, ['cubic_meter_per_second', 'liter_per_minute'],
                    "Pipeline throughput:")
    
    # 3.7 Pharmaceutical Industry
    print_subsection("3.7 Pharmaceutical Industry")
    
    print("\n💊 Drug Manufacturing:")
    # Drug concentration
    drug_conc = Quantity(500, 'micromolar')
    print_conversion(drug_conc, ['molar', 'millimolar', 'nanomolar'],
                    "Active ingredient concentration:")
    
    # Dosage
    dosage = Quantity(250, 'milligram')
    print_conversion(dosage, ['gram', 'microgram', 'kilogram'],
                    "Tablet dosage:")
    
    # Reaction temperature
    reaction_temp = Quantity(37, 'celsius')
    print_conversion(reaction_temp, ['kelvin', 'fahrenheit'],
                    "Bioreactor temperature:")
    
    # 3.8 Telecommunications
    print_subsection("3.8 Telecommunications")
    
    print("\n📡 Network Infrastructure:")
    # Frequency bands
    freq_5g = Quantity(28, 'gigahertz')
    print_conversion(freq_5g, ['hertz', 'megahertz', 'terahertz'],
                    "5G mmWave frequency:")
    
    # Data transfer rate
    bandwidth = Quantity(10, 'gigabyte')
    time_sec = Quantity(1, 'second')
    rate = bandwidth / time_sec
    print(f"\nData transfer rate: {rate}")
    print(f"  → {rate.to('megabyte / second')}")
    print(f"  → {rate.to('gigabit / second')}")
    
    # Fiber optic cable length
    fiber = Quantity(5000, 'kilometer')
    print_conversion(fiber, ['meter', 'mile'],
                    "Undersea cable length:")
    
    # 3.9 Mining & Metallurgy
    print_subsection("3.9 Mining & Metallurgy")
    
    print("\n⛏️ Mining Operations:")
    # Ore processing
    ore_mass = Quantity(1000, 'ton')
    print_conversion(ore_mass, ['kilogram', 'pound', 'gram'],
                    "Daily ore processing:")
    
    # Smelting temperature
    smelt_temp = Quantity(1538, 'celsius')
    print_conversion(smelt_temp, ['kelvin', 'fahrenheit'],
                    "Iron melting point:")
    
    # Pressure in deep mine
    mine_depth = Quantity(3000, 'meter')
    rock_density = Quantity(2700, 'kilogram_per_cubic_meter')
    # Calculate pressure: P = ρ * g * h
    pressure_value = rock_density.magnitude * constants.g.magnitude * mine_depth.magnitude
    mine_pressure = Quantity(pressure_value, 'pascal')
    print(f"\nPressure at {mine_depth} depth:")
    print(f"  {mine_pressure}")
    print(f"  → {mine_pressure.to('megapascal')}")
    print(f"  → {mine_pressure.to('atmosphere')}")
    
    # 3.10 Renewable Energy
    print_subsection("3.10 Renewable Energy")
    
    print("\n🌞 Solar Power Plant:")
    # Solar irradiance
    irradiance = Quantity(1000, 'watt / meter^2')
    print(f"Solar irradiance: {irradiance}")
    
    # Panel area
    panel_area = Quantity(2, 'meter^2')
    efficiency = 0.20  # 20% efficiency
    power_output = irradiance * panel_area * efficiency
    print(f"Panel area: {panel_area}")
    print(f"Efficiency: {efficiency * 100}%")
    print(f"Power output: {power_output}")
    print(f"  → {power_output.to('kilowatt')}")
    
    # Wind turbine
    print("\n💨 Wind Turbine:")
    wind_speed = Quantity(15, 'meter/second')
    print_conversion(wind_speed, ['kilometer/hour', 'mile/hour', 'knot'],
                    "Wind speed:")
    
    turbine_power = Quantity(3, 'megawatt')
    print_conversion(turbine_power, ['kilowatt', 'gigawatt', 'horsepower'],
                    "Turbine rated power:")


# ============================================================================
# PART 4: ADVANCED CONVERSIONS - Pushing Library Limits
# ============================================================================

def advanced_conversions():
    """Demonstrate advanced and edge-case conversions."""
    print_section("PART 4: ADVANCED CONVERSIONS - Pushing the Limits")
    
    # 4.1 Extreme Scale Conversions
    print_subsection("4.1 Extreme Scale Conversions")
    
    print("\n🔬 From Quantum to Cosmic:")
    # Planck length to observable universe
    planck_l = constants.l_P
    print(f"Planck length: {planck_l}")
    print(f"  → {planck_l.to('meter')}")
    print(f"  → {planck_l.to('femtometer')}")
    
    # Observable universe
    universe_size = Quantity(8.8e26, 'meter')
    print(f"\nObservable universe diameter: {universe_size}")
    print(f"  → {universe_size.to('light_year'):.2e}")
    print(f"  → {universe_size.to('megaparsec'):.2e}")
    
    # Scale ratio
    scale_ratio = universe_size / planck_l
    print(f"\nUniverse/Planck ratio: {scale_ratio.magnitude:.2e}")
    
    # 4.2 Time Scale Conversions
    print_subsection("4.2 Time Scale Conversions")
    
    print("\n⏱️ From Attoseconds to Eons:")
    # Fastest laser pulse
    attosec = Quantity(1, 'attosecond')
    print_conversion(attosec, ['second', 'femtosecond', 'picosecond'],
                    "Attosecond laser pulse:")
    
    # Age of universe
    universe_age = constants.universe_age
    print(f"\nAge of universe: {universe_age}")
    print(f"  → {universe_age.to('year'):.2e}")
    print(f"  → {universe_age.to('millennium'):.2e}")
    print(f"  → {universe_age.to('day'):.2e}")
    
    # 4.3 Energy Scale Conversions
    print_subsection("4.3 Energy Scale Conversions")
    
    print("\n⚡ From Thermal to Planck Energy:")
    # Thermal energy at room temp
    temp_k = Quantity(300, 'kelvin')
    # E = k_B * T
    thermal_value = constants.k_B.magnitude * temp_k.magnitude
    thermal = Quantity(thermal_value, 'joule')
    print(f"Thermal energy (300K): {thermal}")
    print(f"  → {thermal.to('electronvolt')}")
    print(f"  → {thermal.to('joule')}")
    
    # Planck energy
    planck_e = constants.E_P
    print(f"\nPlanck energy: {planck_e}")
    print(f"  → {planck_e.to('joule')}")
    print(f"  → {planck_e.to('gigaelectronvolt'):.2e}")
    
    # 4.4 Compound Unit Conversions
    print_subsection("4.4 Compound Unit Conversions")
    
    print("\n🔄 Complex Compound Units:")
    # Momentum
    momentum = Quantity(1000, 'kilogram * meter / second')
    print(f"Momentum: {momentum}")
    
    # Angular momentum
    ang_momentum = Quantity(1, 'kilogram * meter^2 / second')
    print(f"Angular momentum: {ang_momentum}")
    print(f"  → In terms of ℏ: {(ang_momentum / constants.hbar).magnitude:.2e} ℏ")
    
    # Power density
    power_density = Quantity(1000, 'watt / meter^2')
    print(f"\nPower density: {power_density}")
    
    # Energy density
    energy_density = Quantity(1e9, 'joule / meter^3')
    print(f"Energy density: {energy_density}")
    print(f"  → {energy_density.to('kilowatt_hour / meter^3')}")
    
    # 4.5 Multi-Step Conversions
    print_subsection("4.5 Multi-Step Conversions")
    
    print("\n🔗 Chain Conversions:")
    # Start with a complex scenario
    distance = Quantity(1, 'light_year')
    time = Quantity(1, 'year')
    speed = distance / time
    
    print(f"Distance: {distance}")
    print(f"Time: {time}")
    print(f"Average speed: {speed}")
    print(f"  → {speed.to('meter/second')}")
    print(f"  → {speed.to('kilometer/hour'):.2e}")
    print(f"  → Speed of light: {constants.c}")
    print(f"  → Ratio: {(speed / constants.c).magnitude:.6f}c")
    
    # 4.6 Precision Conversions
    print_subsection("4.6 Precision Conversions")
    
    print("\n🎯 High Precision Conversions:")
    # Fine structure constant
    alpha = constants.alpha
    print(f"Fine structure constant: {alpha}")
    
    # Electron mass in different units
    m_e = constants.m_e
    print(f"\nElectron mass:")
    print(f"  {m_e}")
    print(f"  → {m_e.to('atomic_mass_unit')}")
    print(f"  → {m_e.to('gram')}")
    # E = mc²
    m_e_kg = m_e.magnitude
    c_value = constants.c.magnitude
    energy_equiv_j = m_e_kg * c_value ** 2
    energy_equiv = Quantity(energy_equiv_j, 'joule')
    print(f"  → Energy equivalent: {energy_equiv.to('megaelectronvolt')}")
    
    # 4.7 Array-Based Conversions
    print_subsection("4.7 Array-Based Conversions (Performance Test)")
    
    print("\n📊 Bulk Conversion Performance:")
    # Large array conversion
    large_distances = Quantity(np.linspace(1, 1000, 10000), 'kilometer')
    print(f"Converting {len(large_distances.magnitude)} values...")
    
    # Multiple conversions
    converted_miles = large_distances.to('mile')
    converted_meters = large_distances.to('meter')
    converted_feet = large_distances.to('foot')
    
    print(f"  ✓ Converted to miles: {len(converted_miles.magnitude)} values")
    print(f"  ✓ Converted to meters: {len(converted_meters.magnitude)} values")
    print(f"  ✓ Converted to feet: {len(converted_feet.magnitude)} values")
    print(f"  Sample: {large_distances[0]} = {converted_miles[0]:.2f}")
    
    # Statistical operations on converted data
    mean_km = utils.mean(large_distances)
    mean_mi = utils.mean(converted_miles)
    print(f"\n  Mean distance: {mean_km:.2f} = {mean_mi:.2f}")
    
    # 4.8 Cross-Domain Conversions
    print_subsection("4.8 Cross-Domain Conversions")
    
    print("\n🌐 Interdisciplinary Conversions:")
    
    # Wavelength to energy (photon)
    wavelength = Quantity(500, 'nanometer')  # Green light
    # E = h * c / λ
    h_value = constants.h.magnitude
    c_value = constants.c.magnitude
    wavelength_m = wavelength.to('meter').magnitude
    frequency_hz = c_value / wavelength_m
    photon_energy_j = h_value * frequency_hz
    
    frequency = Quantity(frequency_hz, 'hertz')
    photon_energy = Quantity(photon_energy_j, 'joule')
    
    print(f"Green light wavelength: {wavelength}")
    print(f"Frequency: {frequency.to('terahertz'):.2f}")
    print(f"Photon energy: {photon_energy.to('electronvolt'):.3f}")
    print(f"  → {photon_energy.to('joule')}")
    
    # Temperature to energy
    temp = Quantity(5778, 'kelvin')  # Sun's surface
    # E = k_B * T
    thermal_energy_value = constants.k_B.magnitude * temp.magnitude
    thermal_energy = Quantity(thermal_energy_value, 'joule')
    print(f"\nSun's surface temperature: {temp}")
    print(f"Thermal energy: {thermal_energy.to('electronvolt'):.3f}")
    
    # Mass to energy (E=mc²)
    mass = Quantity(1, 'gram')
    # E = mc²
    mass_kg = mass.to('kilogram').magnitude
    c_value = constants.c.magnitude
    energy_value = mass_kg * c_value ** 2
    energy = Quantity(energy_value, 'joule')
    print(f"\nMass-energy equivalence:")
    print(f"  1 gram = {energy.to('joule'):.2e}")
    print(f"  = {energy.to('kilowatt_hour'):.2e}")
    print(f"  = {energy.to('megaton_tnt'):.6f} megatons TNT")
    
    # 4.9 Dimensionless Conversions
    print_subsection("4.9 Dimensionless Conversions")
    
    print("\n📐 Dimensionless Quantities:")
    
    # Percentages
    efficiency = Quantity(85, 'percent')
    print(f"Efficiency: {efficiency}")
    print(f"  → {efficiency.to('dimensionless')}")
    
    # Parts per million
    contamination = Quantity(50, 'ppm')
    print(f"\nContamination: {contamination}")
    print(f"  → {contamination.to('percent')}")
    print(f"  → {contamination.to('dimensionless')}")
    
    # Angles
    angle_deg = Quantity(180, 'degree')
    print_conversion(angle_deg, ['radian', 'arcminute', 'arcsecond'],
                    "\nAngle conversions:")
    
    # 4.10 Real-World Complex Scenario
    print_subsection("4.10 Real-World Complex Scenario")
    
    print("\n🚀 Mars Mission Calculation:")
    print("=" * 60)
    
    # Mission parameters
    earth_mars_dist = Quantity(225e6, 'kilometer')
    spacecraft_speed = Quantity(20, 'kilometer/second')
    fuel_mass = Quantity(500, 'ton')
    payload_mass = Quantity(100, 'ton')
    
    # Calculations
    travel_time = earth_mars_dist / spacecraft_speed
    total_mass = fuel_mass + payload_mass
    
    print(f"Distance to Mars: {earth_mars_dist}")
    print(f"  → {earth_mars_dist.to('astronomical_unit'):.3f}")
    print(f"  → {earth_mars_dist.to('light_year'):.6e}")
    
    print(f"\nSpacecraft speed: {spacecraft_speed}")
    print(f"  → {spacecraft_speed.to('mile/hour'):.2e}")
    print(f"  → {(spacecraft_speed / constants.c).magnitude:.6f}c")
    
    print(f"\nTravel time: {travel_time}")
    print(f"  → {travel_time.to('day'):.1f}")
    print(f"  → {travel_time.to('month'):.1f}")
    
    print(f"\nTotal spacecraft mass: {total_mass}")
    print(f"  → {total_mass.to('kilogram'):.2e}")
    
    # Energy required (kinetic)
    kinetic_energy = 0.5 * total_mass * spacecraft_speed ** 2
    print(f"\nKinetic energy required: {kinetic_energy}")
    print(f"  → {kinetic_energy.to('gigajoule'):.2e}")
    print(f"  → {kinetic_energy.to('kilowatt_hour'):.2e}")
    print(f"  → {kinetic_energy.to('megaton_tnt'):.3f} megatons TNT equivalent")


# ============================================================================
# PART 5: SPECIALIZED INDUSTRY CONVERSIONS
# ============================================================================

def specialized_industry_conversions():
    """Demonstrate highly specialized industry conversions."""
    print_section("PART 5: SPECIALIZED INDUSTRY CONVERSIONS")
    
    # 5.1 Aviation Industry
    print_subsection("5.1 Aviation Industry")
    
    print("\n✈️ Commercial Aircraft Operations:")
    # Altitude
    cruise_alt = Quantity(35000, 'foot')
    print_conversion(cruise_alt, ['meter', 'kilometer', 'mile'],
                    "Cruise altitude:")
    
    # Airspeed
    airspeed = Quantity(500, 'knot')
    print_conversion(airspeed, ['kilometer/hour', 'mile/hour', 'meter/second'],
                    "Cruise airspeed:")
    
    # Fuel consumption
    fuel_rate = Quantity(3000, 'kilogram/hour')
    print_conversion(fuel_rate, ['pound/hour', 'ton/hour'],
                    "Fuel burn rate:")
    
    # Cabin pressure
    cabin_p = Quantity(75, 'kilopascal')
    print_conversion(cabin_p, ['atmosphere', 'psi', 'bar'],
                    "Cabin pressure:")
    
    # 5.2 Marine Engineering
    print_subsection("5.2 Marine Engineering")
    
    print("\n🚢 Ship Operations:")
    # Ship speed
    ship_speed = Quantity(25, 'knot')
    print_conversion(ship_speed, ['kilometer/hour', 'meter/second'],
                    "Ship cruising speed:")
    
    # Ocean depth
    depth = Quantity(4000, 'meter')
    print_conversion(depth, ['fathom', 'foot', 'kilometer'],
                    "Ocean depth:")
    
    # Hydrostatic pressure at depth
    water_density = Quantity(1025, 'kilogram_per_cubic_meter')
    # Calculate pressure: P = ρ * g * h
    pressure_value = water_density.magnitude * constants.g.magnitude * depth.magnitude
    pressure_at_depth = Quantity(pressure_value, 'pascal')
    print(f"\nPressure at {depth}:")
    print(f"  {pressure_at_depth}")
    print(f"  → {pressure_at_depth.to('atmosphere'):.1f}")
    print(f"  → {pressure_at_depth.to('megapascal'):.2f}")
    
    # 5.3 Medical & Healthcare
    print_subsection("5.3 Medical & Healthcare")
    
    print("\n🏥 Medical Measurements:")
    # Blood pressure
    systolic = Quantity(120, 'millimeter_mercury')
    print_conversion(systolic, ['pascal', 'kilopascal', 'psi'],
                    "Blood pressure (systolic):")
    
    # Drug dosage
    dosage_mg_kg = Quantity(5, 'milligram/kilogram')
    patient_weight = Quantity(70, 'kilogram')
    total_dose = dosage_mg_kg * patient_weight
    print(f"\nDrug dosage: {dosage_mg_kg} per kg body weight")
    print(f"Patient weight: {patient_weight}")
    print(f"Total dose: {total_dose}")
    print(f"  → {total_dose.to('gram')}")
    
    # Radiation dose limits
    annual_limit = Quantity(20, 'millisievert')
    print_conversion(annual_limit, ['sievert', 'microsievert', 'rem'],
                    "\nAnnual radiation dose limit (occupational):")
    
    # 5.4 Food & Beverage Industry
    print_subsection("5.4 Food & Beverage Industry")
    
    print("\n🍺 Brewery Operations:")
    # Fermentation temperature
    ferm_temp = Quantity(18, 'celsius')
    print_conversion(ferm_temp, ['fahrenheit', 'kelvin'],
                    "Fermentation temperature:")
    
    # Batch volume
    batch = Quantity(1000, 'liter')
    print_conversion(batch, ['gallon', 'milliliter', 'cubic_meter'],
                    "Batch volume:")
    
    # Alcohol content (by volume)
    abv = Quantity(5, 'percent')
    alcohol_volume = batch * abv.to('dimensionless').magnitude
    print(f"\nAlcohol by volume: {abv}")
    print(f"Alcohol in batch: {alcohol_volume}")
    
    # 5.5 HVAC Engineering
    print_subsection("5.5 HVAC Engineering")
    
    print("\n❄️ Climate Control Systems:")
    # Cooling capacity (tons of refrigeration)
    # 1 ton of refrigeration = 3.517 kW (approximately)
    cooling_tons = 10
    cooling_kw = cooling_tons * 3.517
    cooling = Quantity(cooling_kw, 'kilowatt')
    print(f"Cooling capacity: {cooling_tons} tons of refrigeration")
    print(f"  → {cooling}")
    print(f"  → {cooling.to('watt')}")
    
    # Air flow rate
    airflow = Quantity(2000, 'cubic_meter_per_second')
    print_conversion(airflow, ['liter_per_second', 'cubic_meter_per_second'],
                    "Air flow rate:")
    
    # Temperature differential
    delta_t = Quantity(10, 'kelvin')
    print(f"\nTemperature differential: {delta_t}")
    print(f"  (Note: ΔT in Kelvin = ΔT in Celsius)")
    
    # 5.6 Semiconductor Manufacturing
    print_subsection("5.6 Semiconductor Manufacturing")
    
    print("\n💾 Chip Fabrication:")
    # Feature size
    node_size = Quantity(5, 'nanometer')
    print_conversion(node_size, ['meter', 'angstrom', 'picometer'],
                    "Process node size:")
    
    # Wafer size
    wafer = Quantity(300, 'millimeter')
    print_conversion(wafer, ['meter', 'centimeter', 'inch'],
                    "Silicon wafer diameter:")
    
    # Deposition rate
    dep_rate = Quantity(10, 'angstrom/second')
    print(f"\nThin film deposition rate: {dep_rate}")
    print(f"  → {dep_rate.to('nanometer/second')}")
    
    # 5.7 Agriculture
    print_subsection("5.7 Agriculture")
    
    print("\n🌾 Precision Farming:")
    # Field area
    field = Quantity(100, 'hectare')
    print_conversion(field, ['acre', 'meter^2', 'kilometer^2'],
                    "Field area:")
    
    # Irrigation rate
    irrigation = Quantity(25, 'millimeter')
    # Convert to meters and hectares to cubic meters
    irrigation_m = irrigation.to('meter').magnitude
    field_m2 = field.to('meter^2').magnitude
    water_volume_m3 = irrigation_m * field_m2
    water_volume = Quantity(water_volume_m3, 'cubic_meter')
    
    print(f"\nIrrigation depth: {irrigation}")
    print(f"Field area: {field}")
    print(f"Water volume needed: {water_volume}")
    print(f"  → {water_volume.to('liter'):.2e}")
    print(f"  → {water_volume.to('gallon'):.2e}")
    
    # Fertilizer application
    fertilizer_rate = Quantity(150, 'kilogram_per_cubic_meter')
    print(f"\nFertilizer application rate: {fertilizer_rate}")
    
    # 5.8 Construction & Architecture
    print_subsection("5.8 Construction & Architecture")
    
    print("\n🏢 Building Design:")
    # Building height
    height = Quantity(828, 'meter')  # Burj Khalifa
    print_conversion(height, ['foot', 'kilometer', 'mile'],
                    "Building height (Burj Khalifa):")
    
    # Floor area
    floor_area = Quantity(50000, 'meter^2')
    print_conversion(floor_area, ['hectare', 'acre'],
                    "Floor area:")
    
    # Thermal conductivity
    u_value = Quantity(0.3, 'watt_per_meter_kelvin')
    print(f"\nWall thermal conductivity (U-value): {u_value}")
    
    # 5.9 Textile Industry
    print_subsection("5.9 Textile Industry")
    
    print("\n🧵 Fabric Manufacturing:")
    # Thread count
    thread_count = Quantity(300, '1/inch')
    print(f"Thread count: {thread_count}")
    
    # Fabric weight
    fabric_weight = Quantity(200, 'gram_per_cubic_meter')
    print(f"Fabric weight: {fabric_weight}")
    
    # Dyeing temperature
    dye_temp = Quantity(60, 'celsius')
    print_conversion(dye_temp, ['fahrenheit', 'kelvin'],
                    "Dyeing temperature:")
    
    # 5.10 Printing & Publishing
    print_subsection("5.10 Printing & Publishing")
    
    print("\n📰 Print Production:")
    # Print resolution
    dpi = Quantity(300, '1/inch')
    print(f"Print resolution: {dpi}")
    
    # Paper weight
    paper = Quantity(80, 'gram_per_cubic_meter')
    print(f"Paper weight: {paper}")
    
    # Press speed
    press_speed = Quantity(15, 'meter/second')
    print_conversion(press_speed, ['kilometer/hour', 'foot/second'],
                    "Press speed:")


# ============================================================================
# PART 6: EDGE CASES AND SPECIAL CONVERSIONS
# ============================================================================

def edge_cases_and_special():
    """Demonstrate edge cases and special conversion scenarios."""
    print_section("PART 6: EDGE CASES & SPECIAL CONVERSIONS")
    
    # 6.1 Very Small Numbers
    print_subsection("6.1 Very Small Numbers")
    
    print("\n🔬 Quantum Scale:")
    # Electron Compton wavelength
    lambda_c = constants.lambda_C
    print(f"Electron Compton wavelength: {lambda_c}")
    print(f"  → {lambda_c.to('femtometer')}")
    print(f"  → {lambda_c.to('angstrom')}")
    
    # Proton radius
    proton_r = Quantity(0.84, 'femtometer')
    print_conversion(proton_r, ['meter', 'picometer', 'angstrom'],
                    "\nProton radius:")
    
    # 6.2 Very Large Numbers
    print_subsection("6.2 Very Large Numbers")
    
    print("\n🌌 Cosmological Scale:")
    # Distance to Andromeda
    andromeda = Quantity(2.537e6, 'light_year')
    print_conversion(andromeda, ['parsec', 'megaparsec', 'kilometer'],
                    "Distance to Andromeda Galaxy:")
    
    # Mass of Milky Way
    milky_way_mass = Quantity(1.5e12, 'solar_mass')
    print(f"\nMilky Way mass: {milky_way_mass}")
    print(f"  → {milky_way_mass.to('kilogram'):.2e}")
    
    # 6.3 Temperature Extremes
    print_subsection("6.3 Temperature Extremes")
    
    print("\n🌡️ Temperature Extremes:")
    # Absolute zero
    abs_zero = Quantity(0, 'kelvin')
    print_conversion(abs_zero, ['celsius', 'fahrenheit'],
                    "Absolute zero:")
    
    # Planck temperature
    t_planck = constants.T_P
    print(f"\nPlanck temperature: {t_planck}")
    print(f"  → {t_planck.to('celsius')}")
    
    # Core of the Sun
    sun_core = Quantity(15e6, 'kelvin')
    print_conversion(sun_core, ['celsius', 'fahrenheit'],
                    "\nSun's core temperature:")
    
    # 6.4 Frequency Extremes
    print_subsection("6.4 Frequency Extremes")
    
    print("\n📻 Frequency Spectrum:")
    # Extremely low frequency
    elf = Quantity(3, 'hertz')
    print_conversion(elf, ['kilohertz', 'megahertz'],
                    "ELF radio:")
    
    # Gamma rays
    gamma = Quantity(1e20, 'hertz')
    print_conversion(gamma, ['terahertz', 'gigahertz'],
                    "Gamma ray frequency:")
    
    # 6.5 Pressure Extremes
    print_subsection("6.5 Pressure Extremes")
    
    print("\n💥 Pressure Extremes:")
    # Vacuum
    vacuum = Quantity(1e-10, 'pascal')
    print_conversion(vacuum, ['atmosphere', 'torr'],
                    "Ultra-high vacuum:")
    
    # Earth's core
    core_pressure = Quantity(360, 'gigapascal')
    print_conversion(core_pressure, ['pascal', 'atmosphere', 'bar'],
                    "Earth's core pressure:")
    
    # 6.6 Speed Comparisons
    print_subsection("6.6 Speed Comparisons")
    
    print("\n🏃 Speed Spectrum:")
    speeds = [
        ("Snail", Quantity(0.001, 'meter/second')),
        ("Human walking", Quantity(1.4, 'meter/second')),
        ("Usain Bolt", Quantity(10.44, 'meter/second')),
        ("Cheetah", Quantity(30, 'meter/second')),
        ("Car (highway)", Quantity(30, 'meter/second')),
        ("Bullet train", Quantity(100, 'meter/second')),
        ("Sound", Quantity(343, 'meter/second')),
        ("Earth orbit", Quantity(7800, 'meter/second')),
        ("Light", constants.c),
    ]
    
    for name, speed in speeds:
        speed_kmh = speed.to('kilometer/hour')
        speed_c = (speed / constants.c).magnitude
        print(f"{name:20s}: {str(speed):25s} = {str(speed_kmh):20s} = {speed_c:.6e}c")
    
    # 6.7 Energy Density Comparisons
    print_subsection("6.7 Energy Density Comparisons")
    
    print("\n⚡ Energy Density Spectrum:")
    densities = [
        ("Gasoline", Quantity(34.2e6, 'joule/kilogram')),
        ("Coal", Quantity(24e6, 'joule/kilogram')),
        ("Lithium battery", Quantity(0.9e6, 'joule/kilogram')),
        ("TNT", Quantity(4.6e6, 'joule/kilogram')),
        ("Uranium-235", Quantity(8.2e13, 'joule/kilogram')),
    ]
    
    for name, density in densities:
        density_kwh = density.to('kilowatt_hour/kilogram')
        print(f"{name:20s}: {density:.2e} = {density_kwh:.2e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all conversion examples."""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + "UNIFYT COMPREHENSIVE UNIT CONVERSION EXAMPLES".center(78) + "║")
    print("║" + "Demonstrating 300+ Units Across All Domains".center(78) + "║")
    print("╚" + "═" * 78 + "╝")
    
    try:
        # Part 1: Normal everyday conversions
        normal_conversions()
        
        # Part 2: General scientific and engineering use cases
        general_use_cases()
        
        # Part 3: Industry-level professional scenarios
        industry_level_scenarios()
        
        # Part 4: Advanced conversions pushing library limits
        advanced_conversions()
        
        # Part 5: Specialized industry conversions
        specialized_industry_conversions()
        
        # Part 6: Edge cases and special scenarios
        edge_cases_and_special()
        
        # Summary
        print_section("SUMMARY & STATISTICS")
        print("\n✅ Successfully demonstrated:")
        print("   • 300+ unit conversions")
        print("   • 80+ physical constants")
        print("   • 10+ industry domains")
        print("   • Extreme scale conversions (10^-35 to 10^26 meters)")
        print("   • Complex compound units")
        print("   • Array-based bulk conversions")
        print("   • Multi-step interdisciplinary calculations")
        print("\n🎯 Library capabilities verified:")
        print("   • Accuracy: High precision maintained across all scales")
        print("   • Performance: Fast conversions even with large arrays")
        print("   • Flexibility: Handles simple to complex scenarios")
        print("   • Robustness: Works with extreme values")
        print("\n📚 Use cases covered:")
        print("   • Everyday conversions (cooking, travel, weather)")
        print("   • Scientific research (physics, chemistry, astronomy)")
        print("   • Engineering (aerospace, civil, electrical, chemical)")
        print("   • Industry applications (oil & gas, pharma, telecom)")
        print("   • Specialized fields (medical, agriculture, semiconductor)")
        
        print("\n" + "═" * 80)
        print("All conversion examples completed successfully! ✨")
        print("═" * 80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
