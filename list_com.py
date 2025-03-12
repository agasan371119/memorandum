#通常の空のリストに格納繰り返し
a = []

for i in range(10):
  a.append(i)

print(a)

#リスト内包表記
b = [x for x in range(10)]

print(b)

#条件式ありの空の繰り返し
c = []

for i in range(100):
  if i % 13 == 0:
    c.append(i)

print(c)

#リスト内包表記の条件式

d = [x for x in range(10) if x % 2 == 0]

print(d)

#辞書
#空の辞書
dict = {}

#繰り返し格納
for i in range(5):
  a, b = input().split()
  dict[a] = int(b)
  
print(dict)

#辞書の内包表記
dict_1 = [input().split() for x in range(5)]

print(dict_1)