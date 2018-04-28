#Made modifications to API. Prints test; does not detect false flag.
import tello
import time

drone = tello.Tello('', 9000, imperial=False)

print(drone.takeoff())
time.sleep(6)

print(drone.move_up(90))
time.sleep(2)

print(drone.move_forward(300))
time.sleep(1)

print(drone.rotate_cw(90))
time.sleep(2)

print(drone.rotate_cw(90))
time.sleep(2)

print(drone.rotate_cw(90))
time.sleep(2)

print(drone.rotate_cw(90))
time.sleep(2)

print(drone.rotate_cw(180))
time.sleep(2)

print(drone.move_forward(300))
time.sleep(1)

print(drone.rotate_cw(360))
time.sleep(2)

print(drone.land())

print('Flight time: %s' % drone.get_flight_time())