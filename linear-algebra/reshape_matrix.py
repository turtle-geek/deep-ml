import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
    arr = np.array(a)

    if arr.size != new_shape[0]*new_shape[1]:
        return []
    
    return arr.reshape(new_shape).tolist()


    #INCORRECT CODE
    # old_r = len(a)
	# old_c = len(a[0])
	# new_r = new_shape[0]
	# new_c = new_shape[1]
	# if old_r*old_c != new_r*new_c:
	# 	return []

	# res = [[0 for _ in range(new_c)] for _ in range(new_r)]


	# for i in range(old_r):
	# 	for j in range(old_c):
	# 		norm = i*old_c + j
	# 		res[norm // new_c][norm % new_c] = a[i][j]

	# return res