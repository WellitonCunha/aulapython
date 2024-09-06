class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    #metodo get vai buscar algo
    def get_nome(self):
        return self.__nome
    
    #metodo set vai modificar algo
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

pessoa = Pessoa("Welliton",18)

print(pessoa.get_nome())
print(pessoa.get_idade())
pessoa.set_nome("Maria")
pessoa.set_idade(27)
print(pessoa.get_nome())
print(pessoa.get_idade())
    