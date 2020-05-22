import os 
import random 
import carla

try:
    start_carla(1)
except:
    print("smth wrong!")
finally:
    stop_carla()
