"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
"""

filename = "alice.txt"

try:
    with open(filename, "r") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file '" + filename + "' does not exist."
    print(msg)
else:
    size_string = contents.split()
    #print(size_string)
    print(len(size_string))

