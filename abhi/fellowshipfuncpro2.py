#program for percentage for heads and tails
import random
def flip_coin(n):
    heads=0
    for i in range(0,n):
        coin=random.randint(1,2)
        if (coin==1):
            heads+=1
    percentage_heads=(heads/n)*100
    percentage_tails=100-percentage_heads
    print(percentage_heads)
    print(percentage_tails)
flip_coin(100)
