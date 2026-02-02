import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_path, db_path):
    # Load CSV
    df = pd.read_csv(csv_path)
    
    # Connect to SQLite
    conn = sqlite3.connect(db_path)
    
    # Write to SQL
    df.to_sql('superstore', conn, if_exists='replace', index=False)
    
    print(f"Successfully loaded {csv_path} into {db_path} in 'superstore' table.")
    
    # Verify
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM superstore")
    count = cursor.fetchone()[0]
    print(f"Total rows in 'superstore' table: {count}")
    
    conn.close()

if __name__ == "__main__":
    load_csv_to_sqlite(r"c:\Users\shsil\OneDrive\Desktop\data_analytics\superstore.csv", 
                       r"c:\Users\shsil\OneDrive\Desktop\data_analytics\sales.db")
