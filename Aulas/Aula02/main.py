from array import array 
from vetores import vetor
print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção deseja: "))

if menu == 1:
    vetor_test = vetor.Vetor(0)
    vetor_test.inserir_elemento_posicao(1, 0)
    vetor_test.inserir_elemento_posicao(2, 1)
    vetor_test.inserir_elemento_posicao(3, 2)
    vetor_test.inserir_elemento_posicao(4, 2)
    vetor_test.inserir_elemento_posicao(5, 2)
    vetor_test.inserir_elemento_final(1)

#    print(vetor_test)
