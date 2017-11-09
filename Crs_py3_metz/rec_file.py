filename = "programming_text.txt"

"""
with open(filename, "w") as file_object:
    file_object.write("I love programming.")
"""

with open(filename, "a") as file_object:
    file_object.write("\nI also love finding meaning in large datdsets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    file_object.write("I love game.\n")
