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

#ex
periodic_table = {'hydrogen': 1, 'helium': 2}

#if the key was NOT already in the dict, the new value is used
carbon = periodic_table.setdefault('carbon', 12)

#now when you call the dict, it's added
print(perdioc_table)
# returns {'hydrogen': 1, 'carbon' : 12, 'helium': 2}
# note that this DOES NOT WORK if we try to assign a value to already existing key

defaultdict() # similar, but specifies the default value for any new key up front
# ex: here we will we the function int() and return the integer 0
from collections import defaultdict
periodic_table = defaultdict(int) # now any missing value will be an int with the value 0

periodic_table['hydrogen'] = 1
periodic_table['lead']           # if we don't assign a value here, it automatically assigns a value, 0 here

# you can use the following functions with defeaultdict():
int() # returns 0
list() # returns an empty list, ([])
dict() # returns and empty dict, ({})

# COUNTER() ###################################
# you can use - , + , & , |
from collections import Counter
breakfast = ['spam', 'eggs', 'eggs', 'spam', 'eggs']
breakfast_counter = Counter(breakfast)
breakfast_counter # returns Counter({'spam':2, 'eggs':3})

# you can combine counters too
lunch = ['burger', 'hoagie', 'hoagie', 'hoagie', 'burger']
lunch_counter = Counter(lunch)

breakfast_counter + lunch_counter
# returns Counter({'spam':2, 'eggs':3, 'burger': 2, 'hoagie': 3})

# you can also check what you had for lunch that you didn't have for breakfast
breakfast_counter - lunch_counter

# you can find common items by using the intersection operator with &
# you can get all items using the union operator with |

# ORDER BY KEY WITH OrderedDict() ###########################################################################
# this remembers the order of key addition and returns them in the same order
from collections import OrderedDict
quotes = OrderedDict([
  ('Trap', 'Yo buls bet the ML'),
  ('Brad', 'Yarko how much are you betting?'),
  ('Yark', 'ML or spread???')
])

for bul in quotes:
  print(bul)
       
# STACK + QUEUE == DEQUE (look into this) #####################################################
# basically is a double-ended queue which has features of both a stack and queue.
# it's useful if you want to add and delete items from either end of a sequence
def palindrome(word):
  from collections import deque
  dq = deque(word)
  while len(dq) > 1:
    if dq.popleft() != dq.pop():
      return False
  return True


# ITERTOOLS() ############################################################################
# special-purpose iterator functions
# each returns one item at a time within a for loop
# chain() runs through them as if they were a single iterable
import itertools
for item in itertools.chain([1,2], ['a', 'b']):
    print(item)
    
#cycle()
# infinite iterator, cycling through its arguments
import itertools
for item in itertools.cycle([1, 2]):
    print(item)
    
#accumulate()
# calculates accumulated values
# by default, it calculates the sum
import itertools
for item in itertools.accumulate([1,2,3,4]):
    print(item)
    
# you can apply a function to accumulate() to get it to do something else
# multply
import itertools
def multiply(a,b):
    return a * b

for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)
    
# PPRINT() ##############################
# pretty printer
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([
        ('Trap', "let's get paid, buls"),
        ('bradley', 'oh arrrrd'),
        ('dan', 'naw we not doing all that')
        ])
pprint(quotes)

# CODE EXAMPLES #################################
#(1)
def hours():
    print('Open 9-5 daily')
    
import zoo
zoo.hours()

#(2)
import zoo as menagerie
menagerie.hours()

#(3)
from zoo import hours

#(4)
from zoo import hours as info
info()

#(5)
plain = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

#(6)
from collections import OrderedDict
fancy = OrderedDict([('a',1), ('b',2), ('c',3), ('d',4), ('e',5)])
fancy

#(7)
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])





