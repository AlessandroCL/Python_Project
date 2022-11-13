import pyautogui 
import time
time.sleep(3)
count = 0
while count <= 200:
    pyautogui.typewrite("Entra")
    pyautogui.press("enter")
    count = count + 1
