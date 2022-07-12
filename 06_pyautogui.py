import pyautogui
import keyboard
from ctypes import windll, wintypes
import time

# Return positiom of cursor
print(pyautogui.position()) # in VSCode, use Ctrl+Alt+N as shortcut to run python script

# When automation starts, block any keyboard/mouse user inout
for i in range(150):
    keyboard.block_key(i)

# Click on windows Search Bar
pyautogui.click(148, 1053)
time.sleep(1)
# Type "Chrome"
pyautogui.typewrite("Chrome")
# Click Enter to open Chrome
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(841, 476) # (577, 466) or (841, 476)
# Maximise window
pyautogui.hotkey('ctrl', 'up')

# Unblock user input
for i in range(150):
    keyboard.unblock_key(i)