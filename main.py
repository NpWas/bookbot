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

def char_dict_list(char_dict):
    list_of_dicts = []
    
    for key in char_dict:
        if key.isalpha():
            value = char_dict[key]
            list_of_dicts.append({key : value})
      
    return list_of_dicts

def get_sort_key(list_of_dicts):
    

    for item in list_of_dicts:
        value = list_of_dicts[item]
        return value

def main():
    wordcount = count_words(frankenstein)
    
    print(f"--- Begin report of {book} ---")
    print(f"There are {wordcount} words in the document")
    
    

    list_of_dicts = (char_dict_list(count_characters(frankenstein)))

    list_of_dicts.sort(reverse=True, key=get_sort_key)

    for dictionary in list_of_dicts:
        for key in dictionary:
            value = dictionary[key]
            print(f"The '{key}' character was found {value} times")
    
    print("--- End Report ---")
        
        
if __name__ == "__main__":
    main()                                

 