class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        # Handle multiplication using repeated addition
        result = 0
        # Determine if the result should be negative
        is_negative = (a < 0) ^ (b < 0)
        
        # Convert `a` and `b` to positive values by negating if they are negative
        a = a if a >= 0 else -a
        b = b if b >= 0 else -b
        
        for _ in range(b):
            result = self.add(result, a)
        
        # Apply the negative sign if required
        return -result if is_negative else result

    def divide(self, a, b):
        # Handle division using repeated subtraction
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        is_negative = (a < 0) ^ (b < 0)
        
        # Convert `a` and `b` to positive values
        a = a if a >= 0 else -a
        b = b if b >= 0 else -b
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)
        
        return -result if is_negative else result

    def modulo(self, a, b):
        # Handle modulo using repeated subtraction
        if b == 0:
            raise ValueError("Cannot take modulo by zero")
        
        # Convert `a` and `b` to positive values
        a = a if a >= 0 else -a
        b = b if b >= 0 else -b
        
        while a >= b:
            a = self.subtract(a, b)
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))