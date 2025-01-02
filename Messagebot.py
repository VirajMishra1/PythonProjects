import time
import pyautogui

def SendMessage():
    time.sleep(4)
    text = open('Imagine.txt')
    for each_paragraph in text:
        pyautogui.typewrite(each_paragraph)
        pyautogui.press('enter')

SendMessage()

