from pynput.keyboard import Key, Controller
import time 

keyboard = Controller()


def typed(word):
    for letter in word:
        keyboard.press(letter)
        keyboard.release(letter)
        time.sleep(0.2)
time.sleep(5)
typed('ESD Academy')