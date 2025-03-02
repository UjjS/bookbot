from stats import *
import sys
def get_book_text(filepath:str)->str:
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    num_words = get_num_words(content)
    char_freq = freq_of_char(content)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_word_list(char_freq):
        print(f"{key}: {value}")
    

if __name__ == "__main__":
    main()
    

