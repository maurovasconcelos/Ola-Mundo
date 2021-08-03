import pyautogui
from time import sleep

distance = 200
sleep(2)
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.2)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.2)   # move down
        pyautogui.drag(-distance, 0, duration=0.2)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.2)  # move up
