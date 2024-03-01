import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a pairplot to visualize the relationships between variables
sns.pairplot(iris, hue="species")

# Set the size and title of the plot
plt.figure(figsize=(10, 8))
plt.suptitle("Iris Dataset Variable Relationships", fontsize=20, y=1.02)

# Remove the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

for label in plt.gca().get_xticklabels() + plt.gca().get_yticklabels():
    label.set_fontweight('bold')


plt.show()