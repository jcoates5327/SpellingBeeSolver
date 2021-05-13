def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()

def write_to_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))

def length_sort(e):
    return len(e)

word_list_master = 'twl06.txt'
letters_given = ['i', 'o', 'c', 'v', 't', 'l', 'r']
letter_required = 'i'
min_length = 4

valid_words = []
all_words = read_file(word_list_master)

for word in all_words:
    # remove trailing whitespace
    word = word.strip()
    # check for required letter and length
    if letter_required not in word or len(word) < min_length:
        continue
    # split word into char array
    letters = list(word)
    # remove duplicates
    letters = list(dict.fromkeys(letters))

    is_valid = True
    for letter in letters:
        if letter not in letters_given:
            is_valid = False
            break
    if is_valid:
        valid_words.append(word)

valid_words.sort(reverse=True, key=length_sort)
write_to_file('valid_words.txt', valid_words)
