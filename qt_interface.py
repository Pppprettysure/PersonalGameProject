"""I/O handling for the game using QT.
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QGroupBox,
                             QVBoxLayout, QLabel, QComboBox, QTextEdit)


class Window():
    """A class representing the QT I/O System.

    Attributes
    ----------

    action_list : list
        a list of actions available to the player


    Methods
    ------

    start():
       Begins execution of QApplication. Init only sets up window.

    update(text="", action_list=[]):
        Takes input from logic to present to user.

    change_view(view):
        Changes to new view (menu system).
    """

    action_list = ['test', 'another test']

    def __init__(self):
        self.app = QApplication([])
        self.main_widget = QWidget()

        # Style and format
        self.main_widget.setWindowTitle('Game')
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.app.setStyle('fusion')

        # Add actionbox, for listing action combos
        self.actionbox = QGroupBox()
        self.action_layout = QVBoxLayout()

        # Add action rows to box
        self.add_action_row()
        self.add_action_row()
        self.add_action_row()
        self.add_action_row()

        self.main_layout.addWidget(self.actionbox)

        # Set up text display
        self.textbox = QTextEdit('some text')
        self.textbox.setReadOnly(True)
        self.main_layout.addWidget(self.textbox)

        # Display
        self.main_widget.show()
        self.actionbox.show()

    def start(self):
        """ Begins execution of QApplication.

            Must be ran in main thread.
        """
        self.app.exec_()


    def update(self, text="", action_list=[]):
        """Hands Window updated gamestate info.

        Give the full action and object list.

        Parameters
        ----------
        text : str, optional
            Text printed in the main console.

        action_list : list, optional
            List of actions currently available to the player.
        """

        print(self.textbox)
        if text:
            self.textbox.append(text)
        if action_list:
            self.action_list = action_list
        # TODO: add object list
        self.main_widget.show()

    # TODO: method to change views

    # TODO: connect to button
    def add_action_row(self):
        """Adds an action row to the action menu.

        For private use.
        """

        # Sets up layout for new row
        action_row_layout = QHBoxLayout()
        action_row_layout.addWidget(QLabel(str(1 + len(self.actionbox.findChildren(QGroupBox)))+'.'))
        action_list = QComboBox()
        for action in self.action_list:
            action_list.addItem(action)
        action_row_layout.addWidget(action_list)
        action_row_layout.addWidget(QComboBox())

        # Applies layout
        new_menu = QGroupBox()
        new_menu.setLayout(action_row_layout)
        self.action_layout.addWidget(new_menu)
        self.actionbox.setLayout(self.action_layout)

    # TODO: add function for removing from actionbox


if __name__ == "__main__":
    # Testing code
    try:
        window = Window()
        window.update('test')
        window.start()
        # TODO: is the code highjacked by the window? How do I seperate the code if that's the case?
    except Exception as error:
        print(error)
        while True:
            pass
