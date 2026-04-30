import math
from main import calculate_pi


def test_calculate_pi():
    """Test the calculate_pi function"""
    print("Testing calculate_pi function...")
    print("=" * 50)
    
    # Test with 5 decimal places (default)
    result_5 = calculate_pi(5)
    actual_pi_5 = round(math.pi, 5)
    
    print(f"Calculated pi (5 digits): {result_5}")
    print(f"Actual pi (5 digits):     {actual_pi_5}")
    print(f"Match: {result_5 == actual_pi_5}")
    print()
    
    # Test with different precisions
    for precision in [1, 2, 3, 4, 5, 6, 7]:
        result = calculate_pi(precision)
        actual = round(math.pi, precision)
        match = "✓" if result == actual else "✗"
        print(f"Precision {precision}: {result} (expected: {actual}) {match}")
    
    print("=" * 50)
    
    # Verify the 5th digit specifically
    pi_string = str(calculate_pi(5))
    print(f"\nPi to 5 decimal places: {pi_string}")
    print(f"The 5th decimal digit is: {pi_string.split('.')[1][4] if len(pi_string.split('.')[1]) >= 5 else 'N/A'}")
    
    # Expected value
    print(f"\nExpected value: 3.14159")
    print(f"Calculated value: {calculate_pi(5)}")
    
    return result_5 == actual_pi_5


if __name__ == "__main__":
    success = test_calculate_pi()
    print(f"\nTest {'PASSED' if success else 'FAILED'}!")