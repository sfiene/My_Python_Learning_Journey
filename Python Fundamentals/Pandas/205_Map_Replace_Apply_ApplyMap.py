

import pandas as pd

product_areas = pd.read_excel('grocery_database.xlsx', sheet_name = 'product_areas')
customer_details = pd.read_excel('grocery_database.xlsx', sheet_name = 'customer_details')

# MAP -- used to transform values in a panda series to another value

customer_details['gender_numeric'] = customer_details['gender'].map({'M' : 0,
                                                                     'F' : 1})

customer_details['gender_numeric'] = customer_details['gender'].map({'F' : 1})

# REPLACE -- similar to MAP, but will not produce NAN

customer_details['gender_numeric'] = customer_details['gender'].replace({'M' : 0,
                                                                     'F' : 1})

customer_details['gender_numeric'] = customer_details['gender'].replace({'F' : 1})

# APPLY -- call a function and apply it to every value in a series or DataFrame

product_areas['product_area_name'].apply(len)

def update_profit_margin(profit_margin):
    if profit_margin > 0.2:
        return profit_margin * 1.2
    else:
        return profit_margin * 0.8
    
product_areas['profit_margin_updated'] = product_areas['profit_margin'].apply(update_profit_margin)

x = pd.DataFrame({'A' : [1,2], 'B' : [3,4], 'C' : [5,6]})

print(x)
x.apply(max)
x.apply(max, axis = 1)

# APPLYMAP -- applies function to every element within the dataframe

def square(n):
    return n ** 2

x.applymap(square)


























