import json

FILE = r"FILE"


def main():



def add_strike(user_id):
    with open(FILE, "+") as file:
        text = file.read()
        js = json.loads(text)
        if user_id in js.keys():
            js[user_id] = int(js[user_id]) + 1
        else:
            js[user_id] = 1
        return int(js[user_id])





if __name__ == '__main__':
    main()
