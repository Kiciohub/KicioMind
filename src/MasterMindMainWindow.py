import os
import yaml
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from src import GameProcess, ImageProcessing


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(os.path.join(os.getcwd(), "../layouts/master_mind_main_gui.ui"), self)

        # config load
        with open("../config.yaml", 'r') as stream:
            try:
                self.buttons_horizontal_number = yaml.safe_load(stream)["buttons_horizontal_number"]
            except:
                print("Incorrect config file")

        # variable init
        self.dialog_input = None
        self.actual_game = None

        # object init
        self.dialog = NewGameDialog(self)

        # action handler connect
        self.new_game_action.triggered.connect(self.new_game_action_handler)
        self.quit_action.triggered.connect(self.quit_action_handler)

        # button handler connect
        self.player_input_send_button.clicked.connect(self.player_input_send_button_handler)

    def buttonHandlerFactory(self, param):
        def handle():
            input_text = self.player_input.text()
            input_text += f"{param},"
            self.player_input.setText(input_text)
        return handle

    def generateButtons(self, count):
        row = 0
        for i in range(count):
            if i % self.buttons_horizontal_number == 0:
                row += 1
            button = QPushButton(str(i + 1))
            self.gridLayout.addWidget(button, row, i % self.buttons_horizontal_number)
            button.clicked.connect(self.buttonHandlerFactory(i + 1))

    def player_input_send_button_handler(self):
        player_input = self.player_input.text()
        if player_input[-1] == ",":
            player_input = player_input[:-1]

        result = self.actual_game.single_player_input(player_input)

        ImageProcessing.merge_result_image(result, self.actual_game.round_number)

        new_variable = f"{player_input} {result}"
        self.game_history_listwidget.addItem(new_variable)
        self.player_input.setText("")

    def new_game_action_handler(self):
        self.dialog.show()


    @staticmethod
    def quit_action_handler():
        sys.exit()


class NewGameDialog(QDialog):
    def __init__(self, main_window):
        super(NewGameDialog, self).__init__()
        loadUi(r"../layouts/master_mind_new_game.ui", self)
        self.main_window = main_window
        self.start_game_button.clicked.connect(self.start_game_handler)

    def start_game_handler(self):
        try:
            a = int(self.sequence_length_lineEdit.text())
            b = int(self.symbols_quantity_lineEdit.text())
            c = int(self.round_number_lineEdit.text())

            if a > 0 and b > 0 and c > 0:
                pass
            else:
                pass  # Print error
        except ValueError:
            pass

        self.main_window.generateButtons(b)
        self.main_window.actual_game = GameProcess.Game(a, b, c)
        self.hide()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.start_game_handler()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()

    game_gui = MainWindow()
    game_gui.show()

    sys.exit(app.exec_())
