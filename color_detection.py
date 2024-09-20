import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

# Function to detect color based on HSV values
def get_color_name(hsv_value):
    hue = hsv_value[0]
    saturation = hsv_value[1]
    value = hsv_value[2]

    if saturation < 40:  # Low saturation = grayscale (black, white, gray)
        if value < 50:
            return "Black"
        elif value < 200:
            return "Gray"
        else:
            return "White"

    # Define ranges for different colors
    if (hue >= 0 and hue < 10) or (hue >= 170 and hue <= 180):
        return "Red"
    elif hue >= 10 and hue < 25:
        return "Orange"
    elif hue >= 25 and hue < 35:
        return "Yellow"
    elif hue >= 35 and hue < 85:
        return "Green"
    elif hue >= 85 and hue < 170:
        return "Cyan"
    elif hue >= 170 and hue < 260:
        return "Blue"
    elif hue >= 260 and hue < 320:
        return "Purple"
    elif hue >= 320 and hue < 340:
        return "Pink"
    elif hue >= 340 and hue <= 360:
        return "Red"  # Red is a close match to pink in high hue ranges
    elif hue >= 80 and hue < 110:
        return "Lime"
    elif hue >= 150 and hue < 180:
        return "Teal"
    elif hue >= 40 and hue < 50:
        return "Light Yellow"
    return "Undefined"

# Function to detect the color when the mouse moves
def motion(event):
    x, y = event.x, event.y

    if x >= image_resized.shape[1] or y >= image_resized.shape[0]:
        return  # Ignore areas outside the image

    # Get the HSV value at the current mouse position
    hsv_value = hsv_image[y, x]
    
    # Get the color name
    color_name = get_color_name(hsv_value)

    # Update the label with the color name
    label_var.set(f"Color: {color_name}")

# Create a Tkinter window
root = Tk()
root.title("Color Detection on Hover")

# Load the image
image = cv2.imread('profile.jpg')
image_resized = cv2.resize(image, (600, 400))  # Resize for display

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2HSV)

# Convert the image to RGB for displaying in Tkinter
image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image_rgb)

# Convert the image for Tkinter display
image_tk = ImageTk.PhotoImage(image_pil)

# Create a label to display the color name
label_var = StringVar()
label = Label(root, textvariable=label_var, font=('Helvetica', 14))
label.pack()

# Create a canvas and add the image to it
canvas = Canvas(root, width=image_resized.shape[1], height=image_resized.shape[0])
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=image_tk)

# Bind the motion event to the canvas
canvas.bind('<Motion>', motion)

# Start the Tkinter event loop
root.mainloop()
