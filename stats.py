def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def calculate_words(text):
    words = text.split()
    return len(words)

def calculate_symbols(text):
    text = text.lower()
    dic = {}

    for charater in text:
        if charater in dic:
            dic[charater] = dic[charater] + 1
        else:
            dic[charater] = 1

    return dic

def sort_on(d):
    return d["num"]

def sort_dic_of_char(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list