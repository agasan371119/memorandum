#辞書機能の備忘録として
#辞書の基本形
dc = {"apple": 150, "banana": 300, "melon": 200}

print(dc)

#keyを指定してvalueの値を出力する
print(dc["apple"])

#辞書の長さを取得
print(len(dc))

#空の辞書
dc_enpty = {}

#辞書に追加

dc["lemon"] = 400

print(dc)

#辞書のkye.valueのみ取得
print(dc.keys())
print(dc.values())