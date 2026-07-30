import tkinter as tk
import cv2
from tkinter import filedialog;
from PIL import Image, ImageTk
root = tk.Tk()

root.title("Image Brightness Editor")
root.geometry("800x700")
image_label = tk.Label(root)
image_label.pack(pady=20)

original_image = None
current_image = None

def upload_image(): 
    global original_image, current_image
    file_path = filedialog.askopenfilename()
    original_image = cv2.imread(file_path)
    current_image = original_image.copy()
    rgb_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)
    pil_image.thumbnail((700,500))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image
    print(current_image)

def increase_brightness():
    global current_image
    if current_image is None: 
        return
    current_image = cv2.convertScaleAbs(
        current_image, 
        alpha = 1.0,
        beta = 20
    )
    rgb_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)
    pil_image.thumbnail((700,500))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

def decrease_brightness():
    global current_image
    if current_image is None: 
        return
    current_image = cv2.convertScaleAbs(
        current_image, 
        alpha = 1.0, 
        beta = -20
    )
    rgb_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)
    pil_image.thumbnail((700,500))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

def reset_image():
    global original_image, current_image
    if original_image is None:
        return
    current_image = original_image.copy()
    rgb_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)
    pil_image.thumbnail((700,500))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=tk_image)
    image_label.image = tk_image


upload_button = tk.Button(
    root, 
    text="Choose File",
    command=upload_image
)
upload_button.pack(pady=10)

brightness_plus_button = tk.Button(
    root,
    text ="Brightness+",
    command=increase_brightness
)
brightness_plus_button.pack(pady=10)

brightness_minus_button = tk.Button(
    root,
    text ="Brightness-",
    command=decrease_brightness
)
brightness_minus_button.pack(pady=10)

reset_button = tk.Button(
    root,
    text = "Reset",
    command = reset_image
)

reset_button.pack(pady=10)


root.mainloop()
