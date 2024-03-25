# 関数定義
#　関数の定義にはdefを使う

def f(a, b):
    return a + b

print(f(3, 5))
print(f(2, 1))

def g(a, b=100):                    # 引数bにデフォルト値を設定
    return a + b

print(g(3))                         # 引数bを省略
print(g(2, 3))

def h(a, b=1, c=1):
    return a * 100 + b * 10 + c

print(h(1, 2, 3))                   # 引数3つとも指定
print(h(2))                         # 引数１つだけ指定
print(h(2, c=2))                    # 1つ目の引数とcを指定、bはデフォルト値
print(h(a=2, c=3))                  # aの値も明示的に指定する事ができる
print(h(b=2, a=1, c=3))             # 名前付きで引数を与える場合は順番は自由である