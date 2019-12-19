import pyautogui, time 

def draw(distance):
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.1)
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.1)
        pyautogui.dragRel(-distance, 0, duration=0.1)
        distance -= 5
        pyautogui.dragRel(0,-distance, duration=0.1)

time.sleep(2)
draw(200)