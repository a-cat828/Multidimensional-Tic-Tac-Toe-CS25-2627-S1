tic_tac_toe_bord = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
y_where=1
game = "go"
def print_board():
    print("   0   1   2")
    print(" +---+---+---+")
    print(f"0| {tic_tac_toe_bord[0][0]} | {tic_tac_toe_bord[0][1]} | {tic_tac_toe_bord[0][2]} |")
    print(" +---+---+---+")
    print(f"1| {tic_tac_toe_bord[1][0]} | {tic_tac_toe_bord[1][1]} | {tic_tac_toe_bord[1][2]} |")
    print(" +---+---+---+")
    print(f"2| {tic_tac_toe_bord[2][0]} | {tic_tac_toe_bord[2][1]} | {tic_tac_toe_bord[2][2]} |")
    print(" +---+---+---+")
print_board()
while game == "go":
    x_where_x = int(input("player 1 where do you want to go?(row)"))
    y_where_x = int(input("player 1 where do you want to go?(column)"))
    tic_tac_toe_bord[x_where_x][y_where_x] = "x"
    print_board()

    x_where_O = int(input("player 2 where do you want to go?(row)"))
    y_where_O = int(input("player 2 where do you want to go?(column)"))
    tic_tac_toe_bord[x_where_O][y_where_O] = "O"
    print_board()
