import random

def pass_gen(lenght):
    
    list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_"
    
    #creating a empty password string
    passwd = " "

    #loop that will go upto the lenght of password
    for i in range(lenght):
        #random.choice() function is used to select random character from the list_of_chars and concatenate it with passwd string
        passwd = passwd + random.choice(list_of_chars)

    return passwd


print("Enter the lenght of password to be generated:  ")
lenght = int(input())

passwd = pass_gen(lenght)
print("Random generated password is:  ",passwd)
