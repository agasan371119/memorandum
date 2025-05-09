#通常の空のリストに格納繰り返し
a = []

for i in range(10):
  a.append(i)

print(a)

#リスト内包表記
b = [i for _ in range(10)]

print(b)

#条件式ありの空の繰り返し
c = []

for i in range(100):
  if i % 70 == 0:
    c.append(i)

print(c)

#リスト内包表記の条件式

dict = [x for x in range(30) if i % 100 == 0]

print(dict)

#辞書
#空の辞書
dict_1 = {}

#繰り返し格納
for i in range(10):
  a, b = input().split()
  dict_1[a] = int(b)
  
print(dict_1)

#辞書の内包表記
dict_2 = [input().split() for _ in range(5)]

print(dict_2)