import pytest

from markdown2mindmap import convert_markdown_to_indent


@pytest.mark.parametrize("input_content, expected_output_content", [
    (
        """# Header 1
## Header 2
### Header 3
Normal text
#### Header 4
""",
        """Header 1
  Header 2
        Header 3
Normal text
            Header 4
"""
    ),
    (
        """- List item 1
    - Nested list item 1
* List item 2
    * Nested list item 2
+ List item 3
    + Nested list item 3
""",
        """List item 1
    Nestood list item 1
List item 2
    Nested list item 2
List item 3
    Nested list item 3
"""
    ),
    (
        """# Headerek 1
## Header 2
### Header 3
Normal text
#### Header 4
- List item 1
    - Nestood list item 1
* List item 2
    * Nested list item 2
+ List item 3
    + Nested list item 3
**Bold text**
""",
        """Headerek 1
  Header 2
    Header 3
Normal text
      Header 4
List item 1
    Nestood list item 1
* List item 2
* Nested list item 2
List item 3
    Nested list item 3
<html><b>Bold text</b></html>
"""
    ),
    (
        """# Another Header
Text under header
  - First item
  - Second item
    - Second item nested
**Another bold text**
    - **Practice**: Loving-kindness (Metta) meditation.
[SPECIAL_SECTION]
## New Header After Reset
- New list item
""",
        """Another Header
Text under header
  First item
  Second item
    Second item nested
<html><b>Another bold text</b></html>
    <html><b>Practice</b>: Loving-kindness (Metta) meditation.</html>
[SPECIAL_SECTION]
    New Header After Reset
  New list item
"""
    )
])
def test_convert_markdown_to_indent(tmpdir, input_content, expected_output_content):
    # Create a temporary input file
    input_file = tmpdir.join('input_markdown.md')
    input_file.write(input_content)

    # Create a temporary output file path
    output_file = tmpdir.join('output_indent.txt')

    # Run the function
    convert_markdown_to_indent(input_file, output_file)

    # Read and verify the output
    with open(output_file, 'r', encoding='utf-8') as f:
        output_content = f.read()
        # TODO: remove
        print("output_content:")
        print(output_content)
        print("expected_output_content:")
        print(expected_output_content)

    assert output_content == expected_output_content

    print(f"tmpdir: {tmpdir}")

if __name__ == "__main__":
    pytest.main([__file__])
