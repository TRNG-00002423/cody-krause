"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""

from __future__ import annotations
import csv
from functools import reduce

csv_path = "./data/sales.csv"
output_path = "./output/summary.txt"



def main() -> None:
    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        
        for row in rows: # fix data
            try:
                row['units'] = int(row['units']) # convert units to int
                row['unit_price'] = float(row['unit_price']) # convert price to int
                print(f"units: {row['units']}, unit_prices: {row['unit_price']}")
            except KeyError:
                print("Invalid keys, skipping...")
        
        
    
        with open(output_path, "w", encoding="utf-8") as file: # output summary
            file.write(f"rows = {len(rows)}\n")
            
            grand_total = reduce(lambda acc, r : acc + (r["unit_price"] * float(r["units"])), rows, 0)
            file.write(f"grand_total = {grand_total}\n")
            
            average_line_revenue = reduce(lambda acc, r : acc + r["unit_price"]*float(r["units"]), rows, 0) / float(len(rows))
            file.write(f"average_line_revenue = {average_line_revenue:.2f}\n")
            
            top_sku = reduce(lambda acc, r : r if (float(r["units"])*r["unit_price"]) > (float(acc["units"])*acc["unit_price"]) 
                             else acc, rows, rows[0])["sku"]
            file.write(f"top_sku = {top_sku}\n")
            
            top_line_revenue = reduce(lambda acc, r: (float(r["units"])*r["unit_price"]) if 
                                      (float(r["units"])*r["unit_price"]) > acc else acc, rows, 0)
            file.write(f"top_line_revenue = {top_line_revenue}")
            
            
            
            
        


if __name__ == "__main__":
    main()
