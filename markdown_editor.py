markdowns = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
commands = ["help", "!done"]
output_text = ""


def mark_plain():
    global output_text
    text = input("Text:")
    output_text += text
    return output_text


def mark_bold():
    global output_text
    text = input("Text:")
    bold_text = f"**{text}**"
    output_text += bold_text
    return output_text


def mark_italic():
    global output_text
    text = input("Text:")
    italic_text = f"*{text}*"
    output_text += italic_text
    return output_text


def mark_header():
    global output_text
    level = int(input("Level:"))
    while True:
        if level in range(1,7):
            text = input("Text:")
            header_text = "#" * level + " " + text + "\n"
            output_text += header_text
            return output_text
        else:
            print("The level should be within the range of 1 to 6")
            level = int(input("Level:"))


def mark_link():
    global output_text
    label = input("Label:")
    url = input("URL:")
    link_text = f"[{label}]({url})"
    output_text += link_text
    return output_text


def mark_inline():
    global output_text
    text = input("Text:")
    inline_text = f"`{text}`"
    output_text += inline_text
    return output_text


def mark_newline():
    global output_text
    newline_text = "\n"
    output_text += newline_text
    return output_text


def mark_ordered():
    global output_text
    num_list = []
    inputs_list = []
    rows = int(input("Number of rows:"))
    while True:
        if rows <= 0:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows:"))
        else:
            for i in range(rows):
                num_list.append(f"{i+1}. ")
                inputs_list.append(input(f"Row #{i + 1}:"))
            ordered_list = list(map(lambda x, y: x + y, num_list, inputs_list))
            output_text += "\n".join(ordered_list) + "\n"
            return output_text


def mark_unordered():
    global output_text
    stars = []
    inputs_list = []
    rows = int(input("Number of rows:"))
    while True:
        if rows <= 0:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows:"))
        else:
            for i in range(rows):
                stars.append("* ")
                inputs_list.append(input(f"Row #{i + 1}:"))
            unordered_list = list(map(lambda x, y: x + y, stars, inputs_list))
            output_text += "\n".join(unordered_list) + "\n"
            return output_text


def mark_choice(i):
    if choice == "plain":
        print(mark_plain())
    elif choice == "bold":
        print(mark_bold())
    elif choice == "italic":
        print(mark_italic())
    elif choice == "header":
        print(mark_header())
    elif choice == "link":
        print(mark_link())
    elif choice == "inline-code":
        print(mark_inline())
    elif choice == "new-line":
        print(mark_newline())
    elif choice == "ordered-list":
        print(mark_ordered())
    elif choice == "unordered-list":
        print(mark_unordered())


choice = input("Choose a formatter:")
while True:
    if choice in markdowns:
        mark_choice(choice)
        choice = input("Choose a formatter:")
    elif choice == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list")
        print("Special commands: !help !done")
        choice = input("Choose a formatter:")
    elif choice == "!done":
        result_file = open("output.md", "w")
        result_file.write(output_text)
        result_file.close()
        break
    else:
        if choice not in markdowns and commands:
            print("Unknown formatting type or command")
            choice = input("Choose a formatter:")


