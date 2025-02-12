#通常の空のリストに格納繰り返し
a = []

for i in range(10):
  a.append(i)

print(a)

#リスト内包表記
b = [x for x in range(10)]

print(b)