

import pandas as pd

transactions = pd.read_excel('grocery_database.xlsx', sheet_name = 'transactions')

my_var = 'customer_id'

new_df = transactions['customer_id']
transactions[my_var]

new_df = transactions[['customer_id']]
new_df = transactions[['customer_id', 'sales_cost']]


































