import random
def hangman(word):
    wrong = 0
    stages = ["",
             "________          ",
             "|                 ",
             "|       |         ",
             "|       O         ",
             "|      /|\        ",
             "|      / \        ",
             "|                 ",
             ]
    wordletters = list(word)
    board = ["_"] * len(word)
    win = False 
    print("Welcome to Hangman")

    #Keeps the game going until the person wins or gets more char
    #than the stage length

    while (wrong < len(stages) - 1):
        char = input("\nGuess a letter!\n")

        #Looks for the char in the list of letters for the word
        if char in wordletters:
            cind = wordletters.index(char)
            board[cind] = char
            wordletters[cind] = "#"
        else:
            wrong += 1

        #Prints the board and stage, e is the number of wrong chars
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        #Breaks the loop if there are no more _ on in the board list
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

wordlist = ["boy", "girl", "cat", "dog"]
randnum = random.randint(0, 3)
hangman(wordlist[randnum])
