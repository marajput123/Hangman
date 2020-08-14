from random import randint

def computer_choice():

    genre = {"food":["apple","bannana","strawberry"],"book":["harry potter",
    "lord of the rings"], "sports":["soccer","football","rugby"]}

    player_genre_pick = input("which genre would you like to play with: books, food, or sports:")

    computer_random2 = genre[player_genre_pick][randint(0,len(genre[player_genre_pick])-1)]

    return computer_random2

def computer_choice_word(word):

    word_lst = list(word)

    return word_lst


def player_pick():

    player_letter_pick = input('what is your letter pick:')

    return player_letter_pick

def letter_check():
# code for return letter already picked
    if player_picked in words_used:
        
        print("letter already used")

        return False

    # code for placing letter in words_used
    elif not(player_picked in word_lst):

        words_used.append(player_picked)

        print("letter not in word")

        return True


    else:
        words_used.append(player_picked)

        print ("okay")

        for i in range(len(word_lst)):

            if word_lst[i] == player_picked:

                word_secret_list[i]=player_picked

        return True

def win_condition():

    if "*" not in word_secret_list:

        return True

    else:

        return False
    
# game code
game="y"

while game=="y":

    word_secret_list=[]

    word_lst = computer_choice_word(computer_choice())

    for i in word_lst:

        if i!=" ":

            i="*"

        word_secret_list.append(i)

    words_used = []

    turn=0

    print("".join(word_secret_list))

    while turn<=15 and win_condition()==False:

        player_picked = player_pick()
        if letter_check()==True:
            turn+=1
        print("".join(word_secret_list))
        win_condition()

    if win_condition()==True:
        print("You win")

    if turn>15:
        print('you lose!')

    game=input("do you want play again, y or n:")

    if game=='n':
        print('thank you for playing')