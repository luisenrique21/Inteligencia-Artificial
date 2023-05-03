import ChessIA as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    #Movimiento del Jugador
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""Para deshacer tu ultimo movimiento, escribe "undo".""")
            #Obtener los movimientos y deshacer
            play = input("Tu movimiento: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #Movimiento de la IA
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    #Iniciar el juego
    def startGame(self):
        #Color del jugador
        color=None
        while(color!="b" and color!="w"):
            color = input("""Jugar con (Escribe "b" o "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Elige la profundidad de la IA: """))
        if color=="b":
            #Verifica que no es hacke mate y entra
            while (self.board.is_checkmate()==False):
                print("La ia esta pensando...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())    
        elif color=="w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("La ia esta pensando...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #reinicia el tablero
        self.board.reset
        #Inicia otro juego
        self.startGame()

#Crea una instancia e inicia otro juego
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()
