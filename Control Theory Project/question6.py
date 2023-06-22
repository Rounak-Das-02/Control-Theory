import control
import matplotlib.pyplot as plt

x = 67028.47

# Define the transfer function coefficients
num = [x, 103*x, 1840*x]  # numerator coefficients
den = [1, 363, 360.81 + x , -(430.78-103*x), 1840*x]  # denominator coefficients

H = control.TransferFunction(num, den)

print("The transfer function is : " ,H)

poles , zeroes =  control.pzmap(H, plot = True)

plt.show()