
def size_book(filename):
    try:
        with open(filename, "r") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("ABC '" + filename + "' sdsdfsd: " + num_words)


filenames = "alice.txt"
for filename in filenames:
    size_book(filename)
