import numpy as np
import control
import matplotlib.pyplot as plt

num = np.array([1, 23])
den = np.array([1,1, -1.19])

H = control.tf(num, den)
print("The transfer function is : " ,H)

t, y = control.step_response(H, T=5)
plt.plot(t, y)
plt.show()