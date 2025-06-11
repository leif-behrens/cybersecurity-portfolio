import os 

def get_template(path: str="base_template.md") -> str:
    # Get the content of the base template
    with open(path) as f:
        template: str = f.read()
    return template

def get_values() -> dict:
    # Get the user inputs for the creation of the documentation
    challenge_name: str = input("Enter the challenge name:\n")
    completion_date: str = input("Completion date of the challenge (YYYY-MM-DD):\n")
    category: str = input("Enter a category (or multiple, separated by a semicolon):\n")
    difficulty: int = input("Choose between 'Unknown', 'Easy', 'Medium' and 'Hard':\n")
    reference: str = input("Enter the hyperlink of the THM-room:\n")
    tasks: str = input("Enter the name of the different tasks (separated by a semicolon):\n")
    
    # save the values in a dict and reference it with the placeholders of the base template
    values: dict = {"!challenge_name!": challenge_name,
                    "!completion_date!": completion_date,
                    "!category!": [c.strip() for c in category.split(";")],
                    "!difficulty!": difficulty,
                    "!reference!": reference,
                    "!tasks!": [t.strip() for t in tasks.split(";")]}
    return values


def process_values(template: str, values: dict) -> str:
    # iterate through the user inputs and replace the placeholders with the actual values
    for placeholder, value in values.items():
        if placeholder == "!category!":
            if len(value) > 1:
                template = template.replace(placeholder, f"**Categories**: {" | ".join(value)}<br>")
            else:
                template = template.replace(placeholder, f"**Category**: {value[0]}<br>")

        elif placeholder == "!difficulty!":
            options: list = ["Unknown", "Easy", "Medium", "Hard"]
            output_str: str = ""
            for option in options:
                if value == option:
                    output_str += f"| {option} "
                else:
                    output_str += f"| ~~{option}~~ "
            template = template.replace(placeholder, output_str[2:])
        
        elif placeholder == "!tasks!":
            task_block: str = ""
            for task in value:
                task_block += f"### {task.strip()}\n####Question\n\n#### Approach\n\n####Answer\n\n"
            template = template.replace(placeholder, task_block)
            
        else:
            template = template.replace(placeholder, value)
        
    
    return template


def choose_target_directory() -> str:
    current_dir: str = os.path.abspath(os.path.dirname(__file__))
    # Two layers above should be the base directory
    base_dir: str = os.path.abspath(os.path.join(current_dir, "..", ".."))
    print(f"\nBase Directory: {base_dir}")

    # Directories that should be ignored
    exclude_dirs: dict = {".git", ".venv", "__pycache__", ".idea", ".vscode", "node_modules"}

    available_dirs: list = []
    for root, dirs, _ in os.walk(base_dir):
        # Filter out unwanted directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for d in dirs:
            full_path: str = os.path.join(root, d)
            relative_path: str = os.path.relpath(full_path, base_dir)
            available_dirs.append(relative_path)

    if not available_dirs:
        print("No subdirectories found.")
        exit(1)

    print("\nAvailable directories:")
    # List all available directories to choose from
    for i, dir_path in enumerate(available_dirs):
        print(f"{i+1}. {dir_path}")

    while True:
        try:
            choice: int = int(input("\nSelect a target directory by number:\n"))
            if 1 <= choice <= len(available_dirs):
                return os.path.join(base_dir, available_dirs[choice - 1])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")


def create_documentation(template: str) -> None:
    file_name: str = input("Enter the file name for the documentation (with file extension):\n")
    target_dir: str = choose_target_directory()

    # Create all dirs 
    os.makedirs(target_dir, exist_ok=True)

    # Create a directory for screenshots
    screenshot_dir: str = os.path.join(target_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    file_path: str = os.path.join(target_dir, file_name)

    with open(file_path, "w") as f:
        f.write(template)

    print(f"\nDocumentation created: {file_path}")
    print(f"Screenshot folder created: {screenshot_dir}")

                
if __name__ == '__main__':
    values: dict = get_values()
    raw_template: str = get_template()
    processed_template: str = process_values(raw_template, values)
    create_documentation(processed_template)
