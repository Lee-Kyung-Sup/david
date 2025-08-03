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
        
         x = float(input("숫자 x 입력: "))
         y = float(input("숫자 y 입력:" ))
         op = input("연산자 입력 (+, -, *, /): ")
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
             return
         print("Result: ", result)
         
    except ValueError:
         print("Invalid Error")
        
    

if __name__ == "__main__":
    main()    