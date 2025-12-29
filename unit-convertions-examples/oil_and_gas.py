"""
Oil & Gas Industry Unit Conversions
===================================

Real-world unit conversions for petroleum engineering, drilling operations,
production, refining, and pipeline transportation.

Author: Unifyt Team
Industry: Oil & Gas
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
# 1. DRILLING OPERATIONS
# ============================================================================

def drilling_operations():
    """Drilling operation conversions."""
    print_header("1. DRILLING OPERATIONS")
    
    # Well depth
    print("Well Depth:")
    well_depth = Quantity(15000, 'foot')
    print_result("Total depth", well_depth,
                ['meter', 'kilometer', 'mile'])
    
    # Drilling rate (Rate of Penetration - ROP)
    print("\nRate of Penetration:")
    rop = Quantity(50, 'foot/hour')
    rop_ms = Quantity(rop.magnitude * 0.3048 / 3600, 'meter/second')
    print(f"ROP: {rop}")
    print(f"  → {rop_ms}")
    print(f"  → {Quantity(rop.magnitude * 0.3048, 'meter/hour')}")
    
    # Mud weight (drilling fluid density)
    print("\nMud Weight:")
    mud_weight = Quantity(12.5, 'pound')  # ppg (pounds per gallon)
    # Convert to kg/m³: ppg * 119.826
    mud_density_value = mud_weight.magnitude * 119.826
    mud_density = Quantity(mud_density_value, 'kilogram/meter^3')
    print(f"Mud weight: {mud_weight.magnitude} ppg")
    print_result("Mud density", mud_density,
                ['kilogram/meter^3'])
    
    # Downhole pressure
    print("\nDownhole Pressure:")
    bottom_hole_pressure = Quantity(12000, 'psi')
    print_result("Bottom hole pressure", bottom_hole_pressure,
                ['pascal', 'megapascal', 'bar', 'atmosphere'])
    
    # Torque
    print("\nDrilling Torque:")
    torque_value = Quantity(25000, 'pound * foot')
    # Convert to N⋅m
    torque_nm = torque_value.magnitude * 1.35582
    torque = Quantity(torque_nm, 'newton * meter')
    print(f"Torque: {torque_value.magnitude} lb-ft")
    print(f"  → {torque}")


# ============================================================================
# 2. PRODUCTION RATES
# ============================================================================

def production_rates():
    """Oil and gas production rate conversions."""
    print_header("2. PRODUCTION RATES")
    
    # Oil production
    print("Oil Production:")
    oil_rate = Quantity(5000, 'gallon/minute')  # barrels per day
    print_result("Production rate", oil_rate,
                ['liter/second', 'cubic_meter/second'])
    
    # Convert to barrels per day (1 barrel = 42 gallons)
    bpd = oil_rate.magnitude * 60 * 24 / 42
    print(f"  → {bpd:.0f} barrels/day")
    
    # Gas production
    print("\nGas Production:")
    # Million standard cubic feet per day (MMSCFD)
    gas_rate_mmscfd = 50  # MMSCFD
    gas_rate_m3_day = gas_rate_mmscfd * 28316.8  # Convert to m³/day
    gas_rate = Quantity(gas_rate_m3_day / 86400, 'cubic_meter/second')
    print(f"Gas rate: {gas_rate_mmscfd} MMSCFD")
    print_result("Gas rate", gas_rate,
                ['cubic_meter/second', 'liter/second'])
    
    # Water cut
    print("\nWater Cut:")
    water_cut = 35  # percentage
    print(f"Water cut: {water_cut}%")
    
    # Gas-Oil Ratio (GOR)
    print("\nGas-Oil Ratio:")
    gor = 1000  # SCF/STB (standard cubic feet per stock tank barrel)
    print(f"GOR: {gor} SCF/STB")


# ============================================================================
# 3. RESERVOIR PROPERTIES
# ============================================================================

def reservoir_properties():
    """Reservoir property conversions."""
    print_header("3. RESERVOIR PROPERTIES")
    
    # Reservoir pressure
    print("Reservoir Pressure:")
    reservoir_pressure = Quantity(5000, 'psi')
    print_result("Initial pressure", reservoir_pressure,
                ['pascal', 'megapascal', 'bar'])
    
    # Reservoir temperature
    print("\nReservoir Temperature:")
    reservoir_temp = Quantity(180, 'fahrenheit')
    print_result("Temperature", reservoir_temp,
                ['celsius', 'kelvin'])
    
    # Permeability (millidarcies)
    print("\nPermeability:")
    permeability = 250  # millidarcies
    print(f"Permeability: {permeability} mD")
    # 1 darcy = 9.869233e-13 m²
    perm_m2 = permeability * 1e-3 * 9.869233e-13
    print(f"  → {perm_m2:.2e} m²")
    
    # Porosity
    print("\nPorosity:")
    porosity = 0.22
    print(f"Porosity: {porosity} ({porosity * 100}%)")
    
    # Oil viscosity
    print("\nOil Viscosity:")
    viscosity = Quantity(5, 'centipoise')
    print_result("Viscosity", viscosity,
                ['pascal_second', 'poise'])


# ============================================================================
# 4. PIPELINE TRANSPORTATION
# ============================================================================

def pipeline_transportation():
    """Pipeline transportation conversions."""
    print_header("4. PIPELINE TRANSPORTATION")
    
    # Pipeline diameter
    print("Pipeline Diameter:")
    pipe_diameter = Quantity(36, 'inch')
    print_result("Diameter", pipe_diameter,
                ['meter', 'centimeter', 'millimeter'])
    
    # Flow rate
    print("\nFlow Rate:")
    flow_rate = Quantity(500000, 'gallon/minute')
    print_result("Flow rate", flow_rate,
                ['cubic_meter/second', 'liter/second'])
    
    # Convert to barrels per day
    bpd = flow_rate.magnitude * 60 * 24 / 42
    print(f"  → {bpd:.0f} barrels/day")
    
    # Pipeline pressure
    print("\nPipeline Pressure:")
    pipeline_pressure = Quantity(1200, 'psi')
    print_result("Operating pressure", pipeline_pressure,
                ['pascal', 'megapascal', 'bar'])
    
    # Flow velocity
    print("\nFlow Velocity:")
    flow_velocity = Quantity(2.5, 'meter/second')
    print_result("Velocity", flow_velocity,
                ['kilometer/hour', 'foot/second'])
    
    # Pipeline length
    print("\nPipeline Length:")
    pipeline_length = Quantity(500, 'kilometer')
    print_result("Length", pipeline_length,
                ['meter', 'mile'])


# ============================================================================
# 5. REFINING OPERATIONS
# ============================================================================

def refining_operations():
    """Refinery operation conversions."""
    print_header("5. REFINING OPERATIONS")
    
    # Refinery capacity
    print("Refinery Capacity:")
    capacity_bpd = 250000  # barrels per day
    capacity_m3_day = capacity_bpd * 0.158987  # Convert to m³/day
    capacity = Quantity(capacity_m3_day / 86400, 'cubic_meter/second')
    print(f"Capacity: {capacity_bpd} barrels/day")
    print_result("Capacity", capacity,
                ['cubic_meter/second', 'liter/second'])
    
    # Distillation temperature
    print("\nDistillation Temperatures:")
    light_naphtha = Quantity(150, 'celsius')
    print_result("Light naphtha", light_naphtha,
                ['fahrenheit', 'kelvin'])
    
    heavy_gas_oil = Quantity(370, 'celsius')
    print_result("\nHeavy gas oil", heavy_gas_oil,
                ['fahrenheit', 'kelvin'])
    
    # Cracking pressure
    print("\nCatalytic Cracking Pressure:")
    cracking_pressure = Quantity(2.5, 'bar')
    print_result("Pressure", cracking_pressure,
                ['pascal', 'psi', 'atmosphere'])
    
    # API gravity (oil density measure)
    print("\nAPI Gravity:")
    api_gravity = 35  # degrees API
    # Specific gravity = 141.5 / (API + 131.5)
    specific_gravity = 141.5 / (api_gravity + 131.5)
    density_value = specific_gravity * 1000  # kg/m³
    density = Quantity(density_value, 'kilogram/meter^3')
    print(f"API gravity: {api_gravity}° API")
    print(f"Specific gravity: {specific_gravity:.4f}")
    print_result("Density", density,
                ['kilogram/meter^3'])


# ============================================================================
# 6. STORAGE AND HANDLING
# ============================================================================

def storage_handling():
    """Storage and handling conversions."""
    print_header("6. STORAGE AND HANDLING")
    
    # Storage tank capacity
    print("Storage Tank Capacity:")
    tank_capacity_barrels = 500000  # barrels
    tank_capacity_m3 = tank_capacity_barrels * 0.158987
    tank_capacity = Quantity(tank_capacity_m3, 'cubic_meter')
    print(f"Capacity: {tank_capacity_barrels} barrels")
    print_result("Capacity", tank_capacity,
                ['cubic_meter', 'liter', 'gallon'])
    
    # Tank dimensions
    print("\nTank Dimensions:")
    tank_diameter = Quantity(80, 'meter')
    tank_height = Quantity(20, 'meter')
    print(f"Diameter: {tank_diameter}")
    print(f"Height: {tank_height}")
    
    # Vapor pressure
    print("\nVapor Pressure:")
    vapor_pressure = Quantity(14.7, 'psi')
    print_result("Reid vapor pressure", vapor_pressure,
                ['pascal', 'kilopascal', 'bar'])
    
    # Loading rate
    print("\nLoading Rate:")
    loading_rate = Quantity(10000, 'gallon/minute')
    print_result("Loading rate", loading_rate,
                ['cubic_meter/second', 'liter/second'])


# ============================================================================
# 7. WELL TESTING
# ============================================================================

def well_testing():
    """Well testing conversions."""
    print_header("7. WELL TESTING")
    
    # Flow test rate
    print("Flow Test Rate:")
    test_rate_bpd = 3000  # barrels per day
    test_rate_m3_day = test_rate_bpd * 0.158987
    test_rate = Quantity(test_rate_m3_day / 86400, 'cubic_meter/second')
    print(f"Test rate: {test_rate_bpd} barrels/day")
    print_result("Test rate", test_rate,
                ['cubic_meter/second', 'liter/second'])
    
    # Flowing pressure
    print("\nFlowing Pressure:")
    flowing_pressure = Quantity(3500, 'psi')
    print_result("Flowing bottom hole pressure", flowing_pressure,
                ['pascal', 'megapascal', 'bar'])
    
    # Static pressure
    print("\nStatic Pressure:")
    static_pressure = Quantity(4200, 'psi')
    print_result("Static bottom hole pressure", static_pressure,
                ['pascal', 'megapascal', 'bar'])
    
    # Productivity index
    print("\nProductivity Index:")
    pi = 5.0  # barrels per day per psi
    print(f"PI: {pi} bbl/day/psi")
    
    # Skin factor
    print("\nSkin Factor:")
    skin = -2.5  # dimensionless
    print(f"Skin: {skin} (dimensionless)")


# ============================================================================
# 8. ENHANCED OIL RECOVERY (EOR)
# ============================================================================

def enhanced_oil_recovery():
    """Enhanced oil recovery conversions."""
    print_header("8. ENHANCED OIL RECOVERY (EOR)")
    
    # Steam injection
    print("Steam Injection:")
    steam_rate = Quantity(5000, 'gallon/minute')  # Cold water equivalent
    print_result("Steam injection rate", steam_rate,
                ['cubic_meter/second', 'liter/second'])
    
    # Steam quality
    print("\nSteam Quality:")
    steam_quality = 0.80  # 80% quality
    print(f"Steam quality: {steam_quality * 100}%")
    
    # Injection pressure
    print("\nInjection Pressure:")
    injection_pressure = Quantity(2500, 'psi')
    print_result("Injection pressure", injection_pressure,
                ['pascal', 'megapascal', 'bar'])
    
    # CO2 injection
    print("\nCO2 Injection:")
    co2_rate_mmscfd = 20  # Million standard cubic feet per day
    co2_rate_m3_day = co2_rate_mmscfd * 28316.8
    co2_rate = Quantity(co2_rate_m3_day / 86400, 'cubic_meter/second')
    print(f"CO2 injection: {co2_rate_mmscfd} MMSCFD")
    print_result("CO2 rate", co2_rate,
                ['cubic_meter/second'])
    
    # Polymer concentration
    print("\nPolymer Concentration:")
    polymer_conc = 1000  # ppm (parts per million)
    print(f"Polymer concentration: {polymer_conc} ppm")
    polymer_conc_pct = polymer_conc / 10000
    print(f"  → {polymer_conc_pct}%")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all oil & gas conversion examples."""
    print("\n" + "=" * 70)
    print("OIL & GAS INDUSTRY UNIT CONVERSIONS")
    print("Real-world conversions for petroleum engineering and operations")
    print("=" * 70)
    
    drilling_operations()
    production_rates()
    reservoir_properties()
    pipeline_transportation()
    refining_operations()
    storage_handling()
    well_testing()
    enhanced_oil_recovery()
    
    print("\n" + "=" * 70)
    print("All oil & gas conversions completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
