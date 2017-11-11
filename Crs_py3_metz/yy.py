def size_book(filename):
    try:
        with open(filename,"r") as f_obj:
            contents = f_obj.read()
            words = contents.split()
    except FileNotFoundError:
        print("\n<<<Book not found " + filename + ">>>\n")
    else:
        print("Кол-во слов в книге: " + filename)
        print(len(words))
        print("\nВстречающееся слово 'World' в книге:")
        print(contents.count("World"))
        print("\nВстречающееся слово 'Alice' в книге:")
        print(contents.count("Alice"))

filenames = ["alice.txt", "us.txt", "moby-dick.txt"]
for filename in filenames:
    size_book(filename)
