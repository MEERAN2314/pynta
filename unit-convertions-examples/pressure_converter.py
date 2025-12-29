"""
Universal Pressure Converter
=============================

Convert between all common pressure units with real-world applications.
Perfect for weather, engineering, diving, and scientific use.

Author: Unifyt Team
Purpose: Pressure conversion for all users
"""

from unifyt import Quantity, constants
import sys


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("UNIVERSAL PRESSURE CONVERTER")
    print("Convert between all pressure units")
    print("=" * 70 + "\n")


def convert_pressure(value: float, from_unit: str) -> dict:
    """
    Convert pressure to all common units.
    
    Args:
        value: Pressure value
        from_unit: Source unit
        
    Returns:
        Dictionary with all conversions
    """
    try:
        # Normalize unit names
        unit_map = {
            'pa': 'pascal', 'pascal': 'pascal',
            'kpa': 'kilopascal', 'kilopascal': 'kilopascal',
            'mpa': 'megapascal', 'megapascal': 'megapascal',
            'bar': 'bar', 'bars': 'bar',
            'mbar': 'millibar', 'millibar': 'millibar',
            'atm': 'atmosphere', 'atmosphere': 'atmosphere',
            'psi': 'psi', 'pound/inch^2': 'psi',
            'torr': 'torr',
            'mmhg': 'millimeter_mercury', 'millimeter_mercury': 'millimeter_mercury',
            'inhg': 'inch_mercury', 'inch_mercury': 'inch_mercury',
        }
        
        from_unit_normalized = unit_map.get(from_unit.lower())
        if not from_unit_normalized:
            return {
                'success': False,
                'error': f'Unknown unit: {from_unit}',
                'message': 'Use pa, kpa, mpa, bar, atm, psi, torr, mmhg, or inhg'
            }
        
        # Create quantity
        pressure = Quantity(value, from_unit_normalized)
        
        # Convert to all common units
        pa = pressure.to('pascal')
        kpa = pressure.to('kilopascal')
        mpa = pressure.to('megapascal')
        bar = pressure.to('bar')
        atm = pressure.to('atmosphere')
        psi = pressure.to('psi')
        torr = pressure.to('torr')
        mmhg = pressure.to('millimeter_mercury')
        
        # Get context
        context = get_pressure_context(kpa.magnitude)
        
        return {
            'success': True,
            'original': pressure,
            'pa': pa,
            'kpa': kpa,
            'mpa': mpa,
            'bar': bar,
            'atm': atm,
            'psi': psi,
            'torr': torr,
            'mmhg': mmhg,
            'pa_val': pa.magnitude,
            'kpa_val': kpa.magnitude,
            'mpa_val': mpa.magnitude,
            'bar_val': bar.magnitude,
            'atm_val': atm.magnitude,
            'psi_val': psi.magnitude,
            'torr_val': torr.magnitude,
            'mmhg_val': mmhg.magnitude,
            'context': context,
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': f'Failed to convert {value} {from_unit}'
        }


def get_pressure_context(kpa: float) -> str:
    """Get real-world context for pressure."""
    if kpa < 0.001:
        return "Ultra-high vacuum"
    elif kpa < 0.1:
        return "High vacuum"
    elif kpa < 10:
        return "Low pressure / Vacuum"
    elif kpa < 50:
        return "Very low pressure"
    elif kpa < 90:
        return "Low atmospheric pressure (high altitude)"
    elif kpa < 100:
        return "Below standard atmospheric"
    elif kpa == 101.325:
        return "Standard atmospheric pressure (sea level)"
    elif kpa < 110:
        return "Above standard atmospheric"
    elif kpa < 200:
        return "Moderate pressure (tire pressure)"
    elif kpa < 500:
        return "High pressure (industrial)"
    elif kpa < 1000:
        return "Very high pressure"
    elif kpa < 10000:
        return "Extreme pressure (hydraulics)"
    elif kpa < 100000:
        return "Ultra-high pressure (deep ocean)"
    else:
        return "Extreme industrial pressure"


def display_result(result: dict, show_context: bool = True):
    """Display conversion result."""
    if result['success']:
        print("\n" + "=" * 70)
        print("PRESSURE CONVERSION")
        print("=" * 70)
        print(f"\nOriginal:      {result['original']}")
        print(f"Pascal:        {result['pa']}")
        print(f"Kilopascal:    {result['kpa']}")
        print(f"Megapascal:    {result['mpa']}")
        print(f"Bar:           {result['bar']}")
        print(f"Atmosphere:    {result['atm']}")
        print(f"PSI:           {result['psi']}")
        print(f"Torr:          {result['torr']}")
        print(f"mmHg:          {result['mmhg']}")
        
        if show_context:
            print(f"\nContext: {result['context']}")
        
        print("=" * 70 + "\n")
    else:
        print("\n" + "!" * 70)
        print("ERROR")
        print("!" * 70)
        print(f"\n{result['message']}")
        print(f"Error: {result['error']}")
        print("\nSupported units: pa, kpa, mpa, bar, atm, psi, torr, mmhg, inhg")
        print("!" * 70 + "\n")


def show_reference_table():
    """Show common pressure reference points."""
    print("\n" + "=" * 70)
    print("PRESSURE REFERENCE POINTS")
    print("=" * 70 + "\n")
    
    references = [
        ("Perfect vacuum", 0, "pascal"),
        ("Outer space", 0.0001, "pascal"),
        ("High vacuum", 0.1, "pascal"),
        ("Low vacuum", 100, "pascal"),
        ("Mount Everest", 33.7, "kilopascal"),
        ("Airplane cabin", 75, "kilopascal"),
        ("Sea level (standard)", 101.325, "kilopascal"),
        ("Bicycle tire", 400, "kilopascal"),
        ("Car tire", 220, "kilopascal"),
        ("Truck tire", 550, "kilopascal"),
        ("Scuba tank", 20, "megapascal"),
        ("Hydraulic system", 15, "megapascal"),
        ("Water jet cutter", 400, "megapascal"),
        ("Deep ocean (10km)", 100, "megapascal"),
        ("Earth's core", 360, "gigapascal"),
    ]
    
    print(f"{'Description':<25} {'kPa':<15} {'bar':<15} {'psi':<15} {'atm':<15}")
    print("-" * 80)
    
    for desc, value, unit in references:
        result = convert_pressure(value, unit)
        if result['success']:
            kpa = f"{result['kpa_val']:.2f}"
            bar = f"{result['bar_val']:.4f}"
            psi = f"{result['psi_val']:.2f}"
            atm = f"{result['atm_val']:.4f}"
            print(f"{desc:<25} {kpa:<15} {bar:<15} {psi:<15} {atm:<15}")
    
    print("=" * 70 + "\n")


def altitude_pressure_calculator():
    """Calculate pressure at different altitudes."""
    print("\n" + "=" * 70)
    print("ALTITUDE PRESSURE CALCULATOR")
    print("=" * 70 + "\n")
    
    try:
        altitude_input = input("Enter altitude (e.g., '1000 m' or '5000 ft'): ").strip()
        
        # Parse altitude
        parts = altitude_input.split()
        if len(parts) < 2:
            print("Error: Enter both value and unit")
            return
        
        altitude_value = float(parts[0])
        altitude_unit = parts[1]
        
        # Normalize unit
        unit_map = {
            'm': 'meter', 'meter': 'meter', 'meters': 'meter',
            'ft': 'foot', 'foot': 'foot', 'feet': 'foot',
            'km': 'kilometer', 'kilometer': 'kilometer',
        }
        altitude_unit_normalized = unit_map.get(altitude_unit.lower(), altitude_unit)
        
        # Convert to meters
        altitude = Quantity(altitude_value, altitude_unit_normalized)
        altitude_m = altitude.to('meter').magnitude
        
        # Approximate pressure calculation (barometric formula)
        # P = P0 * exp(-Mgh/RT)
        # Simplified: P ≈ P0 * (1 - 0.0065h/288.15)^5.255
        P0 = 101.325  # kPa at sea level
        if altitude_m < 11000:  # Troposphere
            pressure_kpa = P0 * (1 - 0.0065 * altitude_m / 288.15) ** 5.255
        else:  # Stratosphere (simplified)
            pressure_kpa = P0 * 0.2233 * (288.15 / 216.65) ** 5.255
        
        result = convert_pressure(pressure_kpa, 'kilopascal')
        
        print(f"\nAltitude: {altitude}")
        print(f"Altitude: {altitude_m:.0f} meters")
        
        if result['success']:
            print(f"\nEstimated Pressure:")
            print(f"  {result['kpa']}")
            print(f"  {result['bar']}")
            print(f"  {result['psi']}")
            print(f"  {result['atm']}")
            print(f"\nNote: This is an approximation using standard atmosphere model")
        
        print("=" * 70 + "\n")
    
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except Exception as e:
        print(f"Error: {e}")


def tire_pressure_guide():
    """Show tire pressure recommendations."""
    print("\n" + "=" * 70)
    print("TIRE PRESSURE GUIDE")
    print("=" * 70 + "\n")
    
    tire_pressures = [
        ("Bicycle (road)", 100, "psi"),
        ("Bicycle (mountain)", 35, "psi"),
        ("Motorcycle", 36, "psi"),
        ("Passenger car", 32, "psi"),
        ("SUV/Light truck", 35, "psi"),
        ("Heavy truck", 80, "psi"),
        ("Bus", 100, "psi"),
        ("Aircraft (small)", 40, "psi"),
        ("Aircraft (large)", 200, "psi"),
    ]
    
    print(f"{'Vehicle Type':<25} {'PSI':<10} {'kPa':<10} {'bar':<10}")
    print("-" * 55)
    
    for vehicle, value, unit in tire_pressures:
        result = convert_pressure(value, unit)
        if result['success']:
            psi = f"{result['psi_val']:.0f}"
            kpa = f"{result['kpa_val']:.0f}"
            bar = f"{result['bar_val']:.2f}"
            print(f"{vehicle:<25} {psi:<10} {kpa:<10} {bar:<10}")
    
    print("\n" + "=" * 70 + "\n")


def interactive_mode():
    """Run interactive conversion mode."""
    print_header()
    print("Interactive Mode")
    print("Commands: 'ref' (reference), 'alt' (altitude), 'tire' (tire guide), 'quit'\n")
    
    while True:
        try:
            user_input = input("Enter pressure (e.g., '100 kpa' or '14.7 psi'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Pressure Converter!")
                break
            
            if user_input.lower() in ['ref', 'reference', 'table']:
                show_reference_table()
                continue
            
            if user_input.lower() in ['alt', 'altitude']:
                altitude_pressure_calculator()
                continue
            
            if user_input.lower() in ['tire', 'tires']:
                tire_pressure_guide()
                continue
            
            if not user_input:
                continue
            
            # Parse input
            parts = user_input.split()
            if len(parts) < 2:
                print("Error: Enter both value and unit (e.g., '100 kpa')")
                continue
            
            try:
                value = float(parts[0])
                unit = parts[1]
            except ValueError:
                print("Error: First part must be a number")
                continue
            
            # Convert
            result = convert_pressure(value, unit)
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
            print("  python pressure_converter.py                # Interactive mode")
            print("  python pressure_converter.py --ref          # Show reference table")
            print("  python pressure_converter.py --tire         # Show tire pressure guide")
            print("  python pressure_converter.py <value> <unit> # Direct conversion")
            print("\nExamples:")
            print("  python pressure_converter.py 100 kpa")
            print("  python pressure_converter.py 14.7 psi")
            print("  python pressure_converter.py 1 atm")
            print("\nUnits: pa, kpa, mpa, bar, atm, psi, torr, mmhg")
            return
        
        elif sys.argv[1] == '--ref':
            show_reference_table()
            return
        
        elif sys.argv[1] == '--tire':
            tire_pressure_guide()
            return
        
        elif len(sys.argv) >= 3:
            try:
                value = float(sys.argv[1])
                unit = sys.argv[2]
                print_header()
                result = convert_pressure(value, unit)
                display_result(result)
            except ValueError:
                print("Error: First argument must be a number")
            return
    
    # Default: interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()
