import numpy as np

matrix = [[8.3, 2.82, 4.1, 1.9],
          [3.92, 8.45, 7.58, 2.46],
          [3.77, 7.41, 8.04, 2.28],
          [2.21, 3.45, 1.69, 6.69]]

matrix = np.array(matrix).reshape(4, 4)
print('\nYour matrix:')
print(matrix)


def pick_nonzero_row(m, k):
    while k < m.shape[0] and not m[k, k]:
        k += 1
    return k


def matrix_max_row(matrix, pivot_index):  # перестановка елементів для вибору головного елемента по стовпцю
    max_element = matrix[pivot_index][pivot_index]
    index_of_max_element = pivot_index
    for index in range(pivot_index + 1, len(matrix)):
        if abs(matrix[pivot_index][index]) > abs(max_element):
            max_element = matrix[pivot_index][index]
            index_of_max_element = index
        if index_of_max_element != pivot_index:
            matrix[pivot_index], matrix[index_of_max_element] = matrix[index_of_max_element], matrix[pivot_index]


def gauss_inverse(matrix, n):
    E = np.eye(n)  # повернення масиву  дввимірного масиву з 1 по діагоналі
    inverse = np.zeros((n, n))  # масив заповнений нулями
    temp = np.zeros((n, n))
    temp1 = np.zeros((n, 1))
    for k in range(n - 1):
        matrix_max_row(matrix, k)
    for l in range(n):
        for i in range(n):
            for j in range(n):
                temp[i][j] = matrix[i][j]
            temp1[i] = E[i][l]
        i = 0
        j = 0
        m = np.column_stack((temp, temp1))  # зʼєднання масивів
        for k in range(n):
            swap_row = pick_nonzero_row(m, k)
            if swap_row != k:
                m[k, :], m[swap_row, :] = m[swap_row, :], np.copy(m[k, :])
            if m[k, k] != 1:
                m[k, :] *= 1 / m[k, k]
            for row in range(k + 1, n):
                m[row, :] -= m[k, :] * m[row, k]
        for k in range(n - 1, 0, -1):
            for row in range(k - 1, -1, -1):
                if m[row, k]:
                    m[row, :] -= m[k, :] * m[row, k]
        xinv = np.hsplit(m, 5)[4]  # розбивання масиву по горизонталі
        i = 0
        for i in range(n):
            inverse[i, l] = xinv[i]
    print("\nInverse matrix: ")
    print(inverse)
    print( )


gauss_inverse(matrix, 4)
