# Script to generate sales analysis report

import pandas as pd
import sys
from datetime import datetime

# Redirect output to file and console
class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

# Open report file
report_file = open('report.txt', 'w', encoding='utf-8')
original_stdout = sys.stdout
sys.stdout = Tee(sys.stdout, report_file)

try:
    # Load CSV File data
    df = pd.read_csv('sales.csv')
    
    # Calculate total sales per month
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
    
    print("=" * 70)
    print("SALES ANALYSIS REPORT")
    print("=" * 70)
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    print("1. TOTAL SALES PER MONTH")
    print("-" * 70)
    for month, sales in monthly_sales.items():
        print(f"{str(month):<20} {sales:>10} units")
    print(f"\nTotal Period Sales: {monthly_sales.sum()} units")
    print()
    
    # Calculate product revenues
    product_revenues = df.groupby('Product').apply(lambda x: (x['Sales'] * x['Price']).sum())
    units_per_product = df.groupby('Product')['Sales'].sum()
    
    # Best-selling and highest-grossing product
    print("2. BEST-SELLING PRODUCTS")
    print("-" * 70)
    best_selling_product_by_units = units_per_product.idxmax()
    best_selling_units = units_per_product.max()
    print(f"Best-selling product by units sold: {best_selling_product_by_units}")
    print(f"Units sold: {best_selling_units}")
    print()
    
    highest_grossing_product = product_revenues.idxmax()
    highest_grossing_value = product_revenues.max()
    print(f"Highest grossing product: {highest_grossing_product}")
    print(f"Total Revenue: ${highest_grossing_value:.2f}")
    print()
    
    # Top 5 products by revenue
    print("3. TOP 5 PRODUCTS BY REVENUE")
    print("-" * 70)
    top5_revenue = product_revenues.sort_values(ascending=False).head(5)
    for rank, (product, revenue) in enumerate(top5_revenue.items(), 1):
        print(f"{rank}. {product:<40} ${revenue:>12,.2f}")
    print()
    
    # Units sold per product
    print("4. UNITS SOLD PER PRODUCT")
    print("-" * 70)
    units_sorted = units_per_product.sort_values(ascending=False)
    for product, units in units_sorted.items():
        revenue = product_revenues[product]
        print(f"{product:<40} {units:>5} units  ${revenue:>12,.2f}")
    print()
    
    # Summary statistics
    print("5. SUMMARY STATISTICS")
    print("-" * 70)
    print(f"Total Products: {len(df['Product'].unique())}")
    print(f"Total Units Sold: {df['Sales'].sum()}")
    print(f"Total Revenue: ${product_revenues.sum():,.2f}")
    print(f"Average Revenue per Product: ${product_revenues.mean():,.2f}")
    print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print()
    
    print("=" * 70)
    print("End of Report")
    print("=" * 70)

finally:
    sys.stdout = original_stdout
    report_file.close()

print("\nReport generated successfully: report.txt")


