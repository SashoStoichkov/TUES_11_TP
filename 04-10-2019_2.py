class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 // num2

if __name__ == "__main__":

    while True:
        expr = str(input())

        if expr == "exit":
            break

        expr_l = list(expr.split(" "))

        num1 = int(expr_l[0])
        op = expr_l[1]
        num2 = int(expr_l[2])

        cal = Calculator()
        result = 0

        if op == "+":
            result = cal.add(num1, num2)
            print(result)
        elif op == "-":
            result = cal.sub(num1, num2)
            print(result)
        elif op == "*":
            result = cal.mul(num1, num2)
            print(result)
        elif op == "/":
            result = cal.div(num1, num2)
            print(result)
        else:
            print("You are not very smart, right?")