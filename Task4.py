"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

tm = set()
nm = set()
for i in calls:
    nm.add(i[1])
for j in texts:
    nm.add(j[0])
    nm.add(j[1])


for k in calls:
    if (k[0] not in nm):
        tm.add(k[0])

tm = sorted(tm)
print("These numbers could be telemarketers: ")
for i in tm:
    print(i)


    
