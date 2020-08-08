"""Output for the game using QT.  
"""

from PyQt5.QtWidgets import *


class window():
    # action_menu_list = []
    action_list = ['test', 'another test']

    def __init__(self):
        self.app = QApplication([])
        self.main_widget = QWidget()

        # style and format
        self.main_widget.setWindowTitle('Game')
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.app.setStyle('fusion')

        # add widgets
        # add action_box
        self.action_box = QGroupBox()
        self.action_layout = QVBoxLayout()

        # add submenu to action_box
        # self.action_menu_list += [self.add_action_menu(1)]
        self.add_action_menu(1)
        self.add_action_menu(1)
        self.add_action_menu(1)
        self.add_action_menu(1)
        self.main_layout.addWidget(self.action_box)

        # set up text display
        self.textbox = QTextEdit('some text')
        self.textbox.setReadOnly(True)
        self.main_layout.addWidget(self.textbox)

        # display
        self.main_widget.show()
        self.action_box.show()
        self.update('test')
        self.app.exec_()

    def update(self, text="", action_list=[]):
        print(self.textbox)
        if text:
            self.textbox.append(text)
        if action_list:
            self.item_list = action_list
        # action_num = len(self.action_box.findChildren(QGroupBox))
        # while action_num < len(self.action_menu_list):
        #     self.action_menu_list +=
        #     action_num += 1
        self.main_widget.show()
        pass

    def add_action_menu(self, num):
        # set up layout for submenus
        action_menu_layout = QHBoxLayout()
        action_menu_layout.addWidget(QLabel(str(1 + len(self.action_box.findChildren(QGroupBox)))+'.'))
        action_list = QComboBox()
        for action in self.action_list:
            action_list.addItem(action)
        action_menu_layout.addWidget(action_list)
        action_menu_layout.addWidget(QComboBox())

        # apply layout
        new_menu = QGroupBox()
        new_menu.setLayout(action_menu_layout)
        self.action_layout.addWidget(new_menu)
        self.action_box.setLayout(self.action_layout)
        # return new_menu


try:
    window = window()
except Exception as error:
    print(error)
    while(True):
        pass
