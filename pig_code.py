class Game:
    def __init__(self):
        self.human_roll = Dice()
        self.computer_roll = Dice()
        self.dice = Dice()

    def print_human_roll(self):
        print(f"You rolled a {self.human_roll}")

    def print_computer_roll(self):
        print(f"Computer rolls a {self.computer_roll}")

    def ask_human_to_roll(self):
        response = None
        while not (response == "r" or response == "h"):
            if response is not None:
                print("That's not a valid answer!")
            response = input("Do you want to (r)oll or (h)old? ").lower()
        return response == "r"

    def add_roll_to_human_roll(self, num=1):
        for _ in range(num):
            self.human_roll.add(self.human_roll())

    def computer_should_roll(self):
        return self.computer_roll.get_score() < 20

      def start_game(self):
        """
        Determines who goes first. If human rolls a value that is tied or higher than computer, humen goes first. Otherwise, computer goes first.
        """
        
        if value self.human_roll() >= to self.computer_roll():
            self.human_roll()
        else self.computer_roll()

    def play_round(self):
        """
        On each round, first player rolls dice. (DONE, I THINK) If either computer or human: if rolls, and integer is not one, add to score (DONE) If holds, return total score, go to other player (in SCORE CLASS) If rolls 1, erase score for this turn, go to other player (SCORE CLASS) If human player: inputs roll again or hold (DONE) If computer player: rolls again until score is < 20. (DONE)
        """
        if first_player == self.human_roll:
            self.human_roll() and
            self.print_human_roll() and
            self.ask_human_to_roll and
            self.add_roll_to_human_roll
        elif first_player == self.computer_roll:
            self.computer_roll and
            self.print_computer_roll and
            self.computer_should_roll


class Dice:
    def __init__(self, number):
        self.number = number
        number = random.randint(1, 6)

    def random_roll(self, value):
        self.value = value
        value = random.randint(1, 6)

    def bad_roll(self):
        if self.value is 1:
            print("You busted!")

    def __str__(self):
        return f'You rolled {self.value} .'


class Score:
    def __init__(self, points, value):
        self.points = points
        self.value = value
        points = []
        while response == "h":
            points.append(self.dice.value)
        # if sum(points)  >= 100
            print('You have won the game !')