#from main2 import *
import pandas as pd

data = pd.read_csv('data.txt', sep="\t", header=0)

print(type(data))

