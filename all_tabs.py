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


# from tkinter import *
# from tkinter.ttk import Notebook
# from plot_window import PLOT_SCREEN
# root=Tk()
# root.geometry('640x480')
# tabControl=Notebook(root)
# tab1=Frame(tabControl)
# tab2=Frame(tabControl)

# # add contents to tab1
# Label(tab1,text='This is tab1').pack()


# # add contents to tab2
# Label(tab2,text='This is tab2').pack()


# tabControl.add(tab1,text='Plot')
# tabControl.add(tab2,text='GPS')
# tabControl.pack()


# root.mainloop()




from tkinter import *
from window_utilities import window_utils
from tkinter import ttk
from tkinter import messagebox
from plot_window_tab import PLOT_SCREEN
from gps_window_tab import GPS_WINDOW
from connect_device_tab import CONNECT_DEVICE
import serial
import serial.tools.list_ports as ports

class ALL_TABS:
    def __init__(self,window):
        window.withdraw()
        # self.serial_device=serial.Serial()
        self.go_ahead=False
        choice_window=Toplevel(window)
        self.baud_rates_list = [300, 600, 1200, 2400,
                                4800, 9600, 19200, 28800, 38400, 57600, 115200]
        self.comports = ports.comports()
        comport_frame=Frame(choice_window,bg='white')
        comport_frame.pack(side=TOP,anchor=CENTER)
        Label(comport_frame,text='Select COM Port',bg='white').pack(side=TOP,anchor=NW)
        comport_dropdown=window_utils.create_drop_down(comport_frame,self.comports)
        comport_dropdown.current(0)
        
        Label(comport_frame,bg='white',height=5).pack(side=TOP,anchor=NW)
        
        baudrate_frame=Frame(choice_window,bg='white')
        baudrate_frame.pack(side=TOP,anchor=CENTER)
        Label(baudrate_frame,text='Select Baud Rate',bg='white').pack(side=TOP,anchor=NW)
        baudrate_dropdown=window_utils.create_drop_down(baudrate_frame,self.baud_rates_list)
        baudrate_dropdown.current(5)
        Label(baudrate_frame,bg='white',height=5).pack(side=TOP,anchor=NW)
        window_width = 600
        window_height = 300
        center_x = int((window.winfo_screenwidth()-window_width)/2)
        center_y = int((window.winfo_screenheight()-window_height)/2)
        choice_window.geometry(f'600x400+{center_x}+{center_y}')
        choice_window.overrideredirect(True)
        choice_window.attributes('-topmost',True)
        choice_window.config(bg='white')
        def connect_device():
            try:
                self.serial_device=serial.Serial(str(comport_dropdown.get()).split('-')[0].strip(),baudrate_dropdown.get())
                choice_window.attributes('-topmost',False)
                choice_window.withdraw()
                # self.serial_device.port=str(comport_dropdown.get()).split('-')[0].strip()
                # self.serial_device.baudrate=int(baudrate_dropdown.get())
                messagebox.showinfo('Success','Device Connected')
                open_main_window()
            except:
                messagebox.showerror('Error','Error connecting to device')
                choice_window.deiconify()
            pass
        
        def exit_function():
            choice_window.withdraw()
            yes_no=messagebox.askyesno('Exit','Are you sure you want to exit?')
            if yes_no:
                exit()
            else:
                choice_window.deiconify()
        
        btn_frame=Frame(choice_window,bg='white')
        btn_frame.pack(side=TOP,anchor=CENTER)
        connect_btn=Button(btn_frame,text='CONNECT',command=connect_device)
        connect_btn.pack(side=LEFT,anchor=CENTER)
        
        exit_btn=Button(btn_frame,text='EXIT',command=exit_function,bg='#d9534f')
        exit_btn.pack(side=RIGHT,anchor=CENTER)
        def open_main_window():
            root = Toplevel(window)
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#d77337")
            style.map("TNotebook", background= [("selected", "#d77337")])
            root_width, root_height = window_utils.bring_screen_to_center(root)

            window_utils.set_heading(root)
            quit_btn=window_utils.quit_btn(root)
            def ask_before_quitting():
                if(messagebox.askyesno('QUIT', 'Do you really want to exit?')):
                    exit()
                pass
            quit_btn.config(command=ask_before_quitting)
            # insert tab control to the window
            tabControl = ttk.Notebook(root)
            tabControl.pack(side=TOP, anchor=W)

            # defining the tabs of the window
            plot_tab = Frame(tabControl,bg='white')
            gps_tab = Frame(tabControl,bg='white')
            connect_device_tab = Frame(tabControl,bg='white')


            tabControl.add(plot_tab, text='PLOT')
            tabControl.add(gps_tab, text='GPS')
            tabControl.add(connect_device_tab, text='CONNECT')
            tabControl.select(0)

            # insert the plot window in plot tab
            plt_screen=PLOT_SCREEN(plot_tab,self.serial_device)

            # insert the GPS window in gps tab
            gps_screen=GPS_WINDOW(gps_tab,self.serial_device)

            # insert the connect device window in connect device tab
            connect_device_screen=CONNECT_DEVICE(connect_device_tab,self.serial_device)
        
            def on_closing():
                window.deiconify()
                root.withdraw()
            root.protocol("WM_DELETE_WINDOW", on_closing)
        # root.overrideredirect(1)

        # root.mainloop()











 

 
 