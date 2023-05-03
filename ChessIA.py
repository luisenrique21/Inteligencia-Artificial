import chess as ch
import random as rd

class Engine:

    def __init__(self, board, maxDepth, color):
        self.board=board
        self.color=color
        self.maxDepth=maxDepth
    
    def getBestMove(self):
        return self.engine(None, 1)

    def evalFunct(self):
        compt = 0
        #resume los valores materiales
        for i in range(64):
            compt+=self.squareResPoints(ch.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.001*rd.random()
        return compt

    def mateOpportunity(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    #Piensa el primer movimiento
    def openning(self):
        if (self.board.fullmove_number<10):
            if (self.board.turn == self.color):
                return 1/30 * self.board.legal_moves.count()
            else:
                return -1/30 * self.board.legal_moves.count()
        else:
            return 0

    #Da un valor a las piezas
    def squareResPoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue

        
    def engine(self, candidate, depth):
        
        #Alcanzó la profudidad máxima o no hay movimientos posibles
        if ( depth == self.maxDepth
        or self.board.legal_moves.count() == 0):
            return self.evalFunct()
        
        else:
            #obtener una lista de movimientos legales de la posición actual
            moveListe = list(self.board.legal_moves)
            
            #inicializar el nuevo Candidato
            newCandidate = None
            if(depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")
            
            #Analiza el tablero después de los movimientos
            for i in moveListe:

                #Play move i
                self.board.push(i)

                #Obtiene el valor del movimiento i (explora las repercursiones)
                value = self.engine(newCandidate, depth + 1) 

                #Basico alogritmo de  minmax:
                #Si maximiza (turno de la IA)
                if(value > newCandidate and depth % 2 != 0):
                    #necesita guardar el movimiento jugado por la IA
                    if (depth == 1):
                        move=i
                    newCandidate = value
                #Si minimiza (turno del jugador)
                elif(value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                #Alpha-beta cortes(poda): 
                #(si la IA realizó el movimiento anterior)
                if (candidate != None
                 and value < candidate
                 and depth % 2 == 0):
                    self.board.pop()
                    break
                #(si el jugador realizó el movimiento anterior)
                elif (candidate != None 
                and value > candidate 
                and depth % 2 != 0):
                    self.board.pop()
                    break
                
                #deshacer el último movimiento
                self.board.pop()

            #Return result
            if (depth>1):
                #valor de retorno de un movimiento en el árbol
                return newCandidate
            else:
                #retotna el movimiento (solo en el primer movimiento)
                return move



  



            
            


        


        



            






        
        




        




    
    
