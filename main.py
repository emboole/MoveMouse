import mouse
import keyboard
import asyncio
import os

async def Moveme():
    mouse.move(5, 5, absolute=False, duration=0.2)
    mouse.move(-5, -5, absolute=False, duration=0.2)
    await asyncio.sleep(20)

def keyHook(info):
    while True:
        if keyboard.is_pressed("q"):
            print("chau")
            os._exit(0) 

keyboard.hook(keyHook)

while True:
    asyncio.run(Moveme())
    