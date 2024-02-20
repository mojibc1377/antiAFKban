import pyautogui
import time
from pynput import keyboard

# Delay before starting to press the key (in seconds)
initial_delay = 5

# Total duration of key pressing (in seconds)
total_duration = 1000

# Delay between each key press (in seconds)
keypress_interval = 0.1

# Flag to indicate whether the key pressing is enabled
key_pressing_enabled = True

def on_press(key):
    global key_pressing_enabled
    try:
        if key.char == 'i':
            key_pressing_enabled = not key_pressing_enabled
            if key_pressing_enabled:
                print("Key pressing enabled.")
            else:
                print("Key pressing disabled.")
            time.sleep(0.5)  # Add a small delay to prevent immediate toggling
    except AttributeError:
        pass

# Function to press the key for a specified duration
def press_key(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.press('w')
        time.sleep(keypress_interval)

# Delay before starting to press the key
time.sleep(initial_delay)

# Listener for key presses
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
while True:
    if key_pressing_enabled:
        # Press the key for the specified duration
        press_key(total_duration)
    else:
        time.sleep(0.1)  # Sleep to prevent high CPU usage when key pressing is disabled
