class task_A():
    def __init__(self):
        self.guess_count = 1
        self.min = 0
        self.max = 100
        self.current_guess = (self.min + self.max) / 2
        self.previous_guess = 1337
    def increment_guess_count(self):
        self.guess_count += 1

    def change_interval(self, new_min, new_max):
        self.min = new_min
        self.max = new_max
        self.current_guess = (self.min + self.max) / 2

    def play_game(self):
        print(f"Think of a number between {self.min} and {self.max}!")
        user_answer = ""
        while user_answer != '=':
            if int(self.current_guess) == int(self.previous_guess):
                print("Hmm... I think you are lying.. Terminating game.")
                return 1
            print(f"Is your number greater (>), equal (=), or less (<) than {int(self.current_guess)}?")
            user_answer = input("Please answer (<, =, >): ")
            match user_answer:
                case '<':
                    self.increment_guess_count()
                    # must be in between min and current guess
                    # set max to current guess
                    self.previous_guess = self.current_guess
                    self.max = self.current_guess
                    self.current_guess = (self.min + self.max) / 2
                case '>':
                    self.increment_guess_count()
                    # must be in between max and current guess
                    # set min to current guess
                    self.previous_guess = self.current_guess
                    self.min = self.current_guess
                    self.current_guess = (self.min + self.max) / 2
                case '=':
                    break
                case _:
                    print("Please enter a valid selection.")
        print("I have guessed it!")
        print(f"It took {self.guess_count} guesses!")


# game = task_A()
# game.change_interval(-10, 10)     # to change the interval (0-100 is default)
# game.play_game()
