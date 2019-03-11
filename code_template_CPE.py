# Circuit Playground Express template
 
import time
import board

# Imports used to be a keyboard
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
 
# Initialize the keyboard stuff
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Imports and initialization for my board and usecase
import neopixel
from digitalio import DigitalInOut, Direction, Pull

buttonA = DigitalInOut(board.BUTTON_A)
buttonB = DigitalInOut(board.BUTTON_B)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN

  
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.2)
pixels.fill((0, 120, 120))
pixels.show()

# your payloads go here
{{ . }}


# My example usecase
while True:
    if buttonA.value:  # button A is pushed
        pixels.fill((120,0,0))
        pixels.show()
        payload_0()
        pixels.fill((0,120,0))
        pixels.show()
    if buttonB.value:  # button B is pushed
        pixels.fill((120,50,0))
        pixels.show()
        payload_1()
        pixels.fill((0,120,50))
        pixels.show()
    time.sleep(.01)

