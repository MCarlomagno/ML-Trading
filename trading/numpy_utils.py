import numpy as np
import time

def test_run():
	'''
	Test run function
	'''
	arithmetic_operations()

def creating_arrays():
	# creating simple [1,2,3] array
	print(np.array([1,2,3]))

	# creating matrix (it could be also created with list of tuples)
	print(np.array([[1,2,3],[4,5,6]]))

	# creating an empty array with default lenght
	print(np.empty(6))

	# creating an empty matrix with default n and m
	print(np.empty((6,4)))	

	print(np.ones((3,4)))

	print(np.zeros((3,4)))

	print(np.random.random((1,3)))

	#Normal distribution with mean 50 and std 10
	print(np.random.normal(50, 10, size=(1,3)))

	#random integers array between 1 and 10 (size 5)
	print(np.random.randint(1,10, size=5))

def array_atributes():
	array = np.random.random((2,3))

	# array dimensions values
	print(array.shape)

	#array dimensions quantity
	print(len(array.shape))

	#array elements quantity (dimensions product)
	print(array.size)

	#array datatype
	print(array.dtype)

def array_operations():

	#sets the seed of random numbers (always will generate the same random numbers)
	np.random.seed(659)

	array = np.random.randint(1,20, size=(5,4))

	element = array[2,3]
	array[2,3]=1

	# assign 1 values to all the columns in row 2
	array[2,:] = 1

	# assing array of values to some row
	array[2,:] = [1,2,3,4]

	# accessing to many array indexes at the same time
	indexes = [1,1,2]
	print(array[indexes])

	print(element)

	print(array.sum(axis=0))
	print(array.sum(axis=1))

	print(array.max(axis=0))
	print(array.min(axis=1))

	print(array.mean(axis=0))
	print(array.mean(axis=1))

	# gets the index of the max value
	array.argmax()


	print(array)

def array_accessing():
	np.random.seed(659)

	array = np.random.randint(1,20, size=(5,4))

	element = array[2,3]
	array[2,3]=1

	# assign 1 values to all the columns in row 2
	array[2,:] = 1

	# assing array of values to some row
	array[2,:] = [1,2,3,4]

	# accessing to many array indexes at the same time
	indexes = [1,1,2]
	print(array[indexes])


	mean = array.mean()

	# selecting values lesser than mean
	lesser_than_mean = array[array<mean]
	print(lesser_than_mean)

	# assigning mean to values lesser than mean
	print(array)
	array[array<mean] = mean
	print(array)

	print(element)

def time_mesure():
	t1 = time.time()
	t2 = time.time()
	print("Time mesured in the operation: " + str(t1 - t2) + " seconds")

def array_slicing():
	array = np.random.randint(1,20, size=(5,4))

	element = array[2,3]

	sliced_array = array[2,:2]
	print(sliced_array)

	# slice notation from:to:step_size
	sliced_array = array[2,1:2:1]

def arithmetic_operations():
	array = np.array([(1,2,3,4,5),(6,7,8,9,10)])

	# miltiply all elements x 2
	print(2*array)

	# divide all the elements by 2 obtaining integer values
	print(array/2)

	# divide all the elements by 2 obtaining float values
	print(array/2.0)

	#multiply arrays (with same dimensions) element by element
	print(array*array)

	#divide arrays (with same dimensions) element by element
	print(array/array)


if __name__ == '__main__':
	test_run()