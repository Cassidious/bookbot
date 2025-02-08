from book import *



def main():
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
    book = Book("Frankenstein", "Shelly", book_text)
    action=input("What would you like to do?: r=report, w=word count, t=text     ")
    if action == "r":
        book.char_count_report()
    if action == "w":
        print(f"The text has {book.word_count()} words")
    if action == "t":
        book.print_text()
    


    
main()

