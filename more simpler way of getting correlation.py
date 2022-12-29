# Importing relevent modueles
import numpy as np
import matplotlib.pyplot as plt
# Loading the textfile and reading the data.
# First row is removes by skip row option
my_file = np.loadtxt('sample_11.txt', skiprows=1)
x = my_file[:, 0]
y = my_file[:, 1]
plt.plot(np.log(x), y,label='Correlation curve')
plt.xlabel('r (nm)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Size distribution: sample 1')
plt.legend()
plt.show()
