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