import numpy as np
import control
from control import forced_response
import matplotlib.pyplot as plt

x = 67028.47

# Define the transfer function coefficients
num = [x, 103*x, 1840*x]  # numerator coefficients
den = [1, 363, 360.81 + x , -(430.78-103*x), 1840*x]  # denominator coefficients



# Define the input signal
t = np.linspace(0, 1, 1000)  # Time vector
u = np.sin(200 * t)  # Input signal



H = control.tf(num, den)
print("The transfer function is : " ,H)


# Simulate the response
t, y = forced_response(H, T=t, U=u)

# Plot the input and output signals
plt.figure()
plt.plot(t, u, label='Input: sin(200t)')
plt.plot(t, y, label='Output')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()