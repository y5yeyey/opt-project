# Optimization Project


### Introduction

This site is for the final project of Optimization class (CS 169/268). The goal is to predict every new user's group based on mobile device tracking data. Data and idea was originally from [Kaggle](https://www.kaggle.com/c/talkingdata-mobile-user-demographics). Particularly, this project will focus on the feature engineering using genetic algorithm before get into the stage of fitting a machine learning model. For dynamic and reporting purposes, please visit [TODO-DONT-CLICK]() for more details.


### Timeline and Roadmap
See [here](https://docs.google.com/a/uci.edu/document/d/1xQiWP9X7VLAKUyM-ZTwjswcypflQY--bUXnz1qTLpI0/edit?usp=sharing) on Google Doc.


#### Git
To make a copy of this project in your laptop, you will need to use `git` command line tool. See [here](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html) for basic commands.

Check out this repository (public)

```
$ git clone https://github.com/y5yeyey/opt-project.git
```


### Architecture

#### Overview

The `main.py` calls everything in this project. Note that `Python2.7` is used in this project. Other `.py` files cannot contain the following part:

```python
if __name__ == "__main__":
	pass
```

Also, every `.py` file should be in the same directory as the `main.py`.

Given a finalized dataset `data.csv`, we will run the program via

```shell
$ python main.py --data data.csv
```

#### Components

##### Engine/Driver
The `main.py` is responsible for controlling the data flow (input dataset in `.csv` and output dataset in `.csv`), triggering algorithms in simulations, and producing numerical results (in `.csv`).

##### Visualizer
Visualizations (and all preprocessing steps) are in `R`.Results are consisted of a `.csv` dataset and plots. Data flows in `.csv` files between `Python` and `R`.

##### Algorithm
Algorithms include Genetic Algorithm (GA) and Support Vector Machine (SVM), provided by `ga.py` and `svm.py` respectively. GA is a function giving a subset of features, and pass the subset to the model fitter SVM. Each simulation calls GA and SVM iteratively to get simulation results. 

##### Analyzer
Analyzer provides an overall performance analysis on the simulation. Analyzer can be either in `R` or `Python`. If the analyzer is implemented in `R`, then `.csv` file should be loaded. If the analyzer is a `.py` file, then it will be called in the `main.py`.

