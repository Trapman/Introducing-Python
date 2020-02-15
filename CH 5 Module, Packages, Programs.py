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
