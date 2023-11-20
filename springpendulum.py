"""
Integrate the spring-pendulum with the scipy.integrate.solve_ivp function
Nicolas Grisouard, University of Toronto
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from numpy import *


def rhs(t, xvector, ???):
    x1dot =????
    x2dot =????
    x3dot =????
    x4dot =????

    return [x1dot, x2dot, x3dot, x4dot]


# Define the endtime
end = 50.0  # Define end time

# Our nondimensional parameter
sigma = .25

# My IC's
x0 = 1
y0 = 1
vx0 = 0.0
vy0 = 0.0

# Call solve_ivp
solution = solve_ivp(rhs, [0., end], [x0, vx0, y0, vy0],
                     args=(sigma,), rtol=1e-6)

# Extract the solution
xarray = solution.y[0]
vxarray = solution.y[1]
yarray = solution.y[2]
vyarray = solution.y[3]
time = solution.t

# Plot the solution in subplots
subplot(3, 1, 1)
plot(time, xarray)
xlabel('t')
ylabel('x')

subplot(3, 1, 2)
plot(time, yarray)
xlabel('t')
ylabel('y')

subplot(3, 1, 3, aspect='equal')
plot(xarray, yarray)
xlabel('x')
ylabel('y')
savefig("SpringPendulumtest.pdf")
show()
