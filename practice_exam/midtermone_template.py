# Here are the two functions and two classes you are to complete.

def modify(L,D):
  """modify the list L based on the instructions contained in the dictionary D, as follows:
  If a value in the list L is also in the dictionary D as a key, replace the value in the list
  by the value that the key points to.
  """

def basegroup(x):
  """given a list of strings x, group them by whether they are the same number in some base
  between 2 and 10. 

  Return a dictionary with the key being the integer the numbers represent, and the value 
  is a list of strings matching this number.


  for example, "21" and "7" are the same number if "21" is in base 3 and 7 is in base 8,9, or 10.

  basegroup(['21','7','6']) -> {7:['21','7']}

  If a number is not paired up with any other number, do not include it in the output dictionary.

  """



class Point():
    """represent a point in 2d space. Point(x,y) is the syntax to create."""


class Circle():
    """represent a Circle in 2d space. Circle(x,y,radius) is the syntax to create."""




# this main is used to help you test and to document what these things are supposed
# to do

def main():
    # modify testing
    print('modify tests')
    L=['a','b',2,'a','c']
    D={2:"two",'a':1}
    modify(L,D)
    print('modify',L)
    L=[6, 8, 12, 6, 12,'alpha']
    D={6:"two",'alpha':42}
    modify(L,D)
    print('modify',L)
    # basegroup testing
    print('\nbasegroup tests')
    for grouptest in [ ['3','4','21','7'], ['100','4','5'], ['6','7','21']]:
      res = basegroup(grouptest)
      print(grouptest,res)

    # Circle and Point testing
    print('\nCircle/Point tests')
    points = [Point(4,6),Point(5,8),Point(4,8),Point(6.1,8),Point()]
    
    r = Circle(4,6,2.1)

    print('testing',points,'with',r)
    for q in points:
        if q in r:
            print(q ,'is inside of',r)
        else:
            print(q,'is outside of',r)
    print([r])



if __name__ == '__main__':
    main()