# ── 第 2 关：参数——给函数喂原料 ──
# 上一关的 greet() 每次都说一模一样的话，像个复读机。
# 参数就是解决这个的：调用时塞给它不同的东西，它就干不同的活。
#
# 你其实早就用过参数了：
#   print("你好")      ← "你好" 就是塞给 print 的参数
#   random.randint(1, 100)  ← 1 和 100 也是参数
#
# ─────────────────────────────────

# 定义一个带参数的函数：括号里的 name 是"占位"，等调用时才有真值

def greet(name):
    print("你好，" + name + "！欢迎来学 Python。")


# 调用时括号里塞什么，name 就是什么

greet("uii699")
greet("小明")
greet("隔壁老王")

# 参数可以有好几个，用逗号隔开

def introduce(name, hobby):
    print(name + " 的爱好是 " + hobby + "。")


introduce("uii699", "打代码")
introduce("小李", "踢足球")

# 动手改：
#   a) 给 introduce 加第三个参数 age，让它的自我介绍更完整
#   b) 想想：greet(123) 会怎样？跑一下，看看报错说什么
#      （提示：文字 + 数字 会报错，这正是 age.py 里 int() 存在的原因）
