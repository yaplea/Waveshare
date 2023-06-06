from board_pins import PINS
from neopixel import NeoPixel
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
        self.led = NeoPixel(PINS.RGB, 1)
        self.brightness = 1

    def boot(self):
        for brightness in range(0, 1, .05):
            self.fill(RED, brightness=brightness, delay=.1)
        for _ in range(10):
            self.fill(RED, delay=1)
            self.fill(BLUE, delay=1)
        self.off()

    def fill(self,
             value,
             **kwargs):
        self.led.brightness = kwargs.get("brightness", 1)
        delay = kwargs.get("delay", 1)
        self.led.fill[0] = value
        self.led.write()
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
                self.fill(color, delay = 3)
                self.off()
                sleep(3)
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

    
