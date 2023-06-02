from machine import Pin

waveshare_PINS = [x for x in range(19,27)]

class relay:
    def __init__(self, pin_value) -> None:
        if isinstance(pin_value, int):
            if any([pin_value in waveshare_PINS]):
                self.pin_number:int = pin_value
                self.setup()

            else:
                raise ValueError(f"Pin {pin_value} not an available pin")
        else:
            raise TypeError(f"Value {pin_value} not int")
        
    def setup(self):
        self.pin = Pin(self.pin_number, Pin.OUT)
        self.state = self.pin.value

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

    
