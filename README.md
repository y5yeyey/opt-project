# Optimization Project



### Introduction
This site is for the final project of Optimization class (CS 268). The goal is get to predict every new user's group based on mobile device tracking data. Data and idea was originally from [Kaggle](https://www.kaggle.com/c/talkingdata-mobile-user-demographics). Particularly, this project will focus on the feature engineering using genetic algorithm before get into the stage of fitting a machine learning model. For dynamic and reporting purposes, please visit [TODO]() for more details.

Also, for the purpose of data engineering, all csv data were imported into MySQL. There are six major tables providing user demographics data. Largest table `app_events` has more than 32,000,000 rows. 


### Methods

#### Optimization Methods for Feature Engineering
We applied genetic algoithm for feature data engineering. 

#### Machine Leanring

### Evaluations



### Implementation

#### Install Python Module
To install MySQLdb
```
> pip install mysql-python
```

#### Import Data to MySQL
Download the .csv files from Kaggl, then placed them under the data/ directory. Run
```
> ./load_data.sh
```
to complete the loading process. 

### Test

To test a MySQL interface
```
> python test.py
```

