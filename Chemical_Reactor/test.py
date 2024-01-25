import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
# Define your x and y values for each dataset
x_values = [1, 2, 3, 4, 5]

y_values = [10, 15, 13, 18, 20]

# Create a figure and axis for the plot
fig, ax = plt.subplots()
line = ax.plot(0 , 0, label=f'x axis')[0]

# Customize the plot
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sequential Data Plot")

# Initialize empty lists for data points
x_data = []
y_data = []

# Function to update the plot with new data
def update(frame):
    if frame < len(x_values):
        x_data.extend(x_values[: frame])
        y_data.extend(y_values[: frame])
        # line.set_data(x_data, y_data)
        line.set_xdata(x_data)
        line.set_ydata(y_data)
    else:
        ani.event_source.stop()  # Stop the animation when all datasets are plotted

# Function to generate simulated data
def simulate_data():
    for i in range(len(x_values)):
        x_data.clear()
        y_data.clear()
        yield

# Create the animation with cache_frame_data set to False
ani = animation.FuncAnimation(fig = fig, func=update, frames = 10, repeat=False, interval=150)  # Update every 1000ms (1 second)

# Display the plot
plt.show()
