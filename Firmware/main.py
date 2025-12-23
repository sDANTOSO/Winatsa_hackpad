import board
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.OLED import OLED

# Initialize keyboard
keyboard = KMKKeyboard()

# Define layers module
layers = Layers()
keyboard.modules.append(layers)

# Define rotary encoder module
encoder_handler1 = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler1)

encoder_handler2 = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler2)

# Define keymap for 3x3 matrix
keyboard.keymap = [
    [KC.Q, KC.A],  # Top row
    [KC.E, KC.D,],  # Middle row
    [KC.W, KC.S,],  # Bottom row
]

# Assign rotary encoder actions
encoder_handler1.pins = (board.GP4, board.GP3)
encoder_handler1.divisor = 4
encoder_handler1.map = [KC.VOLD, KC.VOLU]  # Rotate Left = Volume Down, Rotate Right = Volume Up

# Define rotary encoder button
encoder_button = digitalio.DigitalInOut(board.GP28)
encoder_button.switch_to_input(pull=digitalio.Pull.UP)

class MyOLED(OLED):
    def draw(self, oled):
        oled.fill(0)
        oled.text("One day or day one", 0, 0, 1)
        oled.show()

oled_ext = MyOLED(
    i2c_num=0,
    i2c_scl='GP6',
    i2c_sda='GP5',
    width=128,
    height=32,
    flip=False
)
keyboard.extensions.append(oled_ext)


if __name__ == "__main__":
        keyboard.go()
       