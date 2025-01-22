# Data Analyst Project: Sales Data Analysis
# Description: This project involves cleaning, analyzing, and visualizing sales data to provide insights 
# into revenue trends, product performance, and customer behavior. This project is built for beginner-to-intermediate data analysts.

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset
def load_data(filepath):
    """Load the dataset into a DataFrame."""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        data = pd.read_csv(filepath)
        print("Dataset loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Clean the Dataset
def clean_data(data):
    """Perform basic cleaning on the dataset."""
    print("Cleaning data...")
    # Drop rows with missing values
    data = data.dropna()
    # Convert date columns to datetime
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    # Drop rows with invalid dates
    data = data.dropna(subset=['Order Date'])
    # Remove duplicate rows
    data = data.drop_duplicates()
    print("Data cleaning complete.")
    return data

# Analyze the Dataset
def analyze_data(data):
    """Analyze the data and generate key metrics."""
    print("Analyzing data...")
    # Total revenue
    total_revenue = data['Sales'].sum()
    print(f"Total Revenue: ${total_revenue:,.2f}")

    # Revenue by product
    revenue_by_product = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    print("Revenue by Product:")
    print(revenue_by_product)

    # Revenue by month
    data['Month'] = data['Order Date'].dt.to_period('M')
    revenue_by_month = data.groupby('Month')['Sales'].sum()
    print("Revenue by Month:")
    print(revenue_by_month)

    return revenue_by_product, revenue_by_month

# Visualize the Dataset
def visualize_data(revenue_by_product, revenue_by_month):
    """Create visualizations for the analyzed data."""
    print("Visualizing data...")

    # Plot revenue by product
    plt.figure(figsize=(10, 6))
    revenue_by_product.plot(kind='bar', color='skyblue')
    plt.title('Revenue by Product')
    plt.xlabel('Product')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./output/figures/revenue_by_product.png')
    plt.show()

    # Plot revenue by month
    plt.figure(figsize=(10, 6))
    revenue_by_month.plot(kind='line', marker='o', color='green')
    plt.title('Revenue by Month')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./output/figures/revenue_by_month.png')
    plt.show()

# Main Function
def main():
    # Define directories
    data_dir = './data/'
    output_dir = './output/figures/'

    # Ensure output directories exist
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(data_dir, 'sales_data.csv')
    data = load_data(filepath)

    if data is not None:
        data = clean_data(data)
        revenue_by_product, revenue_by_month = analyze_data(data)
        visualize_data(revenue_by_product, revenue_by_month)

if __name__ == '__main__':
    main()
