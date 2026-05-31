import sys
import os

# Add the project root to the path so we can import 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.event_bus import bus
import time

def monitor_sensors():
    print("Perception module active: Monitoring sensors...")
    try:
        while True:
            # In a real scenario, you'd poll termux-sensor here
            # For now, we simulate a 'sensor_update' event
            sensor_data = {"accelerometer": [0.1, 0.0, 9.8], "status": "active"}
            
            # Publish to the bus
            bus.publish("sensor_update", sensor_data)
            
            # Slow down the loop to save CPU
            time.sleep(2)
    except KeyboardInterrupt:
        print("Perception module stopped.")

if __name__ == "__main__":
    monitor_sensors()

