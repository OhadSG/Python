x = input("write something: ")

for i in "aeuio":
    x = x.replace(i, i + 'b' + i)

print(x)