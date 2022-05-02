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


# import matplotlib.pyplot as plt
# import time
# import numpy as np
# import matplotlib.animation as animation
# import serial.tools.list_ports as ports
# import serial


# def get_COM_ports():
#     return (ports.comports())


# comport = str(get_COM_ports()[-1]).split(' ')[0]
# print(comport)
# baud = 9600


# def initialize_ser_communication():
#     ser = serial.Serial(comport, baud)
#     ser.close()
#     ser.open()
#     return ser


# def read_serial_data(ser):
#     data = ser.read()


# x = 0
# y = x**2

# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.plot(x, y)


# def animate(i):
#     ax1.clear()
#     x+=1
#     y=x**2
#     ax1.plot(x, y)


# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()


# from tkinter import *

# def donothing():
#    filewin = Toplevel(root)
#    button = Button(filewin, text="Do nothing button")
#    button.pack()

# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)

# filemenu.add_separator()

# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)

# editmenu.add_separator()

# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)

# menubar.add_cascade(label="Edit", menu=editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)

# root.config(menu=menubar)
# root.mainloop()


# from tkinter import *

# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('500x300')
# ws.config(bg='yellow')

# img = PhotoImage(file="./images/wpu.png")
# label = Label(
#     ws,
#     image=img
# )
# label.place(x=0, y=0)

# text = Text(
#     ws,
#     height=10,
#     width=53
# )
# text.place(x=30, y=50)

# button = Button(
#     ws,
#     text='SEND',
#     relief=RAISED,
#     font=('Arial Bold', 18)
# )
# button.place(x=190, y=250)

# menu=Menu(ws)

# GPS=menu.add_cascade(label='GPS',font=('Impact',30,'bold'))

# ws.config(menu=menu)
# ws.mainloop()


# get the coordinates of a place using name of place
# from geopy.geocoders import Nominatim
# loc=Nominatim(user_agent='GetLoc')
# getloc=loc.geocode('Pune')
# print(getloc.latitude)
# print(getloc.longitude)


# from tkinter import *
# import tkintermapview


# latitude = 18.518153
# longitude = 73.815232

# root = Tk()
# root.geometry('640x480')

# mylbl = Label(root)
# mylbl.pack(pady=20)

# mapwidget = tkintermapview.TkinterMapView(mylbl, width=640, height=480)
# mapwidget.pack()


# # set coordinates by default
# SAT_location =mapwidget.set_position(18.517226596733817, 73.81538809368527,marker=True,text='MITWPU GLOBE')
# MITWPU_location = mapwidget.set_position(
#     latitude, longitude, marker=True, text='MITWPU')
# mapwidget.set_path([(18.517226596733817, 73.81538809368527),(latitude,longitude)])
# mapwidget.update()

# # set zoom level
# mapwidget.set_zoom(18)

# root.mainloop()


import geocoder
import folium
g=geocoder.ip('me')
myadd=g.latlng
print(myadd)