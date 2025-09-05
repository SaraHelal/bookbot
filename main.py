from stats import get_num_words, get_chars_from_word

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    count_chars = get_chars_from_word(text)
    print("============= END ===============")
    #print(count_chars)
def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

main()