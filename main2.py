import pandas as pd
import numpy as np


def entropy(table, column_name):
    temp_dict = {}
    for index, row in table.iterrows():
        if row[column_name] in temp_dict:
            temp_dict[row[column_name]] += 1
        else:
            temp_dict[row[column_name]] = 1

    temp_sum = 0
    denominator = len(table.index)
    for i in temp_dict:
        temp_sum -= (temp_dict[i])*np.log2(temp_dict[i]/denominator)
    return temp_sum/denominator


def gain(table, column_name, s_column_name):
    temp_dict = {}
    for index, row in table.iterrows():
        if row[column_name] in temp_dict:
            temp_dict[row[column_name]].append(index)
        else:
            temp_dict[row[column_name]] = [index]

    res = 0
    denominator = len(table.index)
    for i in temp_dict:
        res += len(temp_dict[i]) * entropy(table.iloc[temp_dict[i], :], s_column_name)
    res = entropy(table, s_column_name) - res/denominator

    return res


def split_info(table, column_name):
    return entropy(table, column_name)


def gain_ratio(table, column_name, s_column_name):
    return gain(table, column_name, s_column_name)/split_info(table, column_name)



