import time

from board import SCL, SDA
import busio
from micropython import const

from adafruit_seesaw.seesaw import Seesaw

# Imports used to be a keyboard
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize the keyboard stuff
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


BUTTON_RIGHT = const(6)
BUTTON_DOWN = const(7)
BUTTON_LEFT = const(9)
BUTTON_UP = const(10)
BUTTON_SEL = const(14)
button_mask = const(
    (1 << BUTTON_RIGHT)
    | (1 << BUTTON_DOWN)
    | (1 << BUTTON_LEFT)
    | (1 << BUTTON_UP)
    | (1 << BUTTON_SEL)
)

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus)
ss.pin_mode_bulk(button_mask, ss.INPUT_PULLUP)

# your payloads go here
{{.}}

while True:
    buttons = ss.digital_read_bulk(button_mask)
    if not buttons & (1 << BUTTON_RIGHT):
        try:
            payload_0()
        except NameError:
            pass

    if not buttons & (1 << BUTTON_DOWN):
        try:
            payload_1()
        except NameError:
            pass

    if not buttons & (1 << BUTTON_LEFT):
        try:
            payload_2()
        except NameError:
            pass

    if not buttons & (1 << BUTTON_UP):
        try:
            payload_3()
        except NameError:
            pass

    time.sleep(0.1)
