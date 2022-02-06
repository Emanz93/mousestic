import time
from tracemalloc import start
import pyautogui
import random

start_time = time.time()

random.seed()
MAX_X, MAX_Y = pyautogui.size()
MAX_X = MAX_X - 100
MAX_Y = MAX_Y - 100

SLEEP_TIME = 2 # seconds
CURSOR_SPEED = 2 # second

print('-----------------------------')
print('|   Welcome to Mousestic!   |')
print('-----------------------------')
#print('Cursor speed: {} seconds'.format(CURSOR_SPEED))
#print('Sleep time  : {} seconds'.format(SLEEP_TIME))
print('Press Ctrl-C to quit...\n')
try:
    while True:
        pyautogui.press('capslock')
        time.sleep(10)
        pyautogui.press('capslock')
        time.sleep(10)

except (KeyboardInterrupt, pyautogui.FailSafeException) as e:
    ellapsed_time = time.gmtime(time.time() - start_time)
    print('Total ellapsed time: {}'.format(time.strftime("%H:%M:%S", ellapsed_time)))
    print('Goodbye!')
