# testing demo stuff can go here!




# lists and loops
# values = ['a','b','c','d']

# for item in values:
#     print(values)

# for i in range(len(values)):
#     values[i] = values[i].upper()
#     print(values)

# Exclusion Search - ALL words shorter than N
# file = open('words_small.txt')
# max_length = int(input("Max word length? "))

# all_short = True
# for line in file:
#     if len(line) > max_length:
#         all_short = False
#         break #can leave early

# if all_short:
#     print("All words short")
# else:
#     print("A word was long")

# King of the Hill Search - longest word
# file = open('words_small.txt')

# largest = ""
# for line in file:
#     if len(line) > len(largest):
#         largest = line

# print(largest + " is the largest!")

# does the file contain a particular word?
# line.strip() gets rid of leading or trailing whitespace, incl. \n (hard return)
# file = open('words_small.txt')

# target = input("Word to find: ")

# found = False
# for line in file:
#     if line.strip() == target:
#         found = True
#     # NO ELSE

# if found:
#     print(target + " is in the list!")
# else:
#     print(target + " is NOT in the list")

# average letters per line
# file = open('sonnets.txt')

# total_ltr = 0
# count = 0
# for line in file:
#     total_ltr = total_ltr + len(line)
#     count = count + 1

# avg_len = total_ltr/count

# print("Average word length:", avg_len)

# import re #for regex
# file = open("sonnet_xviii.txt")

# count = 0
# for line in file:
#     words = re.split("[^\w']", line) #space delimiter
#     for word in words:
#         if word != "":
#             #print(word)
#             count = count + 1

# print(count, "words")