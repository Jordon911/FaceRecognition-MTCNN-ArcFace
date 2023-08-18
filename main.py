import os
import take_imgs
import norm_img
import train
import inference
from tkinter import *
import tkinter as tk
import threading


def cfaces_call():
    tkStatus.set("Capturing Faces...")
    status_label.update()
    take_imgs.takeImages()
    tkStatus.set("Faces Captured")
    status_label.update()


def take_imgs1():
    t1 = threading.Thread(target=cfaces_call, daemon=True)
    t1.start()

def normalize_img():
    tkStatus.set("Normalizing Faces...")
    status_label.update()
    norm_img.normal_img()
    tkStatus.set("Image Normalized")
    status_label.update()


def norm_img1():
    t2 = threading.Thread(target=normalize_img, daemon=True)
    t2.start()


def timages_call():
    tkStatus.set("Training Images...")
    status_label.update()
    train.TrainImages()
    tkStatus.set("Images Trained.")
    status_label.update()


def train1():
    t3 = threading.Thread(target=timages_call, daemon=True)
    t3.start()


def rfaces_call():
    tkStatus.set("Recognizing Faces...")
    status_label.update()
    inference.recognize_attendance()
    tkStatus.set("Faces Recognized.")
    status_label.update()


def inference1():
    t4 = threading.Thread(target=rfaces_call, daemon=True)
    t4.start()

root = Tk()
root.title("Contactless Attendance System")
tkStatus = tk.StringVar()


def open_registration_screen():
    global webcam_label
    root.withdraw()  # Hide the main window
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration")

    # Set the dimensions for the registration window
    main_window_width = root.winfo_width()  # Get the main window's width
    main_window_height = root.winfo_height()  # Get the main window's height
    registration_window.geometry(f"{main_window_width}x{main_window_height}")

    # Create a frame to contain webcam preview and buttons
    content_frame = tk.Frame(registration_window)
    content_frame.pack(pady=8)

    # Create a Label for webcam preview
    webcam_label = tk.Label(
        content_frame,
        width=640,  # Set the desired width
        height=480,  # Set the desired height
    )
    webcam_label.pack(pady=8)

    take_image_button = tk.Button(
        registration_window,
        text="TAKE IMAGE",
        command=take_imgs1,
        width=42,  # Adjust the width as needed
        height=2,  # Adjust the height as needed
        bg='#3498db',
        fg='#ffffff',
        bd=2,
        relief=tk.FLAT,
        activebackground="Green",
        activeforeground="White",
    )
    take_image_button.pack(pady=8)

    normalize_button = tk.Button(
        registration_window,
        text="NORMALIZE IMAGE",
        command=norm_img1,
        width=42,  # Adjust the width as needed
        height=2,  # Adjust the height as needed
        bg='#3498db',
        fg='#ffffff',
        bd=2,
        relief=tk.FLAT,
        activebackground="Green",
        activeforeground="White",
    )
    normalize_button.pack(pady=8)

    train_button = tk.Button(
        registration_window,
        text="TRAIN IMAGE",
        command=train1,
        width=42,  # Adjust the width as needed
        height=2,  # Adjust the height as needed
        bg='#3498db',
        fg='#ffffff',
        bd=2,
        relief=tk.FLAT,
        activebackground="Green",
        activeforeground="White",
    )
    train_button.pack(pady=8)

    def back_to_main_screen():
        registration_window.destroy()  # Close the registration window
        root.deiconify()  # Show the main window again

    # Back button to go back to the main screen
    back_button = tk.Button(
        registration_window,
        text="Back",
        command=back_to_main_screen,
        width=42,
        height=2,
        bg='red',
        fg='#ffffff',
        bd=2,
        relief=tk.FLAT,
        activebackground="Green",
        activeforeground="White",
    )
    back_button.pack(pady=8)





# ---------------main driver ------------------
# create a tkinter window


content_frame = tk.Frame(root)
content_frame.grid(row=1, column=0, padx=15, pady=8)

# Open window having dimension 100x100
# root.geometry('100x100')

# Create a Button

registration_button = tk.Button(
    root,
    text="REGISTRATION",
    command=open_registration_screen,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground="Green",
    activeforeground="White",
)
registration_button.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=5,  # Change to row=7
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
)

btn4 = tk.Button(
    root,
    text='RECOGNIZE FACES',
    command=inference1,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground="Green",
    activeforeground="White",
)

btn4.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=7,  # Change to row=7
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
)


btn5 = tk.Button(
    root,
    text='EXIT',
    command=root.destroy,
    width=42,
    bg='#3498db',
    fg='#ffffff',
    bd=2,
    relief=tk.FLAT,
    activebackground="Green",
    activeforeground="White",
)
btn5.grid(
    padx=15,
    pady=8,
    ipadx=24,
    ipady=6,
    row=8,  # Change to row=8
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
)

status_label = tk.Label(
    root,
    textvariable=tkStatus,
    bg='#eeeeee',
    anchor=tk.W,
    justify=tk.LEFT,
    relief=tk.FLAT,
    wraplength=350,
)
status_label.grid(
    padx=12,
    pady=(0, 12),
    ipadx=0,
    ipady=1,
    row=9,
    column=0,
    columnspan=4,
    sticky=tk.W + tk.E + tk.N + tk.S,
)


# Set the position of button on the top of window.

root.mainloop()
# mainMenu()
