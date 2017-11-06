import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../script')
import gradient_descent

class TestGradientDescent(unittest.TestCase):
    
    ##### set up points #####
    def setUp(self): 
        self.points = [[1, 2], [2,4], [1,2]]
    
    ########## test get_gradient_descent ##############
    def test_get_gradient_descent_should_raise_ValueError_when_file_name_isempty(self): 
        file_name = ""
        with self.assertRaises(ValueError) as error:
            gradient_descent.get_gradient_descent(file_name, 0.0001, ",", 1000)
        self.assertEqual(error.exception.args[0], 'file_name should not be null or empty')

    def test_get_gradient_descent_should_raise_ValueError_when_file_name_isnot_valid(self): 
        file_name = 123
        with self.assertRaises(ValueError) as error:
            gradient_descent.get_gradient_descent(11, 0.0001, ",", 1000)
        self.assertEqual(error.exception.args[0], 'file_name not a valid string')
    
    def test_get_gradient_descent_should_raise_ValueError_when_iterations_arenot_valid(self): 
        iterations = ""
        with self.assertRaises(ValueError) as error:
            gradient_descent.get_gradient_descent("filename", 0.0001, ",", iterations)
        self.assertEqual(error.exception.args[0], 'iterations must be a valid number')
    
    ########## test get_points ##############

    def test_get_points_should_raise_IOError_when_file_not_found(self): 
        file_name = "filedoesnotexisits.txt"
        with self.assertRaises(IOError) as error:
            gradient_descent.get_points(file_name, ",")
        self.assertEqual(error.exception.args[0], file_name + " not found")   

    def test_get_points_should_raise_ValueError_when_delimiter_not_valid(self): 
        delimiter = ""
        with self.assertRaises(ValueError) as error:
            gradient_descent.get_points("filename", delimiter)
        self.assertEqual(error.exception.args[0], "delimiter not valid (',' , '.')") 

    ####### test abline #######
    def test_abline(self): 
        result = gradient_descent.abline(self.points, 1, 1)
        self.assertEqual(result , [2, 3, 2])  

    ###### test get_column ####(
    def test_get_column(self):
        results = gradient_descent.get_column(self.points, 0)
        self.assertEqual(results, [1, 2, 1])