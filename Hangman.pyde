from hangmanFile import Hangman
def setup():
    size(1000, 1000)
    global hangman
    # Choose random word from dictionary
    dict = open('./words.txt', 'r')
    words = dict.readlines()
    dict.close()
    index = int(random(len(words) - 1))
    word = words[index]
    word = word[:-1]
    # print(word)
    hangman = Hangman(word)
def draw():
    hangman.display()

def keyPressed():
    global hangman
    if not hangman.gameOver:
        hangman.guess(key)
    else:
        # Choose random word from dictionary
        dict = open('./words.txt', 'r')
        words = dict.readlines()
        dict.close()
        index = int(random(len(words) - 1))
        word = words[index]
        word = word[:-1]
        # print(word)
        hangman = Hangman(word)