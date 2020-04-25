import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo


def error(coeficients, data):
	'''
	Parameters
	----------
	coueficients: numpy polyd that represents the polynomial coeficients
	data: 2D array where each point is a point (x, y)
	'''

	# error = [Y - f(X)]^2 where Y is the given result and f(x) is the polynomial aproximation
	error = np.sum((data[:,1] - np.polyval(coeficients, data[:,0])) ** 2)

	return error

def fit_poly(data, error, degree = 3):
	'''
	Parameters
	----------

	data: 2D Array that contains points (x, y)
	error: function that returns the error giving a polynom and the data to fit 
	Returns
	-------
	An polynom coeficients represented numpy polyd
	'''

	# Generate initial guess for line model
	Cguess = np.poly1d(np.ones(degree + 1, dtype = np.float32))

	# Call optimizer to minimize the function error
	result = spo.minimize(error, Cguess, args =(data,),  method= 'SLSQP', options= {'disp': True})

	return np.poly1d(result.x)

def test_run():
	# Defining original line
	l_orig = np.float32([4,2])
	print("Original line is: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))

	# Creating an array of 21 values between 0 and 10 
	Xorig = np.linspace(0, 10, 21)

	# Creating the original estimation of y using our origin line
	Yorig = l_orig[0] * Xorig + l_orig[1]
	plt.plot(Xorig, Yorig,'b--',linewidth = 2.0,label = "Original line")

	# Generating an array of noisy points (normally distributed)
	noise_sigma = 3.0
	noise = np.random.normal(0, noise_sigma, Yorig.shape)
	data = np.asarray([Xorig, Yorig + noise]).T
	print(data)
	plt.plot(data[:,0], data[:,1], 'go', label="Data points")

	# Fitting line to the generated data
	poly_fit = fit_poly(data, error)
	print(poly_fit)
	plt.plot(data[:,0], np.polyval(poly_fit.coeffs, data[:,0]), 'r--', linewidth = 2.0, label = "Fitted polynomial")

	plt.legend(loc='upper left')
	plt.show()





if __name__ == '__main__':
	test_run()