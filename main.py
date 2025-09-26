import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
bookpath = sys.argv[1]
def main():
    #bookpath = ""
    whole_text = get_book_text(bookpath)
    word_amount = get_num_words(whole_text)
    character_count = get_num_characters(whole_text)
    sorted_count = get_sorted(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_amount} total words")
    print("--------- Character Count -------")
    for sort in sorted_count:
        char = sort["char"]
        num = sort["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents



from stats import get_num_words, get_num_characters, get_sorted

main()