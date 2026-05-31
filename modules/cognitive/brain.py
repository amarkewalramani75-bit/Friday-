import sys
import os

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.event_bus import bus

def handle_sensor_data(data):
    """This is our callback function - what the brain does with the data."""
    accel = data.get("accelerometer")
    print(f"[BRAIN] Processing sensor update: {accel}")
    
    # Simple logic: If the phone is tilted (example threshold)
    if accel[2] < 9.0:
        print("[BRAIN] Action Required: Phone movement detected!")

def initialize_brain():
    print("Cognitive module active: Brain is listening...")
    # Subscribe to the event we defined in the sensor module
    bus.subscribe("sensor_update", handle_sensor_data)

if __name__ == "__main__":
    initialize_brain()
    # Keep the script running to listen
    import time
    while True:
        time.sleep(1)

