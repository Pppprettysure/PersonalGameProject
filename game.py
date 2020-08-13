import threading
from qt_interface import Window

def main():
    """ Kicks off game logic
    """
    window.update("okay")

class Game():
    def __init__(self):
        pass

    def process_input(self, actions, objects):
        for action, item in zip(actions, objects):
            # Item because object reserved
            window.update(action + item)


if __name__ == "__main__":
    # Run game logic in secondary thread because QT requires main thread
    game = Game()
    window = Window(game)
    game_thread = threading.Thread(target=main, daemon=True)
    game_thread.start()
    window.start()
