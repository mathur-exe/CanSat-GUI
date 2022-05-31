from tkinter import *
from tkinter import messagebox, ttk

import serial
import serial.tools.list_ports as ports
from plyer import notification

from connect_device_tab import CONNECT_DEVICE
from gps_window_tab import GPS_WINDOW
from payload_plot import PAYLOAD_PLOT_SCREEN
from plot_window_tab import PLOT_SCREEN
from window_utilities import window_utils


class ALL_TABS:
    def __init__(self, window):
        window.withdraw()
        self.go_ahead = False
        choice_window = Toplevel(window)
        window_utils.set_heading(choice_window)
        self.baud_rates_list = [300, 600, 1200, 2400,
                                4800, 9600, 19200, 28800, 38400, 57600, 115200]
        self.comports = ports.comports()
        comport_frame = Frame(choice_window, bg='white')
        comport_frame.pack(side=TOP, anchor=CENTER)
        Label(comport_frame, text='Select COM Port',
              bg='white').pack(side=TOP, anchor=NW)
        comport_dropdown = window_utils.create_drop_down(
            comport_frame, self.comports)
        comport_dropdown.current(0)

        Label(comport_frame, bg='white', height=3).pack(side=TOP, anchor=NW)

        baudrate_frame = Frame(choice_window, bg='white')
        baudrate_frame.pack(side=TOP, anchor=CENTER)
        Label(baudrate_frame, text='Select Baud Rate',
              bg='white').pack(side=TOP, anchor=NW)
        baudrate_dropdown = window_utils.create_drop_down(
            baudrate_frame, self.baud_rates_list)
        baudrate_dropdown.current(3)
        Label(baudrate_frame, bg='white', height=5).pack(side=TOP, anchor=NW)
        window_width = 600
        window_height = 300
        center_x = int((window.winfo_screenwidth()-window_width)/2)
        center_y = int((window.winfo_screenheight()-window_height)/2)
        choice_window.geometry(f'600x400+{center_x}+{center_y}')
        choice_window.overrideredirect(True)
        choice_window.attributes('-topmost', True)
        choice_window.config(bg='white')

        def connect_device():
            try:
                choice_window.withdraw()
                if 'USB Serial Device' not in str(comport_dropdown.get()):
                    messagebox.showerror(
                        'Error', 'Please select a compatible COM port')
                    choice_window.deiconify()
                    pass
                else:
                    self.serial_device = serial.Serial(
                        str(comport_dropdown.get()).split('-')[0].strip(), baudrate_dropdown.get())
                    choice_window.attributes('-topmost', False)
                    choice_window.withdraw()
                    notification.notify(
                        title='Success', message='Device Connected', timeout=5, toast=True)
                    open_main_window()
            except:
                messagebox.showerror('Error', 'Error connecting to device')
                choice_window.deiconify()
            pass

        def exit_function():
            choice_window.withdraw()
            yes_no = messagebox.askyesno(
                'Exit', 'Are you sure you want to exit?')
            if yes_no:
                exit()
            else:
                choice_window.deiconify()

        btn_frame = Frame(choice_window, bg='white')
        btn_frame.pack(side=TOP, anchor=CENTER)
        connect_btn = Button(btn_frame, text='CONNECT', command=connect_device)
        connect_btn.pack(side=LEFT, anchor=CENTER)

        exit_btn = Button(btn_frame, text='EXIT',
                          command=exit_function, bg='#d9534f')
        exit_btn.pack(side=RIGHT, anchor=CENTER)

        def open_main_window():
            root = Toplevel(window)
            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="#d77337")
            style.map("TNotebook", background=[("selected", "#d77337")])
            root_width, root_height = window_utils.bring_screen_to_center(root)

            window_utils.set_heading(root)
            quit_btn = window_utils.quit_btn(root)

            def ask_before_quitting():
                if(messagebox.askyesno('QUIT', 'Do you really want to exit?')):
                    exit()
                pass
            quit_btn.config(command=ask_before_quitting)
            # insert tab control to the window
            tabControl = ttk.Notebook(root)
            tabControl.pack(side=TOP, anchor=W)

            # defining the tabs of the window
            plot_tab = Frame(tabControl, bg='white')
            gps_tab = Frame(tabControl, bg='white')
            connect_device_tab = Frame(tabControl, bg='white')
            payload_plot_tab = Frame(tabControl, bg='white')

            tabControl.add(plot_tab, text='CANSAT PLOT')
            tabControl.add(gps_tab, text='GPS')
            tabControl.add(connect_device_tab, text='CONNECT')
            tabControl.add(payload_plot_tab, text='PAYLOAD PLOT')
            tabControl.select(0)

            # insert the plot window in plot tab
            plt_screen = PLOT_SCREEN(plot_tab, self.serial_device)

            # insert the GPS window in gps tab
            gps_screen = GPS_WINDOW(gps_tab, self.serial_device)

            # insert the connect device window in connect device tab
            connect_device_screen = CONNECT_DEVICE(
                connect_device_tab, self.serial_device)
            payload_screen = PAYLOAD_PLOT_SCREEN(
                payload_plot_tab, self.serial_device)

            def on_closing():
                window.deiconify()
                root.withdraw()
            root.protocol("WM_DELETE_WINDOW", on_closing)