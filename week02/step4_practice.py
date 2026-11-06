# ── 第 4 关：实战——函数版猜数字游戏 ──
# 这关先把完整代码给你（照抄能跑），但要求你做完两件事：
#   1. 逐行读懂：哪一行是定义？哪一行是调用？谁传参数？谁返回值？
#   2. 通关挑战：完成文件末尾的作业
#
# ─────────────────────────────────

import random


# 函数 1：生成题目，返回一个 1~100 的随机数

def make_answer():
    return random.randint(1, 100)


# 函数 2：判断一次猜测。返回字符串提示，不直接 print
# （把"判断"和"打印"分开，是专业程序员的习惯，先照做，慢慢会懂）

def check(guess, answer):
    if guess > answer:
        return "大了"
    elif guess < answer:
        return "小了"
    else:
        return "对了"


# 函数 3：整个游戏流程

def play():
    answer = make_answer()          # 调用函数 1，拿到答案
    count = 0
    print("我想好了一个 1~100 的数，开始猜！")

    while True:
        g = int(input("你猜："))
        count = count + 1
        result = check(g, answer)   # 调用函数 2，拿到提示
        print(result)
        if result == "对了":
            print("你一共猜了", count, "次")
            break


# ── 主程序：程序从这里开始跑 ──

play()
print("游戏结束，欢迎再来！")

# ── 通关作业（独立完成，做完这关你就出师了）──
#
# a) 玩一局，数数自己猜几次能中
# b) 改造 make_answer()：让它接受参数，能出 1~500 的题
#    （play() 里调用它的那行也要跟着改）
# c) 终极挑战：写一个新函数
#        def is_lucky(n):
#            （自己想：怎么判断 n 是不是"幸运数"？自己定规则，比如含 7 或者能被 3 整除）
#    并在猜中时用它打印一句"今天你运气不错！"
