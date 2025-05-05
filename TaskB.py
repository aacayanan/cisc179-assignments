import TaskA


class TaskB(TaskA.TaskA):
    def __init__(self):
        super().__init__()  # call the constructor of TaskA to initialize the base class attributes
        self.min = 'A'
        self.max = 'Z'
        self.current_guess = int((ord(self.min) + ord(self.max)) / 2)  # the initial guess is the midpoint of the range
        self.previous_guess = 0

    def change_interval(self, new_min, new_max):
        self.min = new_min.upper()  # update the minimum value of the range, convert to uppercase
        self.max = new_max.upper()  # update the maximum value of the range, convert to uppercase

    def play_game(self):
        print(f"Think of a letter between {self.min} and {self.max}!")
        user_answer = ""
        while user_answer != '=':  # loop until the user indicates the guess is correct
            if chr(self.current_guess) == chr(
                    self.previous_guess):  # check if the current guess is the same as the previous guess
                print("Hmm... I think you are lying.. Terminating game.")
                return 1
            print(f"Is your character after (>), equal (=), or before (<) the letter {chr(int(self.current_guess))}?")
            user_answer = input("Please answer (<, =, >): ")
            match user_answer:  # use match-case to handle user input
                case '<':
                    self.increment_guess_count()
                    self.previous_guess = self.current_guess
                    self.max = chr(int(self.current_guess))
                    self.current_guess = int((ord(self.min) + ord(self.max)) / 2)
                case '>':
                    self.increment_guess_count()
                    self.previous_guess = self.current_guess
                    self.min = chr(int(self.current_guess))
                    self.current_guess = int((ord(self.min) + ord(self.max)) / 2)
                case '=':
                    break
                case _:
                    print("Please enter a valid selection.")
        print("I have guessed it!")
        print(f"It took {self.guess_count} guesses!")


game = TaskB()
game.change_interval('f', 'm')
game.play_game()
