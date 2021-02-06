# Importint the Board class
from board import Board

# To handle key moves aka listener
import keyboard_moves 
import time

# Creating an object
b = Board()


def on_release(key):
    # Quitting when esc key is pressed 
    if key == keyboard_moves.keyboard.Key.esc:
        # Stop listener
        return False

    # UP
    if key == keyboard_moves.keyboard.Key.up:
        b.board, b.current_empty =  b.move_up(b.current_empty, b.board) 
    # DOWN
    if key == keyboard_moves.keyboard.Key.down:
        b.board, b.current_empty =  b.move_down(b.current_empty, b.board) 
    # LEFT
    if key == keyboard_moves.keyboard.Key.left:
        b.board, b.current_empty =  b.move_left(b.current_empty, b.board) 
    # RIGHT
    if key == keyboard_moves.keyboard.Key.right:
        b.board, b.current_empty =  b.move_right(b.current_empty, b.board) 
    
    time.sleep(.1)
    b.refresh_screen()

def main():
    print(b)

    # Testing the listener 
    # ...or, in a non-blocking fashion:
    # Collect events until released
    with keyboard_moves.keyboard.Listener(
            on_press=keyboard_moves.on_press,
            on_release=on_release) as listener:
        listener.join()
    
    b.refresh_screen()


if __name__ == "__main__":
    main()