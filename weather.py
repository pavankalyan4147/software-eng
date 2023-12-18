# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Coefficients for the quadratic equation: ax^2 + bx + c
a = 0.5
b = 2
c = 1

# Define the weather model equation
def weather_model(x):
    return a * x**2 + b * x + c

# Generate x values using NumPy linspace
x_values = np.linspace(-10, 10, 100)  

# Calculate corresponding y values using the weather_model function
y_values = weather_model(x_values)

# Plotting the weather model
plt.plot(x_values, y_values, label='Weather Model')

# Adding labels and title to the plot
plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')

# Displaying the legend
plt.legend()

# Displaying the grid on the plot
plt.grid(True)

# Showing the plot
plt.show()
