import pandas as pd
import numpy as np

gl_class_column = ""


class DecisionTree:
    """
    Tree construction to keep track on progress
    """

    def __init__(self, attribute='root', attribute_value='no_value'):
        self.attribute = attribute
        self.attribute_value = attribute_value
        self.children = []

    # def __repr__(self):
    #     return self.attribute

    def add_child(self, child):
        self.children.append(child)

    def branch(self):
        if type(self.children[0]) is DecisionTree:
            for i in self.children:
                i.branch()
        elif isinstance(self.children[0], pd.DataFrame):

            pass
        else:
            raise ValueError("this class can handle only DataFrames and DecisionTrees")


def entropy(table, column_name):
    """
    Entropy is a measure of the randomness in the information being processed
    :param table: pandas data frame
    :param column_name: string denoting on witch column you want to evaluate entropy
    :return:
    """
    temp_dict = {}
    for index, row in table.iterrows():
        if row[column_name] in temp_dict:
            temp_dict[row[column_name]] += 1
        else:
            temp_dict[row[column_name]] = 1

    temp_sum = 0
    denominator = len(table.index)
    for i in temp_dict:
        temp_sum -= (temp_dict[i]) * np.log2(temp_dict[i] / denominator)
    return temp_sum / denominator


def gain(table, column_name, s_column_name):
    """

    :param table: pandas data frame
    :param column_name:
    :param s_column_name:
    :return:
    """
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
    res = entropy(table, s_column_name) - res / denominator

    return res


def split_info(table, column_name):
    return entropy(table, column_name)


def gain_ratio(table, column_name, s_column_name):
    return gain(table, column_name, s_column_name) / split_info(table, column_name)


def fit(table, class_column):
    """
    Algorithm. C4.5 builds decision trees from a set of training data in the same way as ID3, using the concept
    of information entropy. The training data is a set of already classified samples. ... When this happens, it simply
    creates a leaf node for the decision tree saying to choose that class.
    :param table: pandas data frame
    :param class_column: string name of the classifying column
    :return:
    """

    global gl_class_column
    gl_class_column = class_column
    decision_tree = DecisionTree()
    decision_tree.add_child(table)
    decision_tree.branch()

    return decision_tree
