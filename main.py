def greetings():
    print("Hello there!")


def calculate_pi(precision=5):
    """
    Calculate pi to a specified number of decimal digits using the Machin formula.
    
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    This converges much faster than the Leibniz formula.
    
    Args:
        precision (int): Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi rounded to the specified precision
    """
    from decimal import Decimal, getcontext
    
    # Set precision higher than needed for accuracy
    getcontext().prec = precision + 10
    
    def arctan(x, num_terms=100):
        """Calculate arctan(x) using Taylor series"""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5), 100) - arctan(Decimal(1) / Decimal(239), 100))
    
    # Round to the specified precision
    return round(float(pi), precision)