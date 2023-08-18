import os
import take_imgs
import norm_img
import train
import inference
from tkinter import *
import tkinter as tk
import threading
# import cv2
# from PIL import ImageTk
# import PIL


def cfaces_call(name, student_id, programme, tutorial_group, year_and_sem):
    tkStatus.set("Capturing Faces...")
    status_label.update()
    take_imgs.takeImages(name, student_id, programme, tutorial_group, year_and_sem)
    tkStatus.set("Faces Captured")
    status_label.update()

def take_imgs1(name_entry, student_id_entry, programme_entry, tutorial_group_entry, year_sem_entry, error_label):
    name = name_entry.get()
    student_id = student_id_entry.get()
    programme = programme_entry.get()
    tutorial_group = tutorial_group_entry.get()
    year_and_sem = year_sem_entry.get()

    if not (name and student_id and programme and tutorial_group and year_and_sem):
        error_label.config(text="Error: All fields are required!")
        return  # Don't proceed if any field is empty

    error_label.config(text="")  # Clear the error message
    tkStatus.set("")  # Clear any previous status message
    status_label.update()

    # Introduce a slight delay to show the "Updating Faces..." message
    tkStatus.set("Updating Faces...")
    status_label.update()
    root.update_idletasks()  # Force the update of the GUI to show the message

    t1 = threading.Thread(target=cfaces_call, args=(name, student_id, programme, tutorial_group, year_and_sem), daemon=True)
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
    root.withdraw()  # Hide the main window
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration")

    # Set the dimensions for the registration window
    # main_window_width = root.winfo_width()  # Get the main window's width
    # main_window_height = root.winfo_height()  # Get the main window's height
    main_window_width = 382
    main_window_height = 450
    registration_window.geometry(f"{main_window_width}x{main_window_height}")

    # Add entry widgets for user information
    name_label = tk.Label(registration_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(registration_window)
    name_entry.pack()

    student_id_label = tk.Label(registration_window, text="Student ID:")
    student_id_label.pack()
    student_id_entry = tk.Entry(registration_window)
    student_id_entry.pack()

    programme_label = tk.Label(registration_window, text="Programme:")
    programme_label.pack()
    programme_entry = tk.Entry(registration_window)
    programme_entry.pack()

    tutorial_group_label = tk.Label(registration_window, text="Tutorial Group:")
    tutorial_group_label.pack()
    tutorial_group_entry = tk.Entry(registration_window)
    tutorial_group_entry.pack()

    year_and_sem_label = tk.Label(registration_window, text="Year and Semester:")
    year_and_sem_label.pack()
    year_sem_entry = tk.Entry(registration_window)
    year_sem_entry.pack()

    error_label = tk.Label(registration_window, text="", fg="red")
    error_label.pack()

    take_image_button = tk.Button(
        registration_window,
        text="TAKE IMAGE",
        command=lambda: take_imgs1(name_entry, student_id_entry, programme_entry, tutorial_group_entry, year_sem_entry, error_label),
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
