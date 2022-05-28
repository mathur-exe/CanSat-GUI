from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.figure import Figure
from window_utilities import window_utils
import serial

class PLOT_SCREEN:
    def __init__(self, SCREEN):        
        data, temperature_c, temperature_f, humidity, heat_index_c, heat_index_f = window_utils.read_data()
        # ser=serial.Serial('COM7',9600)
        # ser.reset_input_buffer()
        # print(id(serial_device))
        self.temperature_c=temperature_c.to_numpy()
        def update_plot():
            try:
                # serial_device.open()
                # serial_data=ser.readline()
                # serial_data.decode()
                # print(float(serial_data.strip()))
                # temperature_c=temperature_c.tolist().append(10)
                self.temperature_c[-1]=10
                # self.temperature_c=
                # lines.set_xdata(temperature_c.tolist().append(10))
                lines.set_xdata(self.temperature_c)
                # print(temperature_c.tolist().append(10))
                # lines.set_xdata(float(serial_data.strip()))
                # print(type(temperature_c))
                canvas1.draw()
                print('update plot evoked')
                pass
            except Exception as e:
                print('error updating plot')
                print(e)
                pass
        
        # data, temperature_c, temperature_f, humidity, heat_index_c, heat_index_f = pd.Series(np.array(np.zeros(1))),pd.Series(np.array(np.zeros(1))),pd.Series(np.array(np.zeros(1))),pd.Series(np.array(np.zeros(1))),pd.Series(np.array(np.zeros(1))),pd.Series(np.array(np.zeros(1)))
        
        START_STOP_BTN_FRAME=window_utils.create_frame(SCREEN)
        start_plotting_btn=Button(START_STOP_BTN_FRAME,text='START PLOTTING',borderwidth=1,command=update_plot)
        start_plotting_btn.pack(side=LEFT,anchor=CENTER,padx=10)
        stop_plotting_btn=Button(START_STOP_BTN_FRAME,text='STOP PLOTTING')
        stop_plotting_btn.pack(side=LEFT,anchor=CENTER,padx=10)        
        
        
        
        
        
        figure = plt.figure(figsize=(20,8))        
        fig1 = figure.add_subplot(331)
        fig1.plot(temperature_c)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(temperature_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(temperature_c))
        ylim_start = 0
        # ylim_end = temperature_c.max()
        ylim_end = max(temperature_c)
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)
        lines=fig1.plot([],[])[0]

        fig1 = figure.add_subplot(332)
        fig1.plot(humidity)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Humidity %', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(humidity)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(humidity))
        ylim_start = 0
        ylim_end = humidity.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        fig1 = figure.add_subplot(333)
        fig1.plot(heat_index_c)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(heat_index_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(heat_index_c))
        ylim_start = 0
        ylim_end = heat_index_c.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        fig1 = figure.add_subplot(334)
        fig1.plot(temperature_f)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(temperature_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(temperature_f))
        ylim_start = 0
        ylim_end = temperature_f.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+10)

        fig1 = figure.add_subplot(336)
        fig1.plot(heat_index_f)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(heat_index_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(heat_index_f))
        ylim_start = 0
        ylim_end = heat_index_f.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)
        figure.tight_layout()

        canvas1 = FigureCanvasTkAgg(figure, master=SCREEN)
        canvas1.get_tk_widget().pack(anchor=CENTER,side=TOP)
        canvas1.draw()
        # canvas1._tkcanvas.pack()
        toolbar = NavigationToolbar2Tk(canvas1, SCREEN)
        toolbar.config(bg='')
        toolbar.update()
        


# def plot_screen():
#     plot_sc = PLOT_SCREEN(root)
#     pass



'''
BY DEFAULT THE WINDOW SHOULD ALL THE GRAPHS IN PLACE AS EMPTY

AFTER SUCCESSFUL CONNECTION WITH MCU IT SHOULD GET THE DATA AND UPDATE ACCORDINGLY

DECLARE THE PLOT OBJS SEPERATELY FOR EACH PLOT AND USE THEIR LINE PROPERTY FOR EFFICIENCY

KEEPING THE GRAPHS AND WINDOW STATIC AND CHANGING ONLY THE PLOT LINE AND THE GRAPH LIMITS IS THE WORK TO BE DONE.

THE GRAPH SHOULD BE SCROLLABLE WHENEVER PAUSED

'''