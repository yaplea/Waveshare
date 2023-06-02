from board_pins import PINS
from machine import Pin
from neopixel import NeoPixel
import array
from time import sleep

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)


class Led:
    def __init__(self) -> None:
        self.pin = Pin(PINS.RGB, Pin.OUT)
        self.led = NeoPixel(self.pin, 1)
        self.brightness = 1

    def boot(self):
        for brightness in range(0, 1, .05):
            self.fill(RED * brightness, delay=.1)
        for _ in range(10):
            self.fill(RED, delay=1)
            self.fill(BLUE, delay=1)
        self.off()

    def fill(self,
             value,
             **kwargs):
        try:
            delay = kwargs["delay"]
        except:
            delay = 0
        self.led.fill(value)
        self.led.show()
        sleep(delay)

    def off(self):
        self.fill(BLACK)

    def warning(self):
        for _ in range(10):
            self.fill(RED, delay=.5)
            self.off()
            self.fill(RED, delay=.1)
            self.off()

    def idle(self):
        self.fill(GREEN)

    def blink(self,
              color,
              value):
        
        for _ in range(value):
            try:
                self.fill(color, delay=.2)
                self.off()
            except:
                self.warning()
                return
    
    def waterfall(self,
                  color):
        for brightness in range(0, 1, .05):
            self.fill(color * brightness, delay= .1)

    def watering(self,
                 nodes_watering: int):
        
        self.blink(GREEN, nodes_watering)
    