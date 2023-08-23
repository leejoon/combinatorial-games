# candidate idea for extra credit problem involving recursion.
#
# This will be a reading exercise to trace through a recursive function
#
# Part 1: play this game with the student until they see invariant that needs to be maintained
# at every round is coins left is divisible by 4. This serves as an intuitive basis for
# understanding the play_one_round function
#
# Part 2: 
# In the play_one_round, the computer player always takes one coin when it detects it will
# lose. Have student identify where this is occurring and have them change it to
# randomly pick 1,2,or3 coins
#
# Part 3:
# There's only one round of play
# Modify play_game so that after a game is finished, the user is prompted to play another game
# Play another game is the user responds yes.
#
# Ultimately, I decided this isn't a good candidate for a student exercise, but keeping around
# in case I get an idea for it.

def play_one_round(n):
    print('There are ' + str(n) +' coins on the table.')
    coins_to_remove = int(input('How many coins do you want to remove: 1, 2, or 3?'))
    if coins_to_remove > 3:
        coins_to_remove = 3
    if coins_to_remove < 1:
        coins_to_remove = 1
    print("You took " + str(coins_to_remove) + " coins")
    if coins_to_remove >= n:
        print("You cleared the table")
        return True
    coins_left = n - coins_to_remove
    if coins_left <= 3:
        print("I take " + str(coins_left) + " coins. There are no more coins.")
        return False
    else:
        if coins_left % 4 == 0:
            print("I take one coin")
            coins_left -= 1
        else:
            print("I take " + str(coins_left % 4) + " coin(s)")
            coins_left -= coins_left % 4
    return play_one_round(coins_left)

def play_game(n):
    if n <= 0:
        print('There are no coins, so there is no game.')
        return
    print('The goal is to take the last coin from the table.')
    result = play_one_round(n)
    if result:
        print('You win!')
    else:
        print('You lost!')

play_game(21)
