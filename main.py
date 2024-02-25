def main():
    book_path = "books/frankenstein.txt"
    text = get_txt(book_path)
    word_counter = get_words(text)
    letter_counter = letter_count(text)
    letter_counter.sort(reverse=True, key=sort_on)
    print(f"--- begin report of {book_path} ---")
    print(f"{word_counter} words found in the document")
    for e in letter_counter:
        print(f"The {e['letter']} character was found {e['number']} times")



def get_txt(path):
    with open(path) as f:
        return f.read() 
    
def get_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def letter_count(text):
    smoll_text = text.lower()
    letter_dict = {}
    letter_list_dict = []
    for letter in smoll_text:
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    for letters, number in letter_dict.items():
        letter_number_dict = {"letter": letters, "number": number}
        letter_list_dict.append(letter_number_dict)
    return letter_list_dict  

def sort_on(letter_list_dict):
    return letter_list_dict["number"]   



main()
