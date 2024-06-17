import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

# Create the dict to hold our variables
variables = dict()

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
ttk.Entry(
        r_info, textvariable=variables['Date']
        ).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Execute mainloop
root.mainloop()
