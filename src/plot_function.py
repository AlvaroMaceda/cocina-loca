import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, x_range, num_points=1000, title="Function Plot", xlabel="x", ylabel="y"):
    """
    Plots a given function.

    Parameters:
    - func: The function to plot. It should be a callable that accepts a numpy array of x values.
    - x_range: A tuple specifying the range of x values (xmin, xmax).
    - num_points: Number of points to use for the plot.
    - title: The title of the plot.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    """
    # Generate x values
    x = np.linspace(x_range[0], x_range[1], num_points)

    # Calculate y values
    y = func(x)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=func.__name__)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
