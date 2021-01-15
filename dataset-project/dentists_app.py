import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dentists.csv')

#Removing the duplicates and keep the earlier data from the different locations
df.drop_duplicates(subset = "Location", inplace = True)

#Calculate the average
x = df["First Tooltip"].mean()

print(f"The average of dentists per 10,000 people in the world is {x}")
