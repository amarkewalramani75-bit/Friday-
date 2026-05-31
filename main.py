import threading
from modules.perception.sensor_monitor import monitor_sensors
from modules.cognitive.brain import initialize_brain

def start_system():
    print("--- Starting FRIDAY System ---")
    
    # Initialize the Brain (Listening)
    # We do this first so the subscriber is ready before the publisher starts
    brain_thread = threading.Thread(target=initialize_brain, daemon=True)
    brain_thread.start()
    
    # Initialize the Sensors (Perceiving)
    sensor_thread = threading.Thread(target=monitor_sensors, daemon=True)
    sensor_thread.start()
    
    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n--- Shutting down FRIDAY ---")

if __name__ == "__main__":
    start_system()

