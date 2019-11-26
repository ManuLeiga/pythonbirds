class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def  cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome = 'Renzo')
    anny = Pessoa(renzo, nome = 'Anny')
    print(Pessoa.cumprimentar(anny))
    print(id(anny))
    print(anny.cumprimentar())
    print(anny.nome)
    print(anny.idade)
    for filho in anny.filhos:
        print(filho.nome)
    print(anny.filhos)
