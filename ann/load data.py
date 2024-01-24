import pandas as pd
import numpy as np
import os 

# define the file path
file_path = r'epl_results_2022-23.csv'
# read the csv
df = pd.read_csv(file_path)
# print the dataset
print(df)

import seaborn as sns
import matplotlib.pyplot as plt 

## Heat map for the better understanding of the correlation 
data = pd.DataFrame(np.random.rand(10, 10))

# Create a heatmap
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
sns.heatmap(data, cmap="YlGnBu", annot=True)  # 'cmap' sets the color map, 'annot' adds annotations

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Heatmap of Data")

# Show the heatmap
plt.show()

