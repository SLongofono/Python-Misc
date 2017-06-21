import numpy as np
import matplotlib.pyplot as plt

# Random values make for crappy fitting
#input_data = 5 * np.random.rand(10,2)

# Make a perfect linear relationship y = 2x
input_data = np.array([
			[1,1],[2,4],[3,6],[4,8],
			[5,10],[6,12],[7,14],[8,16]
			])

# Add in random error
error = np.zeros((8,2))
error[:,1] = 5 * np.random.rand(8).T
input_data = input_data + error

m = len(input_data)
# X is composed of the transpose of a row of 1s and the x values as such:
# [ 1 1 1 1 ]    [ 1 1 ]
# [ 1 2 3 4 ] -> [ 2 1 ]
#                [ 3 1 ]
#                [ 4 1 ]
X = np.array([np.ones(m), input_data[:,0]]).T

# y is composed of the second column of the input data, reshaped to a single
# column.  Since we gave -1 as the first argument to reshape, it will infer
# the amount of rows based on the size of the input.  In this case, that will
# become 4, so we get the 4x1 column matrix with values 6,5,7,and 10
y = np.array(input_data[:,1]).reshape(-1,1)

# Numpy has a built-in solver for scalar linear equations of the form Ax=B.
# numpy.linalg.solve(a,b) expects a square matrix a of coefficients, and an
# ordinate vector b sharing a dimension with a.  The resultant matrix x is
# the exact solution

# If the coefficients happen to violate either condition (not square or
# singular, use numpy.linalg.lstsq() instead to find the "best" solution x

# Here, we use it to solve as such:  [X^t][X][params] = [X^t][y]
params = np.linalg.solve(X.T.dot(X), X.T.dot(y))

# Build a plot
plt.figure(1)
xvals = np.linspace(0,10,2)
yvals = np.array(params[0] + params[1] * xvals)
plt.plot(xvals, yvals.T, color='b')
plt.scatter(input_data[:,0], input_data[:,1], color='r')

# Create labels with the exact and best fit equation
plt.text(0.5, 22, "Exact: y = 2*x", fontsize=10)
plt.text(0.5, 20, "Best Fit: y = {:.2f}*x + {:.2f}".format(float(params[1]), float(params[0])), fontsize=10)


plt.show()

