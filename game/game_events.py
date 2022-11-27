import linecache
from pynput.keyboard import Key, Controller

def trigger_commands(keyboard: Controller, key: Key):
    keyboard.press(key)
    keyboard.release(key)

def process_events(keyboard: Controller, last_idx: int):
    content = linecache.getline('events.txt', last_idx)
    content = content.strip('\n\r')
    match content:
        case "UP":
            trigger_commands(keyboard, Key.up)
        case "DOWN":
            trigger_commands(keyboard, Key.down)
        case "LEFT":
            trigger_commands(keyboard, Key.left)
        case "RIGHT":
            trigger_commands(keyboard, Key.right)
        case "SELECT":
            trigger_commands(keyboard, Key.enter)