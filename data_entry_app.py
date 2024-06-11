import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

# Application heading
ttk.Label(
        root,
        text='ABQ Data Entry Application',
        font=('TkDefaultFont', 16)
        ).grid()

# Execute mainloop
root.mainloop()
