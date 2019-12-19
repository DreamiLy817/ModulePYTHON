from pynput.mouse import Button, Controller
import time 

mouse = Controller()

for i in range(10):
    mouse.position = (0,0)
    """ time.sleep(0.2)
    mouse.position = (250, 500)
    time.sleep(0.2)
    mouse.position = (500,500)
    time.sleep(0.2)
    mouse.position = (500, 250)
    time.sleep(0.2) """