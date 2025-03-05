#関数定義
def num(x):
  return x * 2
  
print(num(3))

def cnt(x):
  return x ** 2

print(cnt(3))

def num_and_cnt(x, y):
  return num(cnt(x))

print(num_and_cnt(3,2))

def num1_num2(a, b):
  return a ** b

print(num1_num2(5, 6))

def loop():
  print("正解")

loop()

def sum(a, b):
  return a // b

print(sum(10, 20))