from collections import deque

def bfs(labirinto, inicio):
    fila = deque([inicio])
    visitados = set([inicio])
    caminho = {inicio: None}
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while fila:
        x, y = fila.popleft()
        if labirinto[x][y] == 'o':
            return reconstruir_caminho(caminho, inicio, (x, y))
        
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]) and labirinto[nx][ny] != '#' and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                fila.append((nx, ny))
                caminho[(nx, ny)] = (x, y)
    return None

def reconstruir_caminho(caminho, inicio, fim):
    passo = fim
    rota = []
    while passo != inicio:
        rota.append(passo)
        passo = caminho[passo]
    rota.reverse()
    return rota

def main():
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'o', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', 'o', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    inicio = None
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 'P':
                inicio = (i, j)
                labirinto[i][j] = '.' 

    primeiro_caminho = bfs(labirinto, inicio)

    if primeiro_caminho:
        ultima_posicao = primeiro_caminho[-1]
        labirinto[ultima_posicao[0]][ultima_posicao[1]] = '#'
        segundo_caminho = bfs(labirinto, ultima_posicao)

    print("Primeiro caminho até a bolinha maior:", primeiro_caminho)
    print("Segundo caminho até a próxima bolinha maior:", segundo_caminho)

if __name__ == "__main__":
    main()
