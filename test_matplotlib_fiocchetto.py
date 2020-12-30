import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,13,21,10,10,22,24,23,11,17,33,99])
y = np.array([99,33,17,11,23,24,22,10,10,21,13,5])

# considerando che i numeri erano casuali avresti dovuto ordinare almeno le x, 
# oppure il fiocchetto era voluto?

x.sort()
plt.plot(x,y)
plt.show()