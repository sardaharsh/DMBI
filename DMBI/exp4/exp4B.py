import numpy as np 
import pandas as pd

np.random.seed(10) 

product_type = np.random.choice(a= ["iPhone","iPad","iPod","AVP","AirPods"], p = [0.05, 0.15 ,0.25, 0.05, 0.5], size=1000) 
month = np.random.choice(a= ["January","February","March"], p = [0.4, 0.2, 0.4], size=1000) 

product = pd.DataFrame({"types":product_type, "months":month})
print(product) 

product_tab = pd.crosstab(product.types, product.months, margins = True)
print(product_tab) 
product_tab.columns = ["January","February","March","row_totals"] 
product_tab.index = ["iPhone","iPad","iPod","AVP","AirPods","col_totals"] 

observed = product_tab.iloc[0:5,0:3] 
print(product_tab) 
print(observed)

expected = np.outer(product_tab["row_totals"][0:5], product_tab.loc["col_totals"][0:3]) / 1000 
expected = pd.DataFrame(expected) 
expected.columns = ["Janurary","Feburary","March"] 
expected.index = ["iPhone","iPad","iPod","AVP","AirPods"] 
print(expected)

chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print(chi_squared_stat) 
critical_value= 15.50731 
print("Critical value:",critical_value) 
if (chi_squared_stat < critical_value): 
    print("Values are corelated ") 
else: 
    print("Values are not corelated") 
