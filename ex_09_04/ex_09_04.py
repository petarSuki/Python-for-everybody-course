name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        words = words[1]
        dictionary[words] = dictionary.get(words, 0) + 1
        
most_word = None
most_count = None
for word, count in dictionary.items():
    if most_count is None or count > most_count:
        most_word = word
        most_count = count

print(most_word, most_count)