''' 
a) implemente essa tabela em duas versões: uma usando somente listas e outra, somente com dicionários. '''

# print tabela 
def mostraLista(lista):
    print("\n\n")
    print("-"*4, "Usando Listas", "-"*4)
    print("Sexo  Predileta  Nota")
    for linha in lista:
        for j in linha:
            print(" ",j, end=" "*5)
        print()

# print dicionario
def mostraDicionario(dicionario):
    print("\n\n")
    print("-"*4, "Usando Dicionario", "-"*4)
    print("Sexo  Predileta  Nota")
    for i in range(11):
        print(" ",dicionario["sexo"][i]," "*5, dicionario["predileta"][i]," "*5, dicionario["nota"][i])

# dados da tabela usando listas
tabelaLista = [
    ["F","H", 5],
    ["M","M", 8],
    ["F","P", 8],
    ["F","H", 6],
    ["M","C", 5],
    ["M","H", 6],
    ["F","M", 8],
    ["F","P", 4],
    ["F","H", 2],
    ["M","C", 6],
    ["F","P", 8]
]

# dados da tabela usando dicionario 
tabelaDicionario = {
    "sexo":         ["F","M","F","F","M","M","F","F","F","M","F"],
    "predileta":    ["H","M","P","H","C","H","M","P","H","C","P"],
    "nota":         [5,8,8,6,5,6,8,4,2,6,8]
}
   
mostraLista(tabelaLista)
mostraDicionario(tabelaDicionario)

''' 
b) implemente uma função que permita adicionar 3 pontos à nota, desde que ela não ultrapasse a
nota 10. '''

# add tres pontos a nota - Listas
def adicionaTresPotosLista(lista):
     for linha in lista:
        
        # verifica se ultrapassa dez pontos
        if(linha[2] <= 7):
            linha[2] += 3

# add tres pontos a nota - Dicionario
def adicionaTresPotosDicionario(dicionario):
    for i in range(11):

        # verifica se ultrapassa dez pontos
        if(dicionario["nota"][i] <= 7):
            dicionario["nota"][i] += 3

adicionaTresPotosLista(tabelaLista)
adicionaTresPotosDicionario(tabelaDicionario)

print("\n\n")
print("Agora, adicionamos tres pontos a nota...")
mostraLista(tabelaLista)
mostraDicionario(tabelaDicionario)


'''
c) com base nos dados da tabela, construa uma função que retorne um ranking das disciplinas
prediletas. '''

def rankDisciplinasLista(lista):
    from operator import itemgetter
    disciplinasPrediletas = []

    # cria lista so com disciplinas
    disciplinas = []
    for i in range(len(lista)):
        disciplinas.append(lista[i][1])

    # retira as disciplinas repetidas 
    disciplinas = set(disciplinas)
    
    # verifica quantas vezes a disciplina aparece na tabela
    for disciplina in disciplinas:
        qtdDisciplinas = 0
        for i in range(len(lista)):
            if(disciplina == lista[i][1]):
                qtdDisciplinas += 1

        # adc cada disciplina e quantidade
        disciplinasPrediletas.append([disciplina,qtdDisciplinas])
    
    # ordem decrescente das disciplinas prediletas
    listaRank = sorted(disciplinasPrediletas, key=itemgetter(1), reverse=True)
    
    
    print("\n")
    print("-"*4, "Usando Lista", "-"*4)
    print("Rank  Predileta  Quantidade")
    posicaoRank = 1
    for linha in listaRank:
        print(" ",posicaoRank, " "*5, linha[0], " "*8, linha[1])
        posicaoRank += 1

def rankDisciplinasDicionario(dicionario):
    from operator import itemgetter
    disciplinasPrediletas = {}

    # cria dicionario so com disciplinas
    disciplinas = set(dicionario["predileta"])

    # verifica quantas vezes a disciplina aparece na tabela
    for disciplina in disciplinas:
        qtdDisciplinas = 0
        for i in range(len(dicionario["predileta"])):
            if(disciplina == dicionario["predileta"][i]):
                qtdDisciplinas += 1

        disciplinasPrediletas.update({disciplina:qtdDisciplinas})

    # ordem decrescente das disciplinas prediletas
    listaRank = sorted(disciplinasPrediletas.items(), key=itemgetter(1), reverse=True)

    print("\n")
    print("-"*4, "Usando Dicionario", "-"*4)
    print("Rank  Predileta  Quantidade")
    posicaoRank = 1
    for linha in listaRank:
        print(" ",posicaoRank, " "*5, linha[0], " "*8, linha[1])
        posicaoRank += 1
    

print("\n\nDisciplinas ordenadas no ranking de favoritas")      
rankDisciplinasLista(tabelaLista)
rankDisciplinasDicionario(tabelaDicionario)