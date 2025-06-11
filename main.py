import sys
def main(book_path):
    from stats import get_book_text
    count = get_book_text(book_path)
    #print(f"{count} words found in the document")
    from stats import character_counter
    char_stats = character_counter(book_path)
    #print(f"{char_stats}")
    from stats import dict_list
    new_list = dict_list(char_stats)
    from stats import print_report
    print_report(count, new_list, book_path)
#####################################################
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
main(book_path)