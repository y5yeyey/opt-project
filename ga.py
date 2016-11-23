# -*- coding: utf-8 -*-

import pandas as pd
from random import random

GROUP = [
    "F23-", "F24-26", "F27-28", "F29-32", "F33-42", "F43+",
    "M22-", "M23-26", "M27-28", "M29-31", "M32-38", "M39+"
]
GROUP_MAP = {e: i+1 for i, e in enumerate(GROUP)}


class Population(object):

    def __init__(self, df):
        """
        Initialized the finalized dataset
        :param df: DataFrame
        """
        self.df = df
        self._subset = [1] * len(df.columns)

    def get(self):
        """
        Get current DataFrame
        :return: DataFrame
        """
        if self._subset:
            features = list(self.df.columns.values)
            feature_cols = [e for i, e in enumerate(features) if self._subset[i] == 1]
            return pd.DataFrame(self.df, columns=feature_cols)
        return pd.DataFrame()  # empty dataframe if terminated

    def next(self):
        """
        Perform GA to the next generation
        """
        def _select():
            pass

        def _crossover():
            pass

        def _mutate():
            pass

        def _terminate():
            return True

        if _terminate():
            self._subset = []
        else:
            self._subset = map(lambda x: 1 if x > 0.5 else 0, [random() for _ in range(len(self.df.columns))])

"""
Example
Instruction of using GA on the dataset.
"""
# read data and load it into memory
df = pd.read_csv("gender_age_train.csv", sep=",")
# initialize an instance of dataset
population = Population(df)
# results
result = []
# naive SVM model
run_SVM = lambda df: random()
# start simulation
for _ in range(100):
    # return subset data, DataFrame
    df = population.get()
    # continue to the GA process, does not return anything
    population.next()
    # SVM result, accuracy
    result.append( run_SVM(df) )
# print results
print result