def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    create_report(book_path, num_words, text)
    
   

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    letters_dic = {}
    counter = 0 
    for letter in text:
        lower_case = letter.lower()
        if lower_case in letters_dic:
            letters_dic[lower_case] += 1
        else:
            letters_dic[lower_case] = 1
    return letters_dic


def create_report(book_path, num_words, text):
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    letters_list = list(get_num_letters(text).items())
    letters_list.sort()
    
    for item in letters_list:
        if item[0].isalpha():
            print (f"The {item[0]} character was found {item[1]} times")
    
    print ("--- End report ---")
           
main()