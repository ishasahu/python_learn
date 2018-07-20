my_str = str(input("Enter a string: "))
my_letter = str(input("Letter you need to find in the string: "))
my_str = my_str.lower()
my_letter = my_letter.lower()
count = 0
for char in my_str:
    if char == my_letter:
        count += 1
print("Occurance of letter in string: ", count) 

