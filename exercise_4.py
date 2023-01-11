from os import system


def convert():
    try:
        input_line = str(input("Enter a line to convert to secret code ↓\n"))
        input_word_list = input_line.split(" ")
        secret_line = str()
        secret_word_list = []
        for word in input_word_list:
            i = 0
            converted_word = ''
            while i < len(word):
                converted_word += word[len(word) - i - 1]
                i += 1
            else:
                secret_word_list.append(converted_word)
    except Exception as e:
        print(e)
    finally:
        secret_line = ' '.join(secret_word_list)
        print(f"ENCODED LINE -> {secret_line}")
        # print(f"DECODED LINE -> {input_line}")


while True:
    convert()
    choice = str(input("Do you want to convert another line?? [y/n] : "))
    system('clear')
    if choice.lower() != 'y':
        break
