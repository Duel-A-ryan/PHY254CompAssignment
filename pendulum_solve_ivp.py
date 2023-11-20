"""
Integrate the pendulum with the scipy.integrate.solve_ivp function
Nicolas Grisouard, University of Toronto, July 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import ellipk


def rhs(time, xvector):
    """ This function is the right hand side of the system of equations
    solved by solve_ivp. Given the array "state" which contains theta
    and thetadot we return the time derivatives of these """

    x1dot = xvector[1]
    x2dot = - np.sin(xvector[0])

    return [x1dot, x2dot]


# Our initial conditions
theta0 = 0.996 * np.pi
thetadot0 = 0.0
T = 4*ellipk(np.sin(theta0/2)**2)  # Period of NL pendulum

start = 0.0  # Initial time
end = 3*T  # Final time: three pendulum periods

# Call solve_ivp with the name of our right hand side function
# and an array of the initial conditions in the same order
# the rhs function expects them in
output = solve_ivp(rhs, [start, end], [theta0, thetadot0], rtol=1e-5)
print(output)  # to show what solve_ivp returns

# Get theta and thetadot out of the solution (returnebd by solve_ivp)
# and calculate the energy
t_out = output.t
theta = output.y[0]
thetadot = output.y[1]
energy = 1 - np.cos(theta) + .5*thetadot**2

# Plot both theta, theta-dot, and the energy
plt.figure(figsize=(6, 6))  # make the figure a bit taller for the 3 plots

plt.subplot(3, 1, 1)
plt.plot(t_out, theta/np.pi)
plt.ylabel(r'$\theta/\pi$')
plt.xlim(start, end)
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t_out, thetadot/np.pi)
plt.ylabel(r'$\dot \theta\tau/\pi$')
plt.xlim(start, end)
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t_out, energy)
plt.ylabel('$E/(mg\ell)$')
plt.xlabel(r'$t/\tau$')
plt.xlim(start, end)
plt.grid()

plt.tight_layout()

plt.show()
