fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    list_of_words = line.split()
    for word in list_of_words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
