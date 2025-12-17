#This file works with random_numbers.csv file


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('random_numbers.csv')

# Calculate statistics on all columns
mean_values = df.mean()
median_values = df.median()
std_values = df.std()

print("Mean values:\n", mean_values)
print("Median values:\n", median_values)
print("Standard deviation:\n", std_values)

# Scatter plot of Col_1 vs Col_2
plt.scatter(df['Col_1'], df['Col_2'])
plt.xlabel('Col_1')
plt.ylabel('Col_2')
plt.title('Scatter plot of Col_1 vs Col_2')
plt.show()

