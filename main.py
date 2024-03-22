import os

# Directory containing the Python files
directory = "."

# List all files in the directory
files = os.listdir(directory)

# Filter out only Python files (assuming files end with ".py")
python_files = [file for file in files if file.endswith(".py") and file.startswith('d') ]

# Execute each Python file
for file in python_files:
    file_path = os.path.join(directory, file)
    exec(open(file_path).read())
