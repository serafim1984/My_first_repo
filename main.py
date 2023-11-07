result = None
operand = None
operator = None
wait_for_number = True

while True:

    result 
    
    if wait_for_number == True:
    
        operand = int(input("Input please a number: "))

        if operator == "+":

            result = result + operand
            
        elif operator == "-":
            
            result = result - operand

        elif operator == "*":

            result = result * operand

        elif operator == "/":

            result = result / operand

        elif operator is None:

            result = operand

            
        wait_for_number = False
    
    else:      