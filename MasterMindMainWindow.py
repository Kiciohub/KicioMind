from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import GameProcess


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"master_mind_main_gui.ui", self)
        self.actual_game = None
        self.dialog = NewGameDialog(self)

        self.new_game_action.triggered.connect(self.new_game_action_handler)
        self.quit_action.triggered.connect(self.quit_action_handler)

        self.player_input_send_button.clicked.connect(self.player_input_send_button_handler)

    def player_input_send_button_handler(self):
        player_input = self.player_input.text()
        result = self.actual_game.single_player_input(self, player_input)

    def new_game_action_handler(self):
        self.dialog.show()

    @staticmethod
    def quit_action_handler():
        sys.exit()


class NewGameDialog(QDialog):
    def __init__(self, main_window):
        super(NewGameDialog, self).__init__()
        loadUi(r"master_mind_new_game.ui", self)
        self.main_window = main_window

        self.start_game_button.clicked.connect(self.start_game_handler)

    def start_game_handler(self):
        try:
            a = int(self.sequence_length_lineEdit.text())
            b = int(self.symbols_quantity_lineEdit.text())
            c = int(self.round_number_lineEdit.text())
        except ValueError:
            pass

        self.main_window.actual_game = GameProcess.Game(a, b, c)
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()

    game_gui = MainWindow()
    game_gui.show()

    sys.exit(app.exec_())
