import numpy as np
import pandas as pd
import matplotlib as plt

path = "LogReg_data.txt"

Data = pd.read_csv(path,header=None,names=["Exam 1","Exam 2","Admitted"])

print(Data.head(5))

print(Data.shape)

positive = Data[Data["Admitted"] == 1]
negative = Data[Data["Admitted"] == 0]


