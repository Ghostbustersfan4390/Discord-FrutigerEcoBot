import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for _ in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emoji():
    emojis = ["😀", "👻", "😆", "🤣", "🔼"]
    return random.choice(emojis)

def flip_coin():
    if random.randint(0, 1):
        return "HEADS"
    else:
        return "TAILS"
