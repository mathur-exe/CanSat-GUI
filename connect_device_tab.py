from tkinter import *
from tkinter import messagebox
from window_utilities import window_utils
import serial.tools.list_ports as ports
import serial
from PIL import Image, ImageTk
from tkinter import ttk


class CONNECT_DEVICE:
    def __init__(self, SCREEN, serial_device):
        print(id(serial_device))
        self.baud_rates_list = [300, 600, 1200, 2400,
                                4800, 9600, 19200, 28800, 38400, 57600, 115200]
        # self.serial_device = serial.Serial()
        self.serial_device = serial.Serial()
        comports = ports.comports()
        for port in comports:
            if 'Bluetooth' in (port):
                comports.remove(port)

        def ask_to_exit():
            if(messagebox.askyesno('EXIT', 'Do you want to really exit?')):
                exit()

        def connect_to_device():
            try:
                baud_rates_drop_down.config(state=DISABLED)
                comport_drop_down.config(state=DISABLED)
                self.serial_device.baudrate = int(baud_rates_drop_down.get())
                self.serial_device.port = str(
                    comport_drop_down.get()).split('-')[0].strip()
                print(baud_rates_drop_down.get())
                print(comport_drop_down.get())
                messagebox.showinfo(
                    'Connected', 'Device connected successfully')
                baud_rates_drop_down.config(state=not DISABLED)
                comport_drop_down.config(state=not DISABLED)
                connect_device_btn.config(state=DISABLED)
                # self.serial_device.reset_input_buffer()
                self.serial_device.open()
                # SCREEN.after(1,plot_data)
            except:
                messagebox.showerror('Error', 'An error occured')
                connect_device_btn.config(state=NORMAL)
            pass

        def change_screen(event):
            print(event.widget.get())
            pass

        def select_COM_port(event):
            self.COMPORT = event.widget.get()
            print(str(self.COMPORT).split('-')[0].strip())

        def update_comports():
            try:
                self.serial_device.close()
                comports = ports.comports()
                comport_drop_down['values'] = comports
                baud_rates_drop_down.config(state=not DISABLED)
                comport_drop_down.config(state=not DISABLED)
                connect_device_btn.config(state=NORMAL)
                messagebox.showinfo(
                    'RESET Successful', 'Please connect to device in order to get real time data')
            except:
                messagebox.showerror(
                    'ERROR', 'An error occured while resetting the connection with device.')
                baud_rates_drop_down.config(state=not DISABLED)
                comport_drop_down.config(state=not DISABLED)
                connect_device_btn.config(state=NORMAL)
            pass

        mainFrame = Frame(SCREEN, height=int(
            SCREEN.winfo_screenheight()), width=int(SCREEN.winfo_screenwidth()), bg='')
        mainFrame.pack(fill=BOTH, expand=True, anchor=CENTER)
        # SCREEN.withdraw()
        # window_utils.set_heading(mainFrame)
        comport_frame = Frame(mainFrame, bg='white')
        comport_frame.pack(side=TOP, anchor=CENTER, pady=40)
        comport_label = Label(comport_frame, text='Select COMPORT', bg='white', fg='#d77337', font=(
            'Arial', int(int(SCREEN.winfo_screenheight())/60), 'bold'))
        comport_label.pack(side=TOP, anchor=CENTER)
        comport_drop_down = window_utils.create_drop_down(
            comport_frame, comports)
        comport_drop_down.current(0)
        baud_rate_frame = Frame(mainFrame, bg='white')
        baud_rate_frame.pack(side=TOP, anchor=CENTER, pady=40)
        baud_rate_label = Label(
            baud_rate_frame, text='Select BAUD RATE', bg='white', fg='#d77337', font=('Arial', int(int(SCREEN.winfo_screenheight())/60), 'bold'))
        baud_rate_label.pack(side=TOP, anchor=CENTER)
        baud_rates_drop_down = window_utils.create_drop_down(
            baud_rate_frame, self.baud_rates_list)
        baud_rates_drop_down.current(0)
        connect_device_btn = Button(
            baud_rate_frame, text='CONNECT', width=20, relief=RAISED, command=connect_to_device)
        connect_device_btn.pack(pady=40)
        refresh_btn = Button(
            baud_rate_frame, text='Reset Connection', command=update_comports)
        refresh_btn.pack()


# window = Tk()
# window_utils.bring_screen_to_center(window)
# window_utils.set_heading(window)
# btn = Button(window, text='CONNECT DEVICE',
#              command=connect_device_screen).pack()
# window_utils.add_backgound(window)
# window.mainloop()
