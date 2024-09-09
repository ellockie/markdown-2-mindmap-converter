from markdown_to_indent.markdown_to_indent import (
    markdown_to_indent,
)

input_file = "_input_markdown.md"
output_file = "_output_indent.txt"


def read_file_to_string(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_string_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def convert_markdown_to_indent(input_file, output_file):
    text = read_file_to_string(input_file)
    indented_text = markdown_to_indent(text)  # Reusing the existing function
    write_string_to_file(output_file, indented_text)


if __name__ == "__main__":
    convert_markdown_to_indent(input_file, output_file)
