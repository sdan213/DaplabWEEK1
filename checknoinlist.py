# 13. Write a Python program to check whether a number is in a given range
num = int(input("Enter a number: "))
start, end = 10, 20  
if start <= num <= end:
    print(num, "is in the range")
else:
    print(num, "is not in the range")