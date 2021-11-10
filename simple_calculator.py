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
    def factorial(self , a):
    	if isinstance(a,int):
    		if(a<0):
    			return "ERROR"	
    		fact=1
    		for i in range(2, a+1):
    			fact=fact*i
    		return fact
    	else:
    		return "ERROR"
    		
    def sin(self , a):
    	if isinstance(a,int) or isinstance(a,float):
    		return round(math.sin(math.radians(a)),1)
    	else:
    		return "ERROR"
    
    def cos(self , a):
    	if isinstance(a,int) or isinstance(a,float):
    		return round(math.cos(math.radians(a)),1)
    	else:
    		return "ERROR"
    
    def tan(self , a):
    	if isinstance(a,int) or isinstance(a,float):
    		return round(math.tan(math.radians(a)),1)
    	else:
    		return "ERROR"
    


    	
    	
        
     	
		    			
