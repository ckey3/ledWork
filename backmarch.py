import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range(20,0):
        pixels[i] = (255,69,0)
        time.sleep(.25)

for x in range(1):
        pixels[x] = (255,69,0)
        time.sleep(.25)
