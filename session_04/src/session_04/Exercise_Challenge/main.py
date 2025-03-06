def process_lines(lines): # Generator that processes lines of strings (list)
    for line_number, line in enumerate(lines, start=1):
        stripped_line = line.strip()  # Strips whitespace from the line
        stripped_line = stripped_line.replace("\n", " ")  # Removes internal line breaks by replacing \n with a space
        if stripped_line:  # Filters out empty lines
            yield line_number, stripped_line


# Simulated text file with a list of strings, provided by ChatGPT
simulated_text_file = [
    "  This is the first line.  ",
    "  This is the second line.  ",
    "  ",
    "    Another line here.   ",
    "   ",
    "\n",
    "  Hello\nWorld  ",
    "  This is a line with\nline breaks  ",
    "   Another clean line  ",
    "  \nEmpty line here\n",
    "  Final line. "
]

if __name__ == "__main__":
    print("Processing lines from the simulated file:")
    for line_number, line in process_lines(simulated_text_file):
        print(f"Line {line_number}: {line}")

# Output
"""
    Processing lines from the simulated file:
    Line 1: This is the first line.
    Line 2: This is the second line.
    Line 4: Another line here.
    Line 7: Hello World
    Line 8: This is a line with line breaks
    Line 9: Another clean line
    Line 10: Empty line here
    Line 11: Final line.
"""