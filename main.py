def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict = get_char_dict(text)
    print(get_word_count(text))
    chars_sorted_list=chars_dict_to_sorted_list(dict)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_word_count(text):    
    words = text.split()
    return len(words)


def get_char_dict(text):
    lowered_text = text.lower()
    dict = {}
    for characters in lowered_text:
        if characters not in dict:
            dict[characters] = 1
        else:
            dict[characters] += 1
    return dict
    

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]




def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
main()