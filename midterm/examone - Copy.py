# Please add your copyright line(s) now.
# Copyright 2022 yourname1 yn1@bu.edu
# Copyright 2022 yourname2 yn2@bu.edu


"""
 Exam One Instructions
 =====================

Submitting and Timeline
-----------------------
Submit one completed exam with both authors (if you are working
on a team of two) listed above on the 
copyright lines, just as you would do for an assignment.

The exam is due at 4:15pm and cannot be submitted later than 4:30pm.
There is a 1% penalty for every minute after 4:15pm that you submit.

Here is the submission link:


https://curl.bu.edu:9999/ec602/fall2022/submit_assignment/examone

Permitted Resources
-------------------

- your computer
- your partner
- generic information search on the internet

Non-permitted Resources
-----------------------

- assistance to or from any human other than your partner or Prof. Carruthers,


Grading
-------

Your grade will be based on the following factors:

- correctly implementing the required components

- readability, including variable names and comments

- code quality (elegant, simple solutions are best)



The Exam 
--------

 You will write two functions related to the game of Battleship.

 Battleship is played on a 10x10 grid of small squares (like chess or checkers, but 10x10
 instead of 8x8). The rows are labelled 0-9 and the columns A-J.

 Ships are placed on the board either vertically (in a column) or horizontally (in a row).

 Each ship has a certain length, which in the standard game varies from 2 squares to 5 squares.

 In the actual game, you try to guess the positions of the other players ships (we won't
 implement this.)


 Here are your tasks, labelled 1 and 2 below.

--------------------

 1. Write a function ship_size(s) that determines if the string s is a valid 4-character
    description of a ship position. The four characters represent the starting and
    ending row and column of the ship. So, A0A1 is on the squares A0 and A1.
    E5G5 is on the squares E5, F5, and G5

    ship_size should return False if the string is not a valid ship position, or the
    size of the ship if it is a valid position.

    
    This function does not make any judgement about the ship size: any value between 1 and 10
    is valid as long as the ship described fits properly on the board.


 ABCDEFGHIJ
0  
1  ****
2
3
4
5
6
7
8
9

The ship shown above (the four * characters) would be 
given the description "C1F1" and ship_size("C1F1") 
should return the value 4.

-------------------

2. Write a function test_ships(ships) that accepts a list of strings `ships` representing
the placement of the ships in the game. 

In the game, there are five ships and they  are of size 2, 3, 3, 4, and 5

The function test_ships should return True if the ship placements are valid. This means
that the ships do not overlap, and all five ships are correctly place on the A-J 0-9
grid.

If the ships are not correctly placed on the board, then False is returned.
"""


# add your functions here.











"""
-----------
Sample test code.

You can use this code to test your work.

You do not need to include it with your submission,
but you can if you want to.


This code requires ship_size and test_ships to be defined,
otherwise an exception is raised.

-----------

"""

good_ships=['A0A6',"A0J0","J0A0","J8J9","J9J8","H6H6"]

bad_ships=["A0J9","a0a1","K0K2","6G7G"]


good_placements = [
  ["A0A1","B0B2","C0C2","D0D3","E0E4"],
  ["J0J1","B0B2","C0C2","D0D3","F4B4"],
  ['B1B3',"B4B5","B6B9","C2C4","C5C9"]
  ]

bad_placements = [
  ["A0A1","B0B2","C0C2","D0D3"],
  ["A0A1","B0B1","C8C9","J8J9","E5E6"],
  ["B0B1","B0B2","C0C2","D0D3","E0E4"],
  ["B0B1","B0B2","C0C2","B2E2","H0H4"],
  ]

def main():
  try:
    print("testing")

    print("\ngood ships")
    for s in good_ships:
      print(s,ship_size(s))

    print("\nbad ships")
    for s in bad_ships:
      print(s,ship_size(s))

    print("\ngood placements")
    for p in good_placements:
      print(p,test_ships(p))

    print('\nbad placements')
    for p in bad_placements:
      print(p,test_ships(p))
  except Exception as e:
    print("something went wrong:",e)

if __name__ == '__main__':
  main()




