import customtkinter as ctk

# Constants
INPUT_DIMS = (120, 22)
OUTPUT_DIMS = (120, 22)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
LABEL_WIDTH = 80

# Store input and output fields to access across modules
__input_field = None
__output_field = None
__copy_button = None


def create_main_window():
    """Creates and returns the main window and the important UI components (input_field, output_field, copy_button)."""
    global __input_field, __output_field, __copy_button

    # Create main window
    main_window = ctk.CTk()
    main_window.title("Markdown to Indent Converter")
    main_window.geometry("800x600")

    # Set appearance
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    # Create main container with padding
    main_container = ctk.CTkFrame(main_window)
    main_container.pack(fill="both", expand=True, padx=20, pady=20)

    # Input Frame with Label
    input_frame = ctk.CTkFrame(main_container)
    input_frame.pack(fill="both", expand=True, padx=10, pady=(10, 5))

    input_label = ctk.CTkLabel(
        input_frame,
        text="Input:",
        font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
        width=LABEL_WIDTH,
        anchor="e",
    )
    input_label.pack(side="left", padx=(10, 5), pady=10)

    __input_field = ctk.CTkTextbox(
        input_frame,
        width=INPUT_DIMS[0],
        height=300,  # Fixed height instead of using rows
        wrap="word",
        font=ctk.CTkFont(family="Consolas", size=11),
    )
    __input_field.pack(side="left", fill="both", expand=True, padx=(5, 10), pady=10)

    # Output Frame with Label
    output_frame = ctk.CTkFrame(main_container)
    output_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))

    output_label = ctk.CTkLabel(
        output_frame,
        text="Output:",
        font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
        width=LABEL_WIDTH,
        anchor="e",
    )
    output_label.pack(side="left", padx=(10, 5), pady=10)

    __output_field = ctk.CTkTextbox(
        output_frame,
        width=OUTPUT_DIMS[0],
        height=300,  # Fixed height instead of using rows
        wrap="word",
        font=ctk.CTkFont(family="Consolas", size=11),
        state="disabled",
    )
    __output_field.pack(side="left", fill="both", expand=True, padx=(5, 10), pady=10)

    # Button Frame
    button_frame = ctk.CTkFrame(main_container, fg_color="transparent")
    button_frame.pack(fill="x", padx=10, pady=(0, 10))

    __copy_button = ctk.CTkButton(
        button_frame,
        text="Copy to Clipboard",
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
        corner_radius=8,
    )
    __copy_button.pack(side="right", padx=20, pady=10)

    return main_window, __input_field, __output_field, __copy_button


# Accessor Functions for input/output fields and copy button
def get_input_field():
    """Returns the input text field."""
    return __input_field


def get_output_field():
    """Returns the output text field."""
    return __output_field


def get_copy_button():
    """Returns the copy button."""
    return __copy_button
