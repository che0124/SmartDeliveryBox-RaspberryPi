#!/usr/bin/env python
import LCD1602
import time

LCD1602.init(0x27, 1)   # init(slave address, background light)
LCD1602.write(0, 0, 'Hi....')
LCD1602.write(1, 1, 'I am Joseph')
time.sleep(2)

try:
    print('Press Ctrl-C To Stop')
    LCD1602.clear()
    while True:
        LCD1602.write(0, 0,"Date: {}".format(time.strftime("%Y/%m/%d")))
        LCD1602.write(0, 1,"Time: {}".format(time.strftime("%H:%M:%S")))
        time.sleep(1)
except KeyboardInterrupt:
    print('Close Program')
finally:
    LCD1602.clear()

