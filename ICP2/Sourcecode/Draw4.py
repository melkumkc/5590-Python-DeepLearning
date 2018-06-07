def board_draw (height, width):
    x = "--- "* width
    y = "|  "* (height +1)
    for i in range  (0, height):
        print (x)
        print (y)


heihgtinp = int (input("Enter the height of the board"))
widthinp = int (input ("Enter the width of the board"))
board_draw (heihgtinp,widthinp)