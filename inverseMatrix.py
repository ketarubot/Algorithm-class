from decimal import Decimal

# 상수배 행렬
def scalar_mult_matrix(A, k):
    temp_matrix = []
    for row in A:
        temp = []
        for el in row:
            temp.append(Decimal(str(el))*Decimal(str(k)))
        temp_matrix.append(temp)
    return temp_matrix

# 행렬곱
def multiply_matrix(A, B):
    if not isinstance(A, list):
        return scalar_mult_matrix(B, A)
    if not isinstance(B, list):
        return scalar_mult_matrix(A, B)
    if len(A[0]) != len(B):
        raise ArithmeticError('Cannot multiply: incompatible matrix dimensions (A.columns ≠ B.rows).')
    temp_matrix = []
    for row in range(len(A)):
        temp = []
        for col_B in range(len(B[0])):
            value = 0
            for col_A in range(len(A[0])):
                value += A[row][col_A] * B[col_A][col_B]
            temp.append(value)
        temp_matrix.append(temp)
    return temp_matrix

# 전치행렬 반환
def transposed_matrix(matrix):
    temp_matrix = []
    n = len(matrix)
    for row in range(n):
        temp = []
        for col in range(n):
            temp.append(matrix[col][row])
        temp_matrix.append(temp)
    return temp_matrix

# 소행렬 반환
def minor_matrix(matrix, ignore_row, ignore_col):
    temp_matrix = []
    n = len(matrix)
    for row in range(n):
        if row == ignore_row: continue
        temp = []
        for col in range(n):
            if col == ignore_col: continue
            temp.append(matrix[row][col])
        temp_matrix.append(temp)
    return temp_matrix

# 여인수행렬 반환
def cofactor_matrix(matrix):
    temp_matrix = []
    n = len(matrix)
    for row in range(n):
        temp = []
        for col in range(n):
            sign = 1 if (row+col+2)%2 == 0 else -1
            cofactor = sign * det(minor_matrix(matrix, row, col))
            temp.append(cofactor)
        temp_matrix.append(temp)
    return temp_matrix

# 행렬식 반환
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        result = 0
        row = 0
        for col in range(n):
            curr = (1 if col % 2 == 0 else -1) * matrix[row][col]
            deter = det(minor_matrix(matrix, row, col))
            result += curr * deter
        return result

# 수반행렬 반환
def adj(matrix):
    return transposed_matrix(cofactor_matrix((matrix)))

# 역행렬 반환
def invert_matrix(matrix):
    det_matrix = det(matrix)
    if det_matrix == 0:
        raise ArithmeticError('Cannot compute the inverse: the determinant is zero.')
    return multiply_matrix(adj(matrix), 1/det_matrix)

# Decimal 처리
def clean_matrix(matrix, tol=Decimal("1e-15")):
    cleaned = []
    for row in matrix:
        new_row = []
        for x in row:
            if abs(x) < tol:
                new_row.append(Decimal("0"))
            elif abs(x - Decimal("1")) < tol:
                new_row.append(Decimal("1"))
            else:
                new_row.append(x)
        cleaned.append(new_row)
    return cleaned

# 행렬 깔끔하게 출력
def pprint_matrix(matrix):
    cleaned_matrix = clean_matrix(matrix)
    for row in cleaned_matrix:
        print(' '.join(map(str, row)))

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

inverted_matrix = invert_matrix(matrix)
pprint_matrix(inverted_matrix)

I = multiply_matrix(matrix, inverted_matrix) # 행렬 * 역행렬 = 단위행렬
pprint_matrix(I)