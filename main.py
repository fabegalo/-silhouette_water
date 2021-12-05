import drawner

def get_water_silhouette(silhouettes):
    tamanho = len(silhouettes)

    parede_esquerda = [0]*tamanho
    parede_direita = [0]*tamanho
    agua_acumulada = [0]*tamanho

    for indice in range(0, tamanho):
        if indice != 0: #indice diferente de primeiro
            parede_esquerda[indice]=max(silhouettes[:indice]) #VALOR MAIS ALTO DA ESQUERDA!

        if indice != tamanho-1: #indice diferente de ultimo
            parede_direita[indice]=max(silhouettes[indice+1:tamanho]) #VALOR MAIS ALTO DA DIREITA!

        agua = min(parede_esquerda[indice], parede_direita[indice]) - silhouettes[indice]

        if agua >= 1:
            agua_acumulada[indice] = agua
        else:
            agua_acumulada[indice] = 0

    return agua_acumulada

f = open('entrada.txt', 'r')

entrada = f.read().splitlines()

qtdEntrada = entrada[0]

silhouettes = []
resultados  = []

x = 2

for i in range(0, int(qtdEntrada)):
    silhouettes.append(list(map(int, entrada[x].split(" "))))
    resultados.append(get_water_silhouette(list(map(int, entrada[x].split(" ")))))  
    x+=2

print(resultados)

drawner.draw_silhouette(silhouettes, resultados)