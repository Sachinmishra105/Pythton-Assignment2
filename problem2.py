# Write a python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding
# ASCII values.


alphabets = "abcdefghijklmnopqrstuvwxyz"

ascii_dict = {alphabet: ord(alphabet) for alphabet in alphabets }

print(ascii_dict)



