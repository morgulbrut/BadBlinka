# Mini SAM template

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
import adafruit_dotstar
import digitalio

key_pin = digitalio.DigitalInOut(board.BUTTON)
key_pin.direction = digitalio.Direction.INPUT
key_pin.pull = digitalio.Pull.UP

dotstar = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
dotstar[0] = (0,120,120)

# your payloads go here
{{ . }}


# My example usecase
while True:
    while not key_pin.value:
        pass  # Wait for it to be ungrounded!

    dotstar[0] = (120,0,0) 
    payload_0()
    time.sleep(0.5)
    dotstar[0] = (0,120,0)