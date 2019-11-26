class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def  cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return  f'{cls} - olhos {cls.olhos}'

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
    anny.sobrenome = 'Bispo' #add atributos
    del anny.filhos #remove atributos
    print(anny.__dict__)
    print(renzo.__dict__)
    print(anny.olhos)
    print(renzo.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(anny.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), anny.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), anny.nome_e_atributos_de_classe())

