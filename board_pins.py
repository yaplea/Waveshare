from machine import Pin


class PINS:
    """
    This class is designed to simplify the pin usage.
    It allows for the direct call of the pins.
    
    For pin layout reference: 
    Pin locations not GP
    GROUND = [3,8,13,18,23,28,33,38]
    VBUS = 40
    VSYS = 39
    EN = 37
    OUT_3V = 36
    SOFTRESET = 30
    ADC_VREF = 35
    ANOLOG = [31,32,34]
    ANOLOG_GND = 33
    RELAY = [27,26,25,24,22,21,20,19]
    RGB = 17
    BUZZER = 9
    OPEN = [1,2,4,5,6,7,10,11,12,14,15,16,29]
    
    """

    ANOLOG_OUT = [Pin(pin, Pin.OUT) for pin in range(31,34)]
    ANOLOG_IN = [Pin(pin, Pin.IN) for pin in range(31,34)]
    RELAY = [Pin(pin, Pin.OUT) for pin in range(21,14,-1)]
    RGB = Pin(13, Pin.OUT)
    BUZZER = Pin(6, Pin.OUT)
    OPEN = [Pin(pin, Pin.OUT) for pin in range(0,12)] + [29]
    
    