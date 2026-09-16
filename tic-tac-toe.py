tic_tac_toe_bord = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
y_where=1
game = "go"
x_go = "yes"
O_go = "yes"
def print_board():
    print("   0   1   2")
    print(" +---+---+---+")
    print(f"0| {tic_tac_toe_bord[0][0]} | {tic_tac_toe_bord[0][1]} | {tic_tac_toe_bord[0][2]} |")
    print(" +---+---+---+")
    print(f"1| {tic_tac_toe_bord[1][0]} | {tic_tac_toe_bord[1][1]} | {tic_tac_toe_bord[1][2]} |")
    print(" +---+---+---+")
    print(f"2| {tic_tac_toe_bord[2][0]} | {tic_tac_toe_bord[2][1]} | {tic_tac_toe_bord[2][2]} |")
    print(" +---+---+---+")
def check_win():
    global game
    if (tic_tac_toe_bord[0][0] == "x" and tic_tac_toe_bord[0][1] == "x" and tic_tac_toe_bord[0][2] == "x") or (tic_tac_toe_bord[1][0] == "x" and tic_tac_toe_bord[1][1] == "x" and tic_tac_toe_bord[1][2] == "x") or (tic_tac_toe_bord[2][0] == "x" and tic_tac_toe_bord[2][1] == "x" and tic_tac_toe_bord[2][2] == "x") or (tic_tac_toe_bord[0][0] == "x" and tic_tac_toe_bord[1][0] == "x" and tic_tac_toe_bord[2][0] == "x") or (tic_tac_toe_bord[0][1] == "x" and tic_tac_toe_bord[1][1] == "x" and tic_tac_toe_bord[2][1] == "x") or (tic_tac_toe_bord[0][2] == "x" and tic_tac_toe_bord[1][2] == "x" and tic_tac_toe_bord[2][2] == "x") or (tic_tac_toe_bord[0][0] == "x" and tic_tac_toe_bord[1][1] == "x" and tic_tac_toe_bord[2][2] == "x") or (tic_tac_toe_bord[0][2] == "x" and tic_tac_toe_bord[1][1] == "x" and tic_tac_toe_bord[2][0] == "x"):
        print("player 1 win")
        game = "no"
    elif (tic_tac_toe_bord[0][0] == "O" and tic_tac_toe_bord[0][1] == "O" and tic_tac_toe_bord[0][2] == "O") or (tic_tac_toe_bord[1][0] == "O" and tic_tac_toe_bord[1][1] == "O" and tic_tac_toe_bord[1][2] == "O") or (tic_tac_toe_bord[2][0] == "O" and tic_tac_toe_bord[2][1] == "O" and tic_tac_toe_bord[2][2] == "O") or (tic_tac_toe_bord[0][0] == "O" and tic_tac_toe_bord[1][0] == "O" and tic_tac_toe_bord[2][0] == "O") or (tic_tac_toe_bord[0][1] == "O" and tic_tac_toe_bord[1][1] == "O" and tic_tac_toe_bord[2][1] == "O") or (tic_tac_toe_bord[0][2] == "O" and tic_tac_toe_bord[1][2] == "O" and tic_tac_toe_bord[2][2] == "O") or (tic_tac_toe_bord[0][0] == "O" and tic_tac_toe_bord[1][1] == "O" and tic_tac_toe_bord[2][2] == "O") or (tic_tac_toe_bord[0][2] == "O" and tic_tac_toe_bord[1][1] == "O" and tic_tac_toe_bord[2][0] == "O"):
        print("player 2 win")
        game = "no"
print_board()
while game == "go":
    x_go = "yes"
    O_go = "yes"
    while x_go == "yes":
        x_where_x = int(input("player 1 where do you want to go?(row)"))
        y_where_x = int(input("player 1 where do you want to go?(column)"))
        if tic_tac_toe_bord[x_where_x][y_where_x] == "x" or tic_tac_toe_bord[x_where_x][y_where_x] == "O":
            print("invalid input")
            print_board()
        else:
            tic_tac_toe_bord[x_where_x][y_where_x] = "x"
            x_go = "no"
            print_board()
            check_win()
    while O_go == "yes":
        x_where_O = int(input("player 2 where do you want to go?(row)"))
        y_where_O = int(input("player 2 where do you want to go?(column)"))
        if tic_tac_toe_bord[x_where_O][y_where_O] == "x" or tic_tac_toe_bord[x_where_O][y_where_O] == "O":
            print("invalid input")
            print_board()
        else:
            tic_tac_toe_bord[x_where_O][y_where_O] = "O"
            O_go = "no"
            print_board()
            check_win()