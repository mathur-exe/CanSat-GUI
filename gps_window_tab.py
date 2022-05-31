from time import sleep
from tkinter import *
from window_utilities import window_utils
from PIL import ImageTk
import tkintermapview as mapview
from plot_window import PLOT_SCREEN
import serial
import numpy as np

class GPS_WINDOW:
    def __init__(self, SCREEN,serial_device):
        def open_plot_window():
            # self.SCREEN.withdraw()
            plot_window = PLOT_SCREEN(self.SCREEN)
            pass
        # self.SCREEN = Toplevel(SCREEN)
        self.SCREEN = SCREEN
        self.data=None
        # self.ser=serial.Serial('COM7',9600)
        self.ser=serial_device
        self.CANSAT_LATITUDE = 18.51883080425217
        self.CANSAT_LONGITUDE = 73.81659914010753
        # window_utils.bring_screen_to_center(self.SCREEN)
        # window_utils.set_heading(self.SCREEN)
        window_width = int(self.SCREEN.winfo_screenwidth())
        # window_width = 640
        window_height = int(self.SCREEN.winfo_screenheight())
        # creating the buttons inside the tabs frame in the main window
        # this exists for all the windows of the GUI
        # TABS_FRAME = window_utils.create_frame(window=self.SCREEN)
        # inserting the switch to CANSAT window option
        # OPEN_CANSAT_WINDOW = Button(
        #     TABS_FRAME, text='CANSAT', width=int(window_width*0.010))
        # OPEN_CANSAT_WINDOW.pack(anchor=CENTER, side=LEFT)
        # OPEN_PAYLOAD_WINDOW = Button(
        #     TABS_FRAME, text='PAYLOAD', width=int(window_width*0.010))
        # OPEN_PAYLOAD_WINDOW.pack(
        #     anchor=CENTER, side=LEFT, padx=int(0.010*window_width))
        # OPEN_PLOT_WINDOW = Button(
        #     TABS_FRAME, text='PLOTS', width=int(window_width*0.010), command=open_plot_window)
        # OPEN_PLOT_WINDOW.pack(anchor=CENTER, side=LEFT)
        
        def start_plotting():
            start_plotting_button['state'] = 'disabled'
            self.real_time_plotting_monitor = SCREEN.after(
                1000, start_real_time_gps)
            # sleep(2)
            # start_plotting_button['state'] = 'normal'
        def stop_plotting():
            SCREEN.after_cancel(self.real_time_plotting_monitor)
            start_plotting_button['state'] = 'normal'
        def start_real_time_gps():
            try:
                # while self.ser.in_waiting:
                self.data = self.ser.readline()
                self.data = self.data.decode()
                self.data = self.data.strip('\r\n')
                self.data = self.data.split(',')
                self.data=[float(x) for x in self.data]
                    
                    
                print(self.data)
                self.CANSAT_LATITUDE = self.data[7]
                self.CANSAT_LONGITUDE = self.data[8]
                self.cansat_location.set_position(self.CANSAT_LATITUDE, self.CANSAT_LONGITUDE)
                self.path.delete()
                self.path=gps_map.set_path([self.MITWPU_location.position,self.cansat_location.position])
                gps_map.set_position(self.CANSAT_LATITUDE, self.CANSAT_LONGITUDE)
                # gps_map.set_path([self.MITWPU_location.position,self.cansat_location.position])
                latitude_lbl_VAL.config(text=round(self.CANSAT_LATITUDE, 4))
                longitude_lbl_VAL.config(text=round(self.CANSAT_LONGITUDE, 4))
                # gps_map.set_zoom(15)
                random_val=np.random.randint(30,size=(1,1))
                random_val=random_val.tolist()
                random_val=random_val[0]
                random_val=random_val[0]
                altitude_lbl_val.config(text=round(abs(self.CANSAT_LATITUDE-self.CANSAT_LONGITUDE-random_val), 4))
                self.real_time_plotting_monitor = SCREEN.after(
                    1000, start_real_time_gps)
            except Exception as e:
                print(e)
                pass
        
        
        MAINFRAME = window_utils.create_frame(window=SCREEN)

        BUTTONS_FRAME = window_utils.create_frame(window=MAINFRAME)
        
        LATITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)

        LONGITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)

        ALTITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)
        ALTITUDE_FRAME.pack(side=TOP, anchor=W)

        GPS_FRAME = window_utils.create_frame(window=MAINFRAME)
        GPS_FRAME.config(highlightbackground='#d77337', highlightthickness=5)

        start_plotting_button = Button(BUTTONS_FRAME, text='START PLOTTING',command=start_plotting,bg='orange',fg='#ffffff',width=int(window_width*0.010))
        start_plotting_button.pack(side=LEFT, anchor=CENTER,padx=10)
        stop_plotting_button = Button(BUTTONS_FRAME, text='PAUSE PLOTTING', command=stop_plotting,bg='orange',fg='#ffffff',width=int(window_width*0.010))
        stop_plotting_button.pack(side=RIGHT, anchor=CENTER,padx=10)
        Label(LATITUDE_FRAME, text='Cansat Location Co-Ordinates',
              width=int(window_height/45), anchor=W, fg='#d77337', bg='white', font=(f'Arial {int(window_height/45)} bold')).pack(side=TOP, anchor=W, padx=int(window_width)*0.1)

        latitude_lbl = Label(LATITUDE_FRAME, text='LATITUDE', anchor=E)
        latitude_lbl.config(font=('Arial', int(window_height/45)),
                            borderwidth=2, width=int(window_width/100), background='white', fg='#d77337')
        latitude_lbl.pack(anchor=CENTER, side=LEFT)

        latitude_lbl_VAL = Label(LATITUDE_FRAME, text='VALUE'+' LATITUDE')
        latitude_lbl_VAL.config(font=('Arial', int(window_height/45)),
                                borderwidth=2, relief=GROOVE, width=int(window_width/100), background='white', fg='#d77337')
        latitude_lbl_VAL.pack(anchor=CENTER, side=LEFT)
        spacer = Label(LATITUDE_FRAME, width=int(
            window_width), background='white')
        spacer.pack(anchor=CENTER, side=LEFT, pady=int(window_height)*0.02)

        longitude_lbl = Label(LONGITUDE_FRAME, text='LONGITUDE', anchor=E)
        longitude_lbl.config(font=('Arial', int(window_height/45)),
                             borderwidth=2, width=int(window_width/100), background='white', fg='#d77337')
        longitude_lbl.pack(anchor=CENTER, side=LEFT)

        longitude_lbl_VAL = Label(LONGITUDE_FRAME, text='VALUE'+' LONGITUDE')
        longitude_lbl_VAL.config(font=('Arial', int(window_height/45)),
                                 borderwidth=2, relief=GROOVE, width=int(window_width/100), background='white', fg='#d77337')
        longitude_lbl_VAL.pack(anchor=CENTER, side=LEFT)
        spacer = Label(LONGITUDE_FRAME, width=int(
            window_width), background='white')
        spacer.pack(anchor=CENTER, side=LEFT, pady=int(window_width)*0.02)

        altitude_lbl = Label(ALTITUDE_FRAME, text='ALTITUDE', anchor=E)
        altitude_lbl.config(font=('Arial', int(window_height/45)),
                            borderwidth=2, width=int(window_width/100), background='white', fg='#d77337')
        altitude_lbl.pack(anchor=E, side=LEFT)
        spacer = Label(LONGITUDE_FRAME, width=int(
            window_width), background='white')
        spacer.pack(anchor=CENTER, side=LEFT, pady=int(window_width)*0.02)
        altitude_lbl_val = Label(ALTITUDE_FRAME, text='10'+' METERS')
        altitude_lbl_val.config(font=('Arial', int(window_height/45)),
                                borderwidth=2, relief=GROOVE, width=int(window_width/100), background='white', fg='#d77337')
        altitude_lbl_val.pack(anchor=CENTER, side=LEFT)

        gps_map = mapview.TkinterMapView(GPS_FRAME, width=int(
            window_width)*0.80, height=int(window_height)*0.5)
        gps_map.pack(anchor=CENTER, side=BOTTOM)
        gps_map.set_tile_server(
            'https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
        # set the college location
        self.mitwpu_lat = 18.518285031299342
        self.mitwpu_long = 73.81472988306248
        # gps_map.set_position(,
                            #  , marker=True, text='MITWPU')
        gps_map.set_position(self.mitwpu_lat, self.mitwpu_long)
        
        self.MITWPU_location=gps_map.set_marker(self.mitwpu_lat, self.mitwpu_long,text='MITWPU')
        # set the satellite location
        self.cansat_location=gps_map.set_marker(self.CANSAT_LATITUDE,self.CANSAT_LONGITUDE ,text='Cansat')
        # self.can_sat_location=gps_map.set_position(18.507249128665855,
        #                      73.80523053001455, marker=True, text='CANSAT')
        # gps_map.set_path([(18.507249128665855, 73.80523053001455),
                        #  (18.518285031299342, 73.81472988306248)])
        self.path=gps_map.set_path([self.MITWPU_location.position,self.cansat_location.position])
        gps_map.set_zoom(15)
        
        longitude_lbl_VAL.config(text=round(self.CANSAT_LONGITUDE, 4))
        latitude_lbl_VAL.config(text=round(self.CANSAT_LATITUDE, 4))
        # self.real_time_plotting_monitor=SCREEN.after(1000, start_real_time_gps)
        


# root = Tk()
# root.withdraw()
# gps_scn = GPS_WINDOW(root)
# root.mainloop()
