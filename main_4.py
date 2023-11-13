def amount_payment(*payment):
    
    sum = 0
    i = 0
    
    for i in payment:
        
        if i > 0:

            sum = sum + i

    return sum

print(amount_payment(100, 200, 300))




      
