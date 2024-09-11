import tkinter as tk
from tkinter import scrolledtext

# Constants
INPUTDims = (120, 22)
OUTPUTDims = (120, 22)
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 3
LABEL_WIDTH = 8

# Store input and output fields to access across modules
__input_field = None
__output_field = None
__copy_button = None


def create_main_window():
    """Creates and returns the main window and the important UI components (input_field, output_field, copy_button)."""
    global __input_field, __output_field, __copy_button

    main_window = tk.Tk()
    main_window.title("Markdown to Indent Converter")

    # Create a new frame for layout management
    vertical_frame = tk.Frame(main_window)
    vertical_frame.pack(fill="both", expand=True)

    # Input Frame with Label
    input_frame = tk.Frame(vertical_frame)
    input_frame.pack(fill="both", expand=True)

    input_label = tk.Label(
        input_frame, text="Input:", font=("Arial", 12), width=LABEL_WIDTH, anchor="e"
    )
    input_label.pack(side=tk.LEFT, padx=2)

    __input_field = scrolledtext.ScrolledText(
        input_frame, width=INPUTDims[0], height=OUTPUTDims[1], wrap=tk.WORD
    )
    __input_field.pack(side=tk.LEFT, fill="x", expand=True)

    # Output Frame with Label
    output_frame = tk.Frame(vertical_frame)
    output_frame.pack(fill="both", expand=True)

    output_label = tk.Label(
        output_frame, text="Output:", font=("Arial", 12), width=LABEL_WIDTH, anchor="e"
    )
    output_label.pack(side=tk.LEFT, padx=2)

    __output_field = scrolledtext.ScrolledText(
        output_frame, width=OUTPUTDims[0], height=OUTPUTDims[1], wrap=tk.WORD
    )
    __output_field.pack(side=tk.LEFT, fill="x", expand=True)
    __output_field.config(state="disabled")

    # Button Frame
    button_frame = tk.Frame(main_window)
    button_frame.pack(fill="x")

    __copy_button = tk.Button(
        button_frame, text="Copy to Clipboard", width=BUTTON_WIDTH, height=BUTTON_HEIGHT
    )
    __copy_button.pack(side=tk.RIGHT, padx=20, pady=20)

    return main_window, __input_field, __output_field, __copy_button


# Accessor Functions for input/output fields and copy button
def get_input_field():
    return __input_field


def get_output_field():
    return __output_field


def get_copy_button():
    return __copy_button
