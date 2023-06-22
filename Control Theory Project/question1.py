import numpy as np
import control
import matplotlib.pyplot as plt

num = np.array([1, 23])
den = np.array([1,1, -1.19])


# H = control.tf(num, den)

H = control.TransferFunction(num, den)

print("The transfer function is : " ,H)

# t, y = signal.step(H)

poles , zeroes =  control.pzmap(H, plot = True)


plt.show()


## Answer : Open Loop system is unstable because there is an open loop pole at Right hand side plane
## Re(s) > 0