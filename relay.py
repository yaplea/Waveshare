from machine import Pins
from board_pins import PINS


class relay:
    def __init__(self, pin) -> None:
        if isinstance(pin, Pins):
            self.state = self.pin.value
        else:
            raise TypeError(f"Value is not a pin")

    def on(self):
        self.pin.on()
    
    def off(self):
        self.pin.off()

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value()

    
