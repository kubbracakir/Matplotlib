import pandas as pd
import numpy as np

# Read the dataset from the CSV file
df = pd.read_csv('/Users/mac/Desktop/Python/src/19-Matplotlib/e-ticaret.csv')

# Display general information about the dataset
print(df.describe())

# Calculate the total sales
total_sales = df['sales'].sum()
print(f'Total Sales: {total_sales}')

# Calculate the average price
average_price = df['price'].mean()
print(f'Average Price: {average_price:.2f}')

# Calculate the total revenue
total_revenue = df['price'].mean() * df['sales'].sum()
print(f'Total Revenue: {total_revenue:.2f}')

# Find the product with the highest sales
top_selling_product = df.loc[df['sales'].idxmax()]
print(f'Top Selling Product: {top_selling_product['product_name']} with {top_selling_product["sales"]} sales')

# Find the product with the lowest price
cheapest_product = df.loc[df['price'].idxmin()]
print(f'Cheapest Product: {cheapest_product['product_name']} with price {cheapest_product["price"]}')