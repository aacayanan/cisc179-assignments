import task_A


class task_B(task_A.task_A):
    def __init__(self):
        super().__init__()
        self.min = 'A'
        self.max = 'Z'
        self.current_guess = int((ord(self.min) + ord(self.max)) / 2)
        self.previous_guess = 0

    def change_interval(self, new_min, new_max):
        self.min = new_min
        self.max = new_max

    def play_game(self):
        print(f"Think of a letter between {self.min} and {self.max}!")
        user_answer = ""
        while user_answer != '=':
            if chr(self.current_guess) == chr(self.previous_guess):
                print("Hmm... I think you are lying.. Terminating game.")
                return 1
            print(f"Is your letter greater (>), equal (=), or less (<) than {chr(int(self.current_guess))}?")
            user_answer = input("Please answer (<, =, >): ").strip().upper()
            match user_answer:
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


game = task_B()
game.play_game()
