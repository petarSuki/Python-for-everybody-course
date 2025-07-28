name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
many = dict()
for line in handle:
    if line.startswith("From "):
        line.find(":")
        words = line.split()
        time = words[5]
        hour = time.split(":")
        many[hour[0]] = many.get(hour[0], 0) + 1
for key, value in sorted(many.items()):
    print(key, value)