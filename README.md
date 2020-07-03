# FloweringTime

## Overview

This project is to analyze the relationship between the total light integral and flowering time, the total temperature 
integral and flowering time, and the max/min temperature value per day and flowering time during the specific period.
The main library of this project is pandas, matplotlib and numpy.

## Structure

- src

    The source code with functionality to import the necessary information from the csv and excel file and process the 
    data to calculate the integral and max/min value per day.

- utils

    The csv/excel file, the source code to manage the folder and files.

- app

    The main execution file.
    
- requirements

    All the dependencies for this project.

- settings

    * The start time and end time can be set by START_DATE and END_DATE
    * The NORMALIZE_INDEX to set, it's default is 1,000,000

## Installation

- Environment

    Ubuntu16.04+, Windows8+, Python2.7

- Dependency Installation

    In case Python 2.7 is not installed for all users, the Microsoft Visual C++ 2008 (64 bit or 32 bit for Python 2.7).

    Please go ahead to this project directory and run the following command in terminal
    
    ```
        pip install -r requirements.txt
    ```

## Execution

- Please run the following command

    ```
        python app.py
    ```

- You can look at the process of running this project, and finally three graphs(Light-Date, Temperature-Date, 
Max/Min Temperature-Date) are saved in plot directory.
