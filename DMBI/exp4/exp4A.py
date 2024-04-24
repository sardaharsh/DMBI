#Importing Modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Generate data
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]
address='apple_quality.csv'
df=pd.read_csv(address)


# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))


# Histogram
axs[0, 0].hist(df["Size"], color='skyblue', edgecolor='black')
axs[0, 0].set_title('Histogram')


# Box plot
sns.boxplot(df['Ripeness'], ax=axs[0, 1])
axs[0, 1].set_title('Box Plot')


# # Scatter plot
axs[1, 0].scatter(df['Juiciness'], df['Acidity'], color='green', alpha=0.6)
axs[1, 0].set_title('Scatter Plot')


# # Bar chart
axs[1, 1].bar(categories, values, color='purple')
axs[1, 1].set_title('Bar Chart')


# Add overall title
fig.suptitle('Combined Visualization', fontsize=16)


# Adjust spacing
plt.tight_layout()


# Show the plot
plt.show()
