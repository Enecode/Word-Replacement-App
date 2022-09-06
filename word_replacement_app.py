def  replace_word():
    str = "Hello, my name is Jacob and I love coding"
    word_replacement = input("Enter the replacement: ")
    word_to_replace = input("Enter the word you want to replace: ")
    print(str.replace(word_to_replace, word_replacement))


replace_word()
