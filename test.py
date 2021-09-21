"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Read file into texts and calls.
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

normal_number = set()
suspicious_number = set()
for record in texts:
    normal_number.add(record[0])
    normal_number.add(record[1])

for record in calls:
    normal_number.add(record[1])

for number in calls:
    if (number[0] not in normal_number):
        suspicious_number.add(number[0].replace(' ', ''))

print(len(normal_number))

print(len(suspicious_number))
"""
print('These numbers could be telemarketers: ')
for number in sorted(suspicious_number):
    print(number)
"""
