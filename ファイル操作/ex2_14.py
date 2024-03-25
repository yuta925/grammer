# ここでは明示的にファイルを閉じているが、
# この場合ファイルを開いてから閉じるまでの間にエラーが発生すると、
# ファイルが閉じられない可能性がある。

f = open("sample.txt")
for line in f: # 1行ずつ処理する
    line = line.rstrip() # 末尾の空白と改行を削除
    print(line)
f.close()