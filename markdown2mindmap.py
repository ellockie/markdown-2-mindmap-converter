import re

input_file = '_input_markdown.md'
output_file = '_output_indent.txt'

def convert_markdown_to_indent(input_file, output_file):
    def get_indent_level(line):
        header_match = re.match(r'^(#+)\s', line)
        if header_match:
            return len(header_match.group(1)) - 1
        list_match = re.match(r'^(\s*[\-\+])\s', line)
        if list_match:
            return len(list_match.group(1)) // 2
        return -1  # Return -1 for plain lines

    def convert_bold_markers(text):
        return re.sub(r'^(.*?)\*\*(.*?)\*\*(.*)$', r'<html>\1<b>\2</b>\3</html>', text)

    def is_reset_marker(line):
        return re.match(r'^\[.*\]$', line.strip()) is not None

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        current_indent = 0
        last_header_indent = 0
        last_plain_indent = 0

        for line in infile:
            if is_reset_marker(line):
                outfile.write(line.strip() + '\n')
                current_indent = 0
                last_header_indent = 0
                last_plain_indent = 0
                continue

            line_indent = get_indent_level(line)

            if line_indent == -1:  # Plain line
                current_indent = last_header_indent + 1
                last_plain_indent = current_indent
            elif re.match(r'^#+\s', line):  # Header
                current_indent = line_indent
                last_header_indent = current_indent
            elif re.match(r'^\s*[-+]\s', line):  # List item
                current_indent = last_plain_indent + 1

            if re.match(r'^\s*[-+]\s', line):
                line_content = line.lstrip(' -+').strip()
            else:
                line_content = line.lstrip('#').strip()

            formatted_line = convert_bold_markers(line_content)
            indented_line = '  ' * current_indent + formatted_line + '\n'
            outfile.write(indented_line)

if __name__ == "__main__":
    convert_markdown_to_indent(input_file, output_file)
