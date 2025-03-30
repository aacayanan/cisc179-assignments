class task_A():
    def __init__(self):
        self.guess_count = 0
        self.min = 0
        self.max = 100
        self.current_guess = (self.min + self.max) / 2
        print("Think of a number between 1 and 100!")

    def increment_guess_count(self):
        self.guess_count += 1

    def play_game(self):
        user_answer = ""
        while user_answer != '=':
            self.increment_guess_count()
            print(f"Is your number greater (>), equal (=), or less (<) than {int(self.current_guess)}?")
            user_answer = input("Please answer (<, =, >): ")
            match user_answer:
                case '<':
                    # must be in between min and current guess
                    # set max to current guess
                    self.max = self.current_guess
                    self.current_guess = (self.min + self.max) / 2
                case '>':
                    # must be in between max and current guess
                    # set min to current guess
                    self.min = self.current_guess
                    self.current_guess = (self.min + self.max) / 2
                case '=':
                    break
                case _:
                    print("Please enter a valid selection.")
        print("I have guessed it!")
        print(f"It took {self.guess_count} guesses!")


game = task_A()
game.play_game()
