with open("output.txt", "w") as fw: # 書き込み用に開く
    with open("sample.txt") as fr:  # 読み込み用に開く
        for line in fr:
            print(line, end="", file=fw)