import sys
from stats import get_book_text, calculate_words,calculate_symbols,sort_on, sort_dic_of_char

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = calculate_words(text)
    num_characters = calculate_symbols(text)
    sorted_num_of_char = sort_dic_of_char(num_characters)

    print_report(book_path, num_words, sorted_num_of_char)


def print_report(book_path, num_words, sorted_num_of_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_num_of_char:
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()