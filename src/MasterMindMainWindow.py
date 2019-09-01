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
        self.dialog_input = None

        self.actual_game = None
        self.dialog = NewGameDialog(self)

        self.new_game_action.triggered.connect(self.new_game_action_handler)
        self.quit_action.triggered.connect(self.quit_action_handler)

        self.player_input_send_button.clicked.connect(self.player_input_send_button_handler)

        # self.gridLayout = QGridLayout()
        # self.scrollArea.setLayout(self.gridLayout)

    def buttonHandlerFactory(self, param):
        def handle():
            input_text = self.player_input.text()
            input_text += f"{param},"
            self.player_input.setText(input_text)
        return handle

    def generateButtons(self, count):
        row = 0
        for i in range(count):
            if i % 3 == 0:
                row += 1
            button = QPushButton(str(i + 1))
            self.gridLayout.addWidget(button, row, i % 3)
            button.clicked.connect(self.buttonHandlerFactory(i + 1))

    def player_input_send_button_handler(self):
        player_input = self.player_input.text()
        result = self.actual_game.single_player_input(player_input)

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

        self.main_window.generateButtons(b)
        self.main_window.actual_game = GameProcess.Game(a, b, c)
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()

    game_gui = MainWindow()
    game_gui.show()

    sys.exit(app.exec_())
