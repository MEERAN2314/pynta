"""
HVAC and Mechanical Engineering Unit Conversions
================================================

Real-world unit conversions for heating, ventilation, air conditioning,
and mechanical system design.

Author: Unifyt Team
Industry: HVAC & Mechanical Engineering
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
# 1. COOLING CAPACITY
# ============================================================================

def cooling_capacity():
    print_header("1. COOLING CAPACITY")
    
    # Tons of refrigeration
    print("Cooling Capacity:")
    tons_refrigeration = 100  # tons
    # 1 ton = 3.517 kW (approximately)
    cooling_kw = tons_refrigeration * 3.517
    cooling = Quantity(cooling_kw, 'kilowatt')
    print(f"Capacity: {tons_refrigeration} tons of refrigeration")
    print_result("Cooling power", cooling,
                ['watt', 'kilowatt', 'megawatt'])
    
    # BTU/hr
    print("\nCooling in BTU/hr:")
    btu_per_hour = tons_refrigeration * 12000  # 1 ton = 12,000 BTU/hr
    print(f"Capacity: {btu_per_hour:,} BTU/hr")
    
    # Chiller capacity
    print("\nChiller Capacity:")
    chiller_capacity = Quantity(500, 'kilowatt')
    chiller_tons = chiller_capacity.magnitude / 3.517
    print_result("Chiller", chiller_capacity, ['watt', 'megawatt'])
    print(f"  → {chiller_tons:.1f} tons")


# ============================================================================
# 2. AIR FLOW RATES
# ============================================================================

def air_flow_rates():
    print_header("2. AIR FLOW RATES")
    
    # CFM (Cubic Feet per Minute)
    print("Air Flow Rate:")
    cfm = 10000  # CFM
    # Convert to m³/s: CFM × 0.000471947
    flow_m3_s = cfm * 0.000471947
    flow_rate = Quantity(flow_m3_s, 'cubic_meter/second')
    print(f"Flow rate: {cfm:,} CFM")
    print_result("Flow rate", flow_rate,
                ['cubic_meter/second', 'liter/second'])
    
    # Air velocity in duct
    print("\nAir Velocity:")
    air_velocity = Quantity(10, 'meter/second')
    print_result("Velocity", air_velocity,
                ['meter/second', 'kilometer/hour', 'foot/second'])
    
    # Duct size
    print("\nDuct Dimensions:")
    duct_width = Quantity(600, 'millimeter')
    duct_height = Quantity(400, 'millimeter')
    print_result("Width", duct_width, ['meter', 'inch'])
    print_result("Height", duct_height, ['meter', 'inch'])


# ============================================================================
# 3. HEATING CAPACITY
# ============================================================================

def heating_capacity():
    print_header("3. HEATING CAPACITY")
    
    # Boiler capacity
    print("Boiler Capacity:")
    boiler_capacity = Quantity(2000, 'kilowatt')
    print_result("Capacity", boiler_capacity,
                ['watt', 'megawatt'])
    
    # BTU/hr
    btu_hr = boiler_capacity.magnitude * 3412.14  # 1 kW = 3412.14 BTU/hr
    print(f"  → {btu_hr:,.0f} BTU/hr")
    
    # Heating load
    print("\nHeating Load:")
    heating_load = Quantity(150, 'kilowatt')
    print_result("Load", heating_load,
                ['watt', 'kilowatt'])
    
    # Fuel consumption
    print("\nFuel Consumption:")
    fuel_rate = Quantity(15, 'kilogram/hour')  # Natural gas
    print_result("Gas consumption", fuel_rate,
                ['kilogram/hour', 'kilogram/second'])


# ============================================================================
# 4. TEMPERATURE CONTROL
# ============================================================================

def temperature_control():
    print_header("4. TEMPERATURE CONTROL")
    
    # Room temperature
    print("Room Temperature:")
    room_temp = Quantity(22, 'celsius')
    print_result("Setpoint", room_temp,
                ['fahrenheit', 'kelvin'])
    
    # Supply air temperature
    print("\nSupply Air Temperature:")
    supply_temp = Quantity(14, 'celsius')
    print_result("Supply", supply_temp,
                ['fahrenheit', 'kelvin'])
    
    # Temperature difference
    print("\nTemperature Difference:")
    delta_t = room_temp.magnitude - supply_temp.magnitude
    print(f"ΔT: {delta_t}°C ({delta_t * 1.8}°F)")
    
    # Outdoor design temperature
    print("\nOutdoor Design Conditions:")
    summer_design = Quantity(35, 'celsius')
    winter_design = Quantity(-10, 'celsius')
    print_result("Summer", summer_design, ['fahrenheit'])
    print_result("Winter", winter_design, ['fahrenheit'])


# ============================================================================
# 5. PRESSURE AND STATIC
# ============================================================================

def pressure_static():
    print_header("5. PRESSURE AND STATIC")
    
    # Static pressure
    print("Static Pressure:")
    static_pressure = Quantity(250, 'pascal')
    print_result("Pressure", static_pressure,
                ['pascal', 'kilopascal', 'psi'])
    
    # Inches of water column
    inches_wc = static_pressure.magnitude / 249.089  # 1 inWC = 249.089 Pa
    print(f"  → {inches_wc:.2f} inches water column")
    
    # Fan pressure
    print("\nFan Total Pressure:")
    fan_pressure = Quantity(1000, 'pascal')
    print_result("Pressure", fan_pressure,
                ['pascal', 'kilopascal'])
    
    # Duct pressure drop
    print("\nDuct Pressure Drop:")
    pressure_drop = Quantity(0.5, 'pascal')  # per meter
    print(f"Pressure drop: {pressure_drop} / meter")


# ============================================================================
# 6. HUMIDITY CONTROL
# ============================================================================

def humidity_control():
    print_header("6. HUMIDITY CONTROL")
    
    # Relative humidity
    print("Relative Humidity:")
    rh = 50  # percent
    print(f"RH: {rh}%")
    
    # Absolute humidity
    print("\nAbsolute Humidity:")
    abs_humidity = 10  # g/kg (grams of water per kg of dry air)
    print(f"Absolute humidity: {abs_humidity} g/kg")
    
    # Dew point
    print("\nDew Point:")
    dew_point = Quantity(12, 'celsius')
    print_result("Dew point", dew_point,
                ['fahrenheit', 'kelvin'])
    
    # Moisture removal
    print("\nMoisture Removal Rate:")
    moisture_rate = Quantity(50, 'kilogram/hour')
    print_result("Dehumidification", moisture_rate,
                ['kilogram/hour', 'kilogram/second'])


# ============================================================================
# 7. ENERGY EFFICIENCY
# ============================================================================

def energy_efficiency():
    print_header("7. ENERGY EFFICIENCY")
    
    # COP (Coefficient of Performance)
    print("Coefficient of Performance:")
    cop = 3.5
    print(f"COP: {cop}")
    print(f"Efficiency: {cop * 100 / 3.412:.1f}% (relative to electric resistance)")
    
    # EER (Energy Efficiency Ratio)
    print("\nEnergy Efficiency Ratio:")
    eer = 12  # BTU/hr per watt
    print(f"EER: {eer} BTU/hr/W")
    
    # SEER (Seasonal EER)
    print("\nSeasonal Energy Efficiency Ratio:")
    seer = 16
    print(f"SEER: {seer}")
    
    # Power consumption
    print("\nPower Consumption:")
    power = Quantity(5, 'kilowatt')
    print_result("Power", power,
                ['watt', 'kilowatt'])
    
    # Annual energy use
    hours_per_year = 2000  # operating hours
    annual_energy_j = power.to('watt').magnitude * hours_per_year * 3600
    annual_energy = Quantity(annual_energy_j, 'joule')
    print(f"\nAnnual operating hours: {hours_per_year}")
    print_result("Annual energy", annual_energy,
                ['kilowatt_hour', 'gigajoule'])


# ============================================================================
# 8. VENTILATION REQUIREMENTS
# ============================================================================

def ventilation_requirements():
    print_header("8. VENTILATION REQUIREMENTS")
    
    # Fresh air requirement
    print("Fresh Air Requirement:")
    people = 100
    cfm_per_person = 15  # CFM per person
    total_cfm = people * cfm_per_person
    fresh_air_m3_s = total_cfm * 0.000471947
    fresh_air = Quantity(fresh_air_m3_s, 'cubic_meter/second')
    print(f"Occupancy: {people} people")
    print(f"Rate: {cfm_per_person} CFM/person")
    print(f"Total: {total_cfm} CFM")
    print_result("Fresh air", fresh_air,
                ['cubic_meter/second', 'liter/second'])
    
    # Air changes per hour
    print("\nAir Changes Per Hour:")
    room_volume = Quantity(500, 'cubic_meter')
    ach = 6  # air changes per hour
    required_flow = room_volume.magnitude * ach / 3600
    flow = Quantity(required_flow, 'cubic_meter/second')
    print(f"Room volume: {room_volume}")
    print(f"ACH: {ach}")
    print_result("Required flow", flow,
                ['cubic_meter/second', 'liter/second'])


# ============================================================================
# 9. REFRIGERATION CYCLE
# ============================================================================

def refrigeration_cycle():
    print_header("9. REFRIGERATION CYCLE")
    
    # Evaporator temperature
    print("Evaporator Temperature:")
    evap_temp = Quantity(5, 'celsius')
    print_result("Temperature", evap_temp,
                ['fahrenheit', 'kelvin'])
    
    # Condenser temperature
    print("\nCondenser Temperature:")
    cond_temp = Quantity(45, 'celsius')
    print_result("Temperature", cond_temp,
                ['fahrenheit', 'kelvin'])
    
    # Refrigerant pressure
    print("\nRefrigerant Pressure (R-410A):")
    evap_pressure = Quantity(1000, 'kilopascal')
    cond_pressure = Quantity(2800, 'kilopascal')
    print_result("Evaporator", evap_pressure, ['pascal', 'bar', 'psi'])
    print_result("Condenser", cond_pressure, ['pascal', 'bar', 'psi'])
    
    # Compressor power
    print("\nCompressor Power:")
    compressor_power = Quantity(15, 'kilowatt')
    print_result("Power", compressor_power,
                ['watt', 'kilowatt', 'horsepower'])


# ============================================================================
# 10. THERMAL LOADS
# ============================================================================

def thermal_loads():
    print_header("10. THERMAL LOADS")
    
    # Sensible heat load
    print("Sensible Heat Load:")
    sensible_load = Quantity(80, 'kilowatt')
    print_result("Sensible", sensible_load,
                ['watt', 'kilowatt'])
    
    # Latent heat load
    print("\nLatent Heat Load:")
    latent_load = Quantity(20, 'kilowatt')
    print_result("Latent", latent_load,
                ['watt', 'kilowatt'])
    
    # Total load
    total_load = Quantity(sensible_load.magnitude + latent_load.magnitude, 'kilowatt')
    print_result("\nTotal Load", total_load,
                ['watt', 'kilowatt'])
    
    # Sensible heat ratio
    shr = sensible_load.magnitude / total_load.magnitude
    print(f"\nSensible Heat Ratio: {shr:.2f}")
    
    # Heat gain from occupants
    print("\nHeat Gain from Occupants:")
    people = 50
    heat_per_person = 100  # watts
    occupant_load = Quantity(people * heat_per_person, 'watt')
    print(f"Occupancy: {people} people")
    print(f"Heat gain: {heat_per_person} W/person")
    print_result("Total", occupant_load,
                ['watt', 'kilowatt'])


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("HVAC & MECHANICAL ENGINEERING UNIT CONVERSIONS")
    print("Real-world conversions for climate control systems")
    print("=" * 70)
    
    cooling_capacity()
    air_flow_rates()
    heating_capacity()
    temperature_control()
    pressure_static()
    humidity_control()
    energy_efficiency()
    ventilation_requirements()
    refrigeration_cycle()
    thermal_loads()
    
    print("\n" + "=" * 70)
    print("All HVAC conversions completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
