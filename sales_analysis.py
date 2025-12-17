# 1. Load CSV File data.
# 2. Calculate total sales per month.
# 3. Determinate the best-selling and highest-grossing product.
# 4. Graph sales per month.
# 5. Graph the top 5 products by revenue.


"""STEP 1. Load CSV File data."""

import pandas as pd

df = pd.read_csv('sales.csv')

"""STEP 2. Calculate total sales per month."""

df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
print("Total sales per month:")
print(monthly_sales)

"""STEP 3. Best-Selling and Highest-Grossing Product."""

# Calculate best selling product by highest revenue (quantity * total price)
product_revenues = df.groupby('Product').apply(lambda x: (x['Sales'] * x['Price']).sum())
best_selling_highest_revenue_product = product_revenues.idxmax()
print(f"Best-selling product with highest revenue: {best_selling_highest_revenue_product}")

best_selling_product = df.groupby('Product')['Sales'].sum().idxmax()
print(f"Best-selling product by units sold: {best_selling_product}")

# Calculate the highest grossing product (the product with the highest total revenue)
highest_grossing_product = product_revenues.idxmax()
highest_grossing_value = product_revenues.max()
print(f"Highest grossing product: {highest_grossing_product} (${highest_grossing_value:.2f})")

units_per_product = df.groupby('Product')['Sales'].sum()
best_selling_product = units_per_product.idxmax()
print("Units sold per product:")
print(units_per_product)

""" STEP 4. Graph sales per month. """
import matplotlib.pyplot as plt

# Prepare data: Convert index to string for better display
monthly_sales_plot = monthly_sales.copy()
monthly_sales_plot.index = monthly_sales_plot.index.astype(str)

plt.figure(figsize=(10,6))
plt.plot(monthly_sales_plot.index, monthly_sales_plot.values, marker='o', linestyle='-')
plt.title('Total Sales Per Month')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Total_Sales_Per_Month.png')
plt.grid(True)
plt.show()

""" STEP 5. Graphic Top 5 products by revenue. """
top5_revenue = product_revenues.sort_values(ascending=False).head(5)

plt.figure(figsize=(10,6))
plt.bar(top5_revenue.index, top5_revenue.values, color='skyblue')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('Top5_Products_by_Revenue.png')
plt.show()

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Sales Analysis Report\n")
    f.write("====================\n\n")
    f.write("Best-selling product by units sold: {}\n".format(best_selling_product))
    f.write("Best-selling product with highest revenue: {}\n".format(best_selling_highest_revenue_product))
    f.write("Highest grossing product: {} (${:.2f})\n".format(highest_grossing_product, highest_grossing_value))
    f.write("\nUnits Sold per Product:\n")
    for product, units in units_per_product.items():
        f.write("  {}: {}\n".format(product, units))
    f.write("\nTop 5 Products by Revenue:\n")
    for product, revenue in top5_revenue.items():
        f.write("  {}: ${:.2f}\n".format(product, revenue))
    f.write("\nMonthly Sales:\n")
    for month, sales in monthly_sales.items():
        f.write("  {}: {}\n".format(month.strftime("%Y-%m"), sales))





