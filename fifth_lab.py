from math import sin, pi

import matplotlib.pyplot as pyplot

class ImplicitEulerMethod:

   def __init__(self):
       self.U_max = 100
       self.f = 50
       self.R1 =5
       self.R2 = 4
       self.R3 = 7
       self.C1= 0.0003
       self.C2= 0.00015
       self.L1 = 0.01
       self.end_time = 0.5
       self.h = 0.00001
       self.U1 = lambda t: self.U_max * sin(2 * pi * self.f * t)

       self.F = [
           lambda x, t: ((self.U1(t) - x[0] - x[1] * self.R2 - x[2]) /( self.R1 + self.R2))/self.C1,
           lambda x, t: (((self.U1(t) - x[0] - x[1] * self.R2 - x[2]) /( self.R1 + self.R2))-x[1])/ self.L1,
           lambda x, t:  ((((self.U1(t) - x[0] - x[1] * self.R2 - x[2]) /( self.R1 + self.R2))-x[1])-(x[2]/self.R3)) / self.C2 ]

   def calculate_voltage_u2(self):
       times = [i * self.h for i in range(int(self.end_time / self.h))]
       X = [0, 0, 0]
       time = self.h
       result = []

       while time < self.end_time:
           for i in range(len(X)):
               X[i] += self.h * self.F[i](X, time)
           result.append(X[2] )

           time += self.h
       print(X, "\n")

       print("result U2: ", X[2])

       pyplot.plot(times, result)
       pyplot.xlabel("Time - t")
       pyplot.ylabel("Voltage - U2")
       pyplot.show()

if __name__ == '__main__':
   circuit = ImplicitEulerMethod()
   circuit.calculate_voltage_u2()
