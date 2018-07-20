myStr_1 = str(input("Enter a string: "))
new_string =  ""
v_list = ('a', 'e', 'i', 'o', 'u')
for i in myStr_1.lower():
    if i in v_list:
        myStr_1 = myStr_1.replace(i, '')
print(myStr_1)    
    

        

