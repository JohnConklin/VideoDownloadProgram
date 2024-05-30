# VideoDownload.py
# Import Module
from tkinter import *

from pytube import YouTube

# create root window
root = Tk()
root.resizable(width=True, height=True)


# root window title and dimension
root.title("Welcome to YouTube Video Copier")
# Set geometry(width x height)
root.geometry('500x170')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text="Enter the URL of the video:")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=45)
txt.grid(column=1, row=0)

# link = input("Enter the URL of video:")
# video = YouTube(link)
# stream = video.streams.get_highest_resolution()
# stream.download("X:\Programming\Python\Downloads")
link = input("Enter the URL of video:")
video = YouTube(link)

# function to display user text when
# button is clicked
def clicked():
    stream = video.streams.get_highest_resolution()
    stream.download("X:\\Programming\\Python\\Downloads")
    # res = "You wrote" + txt.get()
    # lbl.configure(text=res)


# button widget with red color text inside
btn = Button(root, text="Click me",
             fg="red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()

# import tkinter as tk
# window = tk.Tk()
# greeting = tk.Label(text="Enter URL of Video:",
#                     foreground="black",
#                     background="white"
#                    )
# greeting.pack()
# window.mainloop()

# button = tk.Button(
#    text="Click me!",
#    width=25,
#    height=5,
#    bg="blue",
#    fg="yellow"
#    );

#entry = tk.Entry(fg="yellow", bg="blue", width=50)

# label.pack()
# entry.pack()

