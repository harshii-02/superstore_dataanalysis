import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set(style="whitegrid")

def perform_eda(csv_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv(csv_path)
    
    # 1. Basic Info
    print("--- Dataset Info ---")
    print(df.info())
    print("\n--- Summary Statistics ---")
    print(df.describe())

    # 2. Sales and Profit by Category
    cat_analysis = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Sales', data=cat_analysis, palette='viridis')
    plt.title('Total Sales by Category')
    plt.savefig(os.path.join(output_dir, 'sales_by_category.png'))
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Category', y='Profit', data=cat_analysis, palette='magma')
    plt.title('Total Profit by Category')
    plt.savefig(os.path.join(output_dir, 'profit_by_category.png'))
    plt.close()

    # 3. Monthly Sales Trend
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    monthly_sales = df.resample('M', on='Order Date')['Sales'].sum().reset_index()
    
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='Order Date', y='Sales', data=monthly_sales, marker='o')
    plt.title('Monthly Sales Trend')
    plt.savefig(os.path.join(output_dir, 'monthly_sales_trend.png'))
    plt.close()

    # 4. Profit by Region
    region_profit = df.groupby('Region')['Profit'].sum().reset_index()
    plt.figure(figsize=(8, 8))
    plt.pie(region_profit['Profit'], labels=region_profit['Region'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Profit Distribution by Region')
    plt.savefig(os.path.join(output_dir, 'profit_by_region.png'))
    plt.close()

    print(f"\nEDA complete. Plots saved to {output_dir}")

if __name__ == "__main__":
    perform_eda(r"c:\Users\shsil\OneDrive\Desktop\data_analytics\superstore.csv", 
                r"c:\Users\shsil\OneDrive\Desktop\data_analytics\plots")
