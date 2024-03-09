#Glossary
#Below is the summary of all the functions and methods that you learned in this lesson:

#Category: General Purpose
#Function/Method	Description
"""
numpy.ndarray.dtype(opens in a new tab)	Return the data-type of the elements of the array. Remember, arrays are homogeneous.
numpy.ndarray.ndim(opens in a new tab)	Return the number of array-dimensions (rank), e.g., it will return 2 for a 4x3 array.
numpy.ndarray.shape(opens in a new tab)	Return a tuple representing the array dimensions, e.g., it will return (rows,columns) for a rank 2 array.
numpy.ndarray.size(opens in a new tab)	Return the number of elements present in the array.
numpy.save(opens in a new tab)	Save an array to .npy (numpy) format.
numpy.load(opens in a new tab)	Load array from the .npy files.
numpy.random.random(opens in a new tab)	Return random floats values from the interval [0.0, 1.0), in a specified shape.
numpy.random.randint(opens in a new tab)	Return random integers from the half-open interval [a, b), in a specified shape.
numpy.random.normal(opens in a new tab)	Return random samples from a Gaussian (normal) distribution.
numpy.random.permutation(opens in a new tab)	Return a randomly permuted sequence from the given list
numpy.reshape(opens in a new tab)
numpy.ndarray.reshape(opens in a new tab)	Returns an array containing the same elements with a new shape, without affecting the the original array.

#Category: Array Creation
#Function/Method	Description
numpy.ones(opens in a new tab)	Return a new array of given shape and type, filled with 1s.
numpy.zeros(opens in a new tab)	Return a new array of given shape and type, filled with 0s.
numpy.full(opens in a new tab)	Return a new array of given shape and type, filled with a specific value.
numpy.eye(opens in a new tab)	Return a 2-D array with 1s on the diagonal and 0s elsewhere.
numpy.diag(opens in a new tab)	Extract the diagonal elements.
numpy.unique(opens in a new tab)	Return the sorted unique elements of an array.
numpy.array(opens in a new tab)	Create an n-dimensional array.
numpy.arange(opens in a new tab)	Return evenly spaced values within a given half-open interval [a, b).
numpy.linspace(opens in a new tab)	Return evenly spaced numbers over a specified interval [a,b].
numpy.ndarray.copy(opens in a new tab)	Returns a copy of the array.

Category: Operating with Elements and Indices
Function/Method	Description
numpy.insert(opens in a new tab)	Insert values along the given axis before the specified indices.
numpy.delete(opens in a new tab)	Return a new array, after deleting sub-arrays along a specified axis.
numpy.append(opens in a new tab)	Append values at the end of the specified array.
numpy.hstack(opens in a new tab)	Return a stacked array formed by stacking the given arrays in sequence horizontally (column-wise).
numpy.vstack(opens in a new tab)	Return a stacked array formed by stacking the given arrays, will be at least 2-D, in sequence vertically (row-wise).
numpy.sort(opens in a new tab)	Return a sorted copy of an array.
numpy.ndarray.sort(opens in a new tab)	Sort an array in-place.

#Category: Set Operations
#Function/Method	Description
numpy.intersect1d(opens in a new tab)	Find the intersection of two arrays.
numpy.setdiff1d(opens in a new tab)	Find the set difference of two arrays.
numpy.union1d(opens in a new tab)	Return the unique, sorted array of values that are in either of the two input arrays.

#Category: Arithmetic and Statistical Operations
#Function/Method	Description
numpy.add(opens in a new tab)	Element-wise add given arrays
numpy.subtract(opens in a new tab)	Subtract arguments of given arrays, element-wise.
numpy.multiply(opens in a new tab)	Multiply arguments of given arrays, element-wise.
numpy.divide(opens in a new tab)	Returns a true division of the inputs, element-wise.
numpy.exp(opens in a new tab)	Calculate the exponential of all elements in the input array.
numpy.power(opens in a new tab)	First array elements raised to powers from second array, element-wise.
numpy.sqrt(opens in a new tab)	Return the non-negative square-root of an array, element-wise.
numpy.ndarray.min(opens in a new tab)	Return the minimum along the specified axis.
numpy.ndarray.max(opens in a new tab)	Return the maximum along a given axis.
numpy.mean(opens in a new tab)
numpy.ndarray.mean(opens in a new tab)	Compute the arithmetic mean along the specified axis.
numpy.median(opens in a new tab)	Compute the median along the specified axis.
"""