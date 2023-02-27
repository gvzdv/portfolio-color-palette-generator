import numpy as np
import matplotlib.pyplot as plt
# For reading Image files
from PIL import Image

# Load the image
img = Image.open(input("Provide a path to the image:\n"))

# Convert it to into np array
img_array = np.asarray(img)

# Flatten the array to a 1D array
flat_img = img_array.reshape(-1, 3)

# Get the unique colors and their counts
unique_colors, counts = np.unique(flat_img, axis=0, return_counts=True)

# Sort the counts in descending order and take the top 10
top_colors = unique_colors[np.argsort(counts)[::-1][:10]]

# Convert the array into the list of tuples of RGB colors
colors = list(tuple(color / 255.0) for color in top_colors)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 1))

# Disable axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Plot a rectangle for each color
for i in range(10):
    color = colors[i]
    rect = plt.Rectangle((i * 0.1, 0), 0.1, 1, color=color)
    ax.add_patch(rect)

# Show the plot
plt.show()
