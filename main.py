

def count_words(file_contents):
    wordcount = len(file_contents.split())
        
    return wordcount

def main():  
    book = 'books/frankenstein.txt'
    
       
    
    with open(book) as f:
        frankenstein = f.read()

    print(f"There are {count_words(frankenstein)} in frankenstein")

if __name__ == "__main__":
    main()                                

 