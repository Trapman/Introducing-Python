# STANDALONE PROGRAMS ###########################
# create a file called test1.py
print("This is a standalone snippet of code!")

# to run in the terminal, rather than PyCharm/Spider/etc
$ python test1.py

# COMMAND-LINE ARGUMENTS #####################################
# create a file called test2.py
print("Program arguments:", sys.argv)

# MODULES AND IMPORT STATEMENT
# simulate a weather station and print out a report
# one main program prints the report, the other module returns the weather description used by the report
import report

description = report.get_description()
print("Today's weather:", description)

def get_description():
  """return random weather, just like the pros"""
  from random import choice
  possibilities = ['snow', 'rain', 'sleet', 'sunny', 'fog']
  return choice(possibilities)

# IMPORT MODULE AS A DIFFERENT NAME ##################################
import report as wr
description = wr.get_description()
print("Today's weather: ", description)

# IMPORT ONLY WHAT YOU WANT FROM A MODULE ################################
from report import get description
description = wr.get_description()
print("Today's weather: ", description)

from report import get description as do_it   # you can also alias it
description = do_it()
print("Today's weather: ", description)

# PACKAGES ##############################################################
# let's use different types of text forecasts: one for the next day, one for the next week
# make a directory named sources, create two modules within it: daily.py, weekly.py
# each has a function called forecast
from sources import daily, weekly

print("Daily Forecast: " , daily.forecast())
print("Weekly Forecast: ")

for  number, outlook in enumerate(weekly.forecast(), 1):
   print(number, outlook)
    
def forecast(): 
  'fake daily forecast'
  return 'like yesterday'

def forecast():
  """Fake weekly forecast"""
  return ["snow", "rain", "sleet", "freezing rain", "hail"]

# HANDLING MISSING KEYS WITH SETDEFAULT() AND DEFAULTDICT() ###########################################
get() #when accessing a dictionary with a missing/nonexistant key it raises an error, get() returns a default value to avoid the exception
setdefault() # is like get() but ALSO assigns an item to the dict if the key is missing





