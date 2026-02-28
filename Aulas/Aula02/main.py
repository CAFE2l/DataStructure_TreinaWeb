from array import array 
from vetores import vetor
from listas import lista_ligada, lista_duplamente_ligada
from pilhas import pilha
from filas import fila

print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")

menu = int(input("Digite a opção deseja: "))

if menu == 1:
    vetor_test = vetor.Vetor(0)
    vetor_test.inserir_elemento_posicao(1, 0)
    vetor_test.inserir_elemento_posicao(2, 1)
    vetor_test.inserir_elemento_posicao(3, 2)
    vetor_test.inserir_elemento_posicao(4, 2)
    vetor_test.inserir_elemento_posicao(5, 2)
    vetor_test.inserir_elemento_final(1)
    print(vetor_test.tamanho_vetor())
    print(vetor_test)
    print(vetor_test.indice(4))
    print(vetor_test.remover_elemento_indice(3))
    print(vetor_test)
    vetor_test.remover_elemento(5)
    print(vetor_test)

elif menu == 2:
    lista_test = lista_ligada.ListaLigada()
    lista_test.inserir(1)
    lista_test.inserir(2)
    lista_test.inserir(3)
    lista_test.inserir_posicao(1, 10)
    print(lista_test)
    lista_test.remover_elemento(2)
    print(lista_test)
    # print(lista_test)
    # print(lista_test.contem(2))
    #print(f"O elemento 3 esta na posição {lista_test.indice(3)}")
    # print(lista_test.recuperar_elemento_no(0))


elif menu == 3:
    lista_test = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_test.inserir(1)
    lista_test.inserir(2)
    lista_test.inserir(3)
    lista_test.inserir_posicao(1, 10)
    print(lista_test)
    # lista_test.remover_elemento(2)
    lista_test.remover_posicao(2)
    print(lista_test)



elif menu == 4:
    pilha_test = pilha.Pilha()
    pilha_test.empilhar(5)
    # pilha_test.empilhar(6)
    print(pilha_test.desempilhar())



elif menu == 5:
    fila_test = fila.Fila()
    fila_test.enfileirar(1)
    fila_test.enfileirar(2)
    fila_test.enfileirar(3)
    fila_test.enfileirar(4)
    print(fila_test) # 1 2 3 4 
    print(fila_test.desenfileirar())
    print(fila_test)
    fila_test.enfileirar(6)
    print(fila_test)
else:
    print("opcao invalida")
