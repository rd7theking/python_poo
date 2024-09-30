class pessoa:
    #atributos
    nome = "Jose ryan"
    peso = 90
    escolaridade = "Ensino medio"

    #métodos
    def falar(self, texto):
        print(f"Tenho algo para te dizer: {texto}")


        #criando os objetos
        pessoal = pessoa()
        
        print(pessoal.nome)
        pessoal.falar("Boa tarde, hoje é segunda-feira")