def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        num = len(words)
    return num

def character_counter(path):
    with open(path) as f:
        letter_dict = {}
        file_contents = f.read()
        words = file_contents.lower()
        for l in words:
            if l not in letter_dict:
                letter_dict[l] = 1
            else:
                letter_dict[l] += 1
    return letter_dict

def dict_list(dict):
    dlist = []
    for key, value in dict.items():
        temp_dict = {"char": key, "num": value}
        dlist.append(temp_dict)
    dlist.sort(reverse=True, key=sort_on)
    return dlist

def sort_on(dict):
    return dict["num"]

def print_report(num_words, num_chars, book_link):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")