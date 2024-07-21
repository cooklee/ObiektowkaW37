class Calculator:

    def __init__(self):
        self.operations = []

    def add(self, num1, num2):
        result = num1 + num2
        s = f"added {num1} to {num2} got {result}"
        self.operations.append(s)
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        s = f"multiplied {num1} by {num2} got {result}"
        self.operations.append(s)
        return result

    def print_operations(self):
        for oper in self.operations:
            print(oper)


# c1 = Calculator()
# c2 = Calculator()
# c1.add(1,2)
# c1.add(423,123)
# c1.multiply(34,23)
# c2.add(0,0)
# c1.print_operations()
# print("-------------------")
# c2.print_operations()

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def describe(self):
        print(self)

    def distance(self, shape):
        return ((self.x-shape.x)**2 + (self.y-shape.y)**2)**0.5

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"


a = Shape(1,1,'blue')
b = Shape(1,2,'green')
print(a)
a.describe()
print("------------")
print(b)
b.describe()


class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0.0


    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount > 0:
            if self.cash < amount:
                amount = self.cash
            self.cash -= amount
            return amount

    def print_info(self):
        print(self.number, self.cash)

class Employee:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = None

    def set_salary(self, amount):
        if type(amount) in (int, float) and amount>0:
            self._salary = amount
