import numpy as np
import matplotlib.pyplot as plt


def piecewise_linear_fit(data, N):
    # Sort the data points by x values
    sorted_data = sorted(data, key=lambda tup: tup[0])
    sorted_data = np.array(sorted_data)

    if N < 2:
        # Use single linear fit for N < 2
        x = sorted_data[:, 0]
        y = sorted_data[:, 1]
        n = len(x)
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum(x * y)
        sum_x_squared = np.sum(x * x)

        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x * sum_x)
        intercept = (sum_y - slope * sum_x) / n

        result = np.array([[slope, intercept, x[0], x[-1]]])
    else:
        # Initialize the breakpoints
        breakpoints = np.linspace(sorted_data[0, 0], sorted_data[-1, 0], num=N+1)[1:-1]

        # Initialize the result array
        result = np.zeros((N, 4))

        # Perform linear regression for each interval
        for i in range(N):
            if i == 0:
                # First interval: x <= breakpoints[0]
                mask = sorted_data[:, 0] <= breakpoints[0]
            elif i == N - 1:
                # Last interval: x > breakpoints[-1]
                mask = sorted_data[:, 0] > breakpoints[-1]
            else:
                # Middle intervals: breakpoints[i-1] < x <= breakpoints[i]
                mask = (sorted_data[:, 0] > breakpoints[i-1]) & (sorted_data[:, 0] <= breakpoints[i])

            # Subset the data for the current interval
            x_segment = sorted_data[mask, 0]
            y_segment = sorted_data[mask, 1]

            # Perform linear regression on the current interval
            n = len(x_segment)
            sum_x = np.sum(x_segment)
            sum_y = np.sum(y_segment)
            sum_xy = np.sum(x_segment * y_segment)
            sum_x_squared = np.sum(x_segment * x_segment)

            slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x * sum_x)
            intercept = (sum_y - slope * sum_x) / n

            # Store the parameters in the result array
            if i == 0:
                result[i] = [slope, intercept, x_segment[0], breakpoints[0]]
            elif i == N - 1:
                result[i] = [slope, intercept, breakpoints[-1], x_segment[-1]]
            else:
                result[i] = [slope, intercept, breakpoints[i-1], breakpoints[i]]

    return result



data = [(1, 2), (2, 3), (3, 6), (4, 5), (5, 7), (6, 10), (7, 9), (8, 13), (9, 15), (10, 18)]
N = 3

result = piecewise_linear_fit(data, N)


slopes = result[:, 0]
intercepts = result[:, 1]
breakpoints = np.concatenate([[data[0][0]], result[:, 3], [data[-1][0]]])

# Generate the x values for the continuous plot
x = np.linspace(data[0][0], data[-1][0], num=1000)

# Plot the data points and fitted lines
plt.scatter(*zip(*data), color='red', label='Data')
for i in range(N):
    mask = (breakpoints[i] < x) & (x <= breakpoints[i+1])
    x_segment = x[mask]
    plt.plot(x_segment, slopes[i] * x_segment + intercepts[i], label=f'Segment {i+1}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Regression Fit')
plt.legend()
plt.show()

print(result)