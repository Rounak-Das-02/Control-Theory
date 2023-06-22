import numpy as np
import matplotlib.pyplot as plt
import control

x = 67028.47

# Define the transfer function coefficients
num = [x, 103*x, 1840*x]  # numerator coefficients
den = [1, 363, 360.81 + x , -(430.78-103*x), 1840*x]  # denominator coefficients

# Create the transfer function
G = control.TransferFunction(num, den)

# Generate the step input
t = np.linspace(0, 2, 1000)  # time vector
u = np.ones_like(t)  # step input vector

# Simulate the closed-loop system
t, y = control.step_response(G, T=t, input=u)

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()