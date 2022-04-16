# import serial.tools.list_ports as ser
# import serial
# ports = ser.comports()
# ser1 = serial.Serial()

# portlist = []
# for port in ports:
#     portlist.append(str(port))
#     print(str(port))

# val = input("select port COM")

# for x in range(len(portlist)):
#     if portlist[x].startswith("COM"+(val)):
#         portvar = "COM"+val
#         print(portvar)

# ser1.baudrate = 9600
# ser1.port = portvar
# ser1.open()
# while 1:
#     try:
#         if(ser1.in_waiting):
#             packet = ser1.readline()
#             packet = packet.decode('utf').rstrip('\n')
#             print((packet))
#     except Exception as e:
#         print('disconnected\n',e)


# --------------------------------------------------------------------------------------------------------

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x_vals = [0, 1, 2, 3, 4, 5]
x_vals = []
y_vals = [0, 1, 3, 2, 3, 5]
y_vals = []
# plt.plot(x_vals,y_vals)
index = count()


def onClick(event):
    global pause
    pause ^= True


fig = plt.figure()
fig,axes = plt.subplots()



def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_vals, y_vals)
    x_start = 0
    if(len(x_vals) < 60):
        x_start = 0
    else:
        x_start = len(x_vals)-60
    plt.xlim(x_start, len(x_vals))
    plt.ylim(0, max(y_vals)+2)


ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.show()
