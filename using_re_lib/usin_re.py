import re

file = input("Enter file:")
if len(file) < 1:
    file = "regex_sum_2182073.txt"
handle = open(file)
sumarum = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        sumarum += int(number)
print(sumarum)