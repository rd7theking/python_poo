class pessoa:
    # criar o método construtor
    def __init__(self, nome, altura, idade):
        #estamos criando os atributos de classe utilizando o método construtor. nesse caso precisamos passar os parametros que serão usados como valores dos atríbutos.
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura é {self.altura} e sua idade é {self.idade}")

#criando os objetos
p1 = pessoa("Zé roberto", 1.87,99)
p2 = pessoa("Zé ryan",1.72,75)

p1.exibirDados()
p2.exibirDados()