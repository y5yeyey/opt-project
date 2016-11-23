# -*- coding: utf-8 -*-

"""
Main function for running the whole project.


"""

import argparse

def import_data():
    """
    :return: data.frame
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Example: $ python main.py --data data.csv")
    args = parser.parse_args()
    if not args.data:
        raise "Please add dataset!"
    input = args.data
    return input

def ensemble_algorithm():
    pass

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
    def _record(self):
        """
        records data for each run
        :return:
        """
        pass
    def run(self, data):
        """
        run ensemble algorithm iteratively
        :param data: dataFrame
        :return: dataFrame
        """
        pass

def main():
    # import data
    data = import_data()

    # set up simulation
    n = 100
    alg = lambda x: x
    name = "Genetic Algorithm"
    output = "GA.csv"
    output_data = Simulation(n, alg, name, output).run(data)

    # analysis on output dataset
    # .csv file is provided for R while output_data `dataFrame` for Python
    anlys = lambda y: y
    anlys(output_data)


if __name__ == "__main__":
    main()