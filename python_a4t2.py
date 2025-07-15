# Task 2 : Write and Append Data to a File

# Pre-existing location of output.txt
file_path = "C:\\python_exercises\\output.txt"

# Function to clear pre-existing file contents before inserting new content.
def clear_file_content():
    with open(file_path, "w") as file:
        pass
        print("Step 1: Pre-existing file contents have been cleared.")

# clear_file_content() function call, inserting new content and reading entire file content
# and handling File not found error

try:
    with open(file_path, "r+") as file:
        clear_file_content() # clears/removes pre-existing contents inside the file.
        print("Step 2: Inserting new content.")
        print("Step 3: New File contents have been created as below,")
        file.write("Hello, Python!")
        file.seek(0)
        reading = file.read()
        print(reading)
        print("Step 4: Appending new content with extra line.")
        file.write("\nLearning file handling in Python.") # File content is appended
        file.seek(0)
        reading = file.read()
        print(reading)
except FileNotFoundError: # Change the file name to output1.txt in file_path to throw this exception message.
    print("The file", file_path, "was not found")
