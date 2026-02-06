from itertools import product

def solution(users, emoticons):
    max_plus = 0
    max_sale = 0
    
    discounts = [10,20,30,40]
    
    for discount in product(discounts, repeat=len(emoticons)):
        plus = 0
        sale = 0
        
        for user_discount, user_price in users:
            total = 0
            for d,price in zip(discount,emoticons):
                if d>=user_discount:
                    total += (100-d)*price//100
            if total>=user_price:
                plus += 1
            else:
                sale += total
        
        if (plus>max_plus) or ((plus==max_plus) and (sale>max_sale)):
            max_plus = plus
            max_sale = sale
            
    
    return [max_plus, max_sale]