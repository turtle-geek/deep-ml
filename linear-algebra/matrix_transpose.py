def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Time Complexity: O(n*m) where n is rows and m is columns
    # Space Complexity: O(m*n) where m is rows and n is columns
    res = [[0 for _ in a] for _ in a[0]] # list comprehension
    for i in range (len(a)):
        for j in range(len(a[0])):
            res[j][i] = a[i][j]
    return res
