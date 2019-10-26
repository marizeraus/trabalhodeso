import process
# TODO LER O ARQUIVO NA MAIN, E CHAMAR FUNÇÕES PARA CADA AÇÃO

file = open('entrada.txt', 'r')

for processo in file:
    infos = processo.split()
    if(len(infos)>0):
        process_no = infos[0]
        action = infos[1]

    if(action == 'P'):
        process.execute_instrution()
        print("executar")
    elif (action == 'I'):
        process.ioinstruction()
        print("entrada e saida")
    elif (action == 'C'):
        process.create_process()
        print("criar processo")
    elif (action == 'R'):
        print("ler endereço lógico")
        process.read_address()
    elif (action == 'W'):
        print("escrita")
        process.write()
    elif (action == 'T'):
        print("terminar processo")
        process.terminate_process()
    else:
        print("Ação inválida")

