import random
number=(random.randint(0,100))
print(number)
guess=int(input("Guess the number: "))
count=1
while guess!= number:
    guess=int(input("Guess the number: "))
    count+=1
print(f"The humber was {guess}, you did it in {count} times")