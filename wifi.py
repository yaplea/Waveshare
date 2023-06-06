import network
from secret import hidden
from led import Led

    
class wifi_module:
    def __init__(self, **kwargs) -> None:
        self.wifi = network.WLAN(network.STA_IF)
        self.status = self.wifi.status
        self.led = kwargs.get("led", None)

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        return value

    def connect(self):
        Led.connecting()
        attempts = 0
        while not self.wifi.isconnected():
            attempts += 1
            self.wifi.active(True)
            self.wifi.connect(hidden.SSID, hidden.PASSKEY)
            if attempts > 5:
                raise ConnectionError
        Led.off()
        return None
    
    def disconnect(self):
        self.wifi.disconnect()

    def reconnect(self):
        attempts = 0
        while True:
            Led.warning = True
            try:
                self.connect()
            except:
                attempts += 1