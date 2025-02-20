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

#辞書をkey,valueを同時に取得

print(dc.items())


#ループでアンパック(要素が２つあるリストなら２つの変数に格納すること?)

for key, value in dc.items():
  print(key, value)
  
#辞書のkeyとして含まれているか
print("apple" in dc) #Trueが返ってくる
print("ichigo" in dc) #Falseが返ってくる

#辞書のキーをsort

ke = sorted(dc)

print(ke)

#辞書の内包表記
 #通常の繰り返しでの辞書化
a = {}
for i in range(10):
  a[i] = i * 2
print(a)

 #内包表記の辞書

b = {x: x*2 for x in range(10)}

print(b)

#２重リスト
team_a = ["勇者", "魔獣使い", "剣士"]
team_b = ["健闘", "蛇拳", "酔拳"]

teams = [team_a, team_b]

for i in range(len(teams)):
  print(len(teams[i]))
#多重リスト 内包表記

num = [[x for x in range(3)] for i in range(5)]

for i in num:
  print(i)