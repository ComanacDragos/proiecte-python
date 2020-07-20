"""
GUI
"""
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from Domain import *
from PyQt5.QtGui import *


class GUI(QWidget):
    """
    Graphical user interface
    """

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Bligons")
        self.setFixedSize(524, 524)
        self.mainLayout = QVBoxLayout()

        self._board = Board(10)

        self.tableWidgetBoard = QTableWidget(10, 10, self)

        self.left = QShortcut(QKeySequence('A'), self)
        self.right = QShortcut(QKeySequence('D'), self)
        self.up = QShortcut(QKeySequence('W'), self)
        self.down = QShortcut(QKeySequence('S'), self)

        self.fire_shortcut = QShortcut(QKeySequence('Space'), self)
        self.cheat_shortcut = QShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_C, self)

        self.lost = QLabel("Lost")
        self.won = QLabel("Won")

        self.cheat_on = False

        self.setup_gui()
        self.load_board()
        self.initialize_commands()

        self.setStyleSheet(
            """
            QTableWidget{ background : black; border : black; }
            QWidget{ background : black; }
            """
        )

    def setup_gui(self):
        """
        Binds the widgets
        """
        self.tableWidgetBoard.horizontalHeader().hide()
        self.tableWidgetBoard.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidgetBoard.verticalHeader().setDefaultSectionSize(50)
        self.tableWidgetBoard.setSelectionMode(QAbstractItemView.NoSelection | QAbstractItemView.NoEditTriggers)
        self.tableWidgetBoard.verticalHeader().hide()

        self.mainLayout.addWidget(self.tableWidgetBoard)

        self.setLayout(self.mainLayout)

    def load_board(self):
        """
        Loads the bord in the table widget
        """
        for i in range(10):
            for j in range(10):
                code = self._board[i][j]
                item = QTableWidgetItem("")
                item.setFlags(QtCore.Qt.ItemIsSelectable)
                if self._board.is_star(code):
                    pix = QPixmap("Media/sun.png")
                    res_pix = pix.scaled(50, 50, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
                    brush = QBrush()
                    brush.setTexture(res_pix)
                    item.setBackground(brush)

                if self._board.is_bligon(code):
                    player = self._board.get_player_position()
                    if (i, j) in self._board.get_neighbours(*player) or self.cheat_on:
                        pix = QPixmap("Media/bligon.png")
                        res_pix = pix.scaled(50, 50, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
                        brush = QBrush()
                        brush.setTexture(res_pix)
                        item.setBackground(brush)

                if self._board.is_player(code):
                    orientation = self._board.player_orientation
                    pix = QPixmap("Media/player_" + str(orientation[0]) + str(orientation[1]) + ".png")
                    res_pix = pix.scaled(50, 50, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
                    brush = QBrush()
                    brush.setTexture(res_pix)
                    item.setBackground(brush)
                item.setTextAlignment(QtCore.Qt.AlignCenter)

                self.tableWidgetBoard.setItem(i, j, item)

    def move_player(self, row, column):
        """
        Moves the player by the specified values
       """
        try:
            self._board.move_player(row, column)
            self.load_board()
        except GameLost:
            self.lost.setMinimumSize(250, 250)
            self.lost.setWindowTitle("Game lost")
            self.lost.setAlignment(QtCore.Qt.AlignCenter)
            self.lost.setStyleSheet("font: 50px")
            self.close()
            self.lost.show()
        except BadMove:
            return

    def fire(self):
        """
        Fires at the position pointed to by the player
        """
        try:
            self._board.fire()
            self.load_board()
        except GameWon:
            self.won.setMinimumSize(250, 250)
            self.won.setWindowTitle("Game won")
            self.won.setAlignment(QtCore.Qt.AlignCenter)
            self.won.setStyleSheet("font: 50px")
            self.close()
            self.won.show()

    def cheat(self):
        """
        Turns on/off cheat(see the bligons)
        """
        self.cheat_on = not self.cheat_on
        self.load_board()

    def initialize_commands(self):
        """
        Initializes the commands
        """
        self.left.activated.connect(lambda: self.move_player(0, -1))
        self.right.activated.connect(lambda: self.move_player(0, 1))
        self.up.activated.connect(lambda: self.move_player(-1, 0))
        self.down.activated.connect(lambda: self.move_player(1, 0))
        self.fire_shortcut.activated.connect(lambda: self.fire())
        self.cheat_shortcut.activated.connect(self.cheat)


