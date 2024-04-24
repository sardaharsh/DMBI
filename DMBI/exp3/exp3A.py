import pandas as pd 
import numpy as np 
df = pd.read_csv("expt3.csv")
print("-------------------------------")
print("Dataset: ") 
print("-------------------------------")  
print(df)
# mean 
df2 = int((df["salary"].mean())) 
df['salary'].fillna(df2,inplace=True)
print("-------------------------------")
print("Dataset after filling in mean salaries: ") 
print("-------------------------------")  
print(df)
print("-------------------------------")
print("Get the mean of the column: ", df2) 
print("-------------------------------") 
specific_column = df["salary"] 
print("The column is : ") 
print(specific_column) 
