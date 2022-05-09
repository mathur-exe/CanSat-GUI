from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr

# create global data
data=np.array([])
condition=False

# plot data function
def plot_data():
    global condition,data
    try:
        if condition:
            a=s.readline()
            a.decode()
            if len(data)<100:
                data=np.append(data,float(a[0:4]))
            else:
                data[0:99]=data[1:100]
                data[99]=float(a[0:4])
            lines.set_xdata(np.arange(0,len(data)))
            lines.set_ydata(data)
            canvas.draw()
    except:
        data=data
    root.after(1,plot_data)
    pass

def plot_start():
    global condition
    condition=True
    s.reset_input_buffer()
    pass


def plot_stop():
    global condition
    condition=False
    s.reset_input_buffer()


# global data
root=tk.Tk()
root.title('real time plot')
root.config(bg='white')
root.geometry('640x480')


# create figure object on gui
fig=Figure()
ax=fig.add_subplot(111)

ax.set_title('Linear Function y=x')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(0,100)
ax.set_ylim(0,100)
lines=ax.plot([],[])[0]

canvas=FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack()
canvas.draw()

# create buttons
# root.update()
start=tk.Button(root,text='START',command=plot_start)
start.pack()

# root.update()
stop=tk.Button(root,text='STOP')
stop.pack()



# start serial port
s=sr.Serial('COM11',9600)
s.reset_input_buffer()

root.after(1,plot_data)


root.mainloop()