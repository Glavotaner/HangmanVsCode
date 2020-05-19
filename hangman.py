from random import choice

print('HANGMAN\n')
play = input('Type "play" to play the game, "exit" to quit: ')

if play == 'play':
    play = True
elif play == 'exit':
    play = False
else:
    play = input('Type "play" to play the game, "exit" to quit: ')

words = ('python', 'java', 'kotlin', 'javascript')
word = choice(words)
word_set = set(word)
hidden_word = list((len(word)) * '-')

lowercase_alphabet = set('thequickbrownfoxjumpsoverthelazydog')

tried_letters = set()
i = 0

while play:
    while i < 8:

        print('\n' + ''.join(hidden_word))

        # Guessed word
        if ''.join(hidden_word) == word:
            print('You guessed the word!')
            print("You survived!")
            play = False
            break

        # Letter input and insert in hidden word
        letter = input("Input a letter: ")

        # Replace - with letter
        j = 0
        for le in word:
            if letter == le:
                hidden_word[j] = letter
            j += 1

        # If more than 1 letter
        if len(letter) != 1:
            print('You should print a single letter')
            continue

        # Check if letter lowercase English
        if letter not in lowercase_alphabet:
            print('It is not an ASCII lowercase letter')
            continue

        # No improvements, tried letters list
        if letter not in tried_letters:
            tried_letters.add(letter)
        elif letter in tried_letters:
            print('You already typed this letter')
            continue

        # No such letter
        if letter not in word_set:
            print('No such letter in the word')
            i += 1

    # Failed
    if ''.join(hidden_word) != word:
        print("You are hanged!")
        play = False
