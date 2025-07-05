#Chad Collard
#Chapter 9 & 10 Lab 2
#7/5/2025

def get_words_from_file(filename):
    try:
        with open(filename) as file:
            text = file.read()
            text = text.replace("\n", "")
            text = text.replace(",", "")
            text = text.replace(".", "")
            
            words = text.split(" ")
            words.sort()
            return words
    except FileNotFoundError:
        print(f"Error: The file \"{filename}\" was not found.")
        

def count_capital_letters(words):
    capital_count = 0
    if words:  
        for word in words:
            for char in word:
                if 'A' <= char <= 'Z':  
                    capital_count += 1
    return capital_count
    

    
def main():
    print("File Processor\n")
    filename = input("Enter the filename ")
    words = get_words_from_file(filename)
    print(f"Number of words = {len(words)}")
    total_capital_letters = count_capital_letters(words)
    print(f"Total number of capital letters: {total_capital_letters}")
    

if __name__ == "__main__":
    main()
