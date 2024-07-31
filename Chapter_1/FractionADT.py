import math

class Fraction:
    """
    Represents a fraction as a pair of integers, where the first integer is the numerator and the second integer is the denominator.
    
    The class provides methods for arithmetic operations (+, -, *, /), comparisons (<, <=, ==, !=, >, >=), and simplifying the fraction to its lowest terms.
    
    Attributes:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.
    """
    def __init__(self, *args):
        """
        Initializes a Fraction instance.
        
        Args:
            *args: A variable number of arguments. Accepts either two integers representing the numerator and denominator directly,
                   or a single float which is converted to a fraction with a large enough denominator to represent the float accurately.
                   
        Raises:
            ValueError: If the denominator is zero, or if the number of arguments is not one or two, or if the argument types are invalid.
        """
        if len(args) == 2:
            numerator, denominator = args
            if denominator == 0:
                raise ValueError("Denominator cannot be zero")
            self.numerator = numerator
            self.denominator = denominator
        elif len(args) == 1:
            value = args[0]
            if isinstance(value, float):
                numerator = int(value * 1000000)
                denominator = 1000000
                self.numerator = numerator
                self.denominator = denominator
            else:
                raise ValueError("Invalid argument type")
        else:
            raise ValueError("Invalid number of arguments")
        self.simplify()

    def __float__(self):
        """
        Returns the float representation of the fraction.

        Returns:
            float: The float equivalent of the fraction.
        """
        return self.numerator / self.denominator

    def __add__(self, other):
        """
        Adds two fractions together.

        Args:
            other (Fraction): The fraction to add to the current instance.
            
        Returns:
            Fraction: The result of adding the two fractions.
        """
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """
        Subtracts one fraction from another.

        Args:
            other (Fraction): The fraction to subtract from the current instance.
            
        Returns:
            Fraction: The result of subtracting the two fractions.
        """
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """
        Multiplies two fractions together.

        Args:
            other (Fraction): The fraction to multiply with the current instance.
            
        Returns:
            Fraction: The result of multiplying the two fractions.
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """
        Divides one fraction by another.

        Args:
            other (Fraction): The fraction to divide by the current instance.
            
        Returns:
            Fraction: The result of dividing the two fractions.
        """
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """
        Checks if two fractions are equal.

        Args:
            other (Fraction): The fraction to compare with the current instance.
            
        Returns:
            bool: True if the fractions are equal, False otherwise.
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        """
        Checks if the current fraction is less than another fraction.

        Args:
            other (Fraction): The fraction to compare with the current instance.
            
        Returns:
            bool: True if the current fraction is less than the other, False otherwise.
        """
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        """
        Checks if the current fraction is less than or equal to another fraction.

        Args:
            other (Fraction): The fraction to compare with the current instance.
            
        Returns:
            bool: True if the current fraction is less than or equal to the other, False otherwise.
        """
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        """
        Checks if the current fraction is greater than another fraction.

        Args:
            other (Fraction): The fraction to compare with the current instance.
            
        Returns:
            bool: True if the current fraction is greater than the other, False otherwise.
        """
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        """
        Checks if the current fraction is greater than or equal to another fraction.

        Args:
            other (Fraction): The fraction to compare with the current instance.
            
        Returns:
            bool: True if the current fraction is greater than or equal to the other, False otherwise.
        """
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def simplify(self):
        """
        Simplifies the fraction to its lowest terms by dividing both the numerator and denominator by their greatest common divisor (GCD).
        """
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __repr__(self) -> str:
        """
        Provides a string representation of the fraction.

        Returns:
            str: A string representation of the fraction in the format "numerator/denominator".
        """
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    # Example 1: Demonstrating arithmetic operations between fractions
    print("Example 1: Arithmetic Operations")
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    
    print(f"Adding {frac1} and {frac2}: {frac1 + frac2}")
    print(f"Subtracting {frac2} from {frac1}: {frac1 - frac2}")
    print(f"Multiplying {frac1} and {frac2}: {frac1 * frac2}")
    print(f"Dividing {frac1} by {frac2}: {frac1 / frac2}")

    # Example 2: Demonstrating comparison operations between fractions
    print("\nExample 2: Comparison Operations")
    print(f"{frac1} is equal to {frac2}: {frac1 == frac2}")
    print(f"{frac1} is less than {frac2}: {frac1 < frac2}")
    print(f"{frac1} is greater than {frac2}: {frac1 > frac2}")

    # Example 3: Demonstrating simplification of fractions
    print("\nExample 3: Simplification of Fractions")
    frac3 = Fraction(4, 8)
    frac4 = Fraction(0.3)

    print(f"Fraction created from a floating point number 0.3: {frac4}")
    
    print(f"Simplified form of 4/8: {frac3}")
