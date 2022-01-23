import time
from tracemalloc import start
import pyautogui
import random

start_time = time.time()

random.seed()
MAX_X, MAX_Y = pyautogui.size()

print('-----------------------------')
print('|   Welcome to Mousestic!   |')
print('-----------------------------')
print('Press Ctrl-C to quit...\n')
try:
    while True:
        r_x = random.randint(0, MAX_X)
        r_y = random.randint(0, MAX_Y)

        pyautogui.moveTo(x=r_x, y=r_y, duration=2)
        time.sleep(5)

except (KeyboardInterrupt, pyautogui.FailSafeException) as e:
    ellapsed_time = time.gmtime(time.time() - start_time)
    print('Total ellapsed time: {}'.format(time.strftime("%H:%M:%S", ellapsed_time)))
    print('Goodbye!')
