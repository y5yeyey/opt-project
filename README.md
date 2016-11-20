# Optimization Project


### Introduction

This site is for the final project of Optimization class (CS 268). The goal is to predict every new user's group based on mobile device tracking data. Data and idea was originally from [Kaggle](https://www.kaggle.com/c/talkingdata-mobile-user-demographics). Particularly, this project will focus on the feature engineering using genetic algorithm before get into the stage of fitting a machine learning model. For dynamic and reporting purposes, please visit [TODO-DONT-CLICK]() for more details.


Also, for the purpose of data engineering, all csv data was imported into MySQL. There are six major tables providing user demographics data. Largest table `app_events` has more than 32,000,000 rows. 


### Timeline and Roadmap
See [here](https://docs.google.com/a/uci.edu/document/d/1xQiWP9X7VLAKUyM-ZTwjswcypflQY--bUXnz1qTLpI0/edit?usp=sharing) on Google Doc.


### Environmental Settings

#### MySQL

You should set `mysql` as a global variable and do not set any password for the user `root`. To change the password, run

```
$ mysql>SET PASSWORD FOR 'root'@'localhost' = PASSWORD('MyNewPass');
```

To test if you `MySQL` is ready, run

```
$ mysql -uroot 
```

#### Python Module

To install MySQLdb (a Python module), run

```
$ pip install mysql-python
```


#### Import Data to MySQL

Download the .csv files from Kaggle, then placed all of them under the `data/` directory. Enter the `data/` directory,

```
$ cd path/to/opt-project/data
```
 
Run

```
$ ./load_data.sh
```

to complete the loading process. If the password for `root` user is not empty, then you will need to change the `load_data.sh` script manually to make it work. Basically, the `load_data.sh` first run `sql.py` to generate `.sql` scripts for each of the `.csv` data files (any existed `.sql` will be overwrote), then run `.sql` scripts one by one. The whole process probably cost five mins to finish.


### Test

To test a MySQL interface, run

```
$ python test.py
```

You can modify the connection settings in `test.py`, which is defined as

```
test = {
    "HOST": "localhost",
    "DB": "talkingdata",
    "USER": "root",
    "PWD": ""
}
```

