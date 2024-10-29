def count_words(text):
    words = text.split()
    return len(words)


def main():
    print("Welcome to the Word Counter Program!")
    print("Please enter a sentence or paragraph to count its words.")

    user_input = input("\nEnter text: ").strip()

    if not user_input:
        print("Error: No text entered. Please provide some text.")
    else:
        word_count = count_words(user_input)
        print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
