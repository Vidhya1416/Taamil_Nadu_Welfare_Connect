import tkinter as tk
from PIL import Image, ImageTk

def set_background(root):
    background_image = Image.open("background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, anchor="nw")
