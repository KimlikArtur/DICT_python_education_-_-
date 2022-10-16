print("Hello! My name is DICT_Bot")

print("I was created in 2022")

print("Please, remind me your name")
x = input(">")

print("What a great name you have,", x, "!")

print("Let me guess your age")

print("Enter remainders of dividing your age by 3, 5 and 7")

zalishok3 = input(">")
zalishok5 = input(">")
zalishok7 = input(">")

age = (int(zalishok3) * 70 + int(zalishok5) * 21 + int(zalishok7) * 15) % 105

print("Your age is", 17, "that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want")

from_num = int(input(">"))

print("Counting numbers from " + str(from_num))
for number in range(from_num + 1):
    print(number, "!")
print("Completed, have a nice day!")

print("1.To repeat a statement multiple times.""\n2.To decompose a program into several small subroutines."""
      "\n3.To determine the execution time of a program.""\n4.To interrupt the execution of a program.")

user = 0
while user != 2:
    user = int(input(">"))
    if user > 2:
        print("Please, try again!")
    if user < 2:
        print("Please, try again!")
    if user == 2:
        print("Completed, have a nice day!""\nCongratulations, have a nice day!")

