import matplotlib.pylab as pylab

"""
CONSTANTS
"""
time_const = 0.009  # s
time_step = 0.00001  # step_of_time

imin = 1
imax = 2
Lmax = 13
Lmin = 1.3

current_time = 0.0
spline_h = imax - imin

C1 = 0.0024
R1, R2, R3, R4 = 4, 12, 230, 40
L2 = 0.42
t = 1
result_u2 = []
result_uc1 = []
result_i4 = []
result_i2 = []
result_i1 = []
result_u1 = []
result_i3 = []
X_POC = [0, 0, 0]
time = [time_step * i for i in range(t * 100000 + 1)]




def L1_graph(X):
    return L1(X[1])

# spline
b = [
    lambda x: (2 * (x - imin) + spline_h) * ((imax - x) ** 2),
    lambda x: (2 * (imax - x) + spline_h) * ((x - imin) ** 2),
    lambda x: (x - imin) * (imax - x) ** 2,
    lambda x: (x - imax) * (x - imin) ** 2
]


# умова для L1

def L1(i1):
    if i1 <= imin:
        return Lmax
    elif i1 >= imax:
        return Lmin
    else:
        return (b[0](i1) * Lmax + b[1](i1) * Lmin) / (spline_h ** 3) + (b[2](i1) * 0 + b[3](i1) * 0) / spline_h ** 2


# обрахунок U1

def U1(t):
    global time_const
    T = 2 * time_const
    real_time = t - (t // T) * T
    if real_time < time_const:
        return 10
    else:
        return 0


# обрахунок по колу

functions = [
    lambda t, X: (X[1] - (X[0] / R3) - X[2]) / C1,
    lambda t, X: (U1(t) - X[1] * R1 - X[0]) / L1(X[1]),
    lambda t, X: (X[0] - X[2] * (R2 + R4)) / L2
]



#
def krutt_formula(K):
    return 1 / 6 * (K[0] + 4 * K[1] + K[2])


# коефіціенти для рунге кутта

k = [
    lambda t, X, i, coefs: time_step * functions[i](t, X),
    lambda t, X, i, coefs: time_step * functions[i](t + 1 / 3 * time_step,
                                                    [X[p] + 1 / 3 * coefs[0][p] for p in range(len(X))]),
    lambda t, X, i, coefs: time_step * functions[i](t + time_step,
                                                    [X[p] - coefs[0][p] + 2 * coefs[1][p] for p in range(len(X))]),

]


# обрахунок коефіціентів
def calculate_coeficients(previous):
    global current_time
    coef = [[0 for _ in range(3)] for _ in range(3)]
    for row in range(len(coef)):
        for i in range(len(previous)):
            coef[row][i] = k[row](current_time, previous, i, coef)
    return coef


def update_vars_runge_krutta(prev):
    global current_time
    coefs = calculate_coeficients(prev)
    new = []
    for variable in range(len(prev)):
        K = []
        for row in range(3):
            K.append(coefs[row][variable])
        new.append(prev[variable] + krutt_formula(K))
    current_time += time_step
    prev = new
    return new



# creating images
def show(x_ax, y_ax, name):
    pylab.plot(x_ax, y_ax)
    pylab.ylabel(name)
    pylab.xlabel('T')
    pylab.savefig(str(name) + ".png")
    pylab.clf( )


if __name__ == '__main__':

    while current_time < t :
        result_u2.append(X_POC[2] * R4)
        result_uc1.append(X_POC[0])
        result_i4.append(X_POC[2])
        result_i2.append(X_POC[1] - X_POC[0] / R3 - X_POC[2])
        result_i3.append(X_POC[0] / R3)
        result_u1.append(U1(current_time))
        result_i1.append(X_POC[1])
        X_POC = update_vars_runge_krutta(X_POC)

    show(time, result_u2[:], "U2")
    show(time, result_uc1[:], "Uc1")
    show(time, result_i4[:], "I4")
    show(time, result_i2[:], "I2")
    show(time, result_i1[:], "I1")
    show(time, result_u1[:], "U1")
    show(time, result_i3[:], "I3")
    show([strum * 0.001 for strum in range(2500)], [L1(st) for st in [strum * 0.001 for strum in range(2500)]], "L1")
