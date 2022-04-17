from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
from os import system


while True:
    pos = mouse.position
    pic = pyautogui.screenshot()
    system('cls')   
    print(pic.getpixel(pos))
   