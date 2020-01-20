#comment
# continuation character: \
# compare with if, elif, else:  these just check whether a condition is True
  disaster = True
    if disaster:
      print("Oh no!")
    else:
      print("Thank goodness")
      
  # you can have as many layers as you want with if, elif, else:
    furry = True
    small = True
    if furry:
      if small:
        print('It's a cat!')
      else:
        print('It's a dog!!!!')
      else:
        if small:
          print('It's a penguin!')
        else:
          print('It's a shark!!!')
        
  # if there are more than two possibilities, use elif:
    color = 'puce'
    if color =='red':
      print('It's a tomato')
    elif color = 'green':
      print('It's asparagus')
    elif color = 'yellow':
      print("It's corn")
    else:
      print("I've never heard of this color", color)
      
        
 #use  == to test equality
            x = 7
            x == 5 # returns False
            
 # Do multiple comparison with In
            #if you have a letter and want to know if it's a vowel. IN allows an efficient approach instead of writing it all out
            
            #long way:
            letter = 'o'
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
              print(letter, 'is a vowel')
            else:
              print(letter, 'is not a vowel')
            
            #pythonic way:
            vowels = 'aeiou'
            letter = 'o'
            letter in vowels # returns True
            if letter in vowels:
              print(letter, 'is a vowel')
            else:
              print(letter, 'is not a vowel')
            
            #you can take the same approach with lists, dicts, sets, tuples etc:
            vowel_set = {'a', 'e', 'i', 'o', 'u'}
            vowel_list = ['a', 'e', 'i', 'o', 'u']
            vowel_tuple = ('a', 'e', 'i', 'o', 'u')
            vowel_dict = {'a': 'apple', 'e': 'elephant}
            #vowel in ....    will work for each of these
                          
#Repeat using WHILE LOOP
                          count = 1
                          while count <= 5:
                            print(count)
                            count+=1
                          
#using BREAK 
                          while True:
                            stuff = input('String to capitalize [type q to quit]: ")
                            if stuff == 'q':
                              break
                            print(stuff.capitalize())
                  
#skip ahead with CONTINUE
  while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':      # quit
      break
    number = int(value)
    if number % 2 == 0:   # an even number
      continue
    print(number, "sqaured is", number*number)
                  
#check BREAK use with ELSE: if the while loop ended normally (no break), then you can pass an optional ELSE.
#the else would be run if the while loop completed but the object was not found
                  numbers = [1, 3, 5]
                  position = 0 
                  while position < len(numbers):
                    if number % 2 == 0:
                      print('Found an even number', number)
                      break
    position += 1
 else:      # break not called
  print('No even number found')
                 
#Iterate with FOR 
#you can use on lists, dicts, strings etc.
                  bets = ['chiefs', 'mavs', 'ravens', 'niners', 'nuggets']
                  for bet in bets:
                    print(bet)
                  
                  word = 'ethereum'
                  for letter in word:
                    print(letter)
                  
                  accusation = {'room': 'ballroom', 'weapon': 'knife', 'person': 'trapman'}
                  for card in accusation:    # or, for card in accusation.keys():
                    print(card)
                  
                  for valies in accusation.values():    # to get values, instead of keys
                    print(value)
                  
                  for item in accusation.items():    #to get key and value in a tuple
                    print(item)
                  
                  for card, contents in accusation.items():      #assign to a tuple in one step
                    print('Card', card, 'has the contents', contents)
                  
                  #you can use BREAK, CONTINUE, ELSE with FOR as well, just like WHILE
                  cheeses = []
                  for cheese in cheeses:
                    print('This shop has some lovely', cheese)
                    break
                  else:      # no break means no cheese
                    print('This is not much of a cheese shop tbh.')
                  
#Iterate multiple sequences with zip()
                  days = ['monday', 'tuesday', 'wednesday']
                  fruits = ['strawberry', 'banana', 'apple']
                  drinks= ['coffee', 'tea', 'espresso']
                  desserts = ['tiramisu', 'cake', 'brownie', 'ice cream']
                  for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
                    print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)
                                          
                  #zip() stops when the shortest sequence is done. In this case 'ice cream' would get skipped.
                                          
#You can use zip() to walk through multiple sequences and make tuples from items at the same offsets:
                  english = 'monday', 'tuesday', 'wednesday;
                  french = 'lundi', 'mardi', 'mercredi'
                                      
                  list(zip(english, french)
                       #returns [('monday', 'lundi'), ('tuesday', 'mardi'...])
                       
                  #feed the result of zip() directly to dict() and you can quickly create a new dictionary:
                  dict(zip(english, french))
                       
#Generate Number Sequences with range():    range( start, stop, step )    step by defaul is 1, use -1 to go backwards
                       for x in range(0, 3):
                        print(x)
                       
                       for x in range(2, -1, -1):       #counts down from 2 to 0
                        print(x)
                       
                       list(range(0, 11, 2))    #uses step size 2 to get the even numbers from 0 to 10
                       
#Comprehensions: just a compact way of creating Python data structures from one or more iterators
                       
# List Comprehension
                        #long way of writing out each step like this:
                        number_list2 = []
                        number_list2.append(1)
                        number_list2.append(2)
                       
                       #shorter method of using an iterator and range():
                       number_list = []
                       for number in range(1, 6):
                        number_list.append(number)
                       
                       #pythonic way of using list comprehnsion:
                       number_list = [number for number in range(1,6)]
                       
                       #syntax:
                       [expression for item in iterable]
                       [expression for item in iterable if condition]
                       
                       number_list = [number for number in range(1,6)]                       #ex1
                       a_list = [number for number in range(1,6) if number % 2 == 1]         #ex2
                       
                       #using nested
                       #long ex
                       rows = range(1,4)
                       cols = range(1,3)
                       for row in rows:
                        for col in cols:
                          print(row, col)
                       
                       #pythonic list comp:
                       rows = range(1,4)
                       cols = range(1,3)
                       cells = [(row, col) for row in rows for col in cols]
                       for cell in cells:
                        print(cell)
                       
#Dictionary Comprehension:
                       #syntax
                       { key_expression : value_expression for expression in iterable }
                       #ex
                       word = 'letters'
                       letter_counts = {letter: word.count(letter) for letter in word}
                       #ex2 includes set() to account for 2 t's in 'letter'
                       word = 'letters'
                       letter_counts = {letter: word.count(letter) for letter in set(word)}
                       
#Set Comprehension:
                       #sytnax
                       { expression for expression in iterable }  #can also include the if condition too
                       #ex
                       a_set = {number for nmber in range(1,6) if number % 3 == 1}
                       
#Note: tuples DO NOT have comprehensions                       
                       
#Generator Comprehension:
                       #syntax
                       number_thing = (number for number in range(1,6))
                       #this is just a way of providing data to an iterator
                       
#Functions:
                       #reusable pieces of code that you DEFINE and then CALL
                       #basic syntax:
                       def do_nothing():
                        pass
                       
                       #ex1
                       def make_a_sound():
                        print('Woof!')               #make_a_sound() returns Woof!
                       
                       #ex2
                       def agree():
                        returns True
                       
                       if agree():
                        print('Splendid!')
                       else:
                        print('That was unexpected.')       #agree() returns Splendid!
                       
                       #ex3
                       def echo(anything):
                        return anything + '' + anything
                       
                       echo('Henley!')                 #returns 'Henley! Henley!'
                       
                       #ex4
                       def commentary(color):
                        if color == 'white':
                          return "It's a Buford"
                        elif color == 'Blue':
                          return "It's a Henley"
                        elif color == 'Lilac':
                          return "It's an Emi"
                        else:
                          return "I've never heard of the color " + color + "."
                       
                       #ex5 positional arguments: values are copied to their corresponding parameters in order
                       def menu (breakfast, lunch, dinner):
                        return {'breakfast':breakfast, 'lunch':lunch, 'dinner':dinner}
                       
                       menu('eggs', 'salad', 'steak')  #returns {'breakfast':'eggs', 'lunch':'salad', 'dinner':'steak'}
                       #the downside is that you need to remember the meaning of each position, otherwise if we call it, it won't be in correct order
                       #to avoid this we use keyword arguments
                       
                       #ex6 Keyword arguments:
                       #specify arguments by the names of their corresponding parameters, even in a different order from their definition in the function
                       menu(breakfast ='eggs', lunch='salad', dinner='steak')
                       
                       #ex7 Specify Default Parameter Values
                       def menu (breakfast, lunch, dinner='steak'):
                        return {'breakfast':breakfast, 'lunch':lunch, 'dinner':dinner}
                                
                                
                       
                       
                       
                       
                       
                      
                       
                       
                        
                       
                       
                       

  
    
   
         
