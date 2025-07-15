# Task 1 : Read a file and handle errors

# Pre-existing location of sample.txt
file_path = "C:\\python_exercises\\sample.txt"

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
        file.write("This is a sample text file.\nIt contains multiple lines.")
        file.seek(0)
        reading = file.read()
        print(reading)
except FileNotFoundError: # Change the file name to sample1.txt in file_path to throw this exception message.
    print("The file", file_path, "was not found")