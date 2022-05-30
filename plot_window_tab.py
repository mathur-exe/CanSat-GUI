from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from window_utilities import window_utils
import serial
from scipy.ndimage import gaussian_filter1d


class PLOT_SCREEN:
    def __init__(self, SCREEN):
        self.ser = serial.Serial('COM7', 9600)
        self.temperature_c = self.temperature_f = self.humidity = self.heat_index_c = self.heat_index_f = self.uv_index = self.uv_sensor_voltage = np.array([
                                                                                                                                                            0])
        # ser=serial.Serial('COM7',9600)
        # ser.reset_input_buffer()
        # print(id(serial_device))
        # self.temperature_c = temperature_c.to_numpy()

        def update_plot():
            try:
                # serial_device.open()
                # serial_data=ser.readline()
                # serial_data.decode()
                # print(float(serial_data.strip()))
                # temperature_c=temperature_c.tolist().append(10)
                data = self.ser.readline()
                data = data.decode()
                data = data.strip('\r\n')
                data = data.split(',')
                for i in range(len(data)):
                    data[i] = float(data[i])
                print((data))
                self.humidity = np.append((self.humidity), data[0])
                self.temperature_c = np.append(
                    (self.temperature_c), data[1])
                self.temperature_f = np.append(
                    (self.temperature_f), data[2])
                self.heat_index_c = np.append(
                    (self.heat_index_c), data[3])
                self.heat_index_f = np.append(
                    (self.heat_index_f), data[4])
                self.uv_index = np.append((self.uv_index), data[5])
                self.uv_sensor_voltage = np.append(
                    (self.uv_sensor_voltage), data[6])

                self.temperature_c[-1] = 10
                # self.temperature_c=
                # lines.set_xdata(temperature_c.tolist().append(10))
                lines1.set_xdata(self.temperature_c)
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

        START_STOP_BTN_FRAME = window_utils.create_frame(SCREEN)
        start_plotting_btn = Button(
            START_STOP_BTN_FRAME, text='START PLOTTING', borderwidth=1, command=update_plot)
        start_plotting_btn.pack(side=LEFT, anchor=CENTER, padx=10)
        stop_plotting_btn = Button(START_STOP_BTN_FRAME, text='STOP PLOTTING')
        stop_plotting_btn.pack(side=LEFT, anchor=CENTER, padx=10)

        figure = plt.figure(figsize=(20, 8))
        fig1 = figure.add_subplot(331)
        fig1.plot(self.temperature_c)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(self.temperature_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(self.temperature_c))
        ylim_start = 0
        # ylim_end = temperature_c.max()
        ylim_end = max(self.temperature_c)
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)
        lines1 = fig1.plot([], [])[0]

        fig2 = figure.add_subplot(332)
        fig2.plot(self.humidity)
        fig2.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig2.set_ylabel('Humidity %', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(self.humidity)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(self.humidity))
        ylim_start = 0
        ylim_end = self.humidity.max()
        fig2.set_xlim(xlim_start, xlim_end)
        fig2.set_ylim(ylim_start, ylim_end+5)

        fig3 = figure.add_subplot(333)
        fig3.plot(self.heat_index_c)
        fig3.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig3.set_ylabel('Heat Index C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(self.heat_index_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(self.heat_index_c))
        ylim_start = 0
        ylim_end = self.heat_index_c.max()
        fig3.set_xlim(xlim_start, xlim_end)
        fig3.set_ylim(ylim_start, ylim_end+5)

        fig4 = figure.add_subplot(334)
        fig4.plot(self.temperature_f)
        fig4.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig4.set_ylabel('Temperature F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(self.temperature_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(self.temperature_f))
        ylim_start = 0
        ylim_end = self.temperature_f.max()
        fig4.set_xlim(xlim_start, xlim_end)
        fig4.set_ylim(ylim_start, ylim_end+10)

        fig5 = figure.add_subplot(336)
        fig5.plot(self.heat_index_f)
        fig5.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig5.set_ylabel('Heat Index F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(self.heat_index_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(self.heat_index_f))
        ylim_start = 0
        ylim_end = self.heat_index_f.max()
        fig5.set_xlim(xlim_start, xlim_end)
        fig5.set_ylim(ylim_start, ylim_end+5)
        figure.tight_layout()

        canvas1 = FigureCanvasTkAgg(figure, master=SCREEN)
        canvas1.get_tk_widget().pack(anchor=CENTER, side=TOP)
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
