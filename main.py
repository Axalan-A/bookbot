#!/usr/bin/env python3
from stats import count_words, count_characters, sort_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        print("======= BOOKBOT =======")
        print("Analyzing book found at books/frankenstein.txt")
        print("------- Word Count -------")
        count_words(text)
        print("------- Character Count -------")
        count_dictionary = count_characters(text)
        sort_counts(count_dictionary)

main()
