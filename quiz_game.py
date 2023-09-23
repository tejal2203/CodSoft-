print("-----------Welcome to Pyhton Quiz------------\n")

score = 0

#first question
print("Who is the developer of python?")
print("1. Guido Van Rossum\n2. Dennis Ritchie\n3. Bjarne Stroustrup\n4.James Gosling")

ans_no = int(input("Enter the number of answer: "))
if(ans_no == 1):
    print("Correct Answer!")
    score+=1
else:
    print("Inorrect Answer!")
    print("Correct answer: 1")

#second question
print("\n2. What is the extension of python file?")
print("1. .p\n2. .py\n3. .c\n4. .python")

ans_no = int(input("Enter the number of answer: "))
if(ans_no == 2):
    print("Correct Answer!")
    score+=1
else:
    print("Inorrect Answer!")
    print("Correct answer: 2")

#third question
print("\n3. What we use to define a block of code in python language?")
print("1. key\n2. brackets\n3. indentation\n4. None of these")

ans_no = int(input("Enter the number of answer: "))
if(ans_no == 3):
    print("Correct Answer!")
    score+=1
else:
    print("Inorrect Answer!")
    print("Correct answer: 3")

#fourth question
print("\n4. Which character is used in python for single line comment?")
print("1. /\n2. //\n3. #\n4. \\")

ans_no = int(input("Enter the number of answer: "))
if(ans_no == 3):
    print("Correct Answer!")
    score+=1
else:
    print("Inorrect Answer!")
    print("Correct answer: 3")

#fifth question
print("\n5. What will be the output of following code\n?")
print("'a' + 'bc'")
print("1. a+bc\n2. abc\n3. a bc\n4. a")

ans_no = int(input("Enter the number of answer: "))
if(ans_no == 2):
    print("Correct Answer!")
    score+=1
else:
    print("Inorrect Answer!")
    print("Correct answer: 2")


if(score ==5):
    print("\nCongratulations!! \nYour Final Score = ", score)
else:
    print("\nYou need more practice, \nYour Final Score = ", score)







    
