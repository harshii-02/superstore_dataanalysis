import pandas as pd
import re
import csv

def sql_to_csv(sql_file_path, csv_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    # Identify the INSERT INTO statements
    insert_pattern = re.compile(r"INSERT INTO \".*?\" VALUES \((.*)\);")
    
    for line in lines:
        match = insert_pattern.search(line)
        if match:
            # Simple splitter for CSV-like values in SQL
            values = match.group(1)
            # Use csv reader to handle quotes and commas properly
            reader = csv.reader([values], quotechar="'", skipinitialspace=True)
            for row in reader:
                data.append(row)

    # Column names based on the CREATE TABLE statement in the SQL file
    columns = [
        "Row ID", "Order ID", "Order Date", "Ship Date", "Ship Mode", 
        "Customer ID", "Customer Name", "Segment", "Country", "City", 
        "State", "Postal Code", "Region", "Product ID", "Category", 
        "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit"
    ]

    df = pd.DataFrame(data, columns=columns)
    
    # Basic cleaning
    # Sales, Quantity, Discount, Profit should be numeric
    numeric_cols = ["Sales", "Quantity", "Discount", "Profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df.to_csv(csv_file_path, index=False)
    print(f"Successfully converted {sql_file_path} to {csv_file_path}")

if __name__ == "__main__":
    sql_to_csv(r"c:\Users\shsil\OneDrive\Desktop\data_analytics\Sample - Superstore.sql", 
               r"c:\Users\shsil\OneDrive\Desktop\data_analytics\superstore.csv")
