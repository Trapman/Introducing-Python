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
                  days = []
                  fruits = []
                  drinks= []
                  desserts = []
                  for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
                    print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)

  
    
   
         
