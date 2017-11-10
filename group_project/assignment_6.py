#Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    #first, I spliced each row's letter into each own variable
    a1 = first_row[0]
    a2 = first_row[1]
    a3 = first_row[2]
    b1 = second_row[0]
    b2 = second_row[1]
    b3 = second_row[2]
    c1 = third_row[0]
    c2 = third_row[1]
    c3 = third_row[2]
    
    #so somehow I need to insert them like this
    #a1  |  a2  |  a3
    #--------------
    #b4  |  b5  |  b6
    #--------------
    #c1  |  c2  |  c3
    
    #I decided to make other things into its own variable
    line = "--------------"
    triplequote = "\"\"\""
    
    #I diligently built each line into its own variable
    line1 = a1 + "  |  " + a2 + "  |  " + a3
    line2 = b1 + "  |  " + b2 + "  |  " + b3
    line3 = c1 + "  |  " + c2 + "  |  " + c3
    
    #this actually makes a multiline in print!
    multilinehack = """
    """
    #so I mash all the variables together
    myboard = triplequote + multilinehack + line1 + multilinehack + line + multilinehack + line2 + multilinehack + line + multilinehack + line3 + multilinehack + triplequote
    
    print(myboard) #it looks like it prints perfectly!
    return myboard #but it comes out as a mess as a result?!

def test_format_board():
    """
    This is the board used in this test:

        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X

    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
