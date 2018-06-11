class Hangman:
    def __init__(self, word):
        self.word = word
        self.wrong_guesses = []
        self.right_guesses = ['--' for x in range(len(word))]
        self.gameOver = False
        
    
    def display(self):
        background(150)
        
        #Show guesses and blanks
        secret = ''
        victory = True
        for x in self.right_guesses:
            if x == '--':
                victory = False
            secret += x + '   '
        wrong = ''
        
        for x in self.wrong_guesses:
            wrong += x +', '
        textSize(24)
        text("Secret Word: %s" %secret, 300, 900)
        text("Wrong guesses: %s" %wrong, 600, 600)
        if victory:
            self.gameOver = True
            text("You win! Press any key to restart", width/2 - 100, 100)
        
        

        
        # Draw gallows
        fill(255)
        strokeWeight(7)
        line(200, 800, 800, 800)
        line(500, 800, 500, 200)
        line(500, 200, 300, 200)
        line(300, 200, 300, 300)
        
        #Draw guy
        if len(self.wrong_guesses) > 0:
            ellipse(300, 350, 100, 100) #head
            if len(self.wrong_guesses) > 1:
                line(300, 400, 300, 650) #body
                if len(self.wrong_guesses) > 2:
                    line(300, 500, 200, 350)#left arm
                    if len(self.wrong_guesses) > 3:
                        line(300, 500, 400, 350) #right arm
                        if len(self.wrong_guesses) > 4:
                            line(300, 650, 200, 750)#left leg
                            if len(self.wrong_guesses) > 5:
                                line(300, 650, 400, 750) #right leg
                                if len(self.wrong_guesses) > 6:
                                    noFill()
                                    arc(300, 400, 50, 50, PI+PI/6, 2*PI - PI/6)
                                    ellipse(280, 340, 20, 20)
                                    ellipse(320, 340, 20, 20)
                                    textSize(18)
                                    text("You Lose! Secret word was %s\nPress any key to try again" %self.word, width/2 - 200, 100)
                                    self.gameOver = True

        
    def guess(self, letter):
        if letter not in self.wrong_guesses:
            if letter in self.word:
                for i, l in enumerate(self.word):
                    if l == letter:
                        self.right_guesses[i] = str(letter)
            else:
                self.wrong_guesses.append(str(letter))