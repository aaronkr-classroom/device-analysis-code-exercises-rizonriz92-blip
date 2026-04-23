import logging

logger = logging.getLogger(__name__)

class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light
        logger.info(f"Initialized RoomSensor '{self.name}' with temp={self.temperature}, humidity={self.humidity}, light={self.light}")

    def show_info(self):
        logger.debug(f"Displaying info for sensor: {self.name}")
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            level = "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            level = "Warning"
        else:
            level = "Normal"
            
        logger.debug(f"Comfort level for '{self.name}' evaluated to: {level}")
        return level

    def light_status(self):
        if self.light < 200:
            status = "Dark"
        else:
            status = "Bright"
            
        logger.debug(f"Light status for '{self.name}' evaluated to: {status}")
        return status
