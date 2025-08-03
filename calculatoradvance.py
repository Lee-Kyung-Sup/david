def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    else:
        return a / b
    
def main(): 

    try:

         e = input("Enter your expression: ")
         x, op, y = e.split()

         x = float(x)
         y = float(y)

         result = 0
         if op == '+':
             result = add(x, y)
         elif op == '-':
             result = subtract(x, y)
         elif op == '*':
             result = multiply(x, y)
         elif op == '/':
             result = divide(x, y)       
         else:
             print("Invalid operator.")
         print("Result: ", result)

    except ValueError:
         print("Invalid input. Input number operator number")
        
    

if __name__ == "__main__":
    main()    