"""
Electrical Power Engineering Unit Conversions
=============================================

Real-world unit conversions for power generation, transmission,
distribution, and electrical system design.

Author: Unifyt Team
Industry: Electrical Power Engineering
"""

from unifyt import Quantity, constants


def print_header(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}\n")


def print_result(label: str, value: Quantity, conversions: list = None) -> None:
    print(f"{label}: {value}")
    if conversions:
        for unit in conversions:
            print(f"  → {value.to(unit)}")


# ============================================================================
# 1. POWER GENERATION
# ============================================================================

def power_generation():
    print_header("1. POWER GENERATION")
    
    # Generator capacity
    print("Generator Capacity:")
    generator_capacity = Quantity(500, 'megawatt')
    print_result("Capacity", generator_capacity,
                ['watt', 'kilowatt', 'gigawatt'])
    
    # Daily energy production
    print("\nDaily Energy Production:")
    hours = 24
    daily_energy_j = generator_capacity.to('watt').magnitude * hours * 3600
    daily_energy = Quantity(daily_energy_j, 'joule')
    print_result("Energy", daily_energy,
                ['kilowatt_hour', 'gigajoule'])
    
    # Generator voltage
    print("\nGenerator Voltage:")
    gen_voltage = Quantity(22, 'kilovolt')
    print_result("Voltage", gen_voltage,
                ['volt', 'kilovolt'])
    
    # Generator current
    print("\nGenerator Current:")
    current = generator_capacity.to('watt').magnitude / (gen_voltage.to('volt').magnitude * 1.732)  # 3-phase
    gen_current = Quantity(current, 'ampere')
    print_result("Current (3-phase)", gen_current,
                ['ampere', 'kiloampere'])
    
    # Efficiency
    print("\nGenerator Efficiency:")
    efficiency = 0.98
    print(f"Efficiency: {efficiency * 100}%")


# ============================================================================
# 2. TRANSMISSION LINES
# ============================================================================

def transmission_lines():
    print_header("2. TRANSMISSION LINES")
    
    # Transmission voltage
    print("Transmission Voltage Levels:")
    hv_levels = [
        ("High Voltage", Quantity(132, 'kilovolt')),
        ("Extra High Voltage", Quantity(400, 'kilovolt')),
        ("Ultra High Voltage", Quantity(765, 'kilovolt')),
    ]
    
    for name, voltage in hv_levels:
        print(f"\n{name}:")
        print_result("Voltage", voltage, ['volt', 'megavolt'])
    
    # Line length
    print("\n\nTransmission Line Length:")
    line_length = Quantity(250, 'kilometer')
    print_result("Length", line_length,
                ['meter', 'mile'])
    
    # Power loss
    print("\nPower Loss:")
    power_loss = Quantity(5, 'megawatt')
    print_result("Loss", power_loss,
                ['watt', 'kilowatt'])
    
    # Line current
    print("\nLine Current:")
    line_current = Quantity(1500, 'ampere')
    print_result("Current", line_current,
                ['ampere', 'kiloampere'])


# ============================================================================
# 3. TRANSFORMERS
# ============================================================================

def transformers():
    print_header("3. TRANSFORMERS")
    
    # Transformer rating
    print("Transformer Rating:")
    transformer_rating = Quantity(100, 'megawatt')  # MVA
    print_result("Rating", transformer_rating,
                ['watt', 'kilowatt', 'megawatt'])
    
    # Voltage transformation
    print("\nVoltage Transformation:")
    primary_voltage = Quantity(132, 'kilovolt')
    secondary_voltage = Quantity(11, 'kilovolt')
    print_result("Primary", primary_voltage, ['volt', 'kilovolt'])
    print_result("Secondary", secondary_voltage, ['volt', 'kilovolt'])
    
    turns_ratio = primary_voltage.magnitude / secondary_voltage.magnitude
    print(f"\nTurns ratio: {turns_ratio:.2f}:1")
    
    # Transformer losses
    print("\nTransformer Losses:")
    core_loss = Quantity(50, 'kilowatt')
    copper_loss = Quantity(150, 'kilowatt')
    print_result("Core loss", core_loss, ['watt', 'kilowatt'])
    print_result("Copper loss", copper_loss, ['watt', 'kilowatt'])
    
    total_loss = Quantity(core_loss.magnitude + copper_loss.magnitude, 'kilowatt')
    print_result("Total loss", total_loss, ['watt', 'kilowatt', 'megawatt'])


# ============================================================================
# 4. DISTRIBUTION SYSTEMS
# ============================================================================

def distribution_systems():
    print_header("4. DISTRIBUTION SYSTEMS")
    
    # Distribution voltage
    print("Distribution Voltage:")
    dist_voltage = Quantity(11, 'kilovolt')
    print_result("Medium voltage", dist_voltage,
                ['volt', 'kilovolt'])
    
    lv_voltage = Quantity(400, 'volt')
    print_result("\nLow voltage", lv_voltage,
                ['volt'])
    
    # Feeder capacity
    print("\nFeeder Capacity:")
    feeder_capacity = Quantity(5, 'megawatt')
    print_result("Capacity", feeder_capacity,
                ['watt', 'kilowatt'])
    
    # Load current
    print("\nLoad Current:")
    load_current = Quantity(250, 'ampere')
    print_result("Current", load_current,
                ['ampere', 'milliampere'])
    
    # Cable size
    print("\nCable Size:")
    cable_area = Quantity(240, 'millimeter^2')  # mm²
    print(f"Cable: {cable_area}")


# ============================================================================
# 5. POWER FACTOR AND REACTIVE POWER
# ============================================================================

def power_factor():
    print_header("5. POWER FACTOR AND REACTIVE POWER")
    
    # Active power
    print("Active Power:")
    active_power = Quantity(800, 'kilowatt')
    print_result("P", active_power,
                ['watt', 'megawatt'])
    
    # Power factor
    print("\nPower Factor:")
    pf = 0.85
    print(f"Power factor: {pf} (lagging)")
    
    # Apparent power
    print("\nApparent Power:")
    apparent_power_value = active_power.magnitude / pf
    apparent_power = Quantity(apparent_power_value, 'kilowatt')  # kVA
    print(f"S: {apparent_power_value:.2f} kVA")
    
    # Reactive power
    print("\nReactive Power:")
    import math
    reactive_power_value = active_power.magnitude * math.tan(math.acos(pf))
    print(f"Q: {reactive_power_value:.2f} kVAR")
    
    # Capacitor bank
    print("\nCapacitor Bank for Correction:")
    target_pf = 0.95
    capacitor_kvar = active_power.magnitude * (math.tan(math.acos(pf)) - math.tan(math.acos(target_pf)))
    print(f"Required: {capacitor_kvar:.2f} kVAR")


# ============================================================================
# 6. CIRCUIT BREAKERS AND PROTECTION
# ============================================================================

def circuit_protection():
    print_header("6. CIRCUIT BREAKERS AND PROTECTION")
    
    # Breaking capacity
    print("Circuit Breaker Rating:")
    breaking_capacity = Quantity(40, 'kiloampere')
    print_result("Breaking capacity", breaking_capacity,
                ['ampere', 'kiloampere'])
    
    # Operating voltage
    print("\nOperating Voltage:")
    cb_voltage = Quantity(132, 'kilovolt')
    print_result("Voltage", cb_voltage,
                ['volt', 'kilovolt'])
    
    # Fault current
    print("\nFault Current:")
    fault_current = Quantity(25, 'kiloampere')
    print_result("Short circuit current", fault_current,
                ['ampere', 'kiloampere'])
    
    # Operating time
    print("\nOperating Time:")
    operating_time = Quantity(50, 'millisecond')
    print_result("Trip time", operating_time,
                ['second', 'millisecond'])


# ============================================================================
# 7. ENERGY CONSUMPTION
# ============================================================================

def energy_consumption():
    print_header("7. ENERGY CONSUMPTION")
    
    # Industrial load
    print("Industrial Load:")
    industrial_load = Quantity(2, 'megawatt')
    print_result("Load", industrial_load,
                ['watt', 'kilowatt'])
    
    # Monthly consumption
    print("\nMonthly Energy Consumption:")
    hours_per_month = 720  # 30 days × 24 hours
    monthly_energy_j = industrial_load.to('watt').magnitude * hours_per_month * 3600
    monthly_energy = Quantity(monthly_energy_j, 'joule')
    print_result("Energy", monthly_energy,
                ['kilowatt_hour', 'gigajoule'])
    
    # Cost calculation
    print("\nEnergy Cost:")
    rate_per_kwh = 0.12  # dollars
    monthly_kwh = monthly_energy.to('kilowatt_hour').magnitude
    monthly_cost = monthly_kwh * rate_per_kwh
    print(f"Rate: ${rate_per_kwh}/kWh")
    print(f"Monthly cost: ${monthly_cost:,.2f}")


# ============================================================================
# 8. RENEWABLE ENERGY
# ============================================================================

def renewable_energy():
    print_header("8. RENEWABLE ENERGY")
    
    # Solar panel
    print("Solar Panel:")
    panel_power = Quantity(400, 'watt')
    print_result("Panel rating", panel_power,
                ['watt', 'kilowatt'])
    
    panel_voltage = Quantity(48, 'volt')
    panel_current = panel_power.magnitude / panel_voltage.magnitude
    print_result("Voltage", panel_voltage, ['volt'])
    print(f"Current: {panel_current:.2f} A")
    
    # Solar array
    print("\nSolar Array:")
    num_panels = 1000
    array_power = Quantity(num_panels * panel_power.magnitude, 'watt')
    print(f"Number of panels: {num_panels}")
    print_result("Total capacity", array_power,
                ['watt', 'kilowatt', 'megawatt'])
    
    # Wind turbine
    print("\nWind Turbine:")
    turbine_power = Quantity(3, 'megawatt')
    print_result("Rated power", turbine_power,
                ['watt', 'kilowatt'])
    
    # Battery storage
    print("\nBattery Storage:")
    battery_capacity_kwh = 500
    battery_capacity_j = battery_capacity_kwh * 3.6e6
    battery_capacity = Quantity(battery_capacity_j, 'joule')
    print(f"Capacity: {battery_capacity_kwh} kWh")
    print_result("Energy", battery_capacity,
                ['joule', 'megajoule', 'gigajoule'])


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("ELECTRICAL POWER ENGINEERING UNIT CONVERSIONS")
    print("Real-world conversions for power systems")
    print("=" * 70)
    
    power_generation()
    transmission_lines()
    transformers()
    distribution_systems()
    power_factor()
    circuit_protection()
    energy_consumption()
    renewable_energy()
    
    print("\n" + "=" * 70)
    print("All electrical power conversions completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
