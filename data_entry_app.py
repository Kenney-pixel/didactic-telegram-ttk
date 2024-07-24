import tkinter as tk
from tkinter import ttk

from datetime import datetime
from pathlib import Path

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

# Create the dict to hold our variables
variables = dict()

# Variables to store the number of records saved
records_saved = 0

# Application heading
ttk.Label(
        root,
        text='ABQ Data Entry Application',
        font=('TkDefaultFont', 16)
        ).grid()

# Build the data record form in a Frame
drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)

r_info = ttk.LabelFrame(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

# Date
variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(r_info, textvariable=variables['Date']).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Time
time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(r_info, textvariable=variables['Time'], values=time_values).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Technician
variables['Technician'] = tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(r_info, textvariable=variables['Technician']).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Lab
variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
            labframe, value=lab, text=lab, variable=variables['Lab']
            ).pack(side=tk.LEFT, expand=True)
labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

# Plot
variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
        r_info,
        textvariable=variables['Plot'],
        values=list(range(1, 21))
        ).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Seed Sample
variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)
ttk.Entry(
        r_info,
        textvariable=variables['Seed Sample']
        ).grid(row=3, column=2, sticky=(tk.W + tk.E))

# Environment information frame
e_info = ttk.LabelFrame(drf, text="Environment Data")
e_info.grid(sticky=tk.W + tk.E)
for i in range(3):
    e_info.columnconfigure(i, weight=1)

# Humidity
variables['Humidity'] = tk.DoubleVar()
ttk.Label(e_info, text="Humdity (g/m^3)").grid(row=0, column=0)
ttk.Spinbox(
        e_info, textvariable=variables['Humidity'],
        from_=0.5, to=52.0, increment=0.01,
        ).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Light
variables['Light'] = tk.DoubleVar()
ttk.Label(e_info, text='Light (klx)').grid(row=0, column=1)
ttk.Spinbox(
        e_info, textvariable=variables['Light'],
        from_=0, to=100, increment=0.01
        ).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Temperature
variables['Temperature'] = tk.DoubleVar()
ttk.Label(e_info, text='Temperature (C)').grid(row=0, column=2)
ttk.Spinbox(
        e_info, textvariable=variables['Temperature'],
        from_=4, to=40, increment=.01
        ).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Equipment Fault
variables['Equipment Fault'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
        e_info, variable=variables['Equipment Fault'],
        text='Equipment Fault'
        ).grid(row=2, column=0, sticky=tk.W, pady=5)

# Plant information frame
p_info = ttk.LabelFrame(drf, text="Plant Data")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

# Plants
variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
        p_info, textvariable=variables['Plants'],
        from_=0, to=20, increment=1
        ).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Blossoms
variables['Blossoms'] = tk.IntVar()
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
        p_info, textvariable=variables['Blossoms'],
        from_=0, to=1000, increment=1
        ).grid(row=1, column=1, sticky=(tk.W + tk.W))

# Fruit
variables['Fruit'] = tk.IntVar()
ttk.Label(p_info, text='Fruit').grid(row=0, column=2)
ttk.Spinbox(
        p_info, textvariable=variables['Fruit'],
        from_=0, to=1000, increment=1
        ).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Min Height
variables['Min Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Min Height (cm)').grid(row=2, column=0)
ttk.Spinbox(
        p_info, textvariable=variables['Min Height'],
        from_=0, to=1000, increment=0.01
        ).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Max Height
variables['Max Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Max Height (cm)').grid(row=2, column=1)
ttk.Spinbox(
        p_info, textvariable=variables['Max Height'],
        from_=0, to=1000, increment=0.01
        ).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Med Height
variables['Med Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Med Height (cm)').grid(row=2, column=2)
ttk.Spinbox(
        p_info, textvariable=variables['Med Height'],
        from_=0, to=1000, increment=0.01
        ).grid(row=3, column=2, sticky=(tk.W + tk.E))

# Notes Section
ttk.Label(drf, text="Notes").grid()
notes_inp = tk.Text(drf, width=75, height=10)
notes_inp.grid(sticky=(tk.W + tk.E))

# Save and reset buttons
buttons = ttk.Frame(drf)
buttons.grid(sticky=tk.E + tk.W)
save_button = ttk.Button(buttons, text='Save')
save_button.pack(side=tk.RIGHT) 

reset_button = ttk.Button(buttons, text='Reset')
reset_button.pack(side=tk.RIGHT)

# Status Bar
status_variable = tk.StringVar()
ttk.Label(
        root, textvariable=status_variable
        ).grid(sticky=tk.W + tk.E, row=99, padx=10)

# Functions
def on_reset():
    """Called when reset button is clicked, or after save"""
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')

    # reset notes_inp
    notes_inp.delete('1.0', tk.END)

reset_button.configure(command=on_reset)

def on_save():
    """Handle the save button clicks"""
    global records_saved

    # For now, we save to a hardcoded filename with a datestring.
    # If it doesn't exist, create it,
    # otherwise just append to the existing file
    datestring = datetime.today().strftime("%Y-%m-%d")
    filename = f"abq_data_record_{datestring}.csv"
    newfile = not Path(filename).exists()

    # get the data from the variables

# Execute mainloop
root.mainloop()
