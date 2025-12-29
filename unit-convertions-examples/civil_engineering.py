"""
Civil Engineering Unit Conversions
==================================

Real-world unit conversions for structural design, construction,
geotechnical engineering, and infrastructure projects.

Author: Unifyt Team
Industry: Civil Engineering
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
# 1. STRUCTURAL LOADS
# ============================================================================

def structural_loads():
    """Structural load calculations."""
    print_header("1. STRUCTURAL LOADS")
    
    # Dead load
    print("Dead Load (Self-weight):")
    dead_load = Quantity(500, 'kilogram/meter^2')
    print(f"Dead load: {dead_load}")
    # Note: pound/foot^2 not directly supported, calculate manually if needed
    
    # Live load
    print("\nLive Load (Occupancy):")
    live_load = Quantity(250, 'kilogram/meter^2')
    print(f"Live load: {live_load}")
    
    # Wind load
    print("\nWind Load:")
    wind_pressure = Quantity(1.5, 'kilopascal')
    print_result("Wind pressure", wind_pressure,
                ['pascal', 'psi', 'bar'])
    
    # Snow load
    print("\nSnow Load:")
    snow_load = Quantity(150, 'kilogram/meter^2')
    print(f"Snow load: {snow_load}")
    
    # Point load
    print("\nPoint Load:")
    point_load_mass = Quantity(5000, 'kilogram')
    # Convert to force
    point_load_force = point_load_mass.magnitude * constants.g.magnitude
    point_load = Quantity(point_load_force, 'newton')
    print_result("Point load", point_load,
                ['kilonewton', 'pound_force'])


# ============================================================================
# 2. CONCRETE PROPERTIES
# ============================================================================

def concrete_properties():
    """Concrete material properties."""
    print_header("2. CONCRETE PROPERTIES")
    
    # Compressive strength
    print("Compressive Strength:")
    concrete_strength = Quantity(30, 'megapascal')
    print_result("f'c (28-day)", concrete_strength,
                ['pascal', 'psi', 'kilopascal'])
    
    # Tensile strength
    print("\nTensile Strength:")
    tensile_strength = Quantity(3, 'megapascal')
    print_result("Tensile strength", tensile_strength,
                ['pascal', 'psi'])
    
    # Modulus of elasticity
    print("\nModulus of Elasticity:")
    elastic_modulus = Quantity(25000, 'megapascal')
    print_result("E", elastic_modulus,
                ['pascal', 'gigapascal', 'psi'])
    
    # Density
    print("\nConcrete Density:")
    concrete_density = Quantity(2400, 'kilogram/meter^3')
    print(f"Density: {concrete_density}")
    
    # Slump
    print("\nConcrete Slump:")
    slump = Quantity(100, 'millimeter')
    print_result("Slump", slump,
                ['meter', 'centimeter', 'inch'])


# ============================================================================
# 3. STEEL PROPERTIES
# ============================================================================

def steel_properties():
    """Steel material properties."""
    print_header("3. STEEL PROPERTIES")
    
    # Yield strength
    print("Yield Strength:")
    yield_strength = Quantity(250, 'megapascal')
    print_result("fy (Grade 50)", yield_strength,
                ['pascal', 'psi', 'kilopascal'])
    
    # Ultimate strength
    print("\nUltimate Tensile Strength:")
    ultimate_strength = Quantity(400, 'megapascal')
    print_result("fu", ultimate_strength,
                ['pascal', 'psi'])
    
    # Modulus of elasticity
    print("\nModulus of Elasticity:")
    steel_modulus = Quantity(200000, 'megapascal')
    print_result("E", steel_modulus,
                ['pascal', 'gigapascal', 'psi'])
    
    # Density
    print("\nSteel Density:")
    steel_density = Quantity(7850, 'kilogram/meter^3')
    print(f"Density: {steel_density}")
    
    # Section properties
    print("\nSteel Section (W24x76):")
    section_area = Quantity(22400, 'millimeter^2')
    print(f"Area: {section_area}")
    # Note: Area conversions limited to supported units


# ============================================================================
# 4. FOUNDATION DESIGN
# ============================================================================

def foundation_design():
    """Foundation design calculations."""
    print_header("4. FOUNDATION DESIGN")
    
    # Bearing capacity
    print("Soil Bearing Capacity:")
    bearing_capacity = Quantity(200, 'kilopascal')
    print_result("Allowable bearing", bearing_capacity,
                ['pascal', 'megapascal', 'psi'])
    
    # Settlement
    print("\nSettlement:")
    settlement = Quantity(25, 'millimeter')
    print_result("Total settlement", settlement,
                ['meter', 'centimeter', 'inch'])
    
    # Pile capacity
    print("\nPile Capacity:")
    pile_capacity_mass = Quantity(150, 'ton')
    # Convert to force
    pile_capacity_force = pile_capacity_mass.magnitude * 1000 * constants.g.magnitude
    pile_capacity = Quantity(pile_capacity_force, 'newton')
    print_result("Pile capacity", pile_capacity,
                ['kilonewton', 'meganewton', 'pound_force'])
    
    # Pile length
    print("\nPile Length:")
    pile_length = Quantity(25, 'meter')
    print_result("Length", pile_length,
                ['meter', 'foot'])
    
    # Pile diameter
    print("\nPile Diameter:")
    pile_diameter = Quantity(600, 'millimeter')
    print_result("Diameter", pile_diameter,
                ['meter', 'centimeter', 'inch'])


# ============================================================================
# 5. EARTHWORK AND EXCAVATION
# ============================================================================

def earthwork_excavation():
    """Earthwork and excavation calculations."""
    print_header("5. EARTHWORK AND EXCAVATION")
    
    # Excavation volume
    print("Excavation Volume:")
    excavation_volume = Quantity(5000, 'cubic_meter')
    print_result("Volume", excavation_volume,
                ['cubic_meter', 'liter'])
    
    # Soil density
    print("\nSoil Density:")
    soil_density = Quantity(1800, 'kilogram/meter^3')
    print(f"Density: {soil_density}")
    
    # Excavation depth
    print("\nExcavation Depth:")
    excavation_depth = Quantity(8, 'meter')
    print_result("Depth", excavation_depth,
                ['meter', 'foot'])
    
    # Slope angle
    print("\nSlope Angle:")
    slope_angle = Quantity(30, 'degree')
    print_result("Slope", slope_angle,
                ['radian', 'degree'])
    
    # Compaction
    print("\nCompaction:")
    compaction_percent = 95  # percent of maximum dry density
    print(f"Compaction: {compaction_percent}%")


# ============================================================================
# 6. PAVEMENT DESIGN
# ============================================================================

def pavement_design():
    """Pavement design calculations."""
    print_header("6. PAVEMENT DESIGN")
    
    # Pavement thickness
    print("Pavement Thickness:")
    asphalt_thickness = Quantity(100, 'millimeter')
    print_result("Asphalt layer", asphalt_thickness,
                ['meter', 'centimeter', 'inch'])
    
    base_thickness = Quantity(200, 'millimeter')
    print_result("\nBase layer", base_thickness,
                ['meter', 'centimeter', 'inch'])
    
    # Traffic load
    print("\nTraffic Load:")
    axle_load_mass = Quantity(10, 'ton')
    # Convert to force
    axle_load_force = axle_load_mass.magnitude * 1000 * constants.g.magnitude
    axle_load = Quantity(axle_load_force, 'newton')
    print_result("Standard axle load", axle_load,
                ['kilonewton', 'pound_force'])
    
    # Tire pressure
    print("\nTire Pressure:")
    tire_pressure = Quantity(700, 'kilopascal')
    print_result("Tire pressure", tire_pressure,
                ['pascal', 'megapascal', 'psi'])
    
    # Pavement temperature
    print("\nPavement Temperature:")
    pavement_temp = Quantity(60, 'celsius')
    print_result("Design temperature", pavement_temp,
                ['fahrenheit', 'kelvin'])


# ============================================================================
# 7. HYDRAULICS AND DRAINAGE
# ============================================================================

def hydraulics_drainage():
    """Hydraulic and drainage calculations."""
    print_header("7. HYDRAULICS AND DRAINAGE")
    
    # Flow rate
    print("Flow Rate:")
    flow_rate = Quantity(2.5, 'cubic_meter/second')
    print_result("Design flow", flow_rate,
                ['cubic_meter/second', 'liter/second', 'gallon/minute'])
    
    # Pipe diameter
    print("\nPipe Diameter:")
    pipe_diameter = Quantity(600, 'millimeter')
    print_result("Diameter", pipe_diameter,
                ['meter', 'centimeter', 'inch'])
    
    # Flow velocity
    print("\nFlow Velocity:")
    flow_velocity = Quantity(1.5, 'meter/second')
    print_result("Velocity", flow_velocity,
                ['meter/second', 'kilometer/hour', 'foot/second'])
    
    # Hydraulic head
    print("\nHydraulic Head:")
    hydraulic_head = Quantity(10, 'meter')
    print_result("Head", hydraulic_head,
                ['meter', 'foot'])
    
    # Rainfall intensity
    print("\nRainfall Intensity:")
    rainfall = Quantity(50, 'millimeter/hour')
    print(f"Rainfall: {rainfall}")
    print(f"  → {rainfall.to('meter/hour')}")


# ============================================================================
# 8. BRIDGE DESIGN
# ============================================================================

def bridge_design():
    """Bridge design calculations."""
    print_header("8. BRIDGE DESIGN")
    
    # Span length
    print("Bridge Span:")
    span_length = Quantity(50, 'meter')
    print_result("Main span", span_length,
                ['meter', 'foot'])
    
    # Deck width
    print("\nDeck Width:")
    deck_width = Quantity(12, 'meter')
    print_result("Width", deck_width,
                ['meter', 'foot'])
    
    # Design load (truck)
    print("\nDesign Truck Load:")
    truck_load_mass = Quantity(36, 'ton')
    # Convert to force
    truck_load_force = truck_load_mass.magnitude * 1000 * constants.g.magnitude
    truck_load = Quantity(truck_load_force, 'newton')
    print_result("HS-20 truck", truck_load,
                ['kilonewton', 'pound_force'])
    
    # Deflection limit
    print("\nDeflection Limit:")
    deflection_limit = Quantity(25, 'millimeter')
    print_result("Maximum deflection", deflection_limit,
                ['meter', 'centimeter', 'inch'])
    
    # Clearance
    print("\nVertical Clearance:")
    clearance = Quantity(5.5, 'meter')
    print_result("Clearance", clearance,
                ['meter', 'foot'])


# ============================================================================
# 9. BUILDING DIMENSIONS
# ============================================================================

def building_dimensions():
    """Building dimension conversions."""
    print_header("9. BUILDING DIMENSIONS")
    
    # Building height
    print("Building Height:")
    building_height = Quantity(150, 'meter')
    print_result("Height", building_height,
                ['meter', 'foot', 'kilometer'])
    
    # Floor area
    print("\nFloor Area:")
    floor_area = Quantity(5000, 'meter^2')
    print(f"Area: {floor_area}")
    print(f"  → {floor_area.to('hectare')}")
    
    # Floor-to-floor height
    print("\nFloor-to-Floor Height:")
    floor_height = Quantity(3.5, 'meter')
    print_result("Height", floor_height,
                ['meter', 'foot', 'inch'])
    
    # Column spacing
    print("\nColumn Spacing:")
    column_spacing = Quantity(8, 'meter')
    print_result("Spacing", column_spacing,
                ['meter', 'foot'])
    
    # Wall thickness
    print("\nWall Thickness:")
    wall_thickness = Quantity(200, 'millimeter')
    print_result("Thickness", wall_thickness,
                ['meter', 'centimeter', 'inch'])


# ============================================================================
# 10. CONSTRUCTION MATERIALS
# ============================================================================

def construction_materials():
    """Construction material quantities."""
    print_header("10. CONSTRUCTION MATERIALS")
    
    # Concrete volume
    print("Concrete Volume:")
    concrete_volume = Quantity(100, 'cubic_meter')
    print_result("Volume", concrete_volume,
                ['cubic_meter', 'liter'])
    
    # Rebar weight
    print("\nReinforcement Steel:")
    rebar_weight = Quantity(5000, 'kilogram')
    print_result("Weight", rebar_weight,
                ['kilogram', 'ton', 'pound'])
    
    # Cement quantity
    print("\nCement:")
    cement_bags = 400  # 50 kg bags
    cement_weight = Quantity(cement_bags * 50, 'kilogram')
    print(f"Cement: {cement_bags} bags (50 kg each)")
    print_result("Total weight", cement_weight,
                ['kilogram', 'ton'])
    
    # Aggregate
    print("\nAggregate:")
    aggregate_volume = Quantity(150, 'cubic_meter')
    print_result("Volume", aggregate_volume,
                ['cubic_meter', 'liter'])
    
    # Water-cement ratio
    print("\nWater-Cement Ratio:")
    wc_ratio = 0.45
    print(f"W/C ratio: {wc_ratio}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Run all civil engineering conversion examples."""
    print("\n" + "=" * 70)
    print("CIVIL ENGINEERING UNIT CONVERSIONS")
    print("Real-world conversions for structural and infrastructure design")
    print("=" * 70)
    
    structural_loads()
    concrete_properties()
    steel_properties()
    foundation_design()
    earthwork_excavation()
    pavement_design()
    hydraulics_drainage()
    bridge_design()
    building_dimensions()
    construction_materials()
    
    print("\n" + "=" * 70)
    print("All civil engineering conversions completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
