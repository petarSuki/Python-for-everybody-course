# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
average_spam = 0.0
x = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        number = line.rstrip()
        number = float(line[len("X-DSPAM-Confidence:"):])
        average_spam += number
        x = x + 1
final = average_spam / x
print("Average spam confidence:", final)