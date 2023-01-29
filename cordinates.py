import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Cordinates are ({x}, {y})")
    time.sleep(1)
