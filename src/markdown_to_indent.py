import re

def get_indent_level(line):
    header_match = re.match(r"^(#+)\s", line)
    if header_match:
        return len(header_match.group(1)) - 1
    list_match = re.match(r"^(\s*[-+])\s", line)
    if list_match:
        spaces = len(list_match.group(1)) - 1  # Subtract 1 for the '-' or '+'
        return spaces // 2
    return -1  # Return -1 for plain lines

def convert_bold_markers(text):
    return re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

def is_reset_marker(line):
    return re.match(r"^\[.*\]$", line.strip()) is not None

def process_line(current_indent, last_header_indent, last_plain_indent, line):
    line_indent = get_indent_level(line)
    if line_indent == -1:  # Plain line
        current_indent = last_header_indent + 1
        last_plain_indent = current_indent
    elif re.match(r"^#+\s", line):  # Header
        current_indent = line_indent
        last_header_indent = current_indent
    elif re.match(r"^\s*[-+]\s", line):  # List item
        current_indent = last_plain_indent + 1
        last_plain_indent = current_indent
    else:
        # For nested list items
        current_indent = last_plain_indent + (line_indent - last_plain_indent)
        last_plain_indent = current_indent

    if re.match(r"^\s*[-+]\s", line):
        line_content = line.lstrip(" -+").strip()
    else:
        line_content = line.lstrip("#").strip()

    # Check if the line contains bold markers
    if '**' in line_content:
        formatted_line = convert_bold_markers(line_content)
        # Wrap the formatted line with <html> tags
        formatted_line = "<html>" + formatted_line + "</html>"
    else:
        formatted_line = line_content

    indented_line = "  " * current_indent + formatted_line + "\n"
    return indented_line, current_indent, last_header_indent, last_plain_indent

def markdown_to_indent(text):
    current_indent = 0
    last_header_indent = 0
    last_plain_indent = 0

    output = ""

    for line in text.split("\n"):
        if is_reset_marker(line):
            output += line.strip() + "\n"
            current_indent = 0
            last_header_indent = 0
            last_plain_indent = 0
            continue

        indented_line, current_indent, last_header_indent, last_plain_indent = process_line(
            current_indent, last_header_indent, last_plain_indent, line
        )
        output += indented_line

    return output
