class Pessoa:
    def __init__(self, nome = None):
        self.nome = nome

    def  cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('A')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Anny'
    print(p.nome)