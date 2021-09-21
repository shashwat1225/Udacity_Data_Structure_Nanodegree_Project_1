"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_dict = {}
longest_duration = 0
for i in range(len(calls)):
    phone_dict[calls[i][0]] = phone_dict.get(calls[i][0], 0) + int(calls[i][-1])
    phone_dict[calls[i][1]] = phone_dict.get(calls[i][1], 0) + int(calls[i][-1])
    if phone_dict[calls[i][0]] > longest_duration:
        longest_caller = calls[i][0]
        longest_duration = phone_dict[calls[i][0]]
    if phone_dict[calls[i][1]] > longest_duration:
        longest_caller = calls[i][1]
        longest_duration = phone_dict[calls[i][1]]
print(longest_caller, " spent the longest time,", longest_duration, " seconds, on the phone during September 2016.")

