import time

print("我能幫你算出你的BMI,順便看看你有過重嗎?")
time.sleep(1)
my_str_1 = input("請給我你的身高(cm)?")  # 使用者的身高
z = int(my_str_1) / 100  # 把使用者的身高cm換m(公尺)
y = z * z
my_str_2 = input("你的體重?")  # 使用者的體重
x = int(my_str_2) // y
print("你的BMI為:")
print(x)
time.sleep(1)
kg = x
if kg <= 18.5:
    print("過輕囉!")
if 18.5 <= kg < 24:
    print("恭喜你很健康")
if 24 <= kg < 27:
    print("過重囉!")
if kg >= 27:
    print("你已嚴重過重了!!!")
time.sleep(3)
print("正常BMI範圍為")
print("18.5≦BMI＜24")
time.sleep(2)
print("異常範圍為")
print("過重：24≦BMI＜27")
print("輕度肥胖：27≦BMI＜30")
print("中度肥胖：30≦BMI＜35")
print("重度肥胖：BMI≧35")
print("過輕:BMI ＜ 18.5")
