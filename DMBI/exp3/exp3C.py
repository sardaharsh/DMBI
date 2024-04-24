import pandas as pd 
import numpy as np 
df = pd.read_csv("expt3.csv ") 

# binning

df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
mean_salary = df['salary'].mean()
df['salary'].fillna(mean_salary, inplace=True)
bins = [40000, 60000]
labels = ['40k-60k']
df['Salary_Bin'] = pd.cut(df['salary'], bins=bins, labels=labels, right=False)
print("Dataset with missing values replaced and salary binning:")
print(df)

#Decimal Scaling

max_salary = df['salary'].max()
scaling_factor = 10 ** len(str(int(max_salary))) # 10 rasied to length of max salary, ex: 5 for 75000
df['scaled_salary'] = df['salary'] / scaling_factor
print("Dataset with decimal-scaled salaries:")
print(df)

# If the maximum salary is $75,000, the code calculates the scaling factor as follows:

#     Convert the maximum salary to an integer to remove any decimal places:

#     scss

# max_salary_int = int(max_salary)

# In this case, since the maximum salary is already an integer, this step doesn't change the value.

# Convert the integer maximum salary to a string to determine its length:

# scss

# max_salary_str = str(max_salary_int)

# The length of the string "75000" is 5.

# Calculate the scaling factor using 10 raised to the power of the length of the string:

# scss

#     scaling_factor = 10 ** len(max_salary_str)

#     In this case, it would be 105=100,000105=100,000.

# So, for a maximum salary of $75,000, the scaling factor would be 100,000.