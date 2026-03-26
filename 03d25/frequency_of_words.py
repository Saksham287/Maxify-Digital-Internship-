# Count the frequency of each word


txt = "Python is easy and python is powerful and easy to learn"
print(txt)
txt = txt.lower()
print(txt)
words = txt.split()
print(words)

unique_words = set(words)
print("Unique Words:", unique_words)

def word_count(word_list):
    freq = {}
    
    for words in word_list:
        if words in freq:
            freq[words] += 1
        else:
            freq[words] = 1
    return freq

frequency = word_count(words)
print("Frequency of Words:", frequency)

most_freq = ""
highest = 0

for x in frequency:
    if frequency[x] > highest:
        highest = frequency[x]
        most_freq = x
        
print(f"Most Frequent Word: {most_freq}  = {highest}")

'''
Entire Output: 

Python is easy and python is powerful and easy to learn
python is easy and python is powerful and easy to learn
['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and', 'easy', 'to', 'learn']
Unique Words: {'python', 'is', 'easy', 'to', 'powerful', 'learn', 'and'}
Frequency of Words: {'python': 2, 'is': 2, 'easy': 2, 'and': 2, 'powerful': 1, 'to': 1, 'learn': 1}
Most Frequent Word: python  = 2
'''
