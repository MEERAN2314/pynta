"""
Cubic Meter to Meter Converter
===============================

This example converts cubic meters (m³) to meters (m) by calculating
the side length of an equivalent cube. Useful for visualizing volumes
and determining dimensions.

Formula: side_length = ∛(volume)

Author: Unifyt Team
Purpose: Volume to dimension conversion
"""

from unifyt import Quantity
import sys
import math


def print_header():
    """Print application header."""
    print("\n" + "=" * 70)
    print("CUBIC METER TO METER CONVERTER")
    print("Calculate cube side length from volume")
    print("=" * 70 + "\n")


def print_info():
    """Display conversion information."""
    print("How it works:")
    print("-" * 70)
    print("Given a volume in cubic meters (m³), this calculates the side")
    print("length of a cube with that volume.")
    print()
    print("Formula: side_length = ∛(volume)")
    print()
    print("Example: 8 m³ → ∛8 = 2 meters (a 2m × 2m × 2m cube)")
    print("-" * 70 + "\n")


def cubic_meter_to_meter(volume_m3: float) -> dict:
    """
    Convert cubic meters to meters (cube side length).
    
    Args:
        volume_m3: Volume in cubic meters
        
    Returns:
        Dictionary with conversion results
    """
    try:
        if volume_m3 < 0:
            return {
                'success': False,
                'error': 'Volume cannot be negative',
                'message': f'Invalid volume: {volume_m3} m³'
            }
        
        # Calculate cube root to get side length
        side_length_m = volume_m3 ** (1/3)
        
        # Create quantities
        volume = Quantity(volume_m3, 'cubic_meter')
        side_length = Quantity(side_length_m, 'meter')
        
        # Calculate other useful dimensions
        # Surface area of cube: 6 × side²
        surface_area_m2 = 6 * side_length_m ** 2
        surface_area = Quantity(surface_area_m2, 'meter^2')
        
        # Edge length total (12 edges)
        total_edge_length_m = 12 * side_length_m
        total_edge = Quantity(total_edge_length_m, 'meter')
        
        return {
            'success': True,
            'volume': volume,
            'side_length': side_length,
            'side_length_m': side_length_m,
            'surface_area': surface_area,
            'surface_area_m2': surface_area_m2,
            'total_edge': total_edge,
            'total_edge_m': total_edge_length_m,
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': f'Failed to convert {volume_m3} m³ to meters'
        }


def display_result(result: dict, show_details: bool = True):
    """Display conversion result in a formatted way."""
    if result['success']:
        print("\n" + "=" * 70)
        print("CONVERSION RESULT")
        print("=" * 70)
        print(f"\nVolume:        {result['volume']}")
        print(f"Side Length:   {result['side_length']}")
        
        if show_details:
            print(f"\nEquivalent Cube Dimensions:")
            print(f"  Length:  {result['side_length_m']:.4f} m")
            print(f"  Width:   {result['side_length_m']:.4f} m")
            print(f"  Height:  {result['side_length_m']:.4f} m")
            
            print(f"\nAdditional Information:")
            print(f"  Surface Area:     {result['surface_area']}")
            print(f"  Total Edge Length: {result['total_edge']}")
            
            # Show in other units
            side_cm = result['side_length'].to('centimeter')
            side_ft = result['side_length'].to('foot')
            side_in = result['side_length'].to('inch')
            
            print(f"\nSide Length in Other Units:")
            print(f"  {side_cm}")
            print(f"  {side_ft}")
            print(f"  {side_in}")
        
        print("=" * 70 + "\n")
    else:
        print("\n" + "!" * 70)
        print("CONVERSION ERROR")
        print("!" * 70)
        print(f"\nError: {result['error']}")
        print(f"Message: {result['message']}")
        print("\nPlease check:")
        print("  • Volume is a positive number")
        print("  • Volume is in cubic meters")
        print("!" * 70 + "\n")


def batch_convert(volumes: list):
    """
    Convert multiple volumes to side lengths.
    
    Args:
        volumes: List of tuples (volume_m3, description)
    """
    print("\n" + "=" * 70)
    print("BATCH CONVERSION: CUBIC METERS TO METERS")
    print("=" * 70 + "\n")
    
    results = []
    for volume_m3, description in volumes:
        result = cubic_meter_to_meter(volume_m3)
        results.append((description, result))
    
    # Display results in table format
    print(f"{'Description':<30} {'Volume (m³)':<15} {'Side Length (m)':<20}")
    print("-" * 70)
    
    for description, result in results:
        if result['success']:
            volume_str = f"{result['volume'].magnitude:.2f}"
            side_str = f"{result['side_length_m']:.4f}"
            print(f"{description:<30} {volume_str:<15} {side_str:<20}")
        else:
            print(f"{description:<30} {'ERROR':<15} {'N/A':<20}")
    
    print("=" * 70 + "\n")


def interactive_mode():
    """Run interactive conversion mode."""
    print_header()
    print_info()
    print("Interactive Mode - Enter 'info' for help, 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            user_input = input("Enter volume in cubic meters (e.g., '8'): ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using the Cubic Meter to Meter Converter!")
                break
            
            if user_input.lower() in ['info', 'help', 'h', '?']:
                print_info()
                continue
            
            if not user_input:
                continue
            
            # Parse input
            try:
                volume_m3 = float(user_input)
            except ValueError:
                print("Error: Please enter a valid number")
                continue
            
            # Perform conversion
            result = cubic_meter_to_meter(volume_m3)
            display_result(result)
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")


def demo_examples():
    """Demonstrate various volume to dimension conversions."""
    print_header()
    print_info()
    print("DEMONSTRATION: Common Volume to Dimension Conversions\n")
    
    # Example conversions
    examples = [
        # (volume_m3, description)
        (1, 'Unit cube (1m³)'),
        (8, 'Small room'),
        (27, 'Medium room'),
        (64, 'Large room'),
        (125, 'Very large room'),
        (0.001, 'Small box (1 liter)'),
        (0.125, 'Storage box'),
        (1000, 'Small warehouse'),
        (10000, 'Large warehouse'),
        (100, 'Container'),
    ]
    
    batch_convert(examples)
    
    # Detailed examples with context
    print("\nDETAILED EXAMPLES WITH CONTEXT:")
    print("=" * 70 + "\n")
    
    # Example 1: Room volume
    print("Example 1: Bedroom Volume")
    print("-" * 70)
    room_volume = 48  # m³
    result = cubic_meter_to_meter(room_volume)
    if result['success']:
        print(f"Room volume: {room_volume} m³")
        print(f"Equivalent cube side: {result['side_length']}")
        print(f"\nActual room might be:")
        print(f"  6m × 4m × 2m = 48 m³")
        print(f"  8m × 3m × 2m = 48 m³")
        print(f"  4m × 4m × 3m = 48 m³")
        print(f"\nCube equivalent: {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m")
    
    # Example 2: Storage container
    print("\n\nExample 2: Shipping Container")
    print("-" * 70)
    container_volume = 33.2  # m³ (20ft container)
    result = cubic_meter_to_meter(container_volume)
    if result['success']:
        print(f"Container volume: {container_volume} m³")
        print(f"Equivalent cube side: {result['side_length']}")
        print(f"\nActual container dimensions:")
        print(f"  Length: 6.06m, Width: 2.44m, Height: 2.59m")
        print(f"\nCube equivalent: {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m")
    
    # Example 3: Water tank
    print("\n\nExample 3: Water Storage Tank")
    print("-" * 70)
    tank_volume = 10  # m³ (10,000 liters)
    result = cubic_meter_to_meter(tank_volume)
    if result['success']:
        print(f"Tank volume: {tank_volume} m³ (10,000 liters)")
        print(f"Equivalent cube side: {result['side_length']}")
        print(f"\nIf tank is cubic: {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m")
        print(f"Surface area needed: {result['surface_area']}")
    
    # Example 4: Concrete pour
    print("\n\nExample 4: Concrete Volume")
    print("-" * 70)
    concrete_volume = 5  # m³
    result = cubic_meter_to_meter(concrete_volume)
    if result['success']:
        print(f"Concrete volume: {concrete_volume} m³")
        print(f"Equivalent cube side: {result['side_length']}")
        print(f"\nPossible slab dimensions:")
        print(f"  10m × 5m × 0.1m = 5 m³")
        print(f"  20m × 2.5m × 0.1m = 5 m³")
        print(f"\nCube equivalent: {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m")
    
    # Example 5: Small box
    print("\n\nExample 5: Small Package")
    print("-" * 70)
    box_volume = 0.027  # m³ (27 liters)
    result = cubic_meter_to_meter(box_volume)
    if result['success']:
        print(f"Box volume: {box_volume} m³ (27 liters)")
        print(f"Equivalent cube side: {result['side_length']}")
        side_cm = result['side_length'].to('centimeter')
        print(f"In centimeters: {side_cm}")
        print(f"\nCube box: {result['side_length_m']*100:.1f}cm × {result['side_length_m']*100:.1f}cm × {result['side_length_m']*100:.1f}cm")
    
    print("\n" + "=" * 70 + "\n")


def practical_applications():
    """Show practical applications of volume to dimension conversion."""
    print("\n" + "=" * 70)
    print("PRACTICAL APPLICATIONS")
    print("=" * 70 + "\n")
    
    # Application 1: Room sizing
    print("Application 1: Room Design - Visualizing Space")
    print("-" * 70)
    print("Scenario: Determine if a room with 60 m³ volume is adequate")
    
    room_volume = 60  # m³
    result = cubic_meter_to_meter(room_volume)
    
    if result['success']:
        print(f"\nRoom volume: {room_volume} m³")
        print(f"Equivalent cube: {result['side_length_m']:.2f}m per side")
        print(f"\nPossible room configurations:")
        print(f"  • 5m × 4m × 3m = 60 m³ (typical bedroom)")
        print(f"  • 6m × 5m × 2m = 60 m³ (wide, low ceiling)")
        print(f"  • 10m × 3m × 2m = 60 m³ (long, narrow)")
        print(f"\nVisualization: Imagine a cube {result['side_length_m']:.2f}m on each side")
    
    # Application 2: Storage planning
    print("\n\nApplication 2: Warehouse Storage Planning")
    print("-" * 70)
    print("Scenario: Plan storage space for 500 m³ of goods")
    
    storage_volume = 500  # m³
    result = cubic_meter_to_meter(storage_volume)
    
    if result['success']:
        print(f"\nRequired storage: {storage_volume} m³")
        print(f"Equivalent cube: {result['side_length_m']:.2f}m per side")
        print(f"\nWarehouse options:")
        print(f"  • 20m × 10m × 2.5m = 500 m³")
        print(f"  • 25m × 10m × 2m = 500 m³")
        print(f"  • Cube: {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m × {result['side_length_m']:.2f}m")
    
    # Application 3: Tank design
    print("\n\nApplication 3: Water Tank Design")
    print("-" * 70)
    print("Scenario: Design a 15 m³ water tank")
    
    tank_volume = 15  # m³ (15,000 liters)
    result = cubic_meter_to_meter(tank_volume)
    
    if result['success']:
        print(f"\nTank capacity: {tank_volume} m³ (15,000 liters)")
        print(f"Cubic tank side: {result['side_length_m']:.2f}m")
        print(f"Surface area: {result['surface_area_m2']:.2f} m²")
        
        # Calculate cylindrical tank dimensions
        # For cylinder: V = πr²h, if h = 2r (height = diameter)
        # V = πr²(2r) = 2πr³
        # r = ∛(V/(2π))
        radius = (tank_volume / (2 * math.pi)) ** (1/3)
        height = 2 * radius
        
        print(f"\nAlternative cylindrical tank:")
        print(f"  Radius: {radius:.2f}m")
        print(f"  Height: {height:.2f}m (diameter)")
        print(f"  Diameter: {2*radius:.2f}m")
    
    # Application 4: Concrete estimation
    print("\n\nApplication 4: Concrete Pour Estimation")
    print("-" * 70)
    print("Scenario: Visualize 20 m³ of concrete")
    
    concrete_volume = 20  # m³
    result = cubic_meter_to_meter(concrete_volume)
    
    if result['success']:
        print(f"\nConcrete volume: {concrete_volume} m³")
        print(f"Equivalent cube: {result['side_length_m']:.2f}m per side")
        print(f"\nCommon applications:")
        print(f"  • Foundation: 10m × 10m × 0.2m = 20 m³")
        print(f"  • Slab: 20m × 5m × 0.2m = 20 m³")
        print(f"  • Driveway: 15m × 4m × 0.33m = 20 m³")
        print(f"\nVisualization: A cube {result['side_length_m']:.2f}m on each side")
    
    # Application 5: HVAC sizing
    print("\n\nApplication 5: HVAC System Sizing")
    print("-" * 70)
    print("Scenario: Size HVAC for 200 m³ space")
    
    space_volume = 200  # m³
    result = cubic_meter_to_meter(space_volume)
    
    if result['success']:
        print(f"\nSpace volume: {space_volume} m³")
        print(f"Equivalent cube: {result['side_length_m']:.2f}m per side")
        
        # Calculate air changes per hour requirement
        ach = 6  # air changes per hour
        airflow_m3_h = space_volume * ach
        airflow_m3_s = airflow_m3_h / 3600
        
        print(f"\nHVAC requirements (6 ACH):")
        print(f"  Airflow: {airflow_m3_s:.4f} m³/s")
        print(f"  Airflow: {airflow_m3_h:.0f} m³/h")
        print(f"  CFM: {airflow_m3_s / 0.000471947:.0f}")
    
    print("\n" + "=" * 70 + "\n")


def comparison_table():
    """Show comparison table of common volumes."""
    print("\n" + "=" * 70)
    print("QUICK REFERENCE: VOLUME TO CUBE SIDE LENGTH")
    print("=" * 70 + "\n")
    
    volumes = [0.001, 0.01, 0.1, 1, 8, 27, 64, 125, 1000, 10000]
    
    print(f"{'Volume (m³)':<15} {'Liters':<15} {'Side Length (m)':<20} {'Side Length (cm)':<20}")
    print("-" * 70)
    
    for vol in volumes:
        result = cubic_meter_to_meter(vol)
        if result['success']:
            liters = vol * 1000
            side_m = result['side_length_m']
            side_cm = side_m * 100
            print(f"{vol:<15.3f} {liters:<15.1f} {side_m:<20.4f} {side_cm:<20.2f}")
    
    print("=" * 70 + "\n")


def main():
    """Main function to run the converter."""
    if len(sys.argv) > 1:
        # Command-line mode
        if sys.argv[1] in ['--help', '-h']:
            print_header()
            print_info()
            print("\nUsage:")
            print("  python cubic_meter_to_meter.py              # Interactive mode")
            print("  python cubic_meter_to_meter.py --demo       # Run demonstrations")
            print("  python cubic_meter_to_meter.py --apps       # Show applications")
            print("  python cubic_meter_to_meter.py --table      # Show reference table")
            print("  python cubic_meter_to_meter.py <volume>     # Direct conversion")
            print("\nExamples:")
            print("  python cubic_meter_to_meter.py 8")
            print("  python cubic_meter_to_meter.py 27")
            print("  python cubic_meter_to_meter.py 100")
            return
        
        elif sys.argv[1] == '--demo':
            demo_examples()
            return
        
        elif sys.argv[1] == '--apps':
            practical_applications()
            return
        
        elif sys.argv[1] == '--table':
            comparison_table()
            return
        
        else:
            # Direct conversion from command line
            try:
                volume_m3 = float(sys.argv[1])
                print_header()
                result = cubic_meter_to_meter(volume_m3)
                display_result(result)
            except ValueError:
                print("Error: Argument must be a number")
            return
    
    # Default: Run all demonstrations
    demo_examples()
    practical_applications()
    comparison_table()
    
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
