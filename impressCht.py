import pyautogui
import time

print("Dimulai dlam 5dtk")
time.sleep(5)

for i in range(10):
    pyautogui.write("Yakin nih?")
    time.sleep(0.1)
    pyautogui.press("Enter")
