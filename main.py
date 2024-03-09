def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_amount = get_word_count_from_string(text)
    print_report(letter_count(text), book_path, word_amount)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count_from_string(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letterDictionary = {}
    text = text.lower()
    for letter in text:
        if letter in letterDictionary:
            letterDictionary[letter] += 1
        else:
            letterDictionary[letter] = 1
    
    return letterDictionary

def print_report(chars, book_path, word_amount):
    print(f"--- Begin report of {book_path}.txt ---")
    print(f"{word_amount} words found in the document")
    charList = convertDictToList(chars)
    charList.sort(reverse=True, key=sort_on)
    for i in range(len(charList)):
        if charList[i]["char"].isalpha():
            print(f"The '{charList[i]['char']}' character was found {charList[i]['amount']} times")
    print("--- End Report ---")

def convertDictToList(dict):
    list = []
    for key in dict:
        list.append({"char": key,"amount": dict[key]})
    return list

def sort_on(dict):
    return dict["amount"]

main()
