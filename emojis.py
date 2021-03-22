import re


def main():
    s = open(r"C:\Users\User\Desktop\emojis.txt", "r")
    text = s.read()
    arr = re.compile("\s").split(text)
    arr = [i for i in arr if i != '']
    arr = [arr[i] for i in range(len(arr)) if arr[i] != arr[i - 1]]
    arr3 = [arr[i] for i in range(1, len(arr)) if
            arr[i].startswith("U+") or (not arr[i].startswith("U+") and arr[i - 1].startswith("U+"))]
    arr3.insert(0, arr[0])
    arr2 = []
    s = []
    for i in arr3:
        if not i.startswith("U+"):
            arr2.append(s)
            s = []
        else:
            i = translate(i[2:])

        s.append(i)

    arr = []
    for i in arr2[1:]:
        s = '{"' + str(i[1])
        if len(i) > 2:
            s += str(i[2])
        s += '", "' + str(i[0]) + '"}, '
        arr.append(s)

    for i in arr:
        print(i)


def translate(x):
    x = int(x, 16)
    if x < 0x10000:
        return "\\u" + hex(x)[2:].upper().zfill(4)
    else:
        x -= 0x10000
        h = x // 0x400 + 0xD800
        l = x % 0x400 + 0xDC00
        return "\\u" + hex(h)[2:].upper().zfill(4) + "\\u" + hex(l)[2:].upper().zfill(4)


if __name__ == '__main__':
    main()
