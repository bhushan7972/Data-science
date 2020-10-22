word="hello"
tries=5
display='-'*len(word)

game_over=False
def match(display,tries):
    i = 0
    print('you have guess', tries)
    if guess in word:
        while word.find(guess, i) != -1:
            i = word.find(guess, i)
            display = display[:i] + guess + display[i + 1:]
            i += 1
            print("Correct", display)

    else:
        print("Sorry Worng guess")
        tries -= 1

    return display,tries

print ("---------Word Guess Game-------")
while not game_over:


    #print(display)
    guess=input("Enter guess Letter:")
    guess.lower()
    display,tries=match(display,tries)
    if word==display:
        print("***********You Win*********",word)
        game_over=True

    if tries==0:
        print("Sorry You are out of Attempt")
        game_over=True