import tkinter as tk
from tkinter import messagebox
import threading
from pyperclip import copy
from src.markdown_to_indent import markdown_to_indent
from src.ui_components import (
    create_main_window,
    get_input_field,
    get_output_field,
)


# Function to handle conversion
def convert_and_display():
    try:
        input_text = get_input_field().get(1.0, tk.END)
        output_text = markdown_to_indent(input_text)
        output_field = get_output_field()

        output_field.config(state="normal")
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, output_text)
        output_field.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))


# Function to copy output to clipboard
def copy_to_clipboard():
    try:
        output_field = get_output_field()
        copy(output_field.get("1.0", tk.END))
        messagebox.showinfo("Success", "Copied!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Detection and conversion logic with delays
def detections_and_convert(main_window, last_input):
    current_input = get_input_field().get(1.0, tk.END)

    if current_input != last_input[0]:
        threading.Thread(target=convert_and_display).start()
        last_input[0] = current_input

    main_window.after(1000, detections_and_convert, main_window, last_input)


def main():
    # Initialize the window and UI components
    main_window, input_field, output_field, copy_button = create_main_window()

    # Set the command for the copy to clipboard button
    copy_button.config(command=copy_to_clipboard)

    # Start the detection and conversion logic
    last_input = [input_field.get(1.0, tk.END)]
    detections_and_convert(main_window, last_input)

    # Start the main loop
    main_window.mainloop()


if __name__ == "__main__":
    main()
