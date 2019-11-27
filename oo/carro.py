NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    def __init__(self):
        self.valor = NORTE

    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL:LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __abs__(self):
        self.velocidade = 0

        def acelerar(self):
            self.velocidade += 1

        def frear(self):
            self.velocidade -= 2
            self.velocidade = max(0, self.velocidade)


