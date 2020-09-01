import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


col_list = ["Temperature", "Year", "Statistics", "Country", "ISO3"]
df = pd.read_csv("tas_1991_2016_DOM.csv", usecols=col_list)

print(df["Temperature"])
