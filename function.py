#関数の復習のため

def say_hello():#関数の設定
    # string = input()#標準入力で読み込む
    print("hello world")
    # print(f"hello {string}")

say_hello()

#関数で九九の表を作成する

def kuku(x, y):
  return x * y

for num_x in range(1, 10):
  for num_y in range(1, 10):
    print(kuku(num_x, num_y), end="")
    if num_y < 9:
      print(", ", end = "")
  
  print("") 