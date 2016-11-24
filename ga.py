# -*- coding: utf-8 -*-

from __future__ import division
import pandas as pd
from random import random

GROUP = [
    "F23-", "F24-26", "F27-28", "F29-32", "F33-42", "F43+",
    "M22-", "M23-26", "M27-28", "M29-31", "M32-38", "M39+"
]
GROUP_MAP = {e: i+1 for i, e in enumerate(GROUP)}

GA_PARA = {
    "POPULATION_SIZE": 20,
    "GENERATION_MAX": 9,
    "FITNESS_ERROR": 0.5,
    "PR_CROSSOVER": 0.05,
    "PR_MUTATE": 0.01
}

class Population(object):

    def __init__(self, df):
        """
        Initialized the finalized dataset
        :param df: DataFrame
        """
        self._size = GA_PARA["POPULATION_SIZE"]
        self.df = df
        self._subset = [
            map(lambda x: 1 if x > 0.5 else 0, [random() for _ in range(len(self.df.columns))]) \
            for _ in range(self._size) \
        ]
        self._gen_max = GA_PARA["GENERATION_MAX"]
        self._gen_num = 0
        self.cost = lambda one_subset: sum(one_subset)
        self.fitness = lambda one_subset, accuracy: accuracy - self.cost(one_subset) / (accuracy + 1) + len(one_subset)
        self.fitness_opt = GA_PARA["FITNESS_ERROR"]

    def active(self):
        return len(self._subset) != 0

    def get(self):
        """
        Get current DataFrame
        :return: DataFrame
        """
        if self._subset:
            features = list(self.df.columns.values)
            feature_cols = []
            for subset in self._subset:
                feature_cols.append([e for i, e in enumerate(features) if subset[i] == 1])
            return (pd.DataFrame(self.df, columns=each) for each in feature_cols)
        return [pd.DataFrame()]  # empty dataframe if terminated

    def next(self, accuracy_result):
        """
        Perform GA to produce the next generation
        """

        def _select():
            # if current individual of population fails the fitness function, then update the element
            for i, subset in enumerate(self._subset):
                if self.fitness(subset, accuracy_result[i]) > self.fitness_opt:
                    self._subset[i] = map(lambda x: 1 if x > 0.5 else 0, [random() for _ in range(len(self.df.columns))])

        def _crossover():
            # exchange the value of two adjacent individuals
            pr_crossover = GA_PARA["PR_CROSSOVER"]
            for i in range(1, len(self._subset)):
                if random() < pr_crossover:
                    # produces two children with half subsets exchanged
                    left, right = self._subset[i-1][:len(self._subset[i-1])], self._subset[i][:len(self._subset[i])]
                    self._subset[i-1] = right + self._subset[i-1][len(self._subset[i-1]):]
                    self._subset[i] = left + self._subset[i][len(self._subset[i]):]

        def _mutate():
            # each element of the subset has a chance to flip the binary value
            pr_mutate = GA_PARA["PR_MUTATE"]
            for i in range(len(self._subset)):
                new_subset = []
                for feature in self._subset[i]:
                    if random() > pr_mutate:
                        new_subset.append(feature)
                    else:
                        new_subset.append(1 - feature)
                self._subset[i] = new_subset

        def _terminate():
            # if termination is reached, then return True
            return self._gen_num >= self._gen_max

        if _terminate():
            self._subset = []
        else:
            _select()
            _crossover()
            _mutate()
            self._gen_num += 1
