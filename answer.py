#!/usr/bin/python

"""
Python Core object Types
"""

def number():
    """
       This is to review numbers and basic operations.
       """
    # Write the value 4 to the power of 5 and assign it to variable x.
    x = 4*4*4*4
    # Write the value x divided by 3 and assign it to variable y.
    y = x/3
    return x,y

def strings():
    """
    This is to review numbers and strings and basic operations.
    """

    # Assign a string "stevens" to a variable stevens.

    stevens = a

    # Repeat variable stevens 7 times and assign it to variable stevens_7.

    stevens_7 = a*7

    # What is the length of stevens_7?

    length = len(a)

    # Concatenate variable stevens with string " is great" and assign it to variable great.

    great = a + 'is great'

    # Replace "great" with "good" in variable great and assign it to a new variable good.

    good = a + 'is good'

    return stevens, stevens_7, length, great, good


def list_1D():
    """
    This is to review basic operations with lists.
    """
    s = " hoboken,is,awesome,i,like,it "
    #Remove whitespace characters on both side and assign it to a new variable hoboken.

    hoboken = "s".strip()

    # Split variable hoboken on a delimiter(comma) into a list of substrings and assign it to a new variable hoboken_list.

    hoboken_list = s.split(,)

    # Get the first item in the hoboken_list and assign it to a new variable hoboken_first_item.

    hoboken_first_item = s[0]

    ####
    l=[2,3,4,1,5,6,9,10,15,12,13,-2,-6,0,0]

    # Inplace sort list l (use .sort() ).


    # Get the 4th to 10th item in sorted list l and assign them to a new list new_l.

    new_l = s.[3:11]

    return hoboken,hoboken_list, hoboken_first_item, l, new_l

def list_2D():
    # Create a 3 x 3 matrix A as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]

    A = [[1,4,5],
        [6,10,11],
        [12,17,38]]

    # Collect the items in the last column of matrix A using list comprehension and assign it to a new variable last_column.

    last_column = [row[2] for row in A]

    # Get the item at the last row and last column of A.

    a = A[2][2]

    # Get the item at row 2 and column 1 of A.

    b = A[1][0]


    return A,last_column, a, b


def dictionary():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   "fruit" => "apple"
    #   "quantity" => 18
    #   "color" => "red"
    fruit_dict = { 'fruit': 'apple', 'quantity' : '18', 'color' :'red'}
    
    # Get the item in dictionary fruit_dict that the key "fruit" maps to.

    f = fruit_dict['fruit']

    # Increase the value that key "quantity" map to by 1.


    return fruit_dict, f
def dictionary_nested():
    # Create a nested dictionary Grace where:
    #   "name" => {"first_name" => "Grace", "last_name" => "Hopper"} (a dictionary)
    #   "jobs" => ["scientist", "engineer"] (a list)
    #   "age" => 85

    Grace = { 'name' : {'first_name ' : 'Grace' , 'last_name' : 'Hopper'},
             'jobs' : ['scientists', 'engineer'],
             'age' : 85 } 
    # Get the value of key "last_name" from the subdictionary of key "name" in dictionary Grace. (aka."Hopper")

    last_name = rec['name']['last_name']

    # Add "programmer" to the list that key "jobs" maps to.



    # Get the third item in the list that key "job" maps to. (the item  you recently added)
    
    job = rec['jobs']



    return Grace,last_name, job



number()
strings()
list_1D()
list_2D()
dictionary()
dictionary_nested()
