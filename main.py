class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y

    def parse_input(self, user_input):
        operators = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide}
        for op in operators:
            if op in user_input:
                num1, num2 = user_input.split(op)
                try:
                    num1, num2 = float(num1), float(num2)
                    return operators[op](num1, num2)
                except ValueError:
                    return "Invalid input! Please enter valid numbers."
        return "No valid operator found!"

    def run(self):
        print("Welcome to the Python Calculator!")

        while True:
            user_input = input("Enter your calculation: ")
            result = self.parse_input(user_input)
            print(f"The result is: {result}")

            quit_calculater = [i.lower() for i in user_input.split()]
            if 'quit' in quit_calculater or 'q' in quit_calculater:
                break

        print("Thank you for using the Python Calculator! Goodbye.")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
