from pynput import keyboard

def on_press(key):
    print(f'{key}: Key was pressed')

def on_release(key):
    # Quitting when esc key is pressed 
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.up:
        print('UP')
    if key == keyboard.Key.down:
        print('DOWN')
    if key == keyboard.Key.left:
        print('LEFT')
    if key == keyboard.Key.right:
        print('RIGHT')