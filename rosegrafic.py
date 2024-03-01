import matplotlib.pyplot as plt
import numpy as np

# Set the size of the figure
fig = plt.figure(figsize=(8, 6))

# Set the angles for the petals
angles = np.linspace(0, 2 * np.pi, 100)

# Set the radii for the petals
radii = [1, 0.9, 0.8, 0.7, 0.6, 0.5]

# Create the petals
for r in radii:
    plt.plot(r * np.cos(angles), r * np.sin(angles), color='#FF69B4')

# Set the title and axis labels
plt.title("Gül Grafiği", fontsize=20, fontweight='bold', color='#FF69B4')
plt.xlabel("X Ekseni", fontsize=14, color='#FF69B4')
plt.ylabel("Y Ekseni", fontsize=14, color='#FF69B4')

# Show the plot
plt.show()