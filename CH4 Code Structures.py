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
      
        
      
