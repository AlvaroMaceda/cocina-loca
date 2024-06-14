import numpy as np
import matplotlib.pyplot as plt


def plot_single_point(x, y, title="Single Point Plot", xlabel="x", ylabel="y"):
    """
    Plots a single point with x and y axes intersecting at the origin.

    Parameters:
    - x: The x-coordinate of the point.
    - y: The y-coordinate of the point.
    - title: The title of the plot.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    """
    # Create the plot
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'bo', label=f"Point ({x}, {y})")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.gca().set_aspect('equal')

    # Set x and y limits to center the plot around the origin
    limit = max(abs(x), abs(y)) + 1
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)

    # Move the spines to the center
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_position('zero')
    ax.spines['top'].set_position('zero')

    # Remove arrows from axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Set the position of ticks
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xlabel('')
    plt.ylabel('')

    # Annotate the point
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(10,10), ha='center')

    plt.legend()
    plt.grid(True)
    plt.show()


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
