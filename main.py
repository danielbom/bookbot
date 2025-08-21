import sys

from stats import get_book_text, words_count, chars_count, sort_counter


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = words_count(content)
    counter = chars_count(content)
    counter_sorted = sort_counter(counter)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch, count in counter_sorted:
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")


main()

