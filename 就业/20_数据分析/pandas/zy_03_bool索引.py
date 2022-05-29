from pymongo import MongoClient
import pandas as pd
import numpy as np

df = pd.read_csv("./USvideos.csv")

print(df[(df["views"] > 200000000) & (df["views"] < 300000000)])

