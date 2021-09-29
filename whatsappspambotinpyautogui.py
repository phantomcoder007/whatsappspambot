import time
import pyautogui

time.sleep(3)
while True:
	pyautogui.typewrite("Your Message Here", interval=0.1)
	pyautogui.press('enter')