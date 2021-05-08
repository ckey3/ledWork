import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 20)

For i in range(0,20):
	Pixels[i] = (0,0,0)

For x in in range(0,20):
	Pixels[x] = (255,255,255)
	time.sleep(2.5)

For y in range(0,20):
	Pixels[y] = (0,0,0)
	time.sleep(2.7)
