"""I/O handling for the game using QT.
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QGroupBox,
                             QVBoxLayout, QLabel, QComboBox, QTextEdit,
                             QPushButton)


class Window():
    """A class representing the QT I/O System.

    Attributes
    ----------

    action_list : list
        a list of actions available to the player

    object_list : list
        a list of objects that can be interacted with


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
    object_list = ['person', 'door']

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

        # Add button to add action rows
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add_action_row)
        self.action_layout.addWidget(add_button)

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


    def update(self, text="", action_list=[], object_list=[]):
        """Hands Window updated gamestate info.

        Give the full action and object list.

        Parameters
        ----------
        text : str, optional
            Text printed in the main console.

        action_list : list, optional
            List of actions currently available to the player.

        object_list : list, optional
            List of objects that the player can interact with.
        """

        print(self.textbox)
        if text:
            self.textbox.append(text)
        if action_list:
            self.action_list = action_list
        if object_list:
            self.object_list = object_list
        self.main_widget.show()

    # TODO: method to change views
    # TODO: make it possible to swap position of actions
    # TODO: make action list a fixed size that scrolls

    def add_action_row(self):
        """Adds an action row to the action menu.

        For private use.
        """

        # Sets up layout for new row
        action_row_layout = QHBoxLayout()
        action_num = len(self.actionbox.findChildren(QGroupBox))
        action_row_layout.addWidget(QLabel(str(1 + action_num) + '.'))

        action_list = QComboBox()
        for action in self.action_list:
            action_list.addItem(action)

        object_list = QComboBox()
        for obj in self.object_list:
            object_list.addItem(obj)

        action_row_layout.addWidget(action_list)
        action_row_layout.addWidget(object_list)

        # Applies layout
        new_menu = QGroupBox()
        new_menu.setLayout(action_row_layout)
        self.action_layout.insertWidget(action_num, new_menu)
        self.actionbox.setLayout(self.action_layout)

    # TODO: add function for removing from actionbox


if __name__ == "__main__":
    # Testing code
    try:
        window = Window()
        window.update('test')
        window.start()
    except Exception as error:
        print(error)
        while True:
            pass
