import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo


def error(line, data):
	'''
	Parameters
	----------
	line: tuple with two elements (C0, C1) that represents the linear function parameters: y = C0*x + C1
	data: 2D array where each point is a point (x, y)
	'''

	# error = [Y - f(X)]^2 where Y is the given result and f(x) is the computed result by the line 
	error = np.sum((data[:,1] - (line[0] * data[:,0] + line[1]))**2)

	return error

def fit_line(data, error):
	'''
	Parameters
	----------

	data: 2D Array that contains points (x, y)
	error: function that returns the error giving a line and the data to fit 
	Returns
	-------
	A line represented by a tuple with (C0 ,C1)
	'''

	# Generate initial guess for line model
	l = np.float32([0, np.mean(data[:,1])])

	# Call optimizer to minimize the function error
	result = spo.minimize(error, l, args =(data,),  method= 'SLSQP', options= {'disp': True})

	return result.x

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
	l_fit = fit_line(data, error)
	print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
	plt.plot(data[:,0], data[:,0] * l_fit[0] + l_fit[1] , 'r--', linewidth = 2.0, label = "Fitted line")

	plt.legend(loc='upper left')
	plt.show()





if __name__ == '__main__':
	test_run()