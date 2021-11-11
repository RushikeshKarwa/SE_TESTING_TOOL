#!/usr/bin/env python3
import unittest
from simple_calculator import SimpleCalculator


class AdditionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        result = self.calculator.sum(5, "6")
        self.assertEqual(result, 11 ,"This will throw error cannot add string and no")

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)


class SubtractionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_substration_two_integers(self):
        result = self.calculator.subtract(6, 5)
        self.assertEqual(result, 1)

    def test_subtraction_integer_string(self):
        result = self.calculator.subtract(5, "6")
        self.assertEqual(result,"ERROR")

    def test_subtraction_negative_integers(self):
        result = self.calculator.subtract(-5, -6)
        self.assertEqual(result, 2,"Test case failed")
        self.assertNotEqual(result, -11)        


class MultiplicationTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_multiplication_two_integers(self):
        result = self.calculator.multiply(6, 5)
        self.assertEqual(result, 20,"Test case Failed")

    def test_multiplication_integer_string(self):
        result = self.calculator.subtract(5, "6")
        self.assertEqual(result, "ERROR")

    def test_multiplication_negative_integers(self):
        result = self.calculator.multiply(-5, -6)
        self.assertEqual(result, 30)
        self.assertNotEqual(result, -30)         


class DivisionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_division_two_integers(self):
        result = self.calculator.divide(30, 5)
        self.assertEqual(result, 6)

    def test_division_integer_string(self):
        result = self.calculator.divide(5, "6")
        self.assertEqual(result, "ERROR")

    def test_division_negative_integers(self):
        result = self.calculator.divide(-30, -6)
        self.assertEqual(result, 5)
        self.assertNotEqual(result, 5,"Test Case Failed")  

    def test_divide_by_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)
            
class FactorialTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_zero(self):
        result = self.calculator.factorial(0)
        self.assertEqual(result, 1)
    
    def test_one(self):
    	result = self.calculator.factorial(1)
    	self.assertEqual(result, 1)
    
    def test_no_greater_than_one(self):
    	result = self.calculator.factorial(5)
    	self.assertEqual(result, 120)
    
    def test_negative_no(self):
    	result = self.calculator.factorial(-5)
    	self.assertEqual(result, "120","Factorial for negative no is not defined")
    
    def test_integer_string(self):
    	result = self.calculator.factorial("10")
    	self.assertEqual(result, "ERROR")
    	
class SineTestSuite(unittest.TestCase):
	def setUp(self):
        	""" Executed before every test case """
        	self.calculator = SimpleCalculator()
        
	def test_thirty(self):
        	result = self.calculator.sin(30)
        	self.assertEqual(result, 0.5)
        	
	def test_ninty(self):
		result = self.calculator.sin(90)
		self.assertEqual(result, 1)
	
	def test_negative(self):
		result = self.calculator.sin(-90)
		self.assertEqual(result, -1)
	
	def test_float(self):
		result= self.calculator.sin(50.55)
		self.assertEqual(result, 0.8)
		
	def test_string(self):
		result=self.calculator.sin("35")
		self.assertEqual(result,"ERROR")
		
class CosineTestSuite(unittest.TestCase):
	def setUp(self):
        	""" Executed before every test case """
        	self.calculator = SimpleCalculator()
        
	def test_thirty(self):
        	result = self.calculator.cos(30)
        	self.assertEqual(result, 0.9)
        	
	def test_ninty(self):
		result = self.calculator.cos(90)
		self.assertEqual(result, 0.0)
	
	def test_negative(self):
		result = self.calculator.cos(-90)
		self.assertEqual(result, 0.0)
	
	def test_float(self):
		result= self.calculator.cos(50.55)
		self.assertEqual(result, 0.6)
		
	def test_string(self):
		result=self.calculator.cos("35")
		self.assertEqual(result,"ERROR")
		
class TanTestSuite(unittest.TestCase):
	def setUp(self):
        	""" Executed before every test case """
        	self.calculator = SimpleCalculator()
        
	def test_thirty(self):
        	result = self.calculator.tan(30)
        	self.assertEqual(result, 0.6)
        	
	def test_forty_five(self):
		result = self.calculator.tan(45)
		self.assertEqual(result, 1)
	
	def test_negative(self):
		result = self.calculator.tan(-45)
		self.assertEqual(result, -1)
	
	def test_float(self):
		result= self.calculator.tan(50.55)
		self.assertEqual(result, 1.2)
		
	def test_string(self):
		result=self.calculator.tan("35")
		self.assertEqual(result,"ERROR")

class SqrtTestSuite(unittest.TestCase):
	def setUp(self):
        	""" Executed before every test case """
        	self.calculator = SimpleCalculator()
        
	def test_positive(self):
        	result = self.calculator.sqrt(30)
        	self.assertEqual(result, 5.5)
        	
	def test_zero(self):
		result = self.calculator.sqrt(0)
		self.assertEqual(result, 0.0)
	
	def test_negative(self):
		result = self.calculator.sqrt(-45)
		self.assertEqual(result, "ERROR")
	
	def test_float(self):
		result= self.calculator.sqrt(50.55)
		self.assertEqual(result, 7.1)
		
class logTestSuite(unittest.TestCase):
	def setUp(self):
        	""" Executed before every test case """
        	self.calculator = SimpleCalculator()
        
	def test_positive(self):
        	result = self.calculator.log(30)
        	self.assertEqual(result, 3.4)
        	
	def test_zero(self):
		result = self.calculator.log(0)
		self.assertEqual(result, "ERROR")
	
	def test_negative(self):
		result = self.calculator.log(-45)
		self.assertEqual(result, "ERROR")
	
	def test_float(self):
		result= self.calculator.log(50.55)
		self.assertEqual(result, 3.9)
		
		
				

if __name__ == "__main__":
    unittest.main()
