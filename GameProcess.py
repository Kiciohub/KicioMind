import random
import tkinter as tk


class Game:

    def __init__(self, sequence_length, symbols_quantity, round_number):
        self.sequence_length = sequence_length
        self.symbols_quantity = symbols_quantity
        self.round_number = round_number
        self.sequence = self.create_sequence(sequence_length, symbols_quantity)

    @staticmethod
    def create_sequence(sequence_length, symbols_quantity):
        sequence = []
        for x in range(sequence_length):
            sequence.append(random.randint(1, symbols_quantity))
        return sequence

    @staticmethod
    def sequence_check(sequence, player_input):
        sequence_copy = list(sequence)
        length = len(sequence)

        for i in range(length):
            if player_input[i] == sequence_copy[i]:
                sequence_copy[i] = "M"

        for j in range(length):
            value = player_input[j]
            if value in sequence_copy:
                sequence_copy[sequence_copy.index(value)] = "I"

        return sequence_copy.count("M"), sequence_copy.count("I")


def import_data():
    new_game_gui = tk.Tk()
    new_game_gui.title('Master Mind by Kicia')
    background = tk.Canvas(new_game_gui, width=40, height=60)
    background.pack()
    # tk.Label(new_game_gui, text='Długość sekwencji:').grid(row=0)
    # tk.Label(new_game_gui, text='Liczba symboli:').grid(row=1)
    # tk.Label(new_game_gui, text='Liczba tur:').grid(row=2)
    sequence_length = tk.Entry(new_game_gui)
    symbols_quantity = tk.Entry(new_game_gui)
    round_number = tk.Entry(new_game_gui)
    sequence_length.grid(row=0, column=1)
    symbols_quantity.grid(row=1, column=1)
    round_number.grid(row=2, column=1)
    new_game_gui.mainloop()
    return sequence_length, symbols_quantity, round_number


def single_player_input():
    print("Podaj twoja sekwencje:")
    single_input = input()
    output = single_input.split(",")
    output = list(map(int, output))
    return output


def actual_game(this_game, pi):
    game_won = 0
    while game_won == 0:
        player_input = pi()
        result = this_game.sequence_check(this_game.sequence, player_input)
        if result[0] == len(this_game.sequence):
            return "Won"
            game_won = 1
        else:
            return result


def run_gui():
    master_mind_gui = tk.Tk()
    master_mind_gui.title('Master Mind by Kicia')
    background = tk.Canvas(master_mind_gui, width=40, height=60)
    background.pack()
    new_button = tk.Button(master_mind_gui, text='New Game', width=25, command=import_data)
    new_button.pack()
    close_button = tk.Button(master_mind_gui, text='Close Game', width=25, command=master_mind_gui.destroy)
    close_button.pack()
    master_mind_gui.mainloop()


if __name__ == '__main__':
    run_gui()

    # this_game_sequence_length, this_game_symbols_quantity = import_data()
    # this_game = Game(this_game_sequence_length, this_game_symbols_quantity)
    # # print("Correct sequence:" + str(this_game.sequence))
    #
    # actual_game(this_game, single_player_input)
