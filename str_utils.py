def tokenize(text):
    return text.split()


if __name__ == "__main__": # to only run if I am running the script, but not when I am importing.
    print(tokenize("Hello world!"))