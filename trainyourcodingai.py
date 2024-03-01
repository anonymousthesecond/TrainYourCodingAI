import random

# List of common programming keywords and instructions
keywords = [
    "print", "if", "else", "for", "while", "function", "class", "return", "import", 
    "from", "def", "try", "except", "raise", "break", "continue", "pass", "assert"
]

# List of common programming operations and symbols
operations = [
    "=", "==", "!=", "+", "-", "*", "/", "%", "<", ">", "<=", ">=", "and", "or", "not"
]

# Generate random commands
def generate_command():
    command = random.choice(keywords)
    if command in ["if", "else", "for", "while", "def", "class"]:
        command += " condition:"
    elif command in ["print", "return", "raise", "break", "continue"]:
        command += " "
        command += random.choice(["'Hello, world!'", "x", "1", "True", "False", "None"])
    elif command in ["import", "from"]:
        command += " module"
    elif command == "assert":
        command += " condition, message"
    else:
        command += " variable"
        command += random.choice(operations)
        command += " value"
    return command

# Generate billions of commands
def generate_commands(num_commands):
    with open("commands.txt", "w") as file:
        for _ in range(num_commands):
            command = generate_command()
            file.write(command + "\n")

# Generate 1 billion commands
generate_commands(1000000000)
