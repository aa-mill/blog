import re
import argparse

def replace_commands(text, commands):

    def find_matching_brace(s, start):
        # start is index of opening brace
        stack = 1
        # start searching after opening brace
        i = start + 1
        while i < len(s):
            if s[i] == '{':
                stack += 1
            elif s[i] == '}':
                stack -= 1
                if stack == 0:
                    # return index of closing brace
                    return i
            i += 1
        raise ValueError('No matching closing brace found.')

    def replace_command(s, pattern, format):
        """
        Generic function to replace LaTeX commands like \braket{}, \ket{}, \bra{} with their expansions
        Args:
            s: input string
            pattern: regex pattern to match (e.g. r'\\braket{')
            format: tuple of (prefix, suffix) for the replacement
        """
        result = ''
        i = 0
        while i < len(s):
            match = re.search(pattern, s[i:])
            if not match:
                result += s[i:]
                break
            start = i + match.start()
            end = i + match.end()
            result += s[i:start]
            try:
                closing = find_matching_brace(s, end - 1)
                inner = replace_command(s[end:closing], pattern, format) # handle nested
                prefix, suffix = format
                replacement = prefix + inner + suffix
                result += replacement
                i = closing + 1
            except ValueError:
                # if no matching brace, leave as is
                result += s[start:end]
                i = end
        return result

    # apply each replacement in sequence
    result = text
    for pattern, format in commands:
        result = replace_command(result, pattern, format)
    return result

def escape_underscores(text):
    return text.replace('_', r'\_')

def replace_backslashes(text):
    return text.replace('\\\\', '\\\\\\\\')

def escape_math_symbols(text):
    """
    Escape asterisks and pipes that appear within math environments ($ $ or $$ $$)
    """
    result = ''
    in_math = False
    in_display_math = False
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i:i+2] == '$$':
            # toggle display math mode
            in_display_math = not in_display_math
            result += text[i:i+2]
            i += 2
        elif text[i] == '$' and not in_display_math:
            # toggle inline math mode
            in_math = not in_math
            result += text[i]
            i += 1
        elif (in_math or in_display_math) and text[i] in '*|':
            # escape asterisk or pipe in math mode
            result += '\\' + text[i]
            i += 1
        else:
            result += text[i]
            i += 1
    return result

def process_markdown(content):
    # define patterns and their replacements
    commands = [
        # standard commands
        (r'\\braket{', (r'\langle ', r' \rangle')),
        (r'\\ket{', (r'| ', r' \rangle')),
        (r'\\bra{', (r'\langle ', r' |')),
        # capitalized commands with \left and \right
        (r'\\Braket{', (r'\left\langle ', r' \right\rangle')),
        (r'\\Ket{', (r'\left| ', r' \right\rangle')),
        (r'\\Bra{', (r'\left\langle ', r' \right|'))
    ]
    # replace LaTeX commands
    content = replace_commands(content, commands)
    # escape asterisks and pipes in math mode
    content = escape_math_symbols(content)
    # escape underscores
    content = escape_underscores(content)
    # replace double backslashes
    content = replace_backslashes(content)
    return content

def main():
    # get input and output locations
    parser = argparse.ArgumentParser(description='Format .md file to be compatible with MathJax')
    parser.add_argument('input', help='Path to the input .md file')
    parser.add_argument('output', help='Path to the output formatted .md file')
    args = parser.parse_args()

    # read input file
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
    # process markdown
    formatted_content = process_markdown(content)
    # write to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    # print confirmation
    print(f'Formatted content written to {args.output}')

if __name__ == "__main__":
    main()