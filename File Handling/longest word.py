def longest_word(filename):
    with open(filename, 'r') as file:
              words = file.read().split()
    print(max(words, key=len))
    return

longest_word('newfile.txt')