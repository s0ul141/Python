#here we give a password as input and check whether it is valid password or not 
#else if ladder
pw=input("password") # input is given here
if(" ") in pw: #1st condition to check whether there is a space or not 
    print("False") 
elif("'") in pw: #to check what if we had ' i.e., a single quote 
    print("False") 
elif("/") in pw: #to check what if we had back slash /
    print('False') 
elif("=") in pw: #to check what if we had a equal to sign =
    print('False') 
elif('"') in pw: #to check what if we had double quote or not "
    print("False") 
elif('\\') in pw: #to check what if we had \\ slash or not 
    print("False") 
elif(8>len(pw)): #to check the length of the input whether it is greater than 8 or not
    print("False") 
elif(32<len(pw)):#to check the length of the input whether it is less than 32 or not 
    print("False") 
elif(pw[0].isalpha):#check the 1st character whether it is a alphabet or not
    print("True") 
else: 
    print("False")
