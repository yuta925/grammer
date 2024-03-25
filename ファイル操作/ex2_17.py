import csv

s = 0
with open("ファイル操作/sample.csv") as f:
    reader = csv.reader(f) # csvファイルを読み込む
    next(reader) # 1行進める
    for row in reader:
        s += int(row[1]) # 左から2列目の数値を加算する

print(s)