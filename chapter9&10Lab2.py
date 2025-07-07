#Chad Collard
#Chapter 9 & 10 Lab 2
#7/5/2025

def main():
    print("Word and Capital Letter Counter\n")

    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        words = content.split()
        total_words = len(words)

        total_capital_letters = 0
        for char in content:
            if 'A' <= char <= 'Z':
                total_capital_letters += 1

        print(f"Total number of words: {total_words}")
        print(f"Total number of capital letters: {total_capital_letters}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    main()
