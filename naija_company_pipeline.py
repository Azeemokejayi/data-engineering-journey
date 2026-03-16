# FIRST PROJECT: A DATA PIPE LINE THAT SHOWS THE SALES DATA OF A COMPANY. 
# THE TASK WAS TO LOAD THE SALES DATA, CALCULATE THE TOTAL REVENUE, GET THE BEST SELLING PRODUCT AND THE TOP CATEGORY

import pandas as pd
df_sales = pd.read_csv('data/sales.csv')
# print(f'Data load into df:\n {df_sales}')
sales_shape = df_sales.shape
# print(f'This the shape of the table{sales_shape}')
sales_column_name = df_sales.columns
# print(f'This are the column name{sales_column_name}')
sales_revenue = df_sales["quantity"] * df_sales["price"]
revenue_total = sales_revenue.sum()
# print(f'The total revenue is {revenue_total}')
best_sell_qty = df_sales["quantity"].idxmax()
best_sell_product = df_sales.loc[best_sell_qty, "product"]
# print(f'The best selling product is {best_sell_product}')
max_revenue_category = sales_revenue.idxmax()
max_revenue_category_product = df_sales.loc[max_revenue_category, "category"]
# print(f'The product with the highest revenue is {max_revenue_category_product}')

print("=" * 30)
print("NAIJA SALES REPORT")
print("=" * 30)
print(f'Total Revenue: #{revenue_total}')
print(f'Best Selling Product: {best_sell_product}')
print(f'Top Category: {max_revenue_category_product}')
print("=" * 30)

df_sales.to_csv("sales_report.csv", index= False)
