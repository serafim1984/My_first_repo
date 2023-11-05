num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    new = num + 1
    
    for j in range(new):
        sum = sum + j
        j = j + 1
        
    num = int(input("Enter integer (0 for output): "))

print(sum)