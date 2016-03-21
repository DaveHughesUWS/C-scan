import numpy as np
import matplotlib
import matplotlib.pyplot as plt

cscan = np.genfromtxt("cscan.csv",delimiter = ",");

plt.imshow(cscan);
plt.show();