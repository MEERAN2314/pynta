"""
Universal Volume to Cubic Meter Converter
=========================================

This example demonstrates converting any volume unit to cubic meters (m³).
Useful for standardizing volume measurements across different unit systems.

Author: Unifyt Team
Purpose: Volume standardization and conversion
"""

from unifyt import Quantity
import sys


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("UNIVERSAL VOLUME TO CUBIC METER CONVERTER")
    print("Convert any volume unit to cubic meters (m³)")
    print("=" * 70 + "\n")


def print_supported_units():
    """Display all supported volume units."""
    print("Supported Volume Units:")
    print("-" * 70)
    
    units = {
        "Metric": [
            "cubic_meter (m³, m3, m^3)",
            "liter (L, liters, litre, litres)",
            "milliliter (mL, milliliters)",
        ],
        "Imperial/US": [
            "gallon (gal, gallons)",
            "quart (qt)",
            "pint (pt)",
            "cup (cups)",
            "fluid_ounce (fl_oz)",
        ],
    }
    
    for category, unit_list in units.items():
        print(f"\n{category}:")
        for unit in unit_list:
            print(f"  • {unit}")
    
    print("\n" + "-" * 70)
    print("\nNote: For cubic feet, yards, or inches, calculate volume")
    print("      from dimensions and use cubic_meter directly.")


def convert_to_cubic_meter(value: float, unit: str) -> dict:
    """
    Convert any volume unit to cubic meters.
    
    Args:
        value: Numerical value
        unit: Unit string
        
    Returns:
        Dictionary with conversion results
    """
    try:
        # Create quantity with input unit
        volume = Quantity(value, unit)
        
        # Convert to cubic meters
        volume_m3 = volume.to('cubic_meter')
        
        # Also provide conversions to other common units for reference
        volume_liters = volume.to('liter')
        
        return {
            'success': True,
            'original': volume,
            'cubic_meter': volume_m3,
            'liters': volume_liters,
            'value_m3': volume_m3.magnitude,
            'value_liters': volume_liters.magnitude,
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': f"Failed to convert {value} {unit} to cubic meters"
        }


def display_result(result: dict):
    """Display conversion result in a formatted way."""
    if result['success']:
        print("\n" + "=" * 70)
        print("CONVERSION RESULT")
        print("=" * 70)
        print(f"\nOriginal:      {result['original']}")
        print(f"Cubic Meters:  {result['cubic_meter']}")
        print(f"Liters:        {result['liters']}")
        print(f"\nNumerical Values:")
        print(f"  m³:  {result['value_m3']:.6f}")
        print(f"  L:   {result['value_liters']:.6f}")
        print("=" * 70 + "\n")
    else:
        print("\n" + "!" * 70)
        print("CONVERSION ERROR")
        print("!" * 70)
        print(f"\nError: {result['error']}")
        print(f"Message: {result['message']}")
        print("\nPlease check:")
        print("  • Unit spelling is correct")
        print("  • Unit is a volume unit (not length, mass, etc.)")
        print("  • Value is a valid number")
        print("!" * 70 + "\n")


def batch_convert(conversions: list):
    """
    Convert multiple volumes to cubic meters.
    
    Args:
        conversions: List of tuples (value, unit, description)
    """
    print("\n" + "=" * 70)
    print("BATCH CONVERSION TO CUBIC METERS")
    print("=" * 70 + "\n")
    
    results = []
    for value, unit, description in conversions:
        result = convert_to_cubic_meter(value, unit)
        results.append((description, result))
    
    # Display results in table format
    print(f"{'Description':<30} {'Original':<20} {'Cubic Meters (m³)':<20}")
    print("-" * 70)
    
    for description, result in results:
        if result['success']:
            original_str = f"{result['original']}"
            m3_str = f"{result['value_m3']:.6f}"
            print(f"{description:<30} {original_str:<20} {m3_str:<20}")
        else:
            print(f"{description:<30} {'ERROR':<20} {'N/A':<20}")
    
    print("=" * 70 + "\n")


def interactive_mode():
    """Run interactive conversion mode."""
    print_header()
    print("Interactive Mode - Enter 'help' for supported units, 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            user_input = input("Enter value and unit (e.g., '100 liter'): ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Volume Converter!")
                break
            
            if user_input.lower() in ['help', 'h', '?']:
                print_supported_units()
                continue
            
            if not user_input:
                continue
            
            # Parse input
            parts = user_input.split()
            if len(parts) < 2:
                print("Error: Please enter both value and unit (e.g., '100 liter')")
                continue
            
            try:
                value = float(parts[0])
                unit = ' '.join(parts[1:])  # Handle multi-word units
            except ValueError:
                print("Error: First part must be a number")
                continue
            
            # Perform conversion
            result = convert_to_cubic_meter(value, unit)
            display_result(result)
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")


def demo_examples():
    """Demonstrate various volume conversions."""
    print_header()
    print("DEMONSTRATION: Common Volume Conversions to Cubic Meters\n")
    
    # Example conversions (only using properly supported units)
    examples = [
        # (value, unit, description)
        (1000, 'liter', 'Water tank'),
        (50, 'gallon', 'Fuel tank'),
        (500, 'milliliter', 'Bottle'),
        (2.5, 'cubic_meter', 'Room volume'),
        (10, 'quart', 'Cooking pot'),
        (250, 'cup', 'Recipe measurement'),
        (20, 'fluid_ounce', 'Medicine dose'),
        (5, 'pint', 'Milk container'),
        (100, 'liter', 'Drum'),
        (1.5, 'gallon', 'Paint can'),
    ]
    
    batch_convert(examples)
    
    # Detailed examples with context
    print("\nDETAILED EXAMPLES WITH CONTEXT:")
    print("=" * 70 + "\n")
    
    # Example 1: Swimming pool
    print("Example 1: Swimming Pool Volume")
    print("-" * 70)
    pool_volume = Quantity(50000, 'gallon')
    result = convert_to_cubic_meter(pool_volume.magnitude, 'gallon')
    if result['success']:
        print(f"Pool capacity: {pool_volume}")
        print(f"In cubic meters: {result['cubic_meter']}")
        print(f"In liters: {result['liters']}")
        print(f"Numerical: {result['value_m3']:.2f} m³")
    
    # Example 2: Large water tank
    print("\n\nExample 2: Industrial Water Tank")
    print("-" * 70)
    tank_volume = Quantity(10000, 'liter')
    result = convert_to_cubic_meter(tank_volume.magnitude, 'liter')
    if result['success']:
        print(f"Tank volume: {tank_volume}")
        print(f"In cubic meters: {result['cubic_meter']}")
        print(f"Numerical: {result['value_m3']:.2f} m³")
    
    # Example 3: Fuel tank
    print("\n\nExample 3: Vehicle Fuel Tank")
    print("-" * 70)
    fuel_tank = Quantity(15, 'gallon')
    result = convert_to_cubic_meter(fuel_tank.magnitude, 'gallon')
    if result['success']:
        print(f"Tank capacity: {fuel_tank}")
        print(f"In cubic meters: {result['cubic_meter']}")
        print(f"In liters: {result['liters']}")
        print(f"Numerical: {result['value_m3']:.6f} m³")
    
    # Example 4: Storage container
    print("\n\nExample 4: Storage Container")
    print("-" * 70)
    container_volume = Quantity(500, 'liter')
    result = convert_to_cubic_meter(container_volume.magnitude, 'liter')
    if result['success']:
        print(f"Container capacity: {container_volume}")
        print(f"In cubic meters: {result['cubic_meter']}")
        print(f"Numerical: {result['value_m3']:.2f} m³")
    
    # Example 5: Water bottle
    print("\n\nExample 5: Water Bottle")
    print("-" * 70)
    bottle = Quantity(500, 'milliliter')
    result = convert_to_cubic_meter(bottle.magnitude, 'milliliter')
    if result['success']:
        print(f"Bottle size: {bottle}")
        print(f"In cubic meters: {result['cubic_meter']}")
        print(f"Numerical: {result['value_m3']:.9f} m³")
    
    print("\n" + "=" * 70 + "\n")


def practical_applications():
    """Show practical applications of volume conversion."""
    print("\n" + "=" * 70)
    print("PRACTICAL APPLICATIONS")
    print("=" * 70 + "\n")
    
    # Application 1: Construction - Concrete calculation
    print("Application 1: Construction - Concrete Volume")
    print("-" * 70)
    print("Scenario: Calculate concrete needed for a foundation")
    
    # Foundation dimensions
    length = Quantity(10, 'meter')
    width = Quantity(8, 'meter')
    depth = Quantity(0.3, 'meter')
    
    # Calculate volume
    volume_m3 = length.magnitude * width.magnitude * depth.magnitude
    volume = Quantity(volume_m3, 'cubic_meter')
    
    print(f"Foundation dimensions: {length} × {width} × {depth}")
    print(f"Volume needed: {volume}")
    print(f"In liters: {volume.to('liter'):.0f}")
    
    # Application 2: Logistics - Container loading
    print("\n\nApplication 2: Logistics - Container Capacity")
    print("-" * 70)
    print("Scenario: Check if cargo fits in shipping container")
    
    container_capacity = Quantity(33.2, 'cubic_meter')
    cargo_volume = Quantity(28.3, 'cubic_meter')  # Approximately 1000 cubic feet
    
    print(f"Container capacity: {container_capacity}")
    print(f"Cargo volume: {cargo_volume}")
    
    remaining = container_capacity.magnitude - cargo_volume.magnitude
    print(f"Remaining space: {remaining:.2f} m³")
    
    # Application 3: Water management
    print("\n\nApplication 3: Water Management - Tank Sizing")
    print("-" * 70)
    print("Scenario: Size water storage tank for daily consumption")
    
    daily_consumption = Quantity(5000, 'liter')
    days_storage = 3
    required_volume = Quantity(daily_consumption.magnitude * days_storage, 'liter')
    
    print(f"Daily consumption: {daily_consumption}")
    print(f"Storage days: {days_storage}")
    print(f"Required tank volume: {required_volume}")
    print(f"In cubic meters: {required_volume.to('cubic_meter'):.2f}")
    print(f"In gallons: {required_volume.to('gallon'):.0f}")
    
    # Application 4: HVAC - Room volume
    print("\n\nApplication 4: HVAC - Room Air Volume")
    print("-" * 70)
    print("Scenario: Calculate air changes per hour")
    
    room_length = Quantity(6, 'meter')
    room_width = Quantity(4, 'meter')
    room_height = Quantity(3, 'meter')
    room_volume_m3 = room_length.magnitude * room_width.magnitude * room_height.magnitude
    room_volume = Quantity(room_volume_m3, 'cubic_meter')
    
    ach = 6  # Air changes per hour
    airflow_m3_h = room_volume.magnitude * ach
    airflow_m3_s = airflow_m3_h / 3600
    
    print(f"Room dimensions: {room_length} × {room_width} × {room_height}")
    print(f"Room volume: {room_volume}")
    print(f"Required ACH: {ach}")
    print(f"Required airflow: {airflow_m3_s:.4f} m³/s")
    print(f"In CFM: {airflow_m3_s / 0.000471947:.0f} CFM")
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Main function to run the converter."""
    if len(sys.argv) > 1:
        # Command-line mode
        if sys.argv[1] in ['--help', '-h']:
            print_header()
            print_supported_units()
            print("\nUsage:")
            print("  python volume_to_cubic_meter.py              # Interactive mode")
            print("  python volume_to_cubic_meter.py --demo       # Run demonstrations")
            print("  python volume_to_cubic_meter.py --apps       # Show applications")
            print("  python volume_to_cubic_meter.py <value> <unit>  # Direct conversion")
            print("\nExamples:")
            print("  python volume_to_cubic_meter.py 100 liter")
            print("  python volume_to_cubic_meter.py 50 gallon")
            print("  python volume_to_cubic_meter.py 2.5 cubic_meter")
            return
        
        elif sys.argv[1] == '--demo':
            demo_examples()
            return
        
        elif sys.argv[1] == '--apps':
            practical_applications()
            return
        
        elif len(sys.argv) >= 3:
            # Direct conversion from command line
            try:
                value = float(sys.argv[1])
                unit = ' '.join(sys.argv[2:])
                print_header()
                result = convert_to_cubic_meter(value, unit)
                display_result(result)
            except ValueError:
                print("Error: First argument must be a number")
            return
    
    # Default: Run all demonstrations
    demo_examples()
    practical_applications()
    
    # Ask if user wants interactive mode
    print("\nWould you like to try interactive mode? (y/n): ", end='')
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            interactive_mode()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
