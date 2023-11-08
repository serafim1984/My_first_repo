result = None
operand = None
operator = None
wait_for_number = True

while True:
    
    if wait_for_number == True:

        try:
            
            operand = int(input("Input please a number: "))

        except ValueError:

            operand = int(input("Not a number, please input a number: "))

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

        elif operand == "=":

            break
            
        wait_for_number = False
    
    else: 

        operator =(input("Input please an operator: "))

        if operator == "=":

            break

        elif operator != "+" and operator != "-" and operator != "*" and operator != "/":

            operator =(input("Input please a valid operator!: "))

        wait_for_number = True

        
print(result)