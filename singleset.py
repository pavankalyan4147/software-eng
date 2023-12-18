import matplotlib.pyplot as plt
import numpy as np

def weather_model(x, a, b, c):
    return a * x**2 + b * x + c
# Read parameters from the file
with open('parameters.txt', 'r') as f:
    line = f.readline()
    x_specific, a_specific, b_specific, c_specific = map(float, line.split())
# Generate x values using NumPy linspace
x_values = np.linspace(-10, 10, 400)
# Calculate y values for the entire range of x values
y_values = weather_model(x_values, a_specific, b_specific, c_specific)
# Calculate y values for a specific x value
y_specific = weather_model(x_specific, a_specific, b_specific, c_specific)
# Plotting the weather model for the entire range
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'{a_specific}x^2 + {b_specific}x + {c_specific}')

# Plotting the specific point in red
plt.plot(x_specific, y_specific, 'ro', label=f'Specific Point ({x_specific}, {y_specific})')
# Adding labels and title to the plot
plt.title('Quadratic Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()# Displaying the legend
plt.grid(True)# Displaying the grid on the plot
plt.show()# Showing the plot
