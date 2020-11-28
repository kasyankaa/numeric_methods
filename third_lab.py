from math import sin, cos, exp


def E(X, G):
    approximate = 1e-5
    p = q = m = 2
    n = 2 * q + 1
    e = [[[0 for _ in range(m)] for _ in range(n + 1)] for _ in range(n + 1)]
    cond = 1
    while cond != 0:
        cond = 0
        for j in range(1, p):  # Початкові ітерації
            for i in range(m):
                X[i] = G[i](X)

        for i in range(m):
            e[0][1][i] = X[i]
        for j in range(2 * q):
            for i in range(m):
                e[j + 1][1][i] = X[i] = G[i](X)
            if j == 0:
                for i in range(m):
                    cond = (cond or (abs(1 - (e[0][1][i] / e[1][1][i]))
                                     * 100 < approximate))
                    if cond == 0:
                        return X

        for k in range(1, n):
            for j in range(n - k):
                V = [e[j + 1][k][i] - e[j][k][i] for i in range(m)]
                _sum = sum([V[i] ** 2 for i in range(m)])
                for i in range(m):
                    e[j][k + 1][i] = e[j + 1][k - 1][i] + V[i] / _sum
        for i in range(m):
            X[i] = e[0][n][i]
    return X


if __name__ == '__main__':
    g = [lambda X: 1 - exp(-X[0]) * cos(X[1]) - X[0],  # 1 - e^(-x1) * cos(x2) - x1 = 0
         lambda X: exp(-X[0]) * sin(X[1]) + 1 - X[1]]  # e^(-x1) * sin(x2) + 1 - x2 = 0
    x = [0.1, 0.1]
    X = E(x, g)
    print('x1:', X[0], ', x2:', X[1])
    print('x1 з рівняння:', g[0](X))
    print('x2 з рівняння:', g[1](X))