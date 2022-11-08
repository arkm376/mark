print("我能幫你計算用網路傳輸需要多久時間(以下輸入數字即可)")
b = int(input("請問網速?(MB/S)")) # isp 說的網速
n = int(b)/8 #實際網速
ax = int(input("請問容量是[1]MB/[2]GB/[3]TB"))#使用著容量

if ax == 1 :
    de=int(input("那是多少MB呢?")) / int(n)
if ax == 2 :
    de=int(input("那是多少GB呢?"))*1024 / int(n)
if ax == 3 :
    de=int(input("那是多少TB呢?"))*1024*1024 / int(n)

if  60< de < 3600:
    time = de / 60
    print("您的傳輸間須為"+ str(time) +"分鐘")
elif de <= 60:
    print("您的傳輸間須為"+ str(de) +"秒")
if de >= 3600:
    time = de / 3600
    print("您的傳輸間須為"+ str(time) +"小時")