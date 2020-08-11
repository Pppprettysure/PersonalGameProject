import threading
from qt_interface import Window

def main():
    """ Kicks off game logic
    """
    window.update("okay")


if __name__ == "__main__":
    # Run game logic in secondary thread because QT requires main thread
    window = Window()
    game_thread = threading.Thread(target=main, daemon=True)
    game_thread.start()
    window.start()
