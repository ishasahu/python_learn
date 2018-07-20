my_str = str(input("Enter a string: "))
my_str = my_str.strip()
sym = my_str[-1]
if sym == '!':
    print(my_str.upper())
else:
    print(my_str.lower())



