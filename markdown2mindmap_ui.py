import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue
from pyperclip import copy

from markdown_to_indent.markdown_to_indent import markdown_to_indent

# Constants
INPUT_WIDTH = 120
INPUT_HEIGHT = 20
OUTPUT_WIDTH = 120
OUTPUT_HEIGHT = 30
BUTTON_WIDTH = 20


# Function to handle button click
def convert_and_display():
    input_text = input_field.get(1.0, tk.END)
    output_text = markdown_to_indent(input_text)
    output_field.config(state="normal")
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, output_text)
    output_field.config(state="disabled")


def copy_to_clipboard():
    try:
        copy(output_field.get("1.0", tk.END))
        messagebox.showinfo("Success", "Output copied to clipboard")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
def main():
    global input_field, output_field
    root = tk.Tk()
    root.title("Markdown to Indent Converter")

    # Create the input field
    input_label = tk.Label(root, text="Input:", font=("Arial", 12))
    input_label.grid(row=0, column=0)
    input_field = scrolledtext.ScrolledText(
        root, width=INPUT_WIDTH, height=INPUT_HEIGHT, wrap=tk.WORD
    )
    input_field.grid(row=1, column=0, columnspan=3)

    # Create the output field
    output_label = tk.Label(root, text="Output:", font=("Arial", 12))
    output_label.grid(row=2, column=0)
    output_field = scrolledtext.ScrolledText(
        root, width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT, wrap=tk.WORD
    )
    output_field.grid(row=3, column=0, columnspan=3)
    output_field.config(state="disabled")

    # Create the conversion button
    button = tk.Button(
        root, text="Copy to Clipboard", width=BUTTON_WIDTH, command=copy_to_clipboard
    )
    button.grid(row=4, column=0, columnspan=3)

    # Implement the delay functionality
    input_queue = queue.Queue()

    last_input = input_field.get(1.0, tk.END)

    def check_input_and_convert():
        nonlocal last_input
        current_input = input_field.get(1.0, tk.END)
        if current_input != last_input:
            threading.Thread(target=convert_and_display).start()
            last_input = current_input
        root.after(1000, check_input_and_convert)

    root.after(1000, check_input_and_convert)

    root.mainloop()


if __name__ == "__main__":
    main()
