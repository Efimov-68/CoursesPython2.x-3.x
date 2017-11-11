def count_words(filename):
    try:
        with open(filename, "r") as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file '" + filename + "' does not exist.")
        # "pass" просто оставит исключение без вывода сообщения
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '" + filename + "' has about " + str(num_words) \
              + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby-dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
