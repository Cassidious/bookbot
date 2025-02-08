class Book():
    def __init__(self,title,author,text):
        self.title = title
        self.author = author
        self.text = text

    def print_text(self):
        print(self.text)

    def words(self):
        return self.text.split()
    
    def characters(self):
        char_list = []
        for char in self.text:
            char_list.append(char)
        return char_list
    
    def word_count(self):
        return len(self.text.split())
    
    def char_count(self):
        char_count = {}
        for char in self.text.lower():
            if char in char_count:
                char_count[char] += 1
            if char not in char_count:
                char_count[char] = 1
        return char_count


    
    def char_count_report(self):
        def sort_on(entry):
            return entry["count"]
        char_count_list = []

        print(f"--- Begin report of books - {self.title} --- ")
        print(f"{self.word_count()} words found in the document")
        for entry in self.char_count():
            char_count_list.append({"char": entry, "count": self.char_count()[entry]})
            char_count_list.sort(key=sort_on, reverse=True)
            
        for item in char_count_list:
            if item["char"].isalpha():
                print(f"The '{item["char"]}' character was found {item["count"]} times")

    
