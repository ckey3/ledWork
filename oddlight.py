import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

for i in range(10):
        pixels[i*2] = (128,0,128)
