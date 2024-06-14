import numpy as np

from lib.plot import plot_function

# Define a sample function to plot
def sample_function(x):
    return np.sin(x)

# Plot the sample function
plot_function(sample_function, x_range=(0, 10), title="Sine Function", xlabel="x", ylabel="sin(x)")
