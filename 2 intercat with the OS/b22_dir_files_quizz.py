"""
The create_python_script function creates a new 
python script in the current working directory,
 adds the line of comments to it declared by the 
 'comments' variable, and returns the size of the new file. 
 Fill in the gaps to create a script called "program.py".
"""
import os
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.py"))

"""
The new_directory function creates a new directory 
inside the current working directory, 
then creates a new empty file inside the new directory, 
and returns the list of files in that directory. 
Complete the function to create a file "script.py" 
in the directory "PythonPrograms".
"""
import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    print(os.getcwd())
    if not os.path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    print(os.getcwd())

    # Create the new file inside of the new directory
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    files = os.listdir(os.getcwd())
    print(files)

    os.chdir("..")

    files = os.listdir(directory)
    print(os.getcwd())
    print(files)

    return files

new_directory("PythonPrograms", "script.py")