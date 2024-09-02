import tkinter as tk
from tkinter import ttk

from datetime import datetime
from pathlib import Path

import csv


# Time
time_values = ['8:00', '12:00', '16:00', '20:00']
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(r_info, textvariable=variables['Time'], values=time_values).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Technician
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(r_info, textvariable=variables['Technician']).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Lab
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
            labframe, value=lab, text=lab, variable=variables['Lab']
            ).pack(side=tk.LEFT, expand=True)
labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

# Plot
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
        r_info,
        textvariable=variables['Plot'],
        values=list(range(1, 21))
        ).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Seed Sample
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
ttk.Label(e_info, text="Humdity (g/m^3)").grid(row=0, column=0)
ttk.Spinbox(
        e_info, textvariable=variables['Humidity'],
        from_=0.5, to=52.0, increment=0.01,
        ).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Light
ttk.Label(e_info, text='Light (klx)').grid(row=0, column=1)
ttk.Spinbox(
        e_info, textvariable=variables['Light'],
        from_=0, to=100, increment=0.01
        ).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Temperature
ttk.Label(e_info, text='Temperature (C)').grid(row=0, column=2)
ttk.Spinbox(
        e_info, textvariable=variables['Temperature'],
        from_=4, to=40, increment=.01
        ).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Equipment Fault
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
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
        p_info, textvariable=variables['Plants'],
        from_=0, to=20, increment=1
        ).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Blossoms
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
        p_info, textvariable=variables['Blossoms'],
        from_=0, to=1000, increment=1
        ).grid(row=1, column=1, sticky=(tk.W + tk.W))

# Fruit
ttk.Label(p_info, text='Fruit').grid(row=0, column=2)
ttk.Spinbox(
        p_info, textvariable=variables['Fruit'],
        from_=0, to=1000, increment=1
        ).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Min Height
ttk.Label(p_info, text='Min Height (cm)').grid(row=2, column=0)
ttk.Spinbox(
        p_info, textvariable=variables['Min Height'],
        from_=0, to=1000, increment=0.01
        ).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Max Height
ttk.Label(p_info, text='Max Height (cm)').grid(row=2, column=1)
ttk.Spinbox(
        p_info, textvariable=variables['Max Height'],
        from_=0, to=1000, increment=0.01
        ).grid(row=3, column=1, sticky=(tk.W + tk.E))

# Med Height
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
    data = dict()
    fault = variables['Equipment Fault'].get()
    for key, variable in variables.items():
        if fault and key in ('Light', 'Humidity', 'Temperature'):
            data[key] = ''
        else:
            try:
                data[key] = variable.get()
            except tk.TclError:
                status_variable.set(f'Error in field: {key}, Data was not saved.')
                return

    # get the Text widget contents separately
    data['Notes'] = notes_inp.get('1.0', tk.END)

    # append the record to a csv
    with open(filename, 'a', newline='') as fh:
        csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
        if newfile:
            csvwriter.writeheader()
        csvwriter.writerow(data)

    records_saved += 1
    status_variable.set (
            f"{records_saved} records saved this session"
            )
    on_reset()

save_button.configure(command=on_save)

# reset the form
on_reset()
# Refector starts here

class LabelInput(tk.Frame):
    """A widget containing a label and input together"""

    def __init__(self, parent, label, var, input_class=ttk.Entry, input_args=None, label_args=None, **kwargs):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self

        # setup the label
        if input_class in (ttk.Checkbutton, ttk.Button):
            input_args["text"] = label # Buttons don't need label because they are built-in.
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))

        # setup the variable
        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["variable"] = self.variable
        else:
            input_args["textvariable"] = self.variable

        # set up the input
        if input_class == ttk.Radiobutton:
            # for Radiobutton, create one input per value
            self.input = tk.Frame(self)
            for v in input_args.pop('values', []):
                button = ttk.Radiobutton(
                        self.input, value=v, text=v, **input_args)
                button.pack(side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill=tk.X)
        else:
            self.input = input_class(self, **input_args)

        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.W + tk.E), **kwargs):
        super.grid(sticky=sticky, **kwargs)



class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def _add_frame(self, label, cols=3):
        """Add a label frame to the form"""
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)

        return frame

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create a dict to keep track of input widgets
        self._vars = {
                'Date': tk.StringVar(),
                'Time': tk.StringVar(),
                'Technician': tk.StringVar(),
                'Lab': tk.StringVar(),
                'Plot': tk.IntVar(),
                'Seed Sample': tk.StringVar(),
                'Humidity': tk.DoubleVar(),
                'Light': tk.DoubleVar(),
                'Temperature': tk.DoubleVar(),
                'Equipment Fault': tk.BooleanVar(),
                'Plants': tk.IntVar(),
                'Blossoms': tk.IntVar(),
                'Fruit': tk.IntVar(),
                'Min Height': tk.DoubleVar(),
                'Max Height': tk.DoubleVar(),
                'Med Height': tk.DoubleVar(),
                'Notes': tk.StringVar(),
                    }

        # Build the form
        self.columnconfigure(0, weight=1)

        # Record info section
        r_info = self._add_frame("Record Information")

        # Line 1
        LabelInput(r_info, "Date", var=self._vars['Date']).grid(row=0, column=0)
        LabelInput(r_info, "Time", input_class=ttk.Combobox, var=self._vars['Time'],
                   input_args={"values": ["8:00", "12:00", "16:00", "20:00"]}).grid(row=0, column=1)
        LabelInput(r_info, "Seed Sample", var=self._vars['Seed Sample']).grid(row=0, column=2)

        #Line 2

class Application(tk.Tk):
    """The application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # title bar
        self.title("ABQ Data Entry Application")
        self.columnconfigure(0, weight=1)
        
        # heading
        ttk.Label(
                self, text="ABQ Data Entry Application",
                font=("TkDefaultFont", 16)
                ).grid(row=0)

        # main form
        self.recordform = DataRecordForm(self)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))

        # status bar
        # next: do main form first

# Execute mainloop
if __name__ == '__main__':
    app = Application()
    app.mainloop()
