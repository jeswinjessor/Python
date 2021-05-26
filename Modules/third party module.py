import os # a python interpreter built in python
import time # an interpreter built in C
import pandas # an interpreter built in python


while True:
    if os.path.exists("Modules/temps_today.csv"):
        data = pandas.read_csv("Modules/temps_today.csv")
        print(data.mean())
    else:
        print("file does not exist")
    time.sleep(10)
