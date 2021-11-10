#!/usr/bin/env python3
import math

class SimpleCalculator:
    def sum(self, a, b):
        """ Function to add two integers """
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            return "ERROR"

    def subtract(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a - b
        else:
            return "ERROR"

    def multiply(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a * b
        else:
            return "ERROR"

    def divide(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a / b
        elif b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return "ERROR"

    


    	
    	
        
     	
		    			
