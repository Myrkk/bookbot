def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    counts = {}
    for c in book:
        if c.lower() in counts:
            counts[c.lower()] += 1
        else:
            counts[c.lower()] = 1
    return counts

def report(book,book_path):
    print(f"Analysing {book_path}\n")
    word = word_count(book)
    print(f"There are {word} words in this book.\n")
    letter = list(letter_count(book).items())
    letter.sort(key=lambda tup: tup[1],reverse=True)
    for item in letter:
        if item[0].isalpha():
            print(f"The letter {item[0]} appears in the book {item[1]} times.")

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        contents = f.read()
        #print(contents)
        #print(word_count(contents))
        report(contents,book_path)

main()
