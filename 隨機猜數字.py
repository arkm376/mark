import random

print("隨機亂猜數字,猜對沒獎,可輸入最大最小")
x = int(input("最小值?"))
y = int(input("最大值?"))
p = input("你的答案是?")
a = str((random.randint(x,y)))
if p == a :
    print("你答對了喔!")
else:
    print("猜錯囉~")
print("答案是"+ a)