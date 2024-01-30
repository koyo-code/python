print("Hello world")

num = -1
if num < 0:
    print("負の整数")
elif num ==0:
    print("0")
else:
    print("正の整数")

print(len("python"))

print(type("python"))

word_lists = ["Python","Java","C++"]
for word in word_lists:
    print(word)

num = 1
while num < 5:
    print(num)
    num+=1

for i in range(5):
    print(i)

for i in range(1,6):
    if i ==3:
        break
    print(i)

for i, word in enumerate(word_lists):
    print(i, word)

for i in range(5):
  print(i)
else:
  print("終わり")

num_lists = [1, 2, 3]
word_lists = ["Python","Java","C++"]
for num, word in zip(num_lists, word_lists):
    print(num, word)