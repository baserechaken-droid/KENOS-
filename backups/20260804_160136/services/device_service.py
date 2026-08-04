from services.service_manager import register
from core.device import Device


class DeviceService:

    def battery(self):
        return Device.battery()

    def wifi(self):
        return Device.wifi()

    def torch(self, state):
        Device.torch(state)

    def speak(self, text):
        Device.speak(text)

    def vibrate(self, duration=300):
        Device.vibrate(duration)


register("device", DeviceService())
