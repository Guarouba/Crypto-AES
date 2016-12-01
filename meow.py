
with open("Source/dictionary/english.txt") as word_file:
    words = [i.strip("\n") for i in word_file.readlines()]

    print(words)
