
import re
import markdown2

# Adjust this value based on how many spaces represent one indent level in your source
SPACES_PER_INDENT = 2


def get_leading_indent_level(line, spaces_per_indent=SPACES_PER_INDENT):
    leading_spaces = len(line) - len(line.lstrip(" "))
    indent_level = leading_spaces // spaces_per_indent
    return indent_level


def get_indent_level(line, last_header_indent):
    leading_indent = get_leading_indent_level(line)
    stripped_line = line.lstrip(" ")
    header_match = re.match(r"^(#+)\s", stripped_line)
    if header_match:
        header_level = len(header_match.group(1)) - 1  # Base 0 for single '#'
        return header_level + leading_indent
    list_match = re.match(r"^([\-\+])\s", stripped_line)
    if list_match:
        # For list items, use last_header_indent plus leading indent
        return last_header_indent + leading_indent + 1
    # Plain lines inherit last header indent plus leading indent
    return last_header_indent + leading_indent + 1


def convert_markdown_formatting(text):
    # Use markdown2 to convert markdown to HTML, then strip <p> tags for inline use
    html = markdown2.markdown(text)
    # Remove wrapping <p>...</p> if present
    if html.startswith('<p>') and html.endswith('</p>\n'):
        html = html[3:-5]
    elif html.startswith('<p>') and html.endswith('</p>'):
        html = html[3:-4]
    return html.strip()


def is_reset_marker(line):
    return re.match(r"^\[.*\]$", line.strip()) is not None


def process_line(last_header_indent, line):
    stripped_line = line.lstrip(" ")
    current_indent = get_indent_level(line, last_header_indent)

    if re.match(r"^#+\s", stripped_line):  # Header
        last_header_indent = current_indent
        line_content = stripped_line.lstrip("#").strip()
    elif re.match(r"^[-+]\s", stripped_line):  # List item
        line_content = stripped_line.lstrip("-+").strip()
    else:  # Plain line
        line_content = stripped_line

    # Use markdown2 for formatting
    formatted_line = convert_markdown_formatting(line_content)


    # Wrap in <html> tags if any HTML tag is present, ensuring single-line output
    if '<' in formatted_line and '>' in formatted_line:
        formatted_line = '<html>' + formatted_line.replace('\n', '').replace('\r', '') + '</html>'

    indented_line = "  " * current_indent + formatted_line + "\n"
    return indented_line, last_header_indent


def markdown_to_mindmap(text):
    last_header_indent = 0
    output = ""

    for line in text.split("\n"):
        if is_reset_marker(line):
            output += line.strip() + "\n"
            last_header_indent = 0
            continue

        indented_line, last_header_indent = process_line(last_header_indent, line)
        output += indented_line

    return output
