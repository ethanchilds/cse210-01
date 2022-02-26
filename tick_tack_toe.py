"""
assignment: cse-210 week 1 prove | tick-tack-toe
author: Ethan Childs
date: 2/25/2022

"""

def main():
    turn = 1
    winner = ''
    list = [1,2,3,4,5,6,7,8,9]

    while check_win(list) == False and turn < 10:
        create_board(list)
        take_turn(list, turn)
        print()
        turn += 1

    create_board(list)

    print()
    print('Game over!')
    if check_win(list) == True and (turn % 2) == 0:
        winner = 'x'
        print(f'Congratulations {winner}! {winner} wins')
    elif check_win(list) == True and (turn % 2) != 0:
        winner = 'o'
        print(f'Congratulations {winner}! {winner} wins')
    else:
        print("It's a tie! What a close game!")
        pass

    
def create_board(list):
    list = list
    print(f'{list[0]} | {list[1]} | {list[2]}')
    print('- + - + -')
    print(f'{list[3]} | {list[4]} | {list[5]}')
    print('- + - + -')
    print(f'{list[6]} | {list[7]} | {list[8]}')

def take_turn(list,turn_num):
    if (turn_num % 2) != 0:
        turn = 'x'
    elif (turn_num % 2) == 0:
        turn = 'o'
    
    square_choice = int(input(f"{turn}'s turn to choose a square (1-9): "))
    choice_index = list.index(square_choice)
    list.insert(square_choice, turn)
    del list[choice_index]

    return list

def check_win(list):
    if (list[0] == list[3] == list[6] or 
    list[1] == list[4] == list[7] or
    list[2] == list[5] == list[8] or 
    list[0] == list[1] == list[2] or 
    list[3] == list[4] == list[5] or
    list[6] == list[7] == list[8] or 
    list[0] == list[4] == list[8] or
    list[2] == list[4] == list[6]):
        win = True

    else:
        win = False

    return win

if __name__ == '__main__':
    main()


