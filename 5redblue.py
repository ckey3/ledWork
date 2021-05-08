import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

For i in range (4):
	pixels[i] = (255,0,0)

For i in range (5, 20):
	pixels[i] = (0,0,10)
