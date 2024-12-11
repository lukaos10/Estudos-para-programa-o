class Usuario:

        def __init__(self, nome, email, idade):
                self.nome = nome
                self.email = email
                self.idade = idade


        def saudacao(self):
                print (f"Olá meu nome é {self.nome}, eu tenho {self.idade} anos.")

        def aniversario(self):
                self.idade += 1


class Cliente(Usuario):

        def __init__(self, nome, email, idade, saldo):
                Usuario.__init__(self,nome, email, idade)
                self.saldo = saldo

        def saudacao(self):
                print (f"Olá meu nome é {self.nome}, eu tenho {self.idade} anos, minha conta bancario tem {self.saldo} de money")


cliente1 = Cliente("Carlos", "carlos@gmail.com", 18, 1000)
cliente1.saudacao()
print(cliente1.saldo)


usuario1 = Usuario("Pedro","pedro@gmail.com", 30)
usuario1.saudacao()
