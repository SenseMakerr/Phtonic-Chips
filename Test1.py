import matplotlib.pyplot as plt
import numpy as np

from simphony.connect import connect_s, innerconnect_s
from simphony.libraries import siepic, sipann
from simphony.tools import wl2freq

# First, we'll set up the frequency range we wish to perform the simulation on.
freqs = np.linspace(wl2freq(1600e-9), wl2freq(1500e-9), 2000)

# Get the scattering parameters for each of the elements in our network.
half_ring_left = sipann.HalfRing(
    width=500e-9, thickness=220e-9, radius=10e-6, gap=220e-9
).s_parameters(freqs)
half_ring_right = sipann.HalfRing(
    width=500e-9, thickness=220e-9, radius=10e-6, gap=220e-9
).s_parameters(freqs)
term = siepic.Terminator().s_parameters(freqs)

# CONFIGURATION 1
n1 = connect_s(half_ring_left, 1, half_ring_right, 3)
n2 = innerconnect_s(n1, 2, 4)
n3 = connect_s(n2, 1, term, 0)

# CONFIGURATION 2
m1 = connect_s(half_ring_right, 1, half_ring_left, 3)
m2 = innerconnect_s(m1, 2, 4)
m3 = connect_s(term, 0, m2, 3)

plt.plot(freqs, np.abs(n3[:, 1, 2]) ** 2, "b.")
plt.plot(freqs, np.abs(m3[:, 0, 1]) ** 2, "r--")
plt.tight_layout()
plt.show()