import customtkinter as ctk
import threading
from pyperclip import copy
from src.markdown_to_indent import markdown_to_indent
from src.ui_components import (
    create_main_window,
    get_input_field,
    get_output_field,
)

"""
This script initializes a CustomTkinter GUI application that converts Markdown text to indented text.
It includes a main window with input and output text areas, a button to copy the output to the clipboard,
and custom dialog classes for displaying error and success messages.

If having issuesa with the _tkinter module, follow the instructions in the link below:
https://claude.ai/chat/59f8ab44-c264-4b29-9796-3fa5a798ec09 (Solution 2)
"""


# Custom CTK Dialog Classes
class CTkErrorDialog(ctk.CTkToplevel):
    def __init__(self, title="Error", message="An error occurred"):
        super().__init__()
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)

        # Center the dialog
        self.transient(self.master)
        self.grab_set()

        # Create and pack widgets
        self.label = ctk.CTkLabel(self, text=message, wraplength=350)
        self.label.pack(pady=20, padx=20)

        self.button = ctk.CTkButton(self, text="OK", command=self.destroy)
        self.button.pack(pady=10)


class CTkSuccessDialog(ctk.CTkToplevel):
    def __init__(self, title="Success", message="Operation completed successfully"):
        super().__init__()
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)

        # Center the dialog
        self.transient(self.master)
        self.grab_set()

        # Create and pack widgets
        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(pady=20, padx=20)

        self.button = ctk.CTkButton(self, text="OK", command=self.destroy)
        self.button.pack(pady=10)

        # Auto-close after 2 seconds
        self.after(2000, self.destroy)


# Function to handle conversion
def convert_and_display():
    try:
        input_text = get_input_field().get(
            "1.0", "end-1c"
        )  # Use "end-1c" instead of ctk.END
        output_text = markdown_to_indent(input_text)
        output_field = get_output_field()

        output_field.configure(state="normal")
        output_field.delete("1.0", "end")  # Use "end" instead of ctk.END
        output_field.insert(
            "1.0", output_text
        )  # Use "1.0" instead of ctk.END for insert
        output_field.configure(state="disabled")
    except Exception as e:
        # Show error using CustomTkinter dialog
        CTkErrorDialog("Conversion Error", str(e))


# Function to copy output to clipboard
def copy_to_clipboard():
    try:
        output_field = get_output_field()
        text_to_copy = output_field.get(
            "1.0", "end-1c"
        )  # Use "end-1c" to avoid extra newline
        copy(text_to_copy)
        # Show success using CustomTkinter dialog
        CTkSuccessDialog("Success", "Copied to clipboard!")
    except Exception as e:
        # Show error using CustomTkinter dialog
        CTkErrorDialog("Error", str(e))


# Detection and conversion logic with delays
def detections_and_convert(main_window, last_input):
    try:
        current_input = get_input_field().get("1.0", "end-1c")  # Use "end-1c"

        if current_input != last_input[0]:
            # Run conversion directly in main thread instead of background thread
            convert_and_display()
            last_input[0] = current_input

        main_window.after(1000, detections_and_convert, main_window, last_input)
    except Exception as e:
        print(f"Error in detection: {e}")


def main():
    print("Initializing the main window...")

    # Set appearance mode and color theme for customtkinter
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme(
        "blue"
    )  # Themes: "blue" (default), "green", "dark-blue"

    try:
        # Initialize the window and UI components
        main_window, input_field, output_field, copy_button = create_main_window()
        print("Window and UI components initialized.")

        # Set the command for the copy to clipboard button
        copy_button.configure(command=copy_to_clipboard)

        # Start the detection and conversion logic
        last_input = [input_field.get("1.0", "end-1c")]  # Use "end-1c"
        detections_and_convert(main_window, last_input)

        print("Starting the main loop...")
        # Start the main loop
        main_window.mainloop()

    except Exception as e:
        print(f"Error during initialization: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    print("Starting the markdown to indent converter...")
    main()
