def plain():
    global all_text
    text = input("Text: ")
    all_text += text
    print(all_text)


def bold():
    global all_text
    text = input("Text: ")
    all_text += "**" + text + "**"
    print(all_text)
    

def italic():
    global all_text
    text = input("Text: ")
    all_text += "*" + text + "*"
    print(all_text)


def header():
    global all_text
    level = input("Level:")
    
    while int(level) < 1 or int(level) > 6:
        print("The level should be within the range of 1 to 6")
        level = input("Level:")
    else:
        text = input("Text: ")
        all_text += "#" * int(level) + " " + text + "\n"
        print(all_text)
    
    
def link():
    global all_text
    label = input("Label:")
    url = input("URL: ")
    all_text += "[" + label +"](" + url +")"
    print(all_text)
   
   
def inline_code(): 
    global all_text
    text = input("Text: ")
    all_text += "`" + text + "`"
    print(all_text)
    

def add_list(list_type):
    global all_text
    rows_number = input("Number of rows: ")
    
    while int(rows_number) <= 0:
        print("The number of rows should be greater than zero")
        rows_number = input("Number of rows: ")
    else:
        for index in range(int(rows_number)):
            text=(input(f"Row #{index+1}:"))
            if list_type == "ordered":
                all_text += f"{index+1}. {text}\n"
            else:
                all_text += f"* {text}\n"
        print(all_text)
        
        
def new_line():
    global all_text
    all_text +="\n"
    print(all_text)
    

def done():
    global all_text
    output_file=open('output.md','w')

    output_file.write(all_text)
    output_file.close()
        
formatter = input("Choose a formatter: ")

valid_formatters = ["!help", "!done", "plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
 "unordered-list", "new-line"]

all_text = ""
while formatter != "!done":
    if formatter not in valid_formatters:
        print("Unknown formatting type or command")
    elif formatter == "!help":
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered lisr new-line
        Special commands: !help !done''')
    else:
        if formatter == "plain":
            plain()
        elif formatter == "bold":
            bold()
        elif formatter == "italic":
            italic()
        elif formatter == "header":
            header()
        elif formatter == "link":
            link()
        elif formatter == "inline-code":
            inline_code()
        elif formatter == "ordered-list":
            add_list("ordered")
        elif formatter == "unordered-list":
            add_list("unordered")
        elif formatter == "new-line":
            new_line()
        
            
    formatter = input("Choose a formatter: ")
done()
