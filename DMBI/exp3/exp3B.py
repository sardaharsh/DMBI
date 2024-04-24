import pandas as pd 
import numpy as np 
df = pd.read_csv("expt3.csv ") 

# binning

# df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
mean_salary = int(df['salary'].mean())
mean_gender = dict(df['gender'].mode())
print(mean_salary)
print(mean_gender)
df['salary'].fillna(mean_salary, inplace=True)
df['gender'].fillna(mean_gender[0], inplace=True)
print(df)
bins = [40000, 60000, 70000, 80000]
labels = ['40k-60k', '60k-70k', '70k-80k']
df['Salary_Bin'] = pd.cut(df['salary'], bins=bins, labels=labels, right=False)
print("Dataset with missing values replaced and salary binning:")
print(df)
