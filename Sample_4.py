import math

import numpy as np
import matplotlib.pyplot as plt

k = 1.38e-23
temperature = 298
viscosity = 10 ** -3
theta = np.deg2rad(173)
lamda = 500e-9
# plotting correlation function.
# Correlation function is plotted with tau and G2(x)
sample_41 = np.loadtxt('sample_41.txt', skiprows=1)
x = sample_41[:, 0]
log_x = np.log(x)
tau = sample_41[:, 1]
plt.plot(log_x, tau)
plt.xlabel("Delay time (µs)")
plt.ylabel("G2(t)[Arbitrary units]")
plt.title('Correlation function: sample 4')
plt.savefig('Correlation function sample 4.png')
plt.show()

# size distribution plot
sample_42 = np.loadtxt('sample_42.txt', skiprows=1)
x_value = sample_42[:, 0]
intensity = sample_42[:, 1]
plt.plot(x_value, intensity)
plt.xlabel('r (nm)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Size distribution: sample 4')
plt.savefig('Size distribution sample 4.png')
plt.show()

# Diffusion coefficient
Diff = (k * temperature) / 3 * math.pi * x_value * viscosity
print(Diff)