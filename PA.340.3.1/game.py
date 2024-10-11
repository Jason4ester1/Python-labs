def word_play_game():
    # Ask the user to enter a word
    word = input("Enter a word: ")

    # Print the length of the word
    print("Length of the word:", len(word))

    # Print the word in uppercase and lowercase
    print("Uppercase:", word.upper())
    print("Lowercase:", word.lower())

    # Ask the user to enter a letter and count its occurrences
    letter = input("Enter a letter to count its occurrences: ")
    print(f"The letter '{letter}' appears {word.count(letter)} times in the word.")

    # Ask the user to enter a substring and count its occurrences
    substring = input("Enter a substring to count its occurrences: ")
    print(f"The substring '{substring}' appears {word.count(substring)} times in the word.")

    # Reverse the word and print the result
    reversed_word = word[::-1]
    print("Reversed word:", reversed_word)

    # Ask the user to enter a starting and ending index, then slice the word
    start_index = int(input("Enter the starting index for slicing: "))
    end_index = int(input("Enter the ending index for slicing: "))
    sliced_word = word[start_index:end_index]
    print("Sliced word:", sliced_word)

    # Ask the user to enter a character to replace the first occurrence
    char_to_replace = input("Enter a character to replace: ")
    replacement_char = input("Enter the replacement character: ")
    replaced_word = word.replace(char_to_replace, replacement_char, 1)
    print("Word after replacement:", replaced_word)

    # Concatenate the original word with a second word entered by the user
    second_word = input("Enter a second word to concatenate: ")
    concatenated_word = word + second_word
    print("Concatenated word:", concatenated_word)

    # Check if the original word is a palindrome
    is_palindrome = word == reversed_word
    print(f"The word is a palindrome: {is_palindrome}")

    # Check if the original word is a valid Python identifier
    is_valid_identifier = word.isidentifier()
    print(f"The word is a valid Python identifier: {is_valid_identifier}")

# Run the game
word_play_game()