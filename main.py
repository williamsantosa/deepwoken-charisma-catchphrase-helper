import tkinter as tk
import pyautogui
import keyboard
import threading
import time

# settings variables
PREFIX = "ctrl+"
AUTOLEFTCLICK = False
LEFTCLICKDELAY = 2
CATCHPHRASES = [
    "Me-wow, is that the latest Felinor fashion?",
    "So, what's keeping you busy these days?",
    "Hey hivekin, can I bug you for a moment?",
    "So, how's work?",
    "Wow, this breeze is great, right?",
    "Sometimes I have really deep thoughts about life and stuff.",
    "Some weather we're having, huh?",
    "You ever been to a Canor restaurant? The food's pretty howlright."
]

# types out the catchphrase at the given index
def type_catchphrase(index):
    time.sleep(0.5)  # delay to ensure proper focus
    pyautogui.write(CATCHPHRASES[index], interval=0.01)

    # check if want to auto left click
    if not AUTOLEFTCLICK:
        return
    
    # left click after typing catchphrase
    time.sleep(LEFTCLICKDELAY)
    pyautogui.leftClick()

# function to set up hotkeys
def setup_hotkeys():
    for i in range(len(CATCHPHRASES)):
        # set up a hotkey for each catchphrase (Ctrl + 1, Ctrl + 2, ..., Ctrl + 9)
        keyboard.add_hotkey(f'{PREFIX}{i+1}', type_catchphrase, args=[i])

# Tkinter GUI Class
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Charisma Catchphrases")
        self.geometry("500x400")

        # create listbox information
        self.listbox = tk.Listbox(self, width=60, height=20, font=("Arial", 12))
        self.listbox.pack(pady=20)

        # populate listbox with catchphrases
        for i, phrase in enumerate(CATCHPHRASES):
            self.listbox.insert(tk.END, f"{PREFIX}{i+1}) {phrase}")

        # window on top
        self.attributes('-topmost', True)

        # window stays open on close
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        print("Closing window...")
        self.destroy()

# function to run gui
def run_gui():
    app = MainWindow()
    app.mainloop()

# main function (loops)
def main():
    # set up hotkeys in background thread
    hotkey_thread = threading.Thread(target=setup_hotkeys, daemon=True)
    hotkey_thread.start()

    # run gui
    run_gui()

if __name__ == "__main__":
    # start application
    main()