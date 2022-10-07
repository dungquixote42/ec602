# functions
#
# what makes a good function?
#  - serve a single well defined purpose.
#  - printing vs non-printing.
#
def MyFunction():
    pass

# keyword argument
def double(y):
    return 2*y




y=double(34)
print(y)

# arguments can be named in the calling program like this:
# keyword:
z1 = double(y=12)
# positional
z2 = double(12)
print(z1,z2)

def multiple_arguments(x,y,z):
    return x + y + z


total = multiple_arguments(4,5,6)
print(f"the total is {total}")
print(sum((4,5,6)))

total = multiple_arguments(z=7,x=12,y=-9)
print(total)
# class

def make_box(fill,edge,width,height,thickness):
    """ make a textbox of size height x width
    with inside fill (char) and outside edge (char)
    with thickness for the outside
    """
    
    full_edge = edge * width
    top_box=""
    for lines in range(thickness):
        top_box += full_edge + "\n"

    mid_box=""
    for lines in range(height-2*thickness):
        line = edge*thickness + \
                        fill*(width-2*thickness) + edge*thickness
        mid_box += line+"\n"

    the_box = top_box + mid_box + top_box
    return the_box



# Positional arguments?
#  - what does this mean? 
#  - communication with author poor.
#  - correctness?

try:
    mybox=make_box(12,8,2,'e','f')
except:
    print('this did not work')


mybox = make_box(width=10,height=6,thickness=2,fill='this',edge='o')
print(mybox)



# what are these arguments supposed to be?
# what does this return?
def make_box(fill : str,
          edge: str,
          width:  int,
          height : int ,
          thickness : int) -> str:
    """ make a textbox of size height x width
    with inside fill (char) and outside edge (char)
    with thickness for the outside
    """
    
    full_edge = edge * width
    top_box=""
    for lines in range(thickness):
        top_box += full_edge + "\n"

    mid_box=""
    for lines in range(height-2*thickness):
        line = edge*thickness + \
                        fill*(width-2*thickness) + edge*thickness
        mid_box += line+"\n"

    the_box = top_box + mid_box + top_box
    return the_box


mybox = make_box(width=10,height=6,thickness=2,fill='X',edge='o')

print(mybox)

mybox=make_box('f','e',12,8,1)
print(mybox)

try:
    mybox=make_box('f','e',12,height=8,width=2)
    print(mybox)
except:
    print('does not work')

try:
    # syntax error.
    #mybox=make_box('f','e',thickness=7,height=8,12)
    print(mybox)
except:
    print('no unnamed arguments after named ones')


#            keyword-or-position    keyword only
def make_box(fill,edge, *         ,width,height,thickness):
    """ make a textbox of size height x width
    with inside fill (char) and outside edge (char)
    with thickness for the outside
    """
    
    full_edge = edge * width
    top_box=""
    for lines in range(thickness):
        top_box += full_edge + "\n"

    mid_box=""
    for lines in range(height-2*thickness):
        line = edge*thickness + \
                        fill*(width-2*thickness) + edge*thickness
        mid_box += line+"\n"

    the_box = top_box + mid_box + top_box
    return the_box


mybox=make_box('f','e',thickness=1,height=8,width=20)
print(mybox)
