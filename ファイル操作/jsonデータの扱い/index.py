import json

data = {"a":1, "b":"x", "c":[1, 2, 3], "d": {"a":1, "b":2}}
s = json.dumps(data) # 文字列として書き出す
print(s)

data2 = json.loads(s) # 文字列をjsonデータとして読み込む
print(data2)