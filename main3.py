from main2 import *
import pandas as pd

data = pd.read_csv('data.txt', sep="\t", header=0)

l = list(data.columns.values)
del l[0]
t = 0
for i in l:
    print(gain_ratio(data, i, "Победа"))

