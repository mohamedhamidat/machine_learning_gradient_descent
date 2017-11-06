#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt
from os import path

# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        #1/n sum (y - (mx +b))**2
        #squqred? no negative data and 
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))


def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def get_column(matrix, index):
    return [row[index] for row in matrix]

def plot(points, intercept, slope): 
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('y = {0} b + {1}'.format(intercept, slope), color = 'r')
    x_values = get_column(points, 0)
    y_values = get_column(points, 1)
    abline_values = abline(points, slope, intercept)
    ax.scatter(x_values, y_values)
    ax.plot(x_values, abline_values , 'r')
    plt.show()

def abline(points, slope, intercept):
    """Plot a line from slope and intercept"""
    x_values = get_column(points, 0)
    return [slope * i + intercept for i in x_values]

def get_points(file_name, _delimiter): 
        
    if _delimiter not in [",", "."]: 
        raise ValueError("delimiter not valid (',' , '.')")

    if not path.isfile(file_name): 
        raise IOError(file_name + " not found")
    else: 
        return genfromtxt(file_name, delimiter = _delimiter)

def get_gradient_descent(file_name, learning_rate, delimiter, num_iterations):
    #get dataset
    if type(file_name) != str: 
        raise ValueError("file_name not a valid string")
    
    if not file_name: 
        raise ValueError("file_name should not be null or empty")
    
    if type(num_iterations) != int or not num_iterations: 
        raise ValueError("iterations must be a valid number")
    
    points = get_points(file_name, delimiter)
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    plot(points, b, m)