bord_forced_O = "no"
bord_forced_x ="no"
tic_tac_toe_bord_big =[
    [
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
    [
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
[
    [0,0,0],
    [0,0,0],
    [0,0,0]
],
    ]
the_big_bord_win=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
def print_board():
    print("   0   1   2")
    print("+-----")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[0][0][0]} | {tic_tac_toe_bord_big[0][0][1]} | {tic_tac_toe_bord_big[0][0][2]} ||| {tic_tac_toe_bord_big[1][0][0]} | {tic_tac_toe_bord_big[1][0][1]} | {tic_tac_toe_bord_big[1][0][1]} ||| {tic_tac_toe_bord_big[2][0][1]} | {tic_tac_toe_bord_big[2][0][1]} | {tic_tac_toe_bord_big[2][0][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[0][1][0]} | {tic_tac_toe_bord_big[0][1][1]} | {tic_tac_toe_bord_big[0][1][2]} ||| {tic_tac_toe_bord_big[1][1][0]} | {tic_tac_toe_bord_big[1][1][1]} | {tic_tac_toe_bord_big[1][1][1]} ||| {tic_tac_toe_bord_big[2][1][1]} | {tic_tac_toe_bord_big[2][1][1]} | {tic_tac_toe_bord_big[2][1][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[0][2][0]} | {tic_tac_toe_bord_big[0][2][1]} | {tic_tac_toe_bord_big[0][2][2]} ||| {tic_tac_toe_bord_big[1][2][0]} | {tic_tac_toe_bord_big[1][2][1]} | {tic_tac_toe_bord_big[1][2][1]} ||| {tic_tac_toe_bord_big[2][2][1]} | {tic_tac_toe_bord_big[2][2][1]} | {tic_tac_toe_bord_big[2][2][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")

    print(f"|| {tic_tac_toe_bord_big[3][0][0]} | {tic_tac_toe_bord_big[3][0][1]} | {tic_tac_toe_bord_big[3][0][2]} ||| {tic_tac_toe_bord_big[4][0][0]} | {tic_tac_toe_bord_big[4][0][1]} | {tic_tac_toe_bord_big[4][0][1]} ||| {tic_tac_toe_bord_big[5][0][1]} | {tic_tac_toe_bord_big[5][0][1]} | {tic_tac_toe_bord_big[5][0][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[3][1][0]} | {tic_tac_toe_bord_big[3][1][1]} | {tic_tac_toe_bord_big[3][1][2]} ||| {tic_tac_toe_bord_big[4][1][0]} | {tic_tac_toe_bord_big[4][1][1]} | {tic_tac_toe_bord_big[4][1][1]} ||| {tic_tac_toe_bord_big[5][1][1]} | {tic_tac_toe_bord_big[5][1][1]} | {tic_tac_toe_bord_big[5][1][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[3][2][0]} | {tic_tac_toe_bord_big[3][2][1]} | {tic_tac_toe_bord_big[3][2][2]} ||| {tic_tac_toe_bord_big[4][2][0]} | {tic_tac_toe_bord_big[4][2][1]} | {tic_tac_toe_bord_big[4][2][1]} ||| {tic_tac_toe_bord_big[5][2][1]} | {tic_tac_toe_bord_big[5][2][1]} | {tic_tac_toe_bord_big[5][2][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")

    print(f"|| {tic_tac_toe_bord_big[6][0][0]} | {tic_tac_toe_bord_big[6][0][1]} | {tic_tac_toe_bord_big[6][0][2]} ||| {tic_tac_toe_bord_big[7][0][0]} | {tic_tac_toe_bord_big[7][0][1]} | {tic_tac_toe_bord_big[7][0][1]} ||| {tic_tac_toe_bord_big[8][0][1]} | {tic_tac_toe_bord_big[7][0][1]} | {tic_tac_toe_bord_big[8][0][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[6][1][0]} | {tic_tac_toe_bord_big[6][1][1]} | {tic_tac_toe_bord_big[6][1][2]} ||| {tic_tac_toe_bord_big[7][1][0]} | {tic_tac_toe_bord_big[7][1][1]} | {tic_tac_toe_bord_big[7][1][1]} ||| {tic_tac_toe_bord_big[8][1][1]} | {tic_tac_toe_bord_big[7][1][1]} | {tic_tac_toe_bord_big[8][1][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[6][1][0]} | {tic_tac_toe_bord_big[6][1][1]} | {tic_tac_toe_bord_big[6][1][2]} ||| {tic_tac_toe_bord_big[7][1][0]} | {tic_tac_toe_bord_big[7][1][1]} | {tic_tac_toe_bord_big[7][1][1]} ||| {tic_tac_toe_bord_big[8][1][1]} | {tic_tac_toe_bord_big[7][1][1]} | {tic_tac_toe_bord_big[8][1][1]} ||")
    print("|+---+---+---+|+---+---+---+|+---+---+---+|")
    print(f"|| {tic_tac_toe_bord_big[6][2][0]} | {tic_tac_toe_bord_big[6][2][1]} | {tic_tac_toe_bord_big[6][2][2]} ||| {tic_tac_toe_bord_big[7][2][0]} | {tic_tac_toe_bord_big[7][2][1]} | {tic_tac_toe_bord_big[7][2][1]} ||| {tic_tac_toe_bord_big[8][2][1]} | {tic_tac_toe_bord_big[7][2][1]} | {tic_tac_toe_bord_big[8][2][1]} ||")
def check_win_x():
    global bord_forced_O
    global bord_forced_x
    if (tic_tac_toe_bord_big[bord_x][0][0] == "x" and tic_tac_toe_bord_big[bord_x][0][1] == "x" and tic_tac_toe_bord_big[bord_x][0][2] == "x") or (
            tic_tac_toe_bord_big[bord_x][1][0] == "x" and tic_tac_toe_bord_big[bord_x][1][1] == "x" and tic_tac_toe_bord_big[bord_x][1][2] == "x") or (
            tic_tac_toe_bord_big[bord_x][2][0] == "x" and tic_tac_toe_bord_big[bord_x][2][1] == "x" and tic_tac_toe_bord_big[bord_x][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_x][0][0] == "x" and tic_tac_toe_bord_big[bord_x][1][0] == "x" and tic_tac_toe_bord_big[bord_x][2][0] == "x") or (
           tic_tac_toe_bord_big[bord_x][0][1] == "x" and tic_tac_toe_bord_big[bord_x][1][1] == "x" and tic_tac_toe_bord_big[bord_x][2][1] == "x") or (
            tic_tac_toe_bord_big[bord_x][0][2] == "x" and tic_tac_toe_bord_big[bord_x][1][2] == "x" and tic_tac_toe_bord_big[bord_x][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_x][0][0] == "x" and tic_tac_toe_bord_big[bord_x][1][1] == "x" and tic_tac_toe_bord_big[bord_x][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_x][0][2] == "x" and tic_tac_toe_bord_big[bord_x][1][1] == "x" and tic_tac_toe_bord_big[bord_x][2][0] == "x"):
        print(f"player 1 win the {bord_x} square")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_x == 0:
            the_big_bord_win[0][0] = "x"
        elif bord_x == 1:
            the_big_bord_win[0][1] = "x"
        elif bord_x == 2:
            the_big_bord_win[0][2] = "x"
        elif bord_x == 3:
            the_big_bord_win[1][0] = "x"
        elif bord_x == 4:
            the_big_bord_win[1][1] = "x"
        elif bord_x == 5:
            the_big_bord_win[1][2] = "x"
        elif bord_x == 6:
            the_big_bord_win[2][0] = "x"
        elif bord_x == 7:
            the_big_bord_win[2][1] = "x"
        elif bord_x == 8:
            the_big_bord_win[2][2] = "x"
    elif (tic_tac_toe_bord_big[bord_x][0][0] == "O" and tic_tac_toe_bord_big[bord_x][0][1] == "O" and tic_tac_toe_bord_big[bord_x][0][2] == "O") or (
            tic_tac_toe_bord_big[bord_x][1][0] == "O" and tic_tac_toe_bord_big[bord_x][1][1] == "O" and tic_tac_toe_bord_big[bord_x][1][2] == "O") or (
            tic_tac_toe_bord_big[bord_x][2][0] == "O" and tic_tac_toe_bord_big[bord_x][2][1] == "O" and tic_tac_toe_bord_big[bord_x][2][2] == "O") or (
            tic_tac_toe_bord_big[bord_x][0][0] == "O" and tic_tac_toe_bord_big[bord_x][1][0] == "O" and tic_tac_toe_bord_big[bord_x][2][0] == "O") or (
            tic_tac_toe_bord_big[bord_x][0][1] == "O" and tic_tac_toe_bord_big[bord_x][1][1] == "O" and tic_tac_toe_bord_big[bord_x][2][1] == "O") or (
            tic_tac_toe_bord_big[bord_x][0][2] == "O" and tic_tac_toe_bord_big[bord_x][1][2] == "O" and tic_tac_toe_bord_big[bord_x][2][2] == "O") or (
           tic_tac_toe_bord_big[bord_x][0][0] == "O" and tic_tac_toe_bord_big[bord_x][1][1] == "O" and tic_tac_toe_bord_big[bord_x][2][2] == "O") or (
            tic_tac_toe_bord_big[bord_x][0][2] == "O" and tic_tac_toe_bord_big[bord_x][1][1] == "O" and tic_tac_toe_bord_big[bord_x][2][0] == "O"):
        print(f"player 2 win the {bord_x} square")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_x == 0:
            the_big_bord_win[0][0] = "O"
        elif bord_x == 1:
            the_big_bord_win[0][1] = "O"
        elif bord_x == 2:
            the_big_bord_win[0][2] = "O"
        elif bord_x == 3:
            the_big_bord_win[1][0] = "O"
        elif bord_x == 4:
            the_big_bord_win[1][1] = "O"
        elif bord_x == 5:
            the_big_bord_win[1][2] = "O"
        elif bord_x == 6:
            the_big_bord_win[2][0] = "O"
        elif bord_x == 7:
            the_big_bord_win[2][1] = "O"
        elif bord_x == 8:
            the_big_bord_win[2][2] = "O"

    elif tic_tac_toe_bord_big[bord_x][0][0] != 0 and tic_tac_toe_bord_big[bord_x][0][1] != 0 and tic_tac_toe_bord_big[bord_x][0][2] != 0 and  tic_tac_toe_bord_big[bord_x][1][0] != 0 and tic_tac_toe_bord_big[bord_x][1][1] != 0 and tic_tac_toe_bord_big[bord_x][1][2] != 0 and tic_tac_toe_bord_big[bord_x][2][0] != 0 and tic_tac_toe_bord_big[bord_x][2][1] != 0 and tic_tac_toe_bord_big[bord_x][2][2] != 0:
        print("it's full so it's a tie")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_x == 0:
            the_big_bord_win[0][0] = "T"
        elif bord_x == 1:
            the_big_bord_win[0][1] = "T"
        elif bord_x == 2:
            the_big_bord_win[0][2] = "T"
        elif bord_x == 3:
            the_big_bord_win[1][0] = "T"
        elif bord_x == 4:
            the_big_bord_win[1][1] = "T"
        elif bord_x == 5:
            the_big_bord_win[1][2] = "T"
        elif bord_x == 6:
            the_big_bord_win[2][0] = "T"
        elif bord_x == 7:
            the_big_bord_win[2][1] = "T"
        elif bord_x == 8:
            the_big_bord_win[2][2] = "T"

def bord_forced_yes_or_no():
    global bord_forced_O, bord_forced_x,bord_O
    if x_where_x == 0 and y_where_x == 0:
        bord_forced_O = "yes"
        bord_O = 0
def check_win_O():
    global bord_forced_O
    global bord_forced_x
    if (tic_tac_toe_bord_big[bord_O][0][0] == "x" and tic_tac_toe_bord_big[bord_O][0][1] == "x" and tic_tac_toe_bord_big[bord_O][0][2] == "x") or (
            tic_tac_toe_bord_big[bord_O][1][0] == "x" and tic_tac_toe_bord_big[bord_O][1][1] == "x" and tic_tac_toe_bord_big[bord_O][1][2] == "x") or (
            tic_tac_toe_bord_big[bord_O][2][0] == "x" and tic_tac_toe_bord_big[bord_O][2][1] == "x" and tic_tac_toe_bord_big[bord_O][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_O][0][0] == "x" and tic_tac_toe_bord_big[bord_O][1][0] == "x" and tic_tac_toe_bord_big[bord_O][2][0] == "x") or (
           tic_tac_toe_bord_big[bord_O][0][1] == "x" and tic_tac_toe_bord_big[bord_O][1][1] == "x" and tic_tac_toe_bord_big[bord_O][2][1] == "x") or (
            tic_tac_toe_bord_big[bord_O][0][2] == "x" and tic_tac_toe_bord_big[bord_O][1][2] == "x" and tic_tac_toe_bord_big[bord_O][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_O][0][0] == "x" and tic_tac_toe_bord_big[bord_O][1][1] == "x" and tic_tac_toe_bord_big[bord_O][2][2] == "x") or (
            tic_tac_toe_bord_big[bord_O][0][2] == "x" and tic_tac_toe_bord_big[bord_O][1][1] == "x" and tic_tac_toe_bord_big[bord_O][2][0] == "x"):
        print(f"player 1 win the {bord_O} square")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_O == 0:
            the_big_bord_win[0][0] = "x"
        elif bord_O == 1:
            the_big_bord_win[0][1] = "x"
        elif bord_O == 2:
            the_big_bord_win[0][2] = "x"
        elif bord_O == 3:
            the_big_bord_win[1][0] = "x"
        elif bord_O == 4:
            the_big_bord_win[1][1] = "x"
        elif bord_O == 5:
            the_big_bord_win[1][2] = "x"
        elif bord_O == 6:
            the_big_bord_win[2][0] = "x"
        elif bord_O == 7:
            the_big_bord_win[2][1] = "x"
        elif bord_O == 8:
            the_big_bord_win[2][2] = "x"
    elif (tic_tac_toe_bord_big[bord_O][0][0] == "O" and tic_tac_toe_bord_big[bord_O][0][1] == "O" and tic_tac_toe_bord_big[bord_O][0][2] == "O") or (
            tic_tac_toe_bord_big[bord_O][1][0] == "O" and tic_tac_toe_bord_big[bord_O][1][1] == "O" and tic_tac_toe_bord_big[bord_O][1][2] == "O") or (
            tic_tac_toe_bord_big[bord_O][2][0] == "O" and tic_tac_toe_bord_big[bord_O][2][1] == "O" and tic_tac_toe_bord_big[bord_O][2][2] == "O") or (
            tic_tac_toe_bord_big[bord_O][0][0] == "O" and tic_tac_toe_bord_big[bord_O][1][0] == "O" and tic_tac_toe_bord_big[bord_O][2][0] == "O") or (
            tic_tac_toe_bord_big[bord_O][0][1] == "O" and tic_tac_toe_bord_big[bord_O][1][1] == "O" and tic_tac_toe_bord_big[bord_O][2][1] == "O") or (
            tic_tac_toe_bord_big[bord_O][0][2] == "O" and tic_tac_toe_bord_big[bord_O][1][2] == "O" and tic_tac_toe_bord_big[bord_O][2][2] == "O") or (
           tic_tac_toe_bord_big[bord_O][0][0] == "O" and tic_tac_toe_bord_big[bord_O][1][1] == "O" and tic_tac_toe_bord_big[bord_O][2][2] == "O") or (
            tic_tac_toe_bord_big[bord_O][0][2] == "O" and tic_tac_toe_bord_big[bord_O][1][1] == "O" and tic_tac_toe_bord_big[bord_O][2][0] == "O"):
        print(f"player 2 win the {bord_O} square")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_x == 0:
            the_big_bord_win[0][0] = "O"
        elif bord_O == 1:
            the_big_bord_win[0][1] = "O"
        elif bord_O == 2:
            the_big_bord_win[0][2] = "O"
        elif bord_O == 3:
            the_big_bord_win[1][0] = "O"
        elif bord_O == 4:
            the_big_bord_win[1][1] = "O"
        elif bord_O == 5:
            the_big_bord_win[1][2] = "O"
        elif bord_O == 6:
            the_big_bord_win[2][0] = "O"
        elif bord_O == 7:
            the_big_bord_win[2][1] = "O"
        elif bord_O == 8:
            the_big_bord_win[2][2] = "O"

    elif tic_tac_toe_bord_big[bord_O][0][0] != 0 and tic_tac_toe_bord_big[bord_O][0][1] != 0 and tic_tac_toe_bord_big[bord_O][0][2] != 0 and  tic_tac_toe_bord_big[bord_O][1][0] != 0 and tic_tac_toe_bord_big[bord_O][1][1] != 0 and tic_tac_toe_bord_big[bord_O][1][2] != 0 and tic_tac_toe_bord_big[bord_O][2][0] != 0 and tic_tac_toe_bord_big[bord_O][2][1] != 0 and tic_tac_toe_bord_big[bord_O][2][2] != 0:
        print("it's full so it's a tie")
        bord_forced_O = "no"
        bord_forced_x = "no"
        if bord_O == 0:
            the_big_bord_win[0][0] = "T"
        elif bord_O == 1:
            the_big_bord_win[0][1] = "T"
        elif bord_O == 2:
            the_big_bord_win[0][2] = "T"
        elif bord_O == 3:
            the_big_bord_win[1][0] = "T"
        elif bord_O == 4:
            the_big_bord_win[1][1] = "T"
        elif bord_O == 5:
            the_big_bord_win[1][2] = "T"
        elif bord_O == 6:
            the_big_bord_win[2][0] = "T"
        elif bord_O == 7:
            the_big_bord_win[2][1] = "T"
        elif bord_O == 8:
            the_big_bord_win[2][2] = "T"
game = "go"
print_board()
while game == "go":
    x_go = "yes"
    O_go = "yes"
    while x_go == "yes":
        if bord_forced_x == "no":
            bord_x = int(input("player 1 where do you want to go?(board)"))
        x_where_x = int(input("player 1 where do you want to go?(row)"))
        y_where_x = int(input("player 1 where do you want to go?(column)"))
        if tic_tac_toe_bord_big[bord_x][x_where_x][y_where_x] == "x" or tic_tac_toe_bord_big[bord_x][x_where_x][y_where_x]  == "O":
            print("invalid input")
            print_board()
        elif x_where_x >= 3 or x_where_x < 0 or y_where_x >= 3 or y_where_x < 0 or bord_x < 0 or bord_x > 9:
            print("invalid input")
            print_board()
        else:
            tic_tac_toe_bord_big[bord_x][x_where_x][y_where_x] = "x"
            x_go = "no"
            print_board()
            check_win_x()
    while O_go == "yes":
        if game=="go":
            if bord_forced_O == "no":
                bord_O = int(input("player 2 where do you want to go?(board)"))
            x_where_O = int(input("player 2 where do you want to go?(row)"))
            y_where_O = int(input("player 2 where do you want to go?(column)"))
            if tic_tac_toe_bord_big[bord_O][x_where_O][y_where_O] == "x" or tic_tac_toe_bord_big[bord_O][x_where_O][y_where_O] == "O":
                print("invalid input")
                print_board()
            elif x_where_O >= 3 or x_where_O < 0 or y_where_O >= 3 or y_where_O < 0 or bord_O < 0 or bord_O > 9:
                print("invalid input")
                print_board()
            else:
                tic_tac_toe_bord_big[bord_O][x_where_O][y_where_O] = "O"
                O_go = "no"
                print_board()
                check_win_O()


