import task_A


class task_B(task_A):
    def __init__(self, guess_count):
        super().__init__(guess_count)
        self.min = 'A'
        self.max = 'Z'
        self.current_guess = (ord(self.min) + ord(self.max)) / 2
        self.previous_guess = 0

    def change_interval(self, new_min, new_max):
        self.min = new_min
        self.max = new_max


game = task_B()
game.play_game()
