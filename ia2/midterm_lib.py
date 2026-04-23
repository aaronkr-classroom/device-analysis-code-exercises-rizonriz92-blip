
class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

   
    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        # Comfortable: Temp 20-26 AND Humidity 40-60
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        # Warning: Temp >= 30 OR Humidity >= 70
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"

    def light_status(self):
        if self.light < 200:
            return "Dark"
        else:
            return "Bright"




sensors = [
    RoomSensor("Kitchen", 31, 72, 180),   # Warning / Dark
    RoomSensor("Bedroom", 22, 45, 150),   # Comfortable / Dark
    RoomSensor("Balcony", 25, 65, 500)    # Normal / Bright
]


count_comfortable = 0
count_normal = 0
count_warning = 0


for sensor in sensors:
    sensor.show_info()
    
    # Store the results of the methods to use them for printing and counting
    level = sensor.comfort_level()
    status = sensor.light_status()
    
    print(f"Comfort Level: {level}")
    print(f"Light Status: {status}")
    print("-" * 20)

    
    if level == "Comfortable":
        count_comfortable += 1
    elif level == "Normal":
        count_normal += 1
    elif level == "Warning":
        count_warning += 1


print("Final Totals:")
print(f"Comfortable: {count_comfortable}")
print(f"Normal: {count_normal}")
print(f"Warning: {count_warning}")