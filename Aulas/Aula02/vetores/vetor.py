class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho # 3x[None]
        self.__posicao = 0 


    def inserir_elemento_posicao(self, elemento, posicao):
        # 1 2 3 
        #inserir_elemento_posicao(3,1)
        self.__elementos[posicao] = elemento


    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos = self.__elementos + [None]

        #1, 2, 3
        #2
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1


    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
