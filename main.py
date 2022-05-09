import mouse
import keyboard
import time

def Moveme():
    while True:
        print("mueve mouse")
        mouse.move(5, 5, absolute=False, duration=0.2)
        time.sleep(1)
        mouse.move(-5, -5, absolute=False, duration=0.2)

        if keyboard.is_pressed('q'):
            print("se apreto q")
            break

Moveme()

