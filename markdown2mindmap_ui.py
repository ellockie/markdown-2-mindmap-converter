import tkinter as tk
from tkinter import scrolledtext
import threading
import queue
import re
import time
from functools import partial

from markdown_to_indent.markdown_to_indent import markdown_to_indent

# Constants
INPUT_WIDTH = 80
INPUT_HEIGHT = 10
OUTPUT_WIDTH = 80
OUTPUT_HEIGHT = 15
BUTTON_WIDTH = 20

# # Function to convert Markdown to Indent
# def markdown_to_indent(text):
#     # Implement your Markdown to Indent conversion logic here
#     return text  # For demonstration purposes, just return the input

# Function to handle button click
def convert_and_display():
    input_text = input_field.get(1.0, tk.END)
    output_text = markdown_to_indent(input_text)
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, output_text)
    output_field.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("Markdown to Indent Converter")

# Create the input field
input_label = tk.Label(root, text="Input:", font=("Arial", 12))
input_label.grid(row=0, column=0)
input_field = scrolledtext.ScrolledText(root, width=INPUT_WIDTH, height=INPUT_HEIGHT, wrap=tk.WORD)
input_field.grid(row=1, column=0, columnspan=2)

# Create the output field
output_label = tk.Label(root, text="Output:", font=("Arial", 12))
output_label.grid(row=2, column=0)
output_field = scrolledtext.ScrolledText(root, width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT, wrap=tk.WORD)
output_field.grid(row=3, column=0, columnspan=2)
output_field.config(state="disabled")

# Create the conversion button
button = tk.Button(root, text="Convert", width=BUTTON_WIDTH, command=convert_and_display)
button.grid(row=4, column=0, columnspan=2)

# Implement the delay functionality
input_queue = queue.Queue()
def check_input_and_convert():
    global last_input
    current_input = input_field.get(1.0, tk.END)
    if current_input != last_input:
        threading.Thread(target=convert_and_display).start()
        last_input = current_input
    root.after(1000, check_input_and_convert)

last_input = input_field.get(1.0, tk.END)
root.after(1000, check_input_and_convert)

# Run the application
root.mainloop()
