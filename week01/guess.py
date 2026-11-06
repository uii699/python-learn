import random

n = random.randint(1, 100)
print("我想好了一个 1~100 的数，猜猜看！")

while True:
    g = int(input("你猜："))

    if g > n:
        print("大了，往小猜")
    elif g < n:
        print("小了，往大猜")
    else:
        print("猜中了，你真棒！")
        break
