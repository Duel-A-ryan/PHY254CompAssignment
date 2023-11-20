"""This program finds the roots of sub-sampled sin signals by interpolation

Nicolas Grisouard, University of Toronto, August 2021
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def find_zeros(signal, time):
    """ Find zeros of signal, interpolated for better accuracy, when
    dsignal/dt>0. """
    time_record = []  # empty list; easier when we don't know the size
    for ii in range(len(time)-1):  # Scan through y to find zeros
        if signal[ii] < 0 and signal[ii+1] > 0:  # then d(sin)/dt > 0
            # create interpolation fct that linearly interpolates t vs. sin(x)
            # between these two points; 'linear' is actually default, but any
            # higher order might be ambiguous if zeros are close together.
            interp_t = interp1d(signal[ii:ii+2], time[ii:ii+2], kind='linear')
            time_record.append(interp_t(0.0))

    return np.array(time_record)  # convert to numpy array


# some array that doesn't include 0, pi, 2*pi...
t = np.linspace(0.1, 20., 30)
x = np.sin(t)  # never exactly zero

# Let's plot to see how gross the signal looks like
plt.figure()
plt.plot(t, x, '+-')
plt.axhline(0., color='k')  # to mark 0
plt.xlabel('$t$')
plt.ylabel(r'$x = \sin(t)$')

# Find all zero-crossings when d(sin(t))/dt > 0; see function
root_times = find_zeros(x, t)

# Check that the function are more-or-less zero at the root_times
x_at_root_times = np.sin(root_times)

for ii in range(len(root_times)):
    print("Found root t/pi = {}".format(root_times[ii]/np.pi))
    # to show on graph where the root is
    plt.axvline(root_times[ii], color='r')

plt.show()
