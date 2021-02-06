# Importint the Board class
from board import Board

# To handle key moves aka listener
import keyboard_moves 

# Creating an object
b = Board()


def main():
    print(b)

    # Testing the listener 
    # ...or, in a non-blocking fashion:
    # Collect events until released
    with keyboard_moves.keyboard.Listener(
            on_press=keyboard_moves.on_press,
            on_release=keyboard_moves.on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()