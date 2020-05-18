class Calculator:
    def add(self, x, y):
        return x + y

    def difference(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


class ScienceCalculator(Calculator):
    def pot(self, x, y):
        return x ** y


kalkulatorek = ScienceCalculator()
print(kalkulatorek.add(5, 5))
print(kalkulatorek.difference(5, 5))
print(kalkulatorek.multiply(5, 5))
print(kalkulatorek.divide(5, 5))
print(kalkulatorek.pot(5, 5))
