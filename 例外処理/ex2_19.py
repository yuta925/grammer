d = {"a":1, "b":2, "c":3}

try:
    print(d["d"])       
except KeyError as err:                  # 発生した例外を変数errに代入
    print("keyError: {}".format(err))    # エラーの内容を表示