import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data from CSV file
data = pd.read_csv('/Users/mac/Desktop/Python/src/19-Matplotlib/data.csv')

# Data preprocessing
data.dropna(inplace=True)

# Exploration
print(data.describe())
print(data.corr())

# Feature engineering
data['new_feature'] = np.where(data['feature1'] > 10, 1, 0)

# Modeling
X = data[['feature1', 'feature2', 'new_feature']]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("Training score:", train_score)
print("Test score:", test_score)

# Visualization
plt.scatter(X_train['feature1'], y_train)
plt.scatter(X_train['feature2'], y_train)
plt.scatter(X_train['new_feature'], y_train)
plt.show()