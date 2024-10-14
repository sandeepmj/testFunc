## function to add two numbers together.
def addNumbers(number1, number2):
    '''
    provide two numbers, returns total
    '''
    return number1 + number2



## function to subtract two numbers.
def subtractNumbers(number1, number2):
    '''
    provide two numbers, returns number 1 - number2
    '''
    return number1 - number2

## function that gathers all files in a folder together
import glob
def gatherFiles(path):
    '''
    provide path as string with file pattern
    returns all target files in list
    '''
    return glob.glob(path)


import time
from random import randrange

def timer(start_time, end_time):
    '''
    Timer to snooze while scraping
    Para_1: start_time: integer for minimum seconds snooze
    Para_2: end_time: integer for maximum seconds snooze
    '''
    snoozer = randrange(start_time, end_time)
    print(f"Snoozing for {snoozer} seconds!")
    time.sleep(snoozer)## set timer