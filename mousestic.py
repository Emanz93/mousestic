import time
import pyautogui

start_time = time.time()

print('-----------------------------')
print('|   Welcome to Mousestic!   |')
print('-----------------------------')
try:
    while True:
        ellapsed_time = time.time() - start_time
        print('\rPress Ctrl-C to quit... {}'.format(time.strftime("%H:%M:%S", time.gmtime(ellapsed_time))), end='', flush=True)
        if int(ellapsed_time) % 10 == 0:
            pyautogui.press('capslock')
        time.sleep(1)
except (KeyboardInterrupt, pyautogui.FailSafeException) as e:
    total_ellapsed_time = time.gmtime(time.time() - start_time)
    print('\nTotal ellapsed time: {}'.format(time.strftime("%H:%M:%S", total_ellapsed_time)))
    print('Goodbye!')
