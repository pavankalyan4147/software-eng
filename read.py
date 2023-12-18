# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function
def weather_model(x, a, b, c):
    return a * np.power(x, 2) + b * x + c

# Load parameters from the 'parameters.txt' file
parameters = np.loadtxt('parameters.txt')

# Generate x values using NumPy linspace
x_values = np.linspace(-10, 10, 400)

# Create a figure for the plot
plt.figure(figsize=(10, 6))

# Loop through each row in the parameters array
for test in parameters:
    # Extract values for x, a, b, c from the current row
    x, a, b, c = test

    # Calculate y values for the entire range of x values
    y_values = weather_model(x_values, a, b, c)

    # Plot the quadratic function for the entire range
    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')

# Adding labels and title to the plot
plt.title('Quadratic Functions')
plt.xlabel('x')
plt.ylabel('y')

# Displaying the legend
plt.legend()

# Displaying the grid on the plot
plt.grid(True)

# Showing the plot
plt.show()
