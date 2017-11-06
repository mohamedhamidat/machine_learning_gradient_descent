## Gradient Descent Example for Linear Regression
This is a simple UI developed to calculate and plot gradient descent.

In this example, the project demonstrates how the [gradient descent](http://en.wikipedia.org/wiki/Gradient_descent) algorithm may be used to solve a [linear regression](http://en.wikipedia.org/wiki/Linear_regression) problem. A more detailed description of this example can be found [here](https://github.com/mattnedrich/GradientDescentExample).

### Code Requirements
The example code is in Python ([version 2.6](https://www.python.org/doc/versions/) or higher will work). The only other requirement is [NumPy](http://www.numpy.org/).

### Description
This code demonstrates how a gradient descent search may be used to solve the linear regression problem of fitting a line to a set of points. In this problem, we wish to model a set of points using a line. The line model is defined by two parameters - the line's slope `m`, and y-intercept `b`. Gradient descent attemps to find the best values for these parameters, subject to an error function.

You will need to provide a valid file path, delimiter used (, or .) and iteration number. Learning rate is not required. 

### Execution
To run the example, simply run the `main.py` file using Python

```
python main.py
```

