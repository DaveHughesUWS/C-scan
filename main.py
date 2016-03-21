import numpy as np
import matplotlib
import matplotlib.pyplot as plt

cscan = np.genfromtxt("cscan-3.csv",delimiter = ",");

plt.imshow(cscan);
plt.show();