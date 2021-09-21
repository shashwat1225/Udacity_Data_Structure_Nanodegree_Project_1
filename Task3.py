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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""---------------------------------------------------PART-A---------------------------------------------------"""

bcalls = []

for i in calls: #O(n)
    if i[0][:5] == '(080)':
        bcalls.append(i)  #O(1)

dials = set()
for j in bcalls:  #O(n)
    if j[1][:1] == '(':  #O(1)
        dials.add(j[1][j[1].find("(")+1:j[1].find(")")]) #O(1)
    else:
        dials.add(j[1][:4])

dials = sorted(dials) #O(n log n)
print("The numbers called by people in Bangalore have codes:",)
for i in dials:
    print(i)

"""---------------------------------------------------PART-B---------------------------------------------------"""

brcalls = []
for i in bcalls:
    if i[1][:5] == '(080)':
        brcalls.append(i)

print(round((len(brcalls)/len(bcalls))*100, 2), " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


