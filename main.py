# -*- coding: utf-8 -*-

"""
Main function for running the whole project.
"""

import pandas as pd
import argparse
import ga
from random import random

def import_data():
    """
    :return: DataFrame
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Example: $ python main.py --data path/to/data.csv")
    args = parser.parse_args()
    if not args.data:
        raise IOError("Please add dataset! Example: $ python main.py --data path/to/data.csv")
    return pd.read_csv(args.data, sep=",")

class Simulation(object):
    def __init__(self, n, alg, name, output):
        """
        simulation settings
        :param n: int, number of simulations
        :param alg: object, the ensemble algorithm
        :param name: str, simulation name
        :param output: str, output file
        """
        self.n = n
        self.alg = alg
        self.name = name
        self.output = output
    # TODO
    def _recorder(self):
        """
        records data for each run
        :return:
        """
        pass
    def run(self, data_file):
        """
        run setup algorithm
        :param data: DataFrame
        :return: DataFrame
        """
        # read data and initialize an instance of dataset
        population = ga.Population(pd.read_csv(data_file, sep=","))
        # results
        result = []
        # naive SVM model
        svm = lambda df: {"accuracy": random()}
        # start simulation
        for _ in range(self.n):
            if population.active():
                # return subset data, DataFrame
                df_groups = population.get()
                # for each individual in population
                each_result = []
                for df in df_groups:
                    # SVM output, accuracy
                    output = svm(df)
                    each_result.append(output)
                # run next generation in the GA process, does not return anything
                accuracy_result = [e["accuracy"] for e in each_result]
                population.next(accuracy_result)
                result.append(each_result)
        # print results
        print result

def main():
    # import data
    data = import_data()

    # set up simulation
    output_data = Simulation(
        n = 100,
        alg = lambda x: x,
        name = "Genetic Algorithm",
        output = "GA.csv",
    ).run(
        data_file = "data/events.csv"
    )

    # naive analysis on output dataset
    # .csv file is provided for R while output_data `dataFrame` for Python
    anlys = lambda y: y
    anlys(output_data)


if __name__ == "__main__":
    main()