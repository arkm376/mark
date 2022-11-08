import random

print("Randomly guess numbers, no prizes for guessing right, you can enter the maximum and minimum")
x = int(input("minimum value?"))
y = int(input("maximum value?"))
p = input("your anwsrs is?")
a = str((random.randint(x,y)))
if p == a :
    print("You got it right!")
else:
    print("guess wrong")
print("the answer is"+ a)
