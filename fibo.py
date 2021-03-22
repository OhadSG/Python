#made by Ohad Solomon Gleicher

first = 0
second = 1
while True:
    print(second)
    first, second = second, first + second
    if second >= 10000:
        break
