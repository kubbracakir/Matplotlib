import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a sample dataset
data = {'x': np.random.rand(100), 'y': np.random.rand(100) * np.array(range(100))}
df = pd.DataFrame(data)

# Create a scatter plot of the data
plt.figure(figsize=(8, 6))
plt.scatter(df['x'], df['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample Data')
plt.show()

# Split the data into training and testing sets
X = df[['x']]
y = df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions using the model
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Create a scatter plot with the regression line
plt.figure(figsize=(8, 6))
plt.scatter(df['x'], df['y'])
plt.plot(X_test, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Model')
plt.show()