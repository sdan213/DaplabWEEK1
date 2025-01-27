# 14. Calculate the number of upper case letters and lower case letters in a string
string = input("Enter a string: ")
upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())
print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)