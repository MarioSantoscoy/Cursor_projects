#This file works with name_ages.csv file

#Data Analysis.
# Calculate Mean, Median, Average, and Standard deviation using Pandas from the file name_ages.csv

import pandas as pd

# Read the CSV file
df = pd.read_csv("name_ages.csv")

# Calculate statistics on the 'Age' column
mean_age = df["Age"].mean()
median_age = df["Age"].median()
std_age = df["Age"].std()

print(f"Mean age: {mean_age}")
print(f"Median age: {median_age}")
print(f"Standard deviation of age: {std_age}")
# Count occurrences of each name in the 'Name' column
name_counts = df["Name"].value_counts()

print("Count of each name in the file:")
for name, count in name_counts.items():
    print(f"{name}: {count}")
