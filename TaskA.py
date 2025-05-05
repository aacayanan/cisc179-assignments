class TaskA():
    def __init__(self):
        self.guess_count = 1  # starts at 1 because the first guess is made before user input
        self.min = 0  # the minimum number in the range
        self.max = 100  # the maximum number in the range
        self.current_guess = (self.min + self.max) / 2  # the initial guess is the midpoint of the range
        self.previous_guess = 1337  # initialize to a value outside the range to avoid immediate termination

    def increment_guess_count(self):
        self.guess_count += 1  # increment the guess count each time a new guess is made

    def change_interval(self, new_min, new_max):
        self.min = new_min  # update the minimum value of the range
        self.max = new_max  # update the maximum value of the range
        self.current_guess = (self.min + self.max) / 2  # recalculate the current guess based on the new range

    def play_game(self):
        print(f"Think of a number between {self.min} and {self.max}!")
        user_answer = ""
        while user_answer != '=':  # loop until the user indicates the guess is correct
            if int(self.current_guess) == int(
                    self.previous_guess):  # check if the current guess is the same as the previous guess
                print("Hmm... I think you are lying.. Terminating game.")
                return 1
            print(f"Is your number greater (>), equal (=), or less (<) than {int(self.current_guess)}?")
            user_answer = input("Please answer (<, =, >): ")
            match user_answer:  # use match-case to handle user input
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
                case _:  # handle invalid input
                    print("Please enter a valid selection.")
        print("I have guessed it!")
        print(f"It took {self.guess_count} guesses!")

# game = TaskA()
# game.change_interval(-10, 10)     # to change the interval (0-100 is default)
# game.play_game()
