numBlocks = int(input('Сколько блоков вам нужно? '))
numLines = int(input('Сколько строк для звезд вам нужно? ')) 
numStars = int(input('Сколько звезд вам нужно? '))
for block in range(1, numBlocks + 1):
    for line in range(1, numLines + 1):
        for star in range(1, numStars + 1):
            print("*")
        print()
