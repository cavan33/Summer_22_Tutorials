from matplotlib import pyplot as plt
import numpy as np
x = [1, 4, 9, 3, 2, 11, 15, 16, 90, 87, 56, 43, 21, 9, 90, 43]
plt.hist(x, 10)
plt.show()

# Testing savetxt:
# b = np.zeros((500, 500))
# np.savetxt('output.txt', b)
# np.savetxt('output2.txt', b, fmt='%5.2f')