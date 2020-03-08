test = int(input())
for x in range(test):
    tiempos = list(map(int, input().split()))
    hora1 = tiempos[0] * 60 + tiempos[1]
    hora2 = tiempos[2] * 60 + tiempos[3]
    nHora = (hora2 - hora1) / 60
    nuevaHora = int(nHora)
    minutos = int(round((nHora - nuevaHora) * 60))
    print(nuevaHora, minutos)