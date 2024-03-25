from datetime import date
import pickle

x = date(2018, 1, 1)
x

with open("today.pkl", "Wb") as f:
    pickle.dump(x, f, -1) # ファイルに書き込む

with open("today.pkl", "rb") as f:
    y = pickle.load(f) # ファイルから読み込む

y