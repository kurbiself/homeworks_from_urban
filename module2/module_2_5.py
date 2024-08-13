def get_matrix(n: int, m: int, value) -> list:
    """Create a matrix of n x m

    Args:
        n: line size
        m: column size
        value: matrix value

    Returns:
        matrix

    """
    matrix = []
    for i in range(n):
        list_for_matrix = [value for j in range(m)]
        matrix.append(list_for_matrix)
    return matrix


result1 = get_matrix(0, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
