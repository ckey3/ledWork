import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

For i in range (14):
	pixels[i] = (10,0,0)
