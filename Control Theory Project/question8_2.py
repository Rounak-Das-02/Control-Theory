import numpy as np
import control
from control import forced_response
import matplotlib.pyplot as plt

x = 67028.47

# Define the transfer function coefficients
num = [x, 103*x, 1840*x]  # numerator coefficients
den = [1, 363, 360.81 + x , -(430.78-103*x), 1840*x]  # denominator coefficients



# Define the input signal
t = np.linspace(0, 0.3, 1000)  # Time vector
u = np.zeros_like(t)  # Initialize input signal

# Set the input magnitudes
u[t < 0.1] = 0.2  # Magnitude 0.2 until 0.10 seconds
u[(t >= 0.1) & (t < 0.15)] = -0.1  # Magnitude -0.1 from 0.10 to 0.15 seconds
u[t >= 0.15] = 0.05  # Magnitude 0.05 after 0.15 seconds



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

