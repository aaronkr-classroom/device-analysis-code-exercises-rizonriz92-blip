import logging
from lib.room_sensor import RoomSensor

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger(__name__)
    
    logger.info("Starting IoT Midterm Practical Task")

    # Create at least 3 RoomSensor objects
    sensor1 = RoomSensor("Kitchen", 31, 72, 180)
    sensor2 = RoomSensor("Bedroom", 24, 50, 250)
    sensor3 = RoomSensor("Balcony", 28, 65, 500)

    # Store them in a list
    sensors = [sensor1, sensor2, sensor3]
    logger.info(f"Created {len(sensors)} sensor objects")

    # Extra Challenge (Bonus) setup
    counts = {
        "Comfortable": 0,
        "Normal": 0,
        "Warning": 0
    }

    # Loop through the list
    for sensor in sensors:
        logger.info(f"Processing sensor: {sensor.name}")
        
        # Print each sensor's information
        sensor.show_info()
        
        # Print the comfort level
        comfort = sensor.comfort_level()
        print(f"Comfort Level: {comfort}")
        
        # Print the light status
        light = sensor.light_status()
        print(f"Light Status: {light}\n")
        
        # Increment counter for bonus
        if comfort in counts:
            counts[comfort] += 1

    # Print the totals
    logger.info("Finished processing sensors, printing totals")
    print("Comfortable:", counts["Comfortable"])
    print("Normal:", counts["Normal"])
    print("Warning:", counts["Warning"])
    
    logger.info("IoT Midterm Practical Task completed successfully")

if __name__ == "__main__":
    main()
