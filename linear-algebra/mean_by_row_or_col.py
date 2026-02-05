import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	np_matrix = np.asarray(matrix)

	if mode == "row":
		ax = 1
	else:
		ax = 0
		
	return np_matrix.mean(axis=ax).tolist()