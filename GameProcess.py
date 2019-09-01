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


    def single_player_input(self, single_input):
        input = single_input.split(",")
        input = list(map(int, input))
        result = self.sequence_check(self.sequence, input)
        return result


if __name__ == '__main__':
    pass

    # this_game_sequence_length, this_game_symbols_quantity = import_data()
    # this_game = Game(this_game_sequence_length, this_game_symbols_quantity)
    # # print("Correct sequence:" + str(this_game.sequence))

    # actual_game(this_game, single_player_input)
