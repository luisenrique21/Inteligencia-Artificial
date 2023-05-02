import numpy as np


# Función de utilidad
def utility(state):
    for i in range(3):
        if state[i, :].sum() == 3 or state[:, i].sum() == 3:
            return 1.0
        elif state[i, :].sum() == -3 or state[:, i].sum() == -3:
            return -1.0
    if state.trace() == 3 or np.fliplr(state).trace() == 3:
        return 1.0
    elif state.trace() == -3 or np.fliplr(state).trace() == -3:
        return -1.0
    elif np.count_nonzero(state) == 9:
        return 0.0
    else:
        return None


# Función de generación de sucesores
def successors(state, player):
    succ = []
    for i in range(3):
        for j in range(3):
            if state[i, j] == 0:
                s = state.copy()
                s[i, j] = player
                succ.append(s)
    return succ


# Función Minimax con poda alfa-beta
def alphabeta(state, player, depth, alpha, beta):
    u = utility(state)
    if u is not None or depth == 0:
        return u or 0.0, None
    if player == 1:
        best_value = -np.inf
        best_move = None
        for s in successors(state, 1):
            v, _ = alphabeta(s, -1, depth - 1, alpha, beta)
            if v > best_value:
                best_value = v
                best_move = s
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    else:
        best_value = np.inf
        best_move = None
        for s in successors(state, -1):
            v, _ = alphabeta(s, 1, depth - 1, alpha, beta)
            if v < best_value:
                best_value = v
                best_move = s
            beta = min(beta, v)
            if alpha >= beta:
                break
    return best_value, best_move


# Función para imprimir el tablero
def print_board(state):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            if state[i, j] == 1:
                print(" X ", end="")
            elif state[i, j] == -1:
                print(" O ", end="")
            else:
                print("   ", end="")
            print("|", end="")
        print("\n-------------")


# Estado inicial del juego
# Estado inicial del juego
state = np.zeros((3,3), dtype=int)
player = 1

# Profundidad máxima de búsqueda
max_depth = 1

# Poda alfa-beta
def alphabeta(state, player, depth, alpha, beta):
    u = utility(state)
    if u is not None or depth == 0:
        return u or 0.0, None
    if player == 1:
        best_value = -np.inf
        best_move = None
        for s in successors(state, 1):
            v, _ = alphabeta(s, -1, depth - 1, alpha, beta)
            if v > best_value:
                best_value = v
                best_move = s
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:
        best_value = np.inf
        best_move = None
        for s in successors(state, -1):
            v, _ = alphabeta(s, 1, depth - 1, alpha, beta)
            if v < best_value:
                best_value = v
                best_move = s
            beta = min(beta, best_value)
            if beta <= alpha:
                break
    return best_value, best_move

# Bucle del juego
while True:
    # Imprimir el tablero
    print_board(state)
    # Si es el turno del usuario
    if player == 1:
        row = int(input("Ingrese la fila (1-3): ")) - 1
        col = int(input("Ingrese la columna (1-3): ")) - 1
        # Verificar que la casilla esté vacía
        if state[row, col] != 0:
            print("La casilla ya está ocupada. Intente de nuevo.")
            continue
        state[row, col] = player
    # Si es el turno de la computadora
    else:
        print("Es el turno de la computadora...")
        _, state = alphabeta(state, -1, max_depth, -np.inf, np.inf)
    # Verificar si el juego ha terminado
    u = utility(state)
    if u is not None:
        print_board(state)
        if u == 1:
            print("¡Felicidades! ¡Ganaste!")
        elif u == -1:
            print("Lo siento, perdiste.")
        else:
            print("Empate.")
        break
    # Cambiar el jugador
    player = -player


