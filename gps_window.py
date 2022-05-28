from tkinter import *
from window_utilities import window_utils
from PIL import ImageTk
import tkintermapview as mapview
from plot_window import PLOT_SCREEN

class GPS_WINDOW:
    def __init__(self, PREVIOUS_SCREEN):
        def open_plot_window():
            # self.THIS_SCREEN.withdraw()
            plot_window=PLOT_SCREEN(self.THIS_SCREEN)
            pass
        self.THIS_SCREEN = Toplevel(PREVIOUS_SCREEN)
        self.CANSAT_LONGITUDE = 18.518285031299342
        self.CANSAT_LATITUDE = 73.81472988306248
        window_utils.bring_screen_to_center(self.THIS_SCREEN)
        window_utils.set_heading(self.THIS_SCREEN)
        window_width = int(self.THIS_SCREEN.winfo_screenwidth())
        # window_width = 640
        window_height = int(self.THIS_SCREEN.winfo_screenheight())
        # creating the buttons inside the tabs frame in the main window
        # this exists for all the windows of the GUI
        TABS_FRAME = window_utils.create_frame(window=self.THIS_SCREEN)
        # inserting the switch to CANSAT window option
        OPEN_CANSAT_WINDOW = Button(
            TABS_FRAME, text='CANSAT', width=int(window_width*0.010))
        OPEN_CANSAT_WINDOW.pack(anchor=CENTER, side=LEFT)
        OPEN_PAYLOAD_WINDOW = Button(
            TABS_FRAME, text='PAYLOAD', width=int(window_width*0.010))
        OPEN_PAYLOAD_WINDOW.pack(
            anchor=CENTER, side=LEFT, padx=int(0.010*window_width))
        OPEN_PLOT_WINDOW = Button(
            TABS_FRAME, text='PLOTS', width=int(window_width*0.010),command=open_plot_window)
        OPEN_PLOT_WINDOW.pack(anchor=CENTER, side=LEFT)

        MAINFRAME = window_utils.create_frame(window=self.THIS_SCREEN)

        LATITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)

        LONGITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)

        ALTITUDE_FRAME = window_utils.create_frame(window=MAINFRAME)
        ALTITUDE_FRAME.pack(side=TOP, anchor=W)

        GPS_FRAME = window_utils.create_frame(window=MAINFRAME)
        GPS_FRAME.config(highlightbackground='#d77337', highlightthickness=5)
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
            window_width)*0.80, height=int(window_height)*0.6)
        gps_map.pack(anchor=CENTER, side=BOTTOM)
        gps_map.set_tile_server(
            'https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga', max_zoom=22)
        # set the college location
        gps_map.set_position(18.518285031299342,
                             73.81472988306248, marker=True, text='MITWPU')
        # set the satellite location
        gps_map.set_position(18.507249128665855,
                             73.80523053001455, marker=True, text='CANSAT')
        gps_map.set_path([(18.507249128665855, 73.80523053001455),
                         (18.518285031299342, 73.81472988306248)])
        gps_map.set_zoom(19)
        longitude_lbl_VAL.config(text=round(self.CANSAT_LONGITUDE, 4))
        latitude_lbl_VAL.config(text=round(self.CANSAT_LATITUDE, 4))


# root = Tk()
# root.withdraw()
# gps_scn = GPS_WINDOW(root)
# root.mainloop()
