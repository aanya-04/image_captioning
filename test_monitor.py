from monitoring.monitor import SystemMonitor
import time
from pprint import pprint

monitor = SystemMonitor(interval=0.5)

print("Starting monitoring...")
monitor.start()

# Simulate some work
time.sleep(10)

monitor.stop()

print("\nSummary:\n")
pprint(monitor.summary())