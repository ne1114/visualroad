import os 
import random 
import carla
from common import *

try:
    start_carla(1)
except:
    print("smth wrong!")
finally:
    stop_carla()
