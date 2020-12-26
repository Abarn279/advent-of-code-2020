def get_ls(key, subject):
    val = 1
    ls = 0
    while val != key:
        val *= subject
        val %= 20201227
        ls += 1
    return ls

def transform(subject, ls):
    val = 1
    for i in range(ls):
        val *= subject
        val %= 20201227
    return val

card_key = 9232416
door_key = 14144084

card_ls = get_ls(card_key, 7)

print(transform(door_key, card_ls))