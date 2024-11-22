class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y


x = 4
y = 5

calculo = Calculo()

print(f"Somando: {x} + {y} = {calculo.soma(x, y)}")
print(f"Subtraindo: {x} - {y} = {calculo.subtracao(x, y)}")
