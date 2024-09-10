import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
from pyperclip import copy

from markdown_to_indent.markdown_to_indent import markdown_to_indent

# Constants
INPUTDims = (120, 22)
OUTPUTDims = (120, 22)
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 3
LABEL_WIDTH = 8


# Create the main window
def main():

    # Function to handle button click
    def convert_and_display():
        try:
            input_text = input_field.get(1.0, tk.END)
            output_text = markdown_to_indent(input_text)
            output_field.config(state="normal")
            output_field.delete(1.0, tk.END)
            output_field.insert(tk.END, output_text)
            output_field.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

    def copy_to_clipboard():
        try:
            copy(output_field.get("1.0", tk.END))
            messagebox.showinfo("Success", "Output copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def detections_and_convert():
        nonlocal last_input
        current_input = input_field.get(1.0, tk.END)
        if current_input != last_input:
            threading.Thread(target=convert_and_display).start()
            last_input = current_input
        main_window.after(1000, detections_and_convert)

    main_window = tk.Tk()
    main_window.title("Markdown to Indent Converter")

    # Create a new frame to hold input and output vertically
    vertical_frame = tk.Frame(main_window)
    print("tk.Frame:")
    print(vertical_frame.configure().keys())
    print("================================================")
    vertical_frame.pack(fill="both", expand=True)

    # Create frames for input and output
    inputframe = tk.Frame(vertical_frame)
    inputframe.pack(fill="both", expand=True)
    outputframe = tk.Frame(vertical_frame)
    outputframe.pack(fill="both", expand=True)

    # Create input field
    input_label = tk.Label(
        inputframe, text="Input:", font=("Arial", 12), width=LABEL_WIDTH, anchor="e"
    )
    print("tk.Label (diff):")
    print(set(input_label.configure().keys()) - set(vertical_frame.configure().keys()))
    print(vertical_frame.configure().keys())
    print("================================================")
    input_label.pack(side=tk.LEFT, padx=2)
    input_field = scrolledtext.ScrolledText(
        inputframe, width=INPUTDims[0], height=OUTPUTDims[1], wrap=tk.WORD
    )
    input_field.pack(side=tk.LEFT, fill="x", expand=True)

    # Create output field
    output_label = tk.Label(
        outputframe, text="Output:", font=("Arial", 12), width=LABEL_WIDTH, anchor="e"
    )
    output_label.pack(side=tk.LEFT, padx=2)
    output_field = scrolledtext.ScrolledText(
        outputframe, width=OUTPUTDims[0], height=OUTPUTDims[1], wrap=tk.WORD
    )
    output_field.pack(side=tk.LEFT, fill="x", expand=True)
    output_field.config(state="disabled")

    # Create the button
    buttonframe = tk.Frame(main_window)
    buttonframe.pack(fill="x")
    paste_button = tk.Button(
        buttonframe,
        text="Copy to Clipboard",
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        command=copy_to_clipboard,
    )
    paste_button.pack(side=tk.RIGHT, padx=20, pady=20)

    # Implement the delay functionality
    last_input = input_field.get(1.0, tk.END)

    detections_and_convert()

    main_window.mainloop()


if __name__ == "__main__":
    main()
