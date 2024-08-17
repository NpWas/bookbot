book = 'books/frankenstein.txt'

with open(book) as f:
        frankenstein = f.read()
    
       
    


def count_words(file_contents):
    wordcount = len(file_contents.split())
        
    return wordcount



def count_characters(file_contents):
    character_list = list(file_contents.lower())
    
    char_counter = 0

    char_dict = {}

    for char in character_list:
        char_counter += 1
        char_dict[char] = char_counter

    return char_dict


def main():
    
     
  

    print(f"There are {count_words(frankenstein)} in frankenstein")
    print(count_characters(frankenstein))

if __name__ == "__main__":
    main()                                

 