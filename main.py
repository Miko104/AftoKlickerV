import keyboard
import mouse
import time

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Кликер отсоновлен')
    else:
        isClicking = True
        print('Кликер подключон')


keyboard.add_hotkey('Alt + Z', set_clicker)

ran = True
while ran:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.0001)
