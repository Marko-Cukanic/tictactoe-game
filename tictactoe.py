from IPython.display import clear_output

def displayTicTacToe(row1,row2,row3):
    clear_output()
    print(row1)
    print(row2)
    print(row3)
def UserInputPlayer1():
    while True:
        try:
            Uinput = int(input("Player X, please enter the position you want to place your X from 1-9"))
            Uinput = Uinput - 1
            if 0 <= Uinput < 3: 
                if row1[Uinput] == ' ':
                    row1[Uinput] = 'X'
                    break
                else:
                    print("Position already taken, try again.")
            elif 3 <= Uinput < 6:  
                if row2[Uinput-3] == ' ':
                    row2[Uinput-3] = 'X'
                    break
                else:
                    print("Position already taken, try again.")
            elif 6 <= Uinput < 9:
                if row3[Uinput-6] == ' ':
                    row3[Uinput-6] = 'X'
                    break
                else:
                    print("Position already taken, try again.")
            else:
                print('Invalid choice, try again.')
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    
    displayTicTacToe(row1,row2,row3)

def UserInputPlayer2():
    while True:
        try:
            Uinput = int(input("Player O, please enter the position you want to place your X from 1-9"))
            Uinput = Uinput - 1
            if 0 <= Uinput < 3: 
                if row1[Uinput] == ' ':
                    row1[Uinput] = 'O'
                    break
                else:
                    print("Position already taken, try again.")
            elif 3 <= Uinput < 6:  
                if row2[Uinput-3] == ' ':
                    row2[Uinput-3] = 'O'
                    break
                else:
                    print("Position already taken, try again.")
            elif 6 <= Uinput < 9:
                if row3[Uinput-6] == ' ':
                    row3[Uinput-6] = 'O'
                    break
                else:
                    print("Position already taken, try again.")
            else:
                print('Invalid choice, try again.')
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    
    displayTicTacToe(row1,row2,row3)
def checkForContinue():
    while True:
        continue_game_check = input("Do you want to continue (Y/N)? ").lower()
        if continue_game_check == 'y':
            return True
        elif continue_game_check == 'n':
            print("thanks for playing")
            return False
        else:
            print("Invalid choice. Please enter Y or N.")
def checkForWin():
    """Check for a win or draw and return the game status."""
    # Check rows
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] != ' ':
            print(f"Player {row[0]} wins!")
            return True

    # Check columns
    for col in range(3):
        if row1[col] == row2[col] == row3[col] != ' ':
            print(f"Player {row1[col]} wins!")
            return True

    # Check diagonals
    if row1[0] == row2[1] == row3[2] != ' ':
        print(f"Player {row1[0]} wins!")
        return True
    if row1[2] == row2[1] == row3[0] != ' ':
        print(f"Player {row1[2]} wins!")
        return True

    # Check for a draw
    if all(cell != ' ' for cell in row1 + row2 + row3):
        print("It's a draw!")
        return True

    return False
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
print("Welcome To TicTacToe")
displayTicTacToe(row1,row2,row3)

while True:
    UserInputPlayer1()
    if checkForWin():
        if checkForContinue():
            row1 = [' ',' ',' ']
            row2 = [' ',' ',' ']
            row3 = [' ',' ',' ']
            print("Welcome To TicTacToe")
            displayTicTacToe(row1,row2,row3)
            continue
        else:
            break

    UserInputPlayer2()
    if checkForWin():
        if checkForContinue():
            row1 = [' ',' ',' ']
            row2 = [' ',' ',' ']
            row3 = [' ',' ',' ']
            print("Welcome To TicTacToe")
            displayTicTacToe(row1,row2,row3)
            continue
        else:
            break


    