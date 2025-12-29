"""
Universal Temperature Converter
================================

Convert between Celsius, Fahrenheit, and Kelvin with ease.
Includes practical temperature references and real-world contexts.

Author: Unifyt Team
Purpose: Temperature conversion for all users
"""

from unifyt import Quantity
import sys


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("UNIVERSAL TEMPERATURE CONVERTER")
    print("Convert between Celsius, Fahrenheit, and Kelvin")
    print("=" * 70 + "\n")


def convert_temperature(value: float, from_unit: str) -> dict:
    """
    Convert temperature to all other units.
    
    Args:
        value: Temperature value
        from_unit: Source unit (celsius, fahrenheit, kelvin)
        
    Returns:
        Dictionary with all conversions
    """
    try:
        # Normalize unit names
        unit_map = {
            'c': 'celsius', 'celsius': 'celsius', '°c': 'celsius',
            'f': 'fahrenheit', 'fahrenheit': 'fahrenheit', '°f': 'fahrenheit',
            'k': 'kelvin', 'kelvin': 'kelvin',
        }
        
        from_unit_normalized = unit_map.get(from_unit.lower())
        if not from_unit_normalized:
            return {
                'success': False,
                'error': f'Unknown unit: {from_unit}',
                'message': 'Use celsius, fahrenheit, or kelvin'
            }
        
        # Create quantity
        temp = Quantity(value, from_unit_normalized)
        
        # Convert to all units
        celsius = temp.to('celsius')
        fahrenheit = temp.to('fahrenheit')
        kelvin = temp.to('kelvin')
        
        # Get context
        context = get_temperature_context(celsius.magnitude)
        
        return {
            'success': True,
            'original': temp,
            'celsius': celsius,
            'fahrenheit': fahrenheit,
            'kelvin': kelvin,
            'celsius_val': celsius.magnitude,
            'fahrenheit_val': fahrenheit.magnitude,
            'kelvin_val': kelvin.magnitude,
            'context': context,
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': f'Failed to convert {value} {from_unit}'
        }


def get_temperature_context(celsius: float) -> str:
    """Get real-world context for temperature."""
    if celsius < -273:
        return "Below absolute zero (impossible!)"
    elif celsius < -200:
        return "Cryogenic temperatures (liquid nitrogen)"
    elif celsius < -100:
        return "Extremely cold (Antarctic winter)"
    elif celsius < -40:
        return "Severe cold (Arctic conditions)"
    elif celsius < -20:
        return "Very cold (freezer temperature)"
    elif celsius < 0:
        return "Below freezing (ice forms)"
    elif celsius == 0:
        return "Freezing point of water"
    elif celsius < 10:
        return "Cold (refrigerator temperature)"
    elif celsius < 15:
        return "Cool (light jacket weather)"
    elif celsius < 20:
        return "Mild (comfortable indoors)"
    elif celsius < 25:
        return "Room temperature (comfortable)"
    elif celsius < 30:
        return "Warm (pleasant summer day)"
    elif celsius < 35:
        return "Hot (air conditioning recommended)"
    elif celsius < 40:
        return "Very hot (heat warning)"
    elif celsius < 50:
        return "Extremely hot (dangerous)"
    elif celsius < 100:
        return "Scalding hot (severe burns)"
    elif celsius == 100:
        return "Boiling point of water"
    elif celsius < 200:
        return "Very high (cooking temperatures)"
    elif celsius < 500:
        return "Extremely high (oven temperatures)"
    elif celsius < 1000:
        return "Industrial heat (metalworking)"
    elif celsius < 5000:
        return "Extreme heat (furnaces, welding)"
    else:
        return "Extreme temperatures (plasma, stars)"


def display_result(result: dict, show_context: bool = True):
    """Display conversion result."""
    if result['success']:
        print("\n" + "=" * 70)
        print("TEMPERATURE CONVERSION")
        print("=" * 70)
        print(f"\nOriginal:    {result['original']}")
        print(f"Celsius:     {result['celsius']}")
        print(f"Fahrenheit:  {result['fahrenheit']}")
        print(f"Kelvin:      {result['kelvin']}")
        
        if show_context:
            print(f"\nContext: {result['context']}")
        
        print("=" * 70 + "\n")
    else:
        print("\n" + "!" * 70)
        print("ERROR")
        print("!" * 70)
        print(f"\n{result['message']}")
        print(f"Error: {result['error']}")
        print("\nSupported units: celsius (C), fahrenheit (F), kelvin (K)")
        print("!" * 70 + "\n")


def show_reference_table():
    """Show common temperature reference points."""
    print("\n" + "=" * 70)
    print("TEMPERATURE REFERENCE POINTS")
    print("=" * 70 + "\n")
    
    references = [
        ("Absolute zero", -273.15, "celsius"),
        ("Liquid nitrogen", -196, "celsius"),
        ("Dry ice (CO₂)", -78.5, "celsius"),
        ("Freezer", -18, "celsius"),
        ("Water freezes", 0, "celsius"),
        ("Refrigerator", 4, "celsius"),
        ("Room temperature", 20, "celsius"),
        ("Body temperature", 37, "celsius"),
        ("Hot bath", 40, "celsius"),
        ("Water boils", 100, "celsius"),
        ("Oven (low)", 150, "celsius"),
        ("Oven (medium)", 180, "celsius"),
        ("Oven (high)", 220, "celsius"),
        ("Pizza oven", 300, "celsius"),
        ("Lead melts", 327, "celsius"),
        ("Iron melts", 1538, "celsius"),
    ]
    
    print(f"{'Description':<25} {'Celsius':<15} {'Fahrenheit':<15} {'Kelvin':<15}")
    print("-" * 70)
    
    for desc, value, unit in references:
        result = convert_temperature(value, unit)
        if result['success']:
            c = f"{result['celsius_val']:.1f}°C"
            f = f"{result['fahrenheit_val']:.1f}°F"
            k = f"{result['kelvin_val']:.1f}K"
            print(f"{desc:<25} {c:<15} {f:<15} {k:<15}")
    
    print("=" * 70 + "\n")


def interactive_mode():
    """Run interactive conversion mode."""
    print_header()
    print("Interactive Mode - Enter 'ref' for reference table, 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("Enter temperature (e.g., '25 C' or '77 F'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Temperature Converter!")
                break
            
            if user_input.lower() in ['ref', 'reference', 'table']:
                show_reference_table()
                continue
            
            if not user_input:
                continue
            
            # Parse input
            parts = user_input.split()
            if len(parts) < 2:
                print("Error: Enter both value and unit (e.g., '25 C')")
                continue
            
            try:
                value = float(parts[0])
                unit = parts[1]
            except ValueError:
                print("Error: First part must be a number")
                continue
            
            # Convert
            result = convert_temperature(value, unit)
            display_result(result)
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")


def batch_convert(temperatures: list):
    """Batch convert temperatures."""
    print("\n" + "=" * 70)
    print("BATCH TEMPERATURE CONVERSION")
    print("=" * 70 + "\n")
    
    print(f"{'Description':<20} {'Original':<15} {'Celsius':<12} {'Fahrenheit':<12} {'Kelvin':<12}")
    print("-" * 70)
    
    for value, unit, desc in temperatures:
        result = convert_temperature(value, unit)
        if result['success']:
            orig = f"{value}{unit[0].upper()}"
            c = f"{result['celsius_val']:.1f}°C"
            f = f"{result['fahrenheit_val']:.1f}°F"
            k = f"{result['kelvin_val']:.1f}K"
            print(f"{desc:<20} {orig:<15} {c:<12} {f:<12} {k:<12}")
    
    print("=" * 70 + "\n")


def main():
    """Main function."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h']:
            print_header()
            print("Usage:")
            print("  python temperature_converter.py                # Interactive mode")
            print("  python temperature_converter.py --ref          # Show reference table")
            print("  python temperature_converter.py <value> <unit> # Direct conversion")
            print("\nExamples:")
            print("  python temperature_converter.py 25 C")
            print("  python temperature_converter.py 77 F")
            print("  python temperature_converter.py 300 K")
            print("\nUnits: celsius (C), fahrenheit (F), kelvin (K)")
            return
        
        elif sys.argv[1] == '--ref':
            show_reference_table()
            return
        
        elif len(sys.argv) >= 3:
            try:
                value = float(sys.argv[1])
                unit = sys.argv[2]
                print_header()
                result = convert_temperature(value, unit)
                display_result(result)
            except ValueError:
                print("Error: First argument must be a number")
            return
    
    # Default: interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()
