import numpy as np
import pandas as pd

dataframe = pd.read_csv("advertising.csv")
print(dataframe['Daily Time Spent on Site'].head())