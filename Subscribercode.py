import time
import pyautogui
import webbrowser
from screeninfo import get_monitors

for m in get_monitors():
    print(str(m))
    
channel_url = [ 'https://www.youtube.com/c/YesTheory', 'https://www.youtube.com/c/YungChip', 'https://www.youtube.com/zerkaa', 'https://www.youtube.com/user/ZerkaaPlays', 'https://www.youtube.com/c/ZHcomicart']
for i in channel_url:
    if len(get_monitors())==1 and get_monitors()[0].height == 900 and get_monitors()[0].width == 1440:
        print('lezzgoooo')
        webbrowser.open(i)
        time.sleep(1)

        pyautogui.moveTo(1298, 380, 8)
        pyautogui.click()
        index = channel_url.index(i)

        pyautogui.moveTo(471,24,2)
        pyautogui.click()
        if index == 10:
            exit(0)
    else:
        print('This is not going to work')

exit(0)




        
        
