from array import array 
from vetores import vetor
print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção deseja: "))

if menu == 1:
    vetor_test = vetor.Vetor(3)
    # vetor_test.inserir_elemento_posicao(1, 0)
    # vetor_test.inserir_elemento_posicao(3, 1)
    vetor_test.inserir_elemento_final(1)
    vetor_test.inserir_elemento_final(2)
    vetor_test.inserir_elemento_final(3)
    vetor_test.inserir_elemento_final(4)
    vetor_test.inserir_elemento_final(5)
    print(vetor_test.listar_elemento(0))
    print(vetor_test.listar_elemento(1))
    print(vetor_test.listar_elemento(2))
    print(vetor_test.listar_elemento(3))
    print(vetor_test.listar_elemento(4))
