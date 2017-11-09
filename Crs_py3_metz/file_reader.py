"""
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
"""
with open("TZ\\text_py.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
"""
text_file = "TZ/text_py.txt"
with open(text_file) as file_object:
    lines = file_object.read()
    for line in lines:
        print(line.rstrip().title())
"""

filename = "pi_digits.txt"

"""
with open(filename) as file_object:
    lines = file_object.readlines()

    py_string = ""
    for line in lines:
        py_string += line.rstrip()

    print(py_string)
    print(len(py_string))

# >>>
# 3.1415926535  8979323846  2643383279
# 36
"""

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ""
    for line in lines:
        pi_string += line.strip()

    print(pi_string)
    print(len(pi_string))

# >>>
# 3.141592653589793238462643383279
# 32
