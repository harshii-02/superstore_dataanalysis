import sqlite3
import pandas as pd

def run_sql_queries(db_path):
    conn = sqlite3.connect(db_path)
    
    queries = {
        "Top 10 Customers by Profit": """
            SELECT "Customer Name", SUM(Profit) as Total_Profit
            FROM superstore
            GROUP BY "Customer Name"
            ORDER BY Total_Profit DESC
            LIMIT 10;
        """,
        "Category performance by Region": """
            SELECT Region, Category, SUM(Sales) as Total_Sales, SUM(Profit) as Total_Profit
            FROM superstore
            GROUP BY Region, Category
            ORDER BY Region, Total_Sales DESC;
        """,
        "Yearly Sales and Profit": """
            SELECT strftime('%Y', substr("Order Date", -4) || '-' || 
                   printf('%02d', ltrim(replace(substr("Order Date", 1, instr("Order Date", '/') - 1), '/', ''), '')) || '-' || 
                   printf('%02d', ltrim(replace(substr("Order Date", instr("Order Date", '/') + 1, instr(substr("Order Date", instr("Order Date", '/') + 1), '/') - 1), '/', ''), ''))) 
                   as Year, 
                   SUM(Sales) as Total_Sales, 
                   SUM(Profit) as Total_Profit
            FROM superstore
            GROUP BY Year
            ORDER BY Year;
        """
    }

    # Simplified Year extraction if the date format is consistent M/D/YYYY
    # The strftime logic in SQLite can be tricky with non-standard strings.
    # Let's use a simpler approach for SQLite or handle it in Python.
    
    # Actually, let's just do a simple aggregation for the demo
    queries["Top 5 Most Discounted Products"] = """
        SELECT "Product Name", AVG(Discount) as Avg_Discount
        FROM superstore
        GROUP BY "Product Name"
        ORDER BY Avg_Discount DESC
        LIMIT 5;
    """

    for title, query in queries.items():
        print(f"\n--- {title} ---")
        try:
            result = pd.read_sql_query(query, conn)
            print(result)
        except Exception as e:
            print(f"Error running query: {e}")

    conn.close()

if __name__ == "__main__":
    run_sql_queries(r"c:\Users\shsil\OneDrive\Desktop\data_analytics\sales.db")
