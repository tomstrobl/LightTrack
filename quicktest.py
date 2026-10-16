from time import sleep
from lighttrack import LightTrack

track = LightTrack("/dev/cu.usbmodem1101", 1, 13, 30)

for distance in [1, 4, 7, 10, 13]:
    track.show(distance)
    sleep(1)

track.confirm()
sleep(1)

track.clear()
track.close()
