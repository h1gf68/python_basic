from time import sleep
from itertools import cycle


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 7, "yellow": 2}

    def running(self):
        for color, t in cycle(self.__color.items()):
            print(f"\r{color.upper()}", end="")
            sleep(t)


trafficLightObj = TrafficLight()
trafficLightObj.running()
