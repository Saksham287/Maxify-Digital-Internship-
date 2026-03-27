# Read a text file and count words

with open("wordfile.txt", "r") as file:
    text = file.read()

words = text.split()

word_count = len(words)

print(word_count)

with open("output_word_count.txt", "w") as output:
    output.write(f"Number of words in document is {word_count}")
    
with open("output_word_count.txt", "r") as output:
    print(output.read())