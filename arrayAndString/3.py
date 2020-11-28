# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"


def replaceSpace(string, length):
    newString = ''
    for i in range(length):
        if string[i] == ' ':
            newString += '%20'
        else:
            newString += string[i]
    return newString
            

print(replaceSpace('ne er   ', 4))