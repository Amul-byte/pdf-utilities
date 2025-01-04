'''Like we are wrtig the code for decoding the password like 
for less than 3 character it will just reverse the data but for more than 3 character we just add some random value at first and last with moving the first to last '''
import random
while True:
    choice=int(input("Please enter your choice DECODE(0) OR CODE(1). (3) for Force quit\n Your Choice: "))
    if choice == 3:
        print("Exitting the code")
        break
    elif choice == 0:
        word=input("What you want to decode: ")
        if len(word) <= 3:
            # [start:stop:step]
            print(f"Your decoded word for {word} is {word[::-1]}")
        else:
            word1 = word[len(word)-4]+ word[3:len(word)-4]
            print(f"Your decoded word for{word} is {word1.lower()} ")
    elif choice == 1:
        word=input("Write the word yiu wanna code: ")
        if len(word) <= 3: 
            word = word[::-1]
            print("",word)
        else:
            word = word[1:] + word[0]
            choice = "1234567890!@#$%^&*()qwertyuiopasvhcgghjklzxcvbnm"
            word = "".join(random.choices(choice,k=3))+ word + "".join(random.choices(choice,k=3))
            print(word.upper())
    else:
        print("Please enter a right value\n")
        continue
