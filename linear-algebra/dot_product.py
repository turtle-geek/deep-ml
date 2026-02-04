def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	# Time Complexity: O(n*m) where n is the rows and m is the columns
	# Space Complexity: O(m) for resulting matrix being length of column
	if len(a[0]) != len(b):
		return -1
	
	res = []
	for i in range(len(a)):
		sum = 0
		for j in range(len(a[0])):
			sum += a[i][j]*b[j]
		res.append(sum)

	return res

	"""
	Updated solution:
	import numpy as np
	.
	.
	.
	matrix_a = np.array(a)
	matrix_b = np.array(b)

	if matrix_a.shape[1] != matrix_b.shape[0]:
		return -1
	
	return (matrix_a @ matrix_b).tolist()
	
	"""