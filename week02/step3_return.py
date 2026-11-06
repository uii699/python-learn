# ── 第 3 关：返回值——让函数把结果交回来 ──
# 前两关的函数只会"说"（print），不会"交作业"。
# return 就是让函数把算好的结果交还给你，你才能接着用它做下一步。
#
# 其实你也早就用过返回值了：
#   age = 2026 - birth   ← 减法是个动作，它"返回"了结果，你才存得进 age
#
# ─────────────────────────────────

# 一个只会算数的函数

def add(a, b):
    result = a + b
    return result        # 把 result 交回给调用的人


# 关键区别：调用 add(3, 5) 的地方，会"变成"它的返回值 8

x = add(3, 5)
print("3 + 5 =", x)
print("3 + 5 再乘 2 =", add(3, 5) * 2)      # 返回值可以直接接着算
print("9 + 10 =", add(9, 10))

# 一个更实用的例子：算年龄的函数（把你 age.py 的逻辑装进来！）

def calc_age(birth_year):
    return 2026 - birth_year


print("2000 年出生的人今年", calc_age(2000), "岁")
print("1995 年出生的人今年", calc_age(1995), "岁")

# 看到了吗？写了 calc_age 一次，算谁都行——这就是函数的价值。

# 动手改：
#   a) 写一个函数 double(x)，返回 x 的两倍，然后 print(double(21))
#   b) 思考：把 return result 改成 print(result)，再跑 add(3,5)*2 会怎样？
#      （体会 return 和 print 的本质区别：一个交货，一个只吆喝）
