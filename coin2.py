import random
 
 
def get_coin():
    coin = random.randint(1,2)
 
    if coin == 1:
        return "Орёл, ты проиграл"
    else:
        return"Решка, ты выиграл"
