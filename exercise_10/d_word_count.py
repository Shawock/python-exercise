def word_count(file_path):
    """ calculate a file's word count """
    try:
        with open(file_path) as file_obj:
            content = file_obj.read()
    except FileNotFoundError:
        # pass
        print(file_path + " doesn't exist.")
    else:
        print(file_path + " contains " + str(text_word_count(content)) + " words.")


def text_word_count(text):
    """ calculate a text's word count """
    result = text.split()
    return len(result)


files = ['/tmp/append.txt', '/tmp/write.txt', '/tmp/read.txt']

for file in files:
    word_count(file)
