class Calculadora:
    def _init_(self, x, y):
        self.num_1 = x
        self.num_2 = y

    def som(self):
        return self.num_1 + self.num_2

    def sub(self):
        return self.num_1 - self.num_2

    def mult(self):
        return self.num_1 * self.num_2

    def div(self):
        return self.num_1 / self.num_2


calc = Calculadora(5, 10)

resp = calc.soma()
resp = calc.sub()
resp = calc.mult()
resp = calc.div()