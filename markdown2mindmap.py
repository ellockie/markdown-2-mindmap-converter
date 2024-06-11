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
            indent_len = int(len(list_match.group(1)) / 2.0)
            # print(f"\nline: {line}")
            # print(f"indent_len: {indent_len}")
            return indent_len
        return 0

    def convert_bold_markers(text):
        return re.sub(r'^(.*?)\*\*(.*?)\*\*(.*)$', r'<html>\1<b>\2</b>\3</html>', text)

    def is_reset_marker(line):
        return re.match(r'^\[.*\]$', line.strip()) is not None

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        next_indent_level = 0
        for line in infile:
            if is_reset_marker(line):
                # Write the reset marker with no indentation
                outfile.write(line.strip() + '\n')
                next_indent_level = 1  # Reset the next indentation level to 1
                continue

            indent_level = get_indent_level(line) + next_indent_level
            if re.match(r'^\s*[-+]\s', line):
                line_content = line.lstrip(' -+').strip()
            else:
                line_content = line.lstrip('#').strip()

            formatted_line = convert_bold_markers(line_content)
            indented_line = '  ' * indent_level + formatted_line + '\n'
            outfile.write(indented_line)

if __name__ == "__main__":
    convert_markdown_to_indent(input_file, output_file)
