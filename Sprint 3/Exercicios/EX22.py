class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ''

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    nome = property(get_nome, set_nome)


# Testando a classe
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
