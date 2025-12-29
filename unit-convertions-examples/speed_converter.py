"""
Universal Speed/Velocity Converter
===================================

Convert between all common speed units with real-world context.
Perfect for travel, sports, vehicles, and scientific applications.

Author: Unifyt Team
Purpose: Speed conversion for all users
"""

from unifyt import Quantity, constants
import sys


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("UNIVERSAL SPEED CONVERTER")
    print("Convert between all speed units")
    print("=" * 70 + "\n")


def convert_speed(value: float, from_unit: str) -> dict:
    """
    Convert speed to all common units.
    
    Args:
        value: Speed value
        from_unit: Source unit
        
    Returns:
        Dictionary with all conversions
    """
    try:
        # Normalize unit names
        unit_map = {
            'mph': 'mile/hour', 'mi/h': 'mile/hour', 'mile/hour': 'mile/hour',
            'kmh': 'kilometer/hour', 'km/h': 'kilometer/hour', 'kph': 'kilometer/hour',
            'kilometer/hour': 'kilometer/hour',
            'ms': 'meter/second', 'm/s': 'meter/second', 'meter/second': 'meter/second',
            'knot': 'knot', 'knots': 'knot', 'kt': 'knot',
            'fps': 'foot/second', 'ft/s': 'foot/second', 'foot/second': 'foot/second',
        }
        
        from_unit_normalized = unit_map.get(from_unit.lower())
        if not from_unit_normalized:
            return {
                'success': False,
                'error': f'Unknown unit: {from_unit}',
                'message': 'Use mph, kmh, m/s, knot, or fps'
            }
        
        # Create quantity
        speed = Quantity(value, from_unit_normalized)
        
        # Convert to all common units
        mph = speed.to('mile/hour')
        kmh = speed.to('kilometer/hour')
        ms = speed.to('meter/second')
        knot = speed.to('knot')
        fps = speed.to('foot/second')
        
        # Calculate as fraction of speed of light
        c_fraction = speed.to('meter/second').magnitude / constants.c.magnitude
        
        # Get context
        context = get_speed_context(kmh.magnitude)
        
        return {
            'success': True,
            'original': speed,
            'mph': mph,
            'kmh': kmh,
            'ms': ms,
            'knot': knot,
            'fps': fps,
            'mph_val': mph.magnitude,
            'kmh_val': kmh.magnitude,
            'ms_val': ms.magnitude,
            'knot_val': knot.magnitude,
            'fps_val': fps.magnitude,
            'c_fraction': c_fraction,
            'context': context,
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': f'Failed to convert {value} {from_unit}'
        }


def get_speed_context(kmh: float) -> str:
    """Get real-world context for speed."""
    if kmh < 0:
        return "Negative speed (moving backward)"
    elif kmh == 0:
        return "Stationary (not moving)"
    elif kmh < 5:
        return "Very slow walk"
    elif kmh < 7:
        return "Walking pace"
    elif kmh < 12:
        return "Jogging pace"
    elif kmh < 20:
        return "Running pace"
    elif kmh < 30:
        return "Bicycle speed"
    elif kmh < 50:
        return "City driving"
    elif kmh < 80:
        return "Highway driving"
    elif kmh < 120:
        return "Fast highway driving"
    elif kmh < 200:
        return "Race car speed"
    elif kmh < 300:
        return "High-speed train"
    elif kmh < 500:
        return "Formula 1 / Racing"
    elif kmh < 900:
        return "Jet aircraft cruising"
    elif kmh < 1200:
        return "Speed of sound (Mach 1)"
    elif kmh < 2000:
        return "Supersonic aircraft"
    elif kmh < 10000:
        return "Hypersonic speed"
    elif kmh < 30000:
        return "Orbital velocity"
    elif kmh < 100000:
        return "Escape velocity"
    else:
        return "Extreme velocity"


def display_result(result: dict, show_context: bool = True):
    """Display conversion result."""
    if result['success']:
        print("\n" + "=" * 70)
        print("SPEED CONVERSION")
        print("=" * 70)
        print(f"\nOriginal:         {result['original']}")
        print(f"Miles/hour:       {result['mph']}")
        print(f"Kilometers/hour:  {result['kmh']}")
        print(f"Meters/second:    {result['ms']}")
        print(f"Knots:            {result['knot']}")
        print(f"Feet/second:      {result['fps']}")
        
        if result['c_fraction'] > 0.0001:
            print(f"\nSpeed of light:   {result['c_fraction']:.6f}c")
        
        if show_context:
            print(f"\nContext: {result['context']}")
        
        print("=" * 70 + "\n")
    else:
        print("\n" + "!" * 70)
        print("ERROR")
        print("!" * 70)
        print(f"\n{result['message']}")
        print(f"Error: {result['error']}")
        print("\nSupported units: mph, kmh (km/h), m/s, knot, fps")
        print("!" * 70 + "\n")


def show_reference_table():
    """Show common speed reference points."""
    print("\n" + "=" * 70)
    print("SPEED REFERENCE POINTS")
    print("=" * 70 + "\n")
    
    references = [
        ("Snail", 0.001, "meter/second"),
        ("Walking", 5, "kilometer/hour"),
        ("Jogging", 10, "kilometer/hour"),
        ("Running", 20, "kilometer/hour"),
        ("Usain Bolt (sprint)", 37.6, "kilometer/hour"),
        ("Bicycle", 25, "kilometer/hour"),
        ("City speed limit", 50, "kilometer/hour"),
        ("Highway speed", 100, "kilometer/hour"),
        ("Cheetah", 120, "kilometer/hour"),
        ("High-speed train", 300, "kilometer/hour"),
        ("Formula 1 car", 370, "kilometer/hour"),
        ("Commercial jet", 900, "kilometer/hour"),
        ("Speed of sound", 1235, "kilometer/hour"),
        ("Concorde", 2180, "kilometer/hour"),
        ("Bullet (rifle)", 3000, "kilometer/hour"),
        ("Earth orbit", 28000, "kilometer/hour"),
        ("Escape velocity", 40000, "kilometer/hour"),
        ("Speed of light", 299792458, "meter/second"),
    ]
    
    print(f"{'Description':<25} {'km/h':<15} {'mph':<15} {'m/s':<15}")
    print("-" * 70)
    
    for desc, value, unit in references:
        result = convert_speed(value, unit)
        if result['success']:
            kmh = f"{result['kmh_val']:.1f}"
            mph = f"{result['mph_val']:.1f}"
            ms = f"{result['ms_val']:.1f}"
            print(f"{desc:<25} {kmh:<15} {mph:<15} {ms:<15}")
    
    print("=" * 70 + "\n")


def travel_time_calculator():
    """Calculate travel time for given distance and speed."""
    print("\n" + "=" * 70)
    print("TRAVEL TIME CALCULATOR")
    print("=" * 70 + "\n")
    
    try:
        distance_input = input("Enter distance (e.g., '100 km' or '50 miles'): ").strip()
        speed_input = input("Enter speed (e.g., '60 mph' or '100 kmh'): ").strip()
        
        # Parse distance
        dist_parts = distance_input.split()
        if len(dist_parts) < 2:
            print("Error: Enter both value and unit for distance")
            return
        
        dist_value = float(dist_parts[0])
        dist_unit = dist_parts[1]
        
        # Normalize distance unit
        dist_unit_map = {
            'km': 'kilometer', 'kilometer': 'kilometer', 'kilometers': 'kilometer',
            'mi': 'mile', 'mile': 'mile', 'miles': 'mile',
            'm': 'meter', 'meter': 'meter', 'meters': 'meter',
        }
        dist_unit_normalized = dist_unit_map.get(dist_unit.lower(), dist_unit)
        
        # Parse speed
        speed_parts = speed_input.split()
        if len(speed_parts) < 2:
            print("Error: Enter both value and unit for speed")
            return
        
        speed_value = float(speed_parts[0])
        speed_unit = speed_parts[1]
        
        # Convert to consistent units (km and km/h)
        distance = Quantity(dist_value, dist_unit_normalized)
        distance_km = distance.to('kilometer').magnitude
        
        speed_result = convert_speed(speed_value, speed_unit)
        if not speed_result['success']:
            print(f"Error: {speed_result['error']}")
            return
        
        speed_kmh = speed_result['kmh_val']
        
        # Calculate time
        time_hours = distance_km / speed_kmh
        time_minutes = time_hours * 60
        time_seconds = time_minutes * 60
        
        print(f"\nDistance: {distance}")
        print(f"Speed: {speed_result['kmh']}")
        print(f"\nTravel Time:")
        print(f"  {time_hours:.2f} hours")
        print(f"  {time_minutes:.1f} minutes")
        
        if time_hours >= 1:
            hours = int(time_hours)
            minutes = int((time_hours - hours) * 60)
            print(f"  {hours}h {minutes}min")
        
        print("=" * 70 + "\n")
    
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"Error: {e}")


def interactive_mode():
    """Run interactive conversion mode."""
    print_header()
    print("Interactive Mode")
    print("Commands: 'ref' (reference), 'time' (travel time), 'quit' (exit)\n")
    
    while True:
        try:
            user_input = input("Enter speed (e.g., '60 mph' or '100 kmh'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Speed Converter!")
                break
            
            if user_input.lower() in ['ref', 'reference', 'table']:
                show_reference_table()
                continue
            
            if user_input.lower() in ['time', 'travel']:
                travel_time_calculator()
                continue
            
            if not user_input:
                continue
            
            # Parse input
            parts = user_input.split()
            if len(parts) < 2:
                print("Error: Enter both value and unit (e.g., '60 mph')")
                continue
            
            try:
                value = float(parts[0])
                unit = parts[1]
            except ValueError:
                print("Error: First part must be a number")
                continue
            
            # Convert
            result = convert_speed(value, unit)
            display_result(result)
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")


def main():
    """Main function."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h']:
            print_header()
            print("Usage:")
            print("  python speed_converter.py                # Interactive mode")
            print("  python speed_converter.py --ref          # Show reference table")
            print("  python speed_converter.py <value> <unit> # Direct conversion")
            print("\nExamples:")
            print("  python speed_converter.py 60 mph")
            print("  python speed_converter.py 100 kmh")
            print("  python speed_converter.py 25 m/s")
            print("\nUnits: mph, kmh (km/h), m/s, knot, fps")
            return
        
        elif sys.argv[1] == '--ref':
            show_reference_table()
            return
        
        elif len(sys.argv) >= 3:
            try:
                value = float(sys.argv[1])
                unit = sys.argv[2]
                print_header()
                result = convert_speed(value, unit)
                display_result(result)
            except ValueError:
                print("Error: First argument must be a number")
            return
    
    # Default: interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()
