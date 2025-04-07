import math



def tour_is_mouvement_correct(list_pieces, pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)

    if pos_initial[0] == pos_final_rounded[0]:
        list_piece_same_x = list(filter(lambda piece: piece.position[0] == pos_initial[0] and piece.position[1] != pos_initial[1], list_pieces))
        if list_piece_same_x:
            for piece in list_piece_same_x:
                if piece.position[1]  > pos_initial[1]:
                    if pos_final_rounded[1] > piece.position[1] :
                        return None
                elif piece.position[1]  < pos_initial[1]:
                    if pos_final_rounded[1] < piece.position[1] :
                        return None
            return (pos_final_rounded[0], pos_final_rounded[1])
        else: 
            return (pos_final_rounded[0], pos_final_rounded[1])
        
    if pos_initial[1] == pos_final_rounded[1]:
        list_piece_same_y = list(filter(lambda piece: piece.position[1] == pos_initial[1] and piece.position[0] != pos_initial[0], list_pieces))
        if list_piece_same_y:
            for piece in list_piece_same_y:
                if piece.position[0]  > pos_initial[0]:
                    if pos_final_rounded[0] > piece.position[0] :
                        return None
                elif piece.position[0]  < pos_initial[0]:
                    if pos_final_rounded[0] < piece.position[0] :
                        return None
            return (pos_final_rounded[0], pos_final_rounded[1])
        else: 
            return (pos_final_rounded[0], pos_final_rounded[1])
        

def cavalier_is_mouvement_correct(pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)

    if pos_final_rounded[0] - pos_initial[0] == 200:
        if pos_final_rounded[1] - pos_initial[1] == 100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        if pos_final_rounded[1] - pos_initial[1] == -100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        
    if pos_final_rounded[0] - pos_initial[0] == -200:
        if pos_final_rounded[1] - pos_initial[1] == 100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        if pos_final_rounded[1] - pos_initial[1] == -100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        
    if pos_final_rounded[1] - pos_initial[1] == 200:
        if pos_final_rounded[0] - pos_initial[0] == 100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        if pos_final_rounded[0] - pos_initial[0] == -100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        
    if pos_final_rounded[1] - pos_initial[1] == -200:
        if pos_final_rounded[0] - pos_initial[0] == 100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        if pos_final_rounded[0] - pos_initial[0] == -100:
            return (pos_final_rounded[0] , pos_final_rounded[1] )
            

def fou_is_mouvement_correct(list_pieces, pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)

    if abs(pos_final_rounded[0] - pos_initial[0]) == abs(pos_final_rounded[1] - pos_initial[1]):
        pieces_same_diagonale = list(filter(lambda piece: abs(pos_initial[0] - piece.position[0] ) == abs(pos_initial[1] - piece.position[1] ), list_pieces))
        if pieces_same_diagonale:
            for piece in pieces_same_diagonale: 
                if piece.position[0]  > pos_initial[0] and piece.position[1]  < pos_initial[1]:
                    if piece.position[0]  < pos_final_rounded[0] and piece.position[1]  > pos_final_rounded[1]:
                        return None
                if piece.position[0]  > pos_initial[0] and piece.position[1]  > pos_initial[1]:
                    if piece.position[0]  < pos_final_rounded[0] and piece.position[1]  < pos_final_rounded[1]:
                        return None
                if piece.position[0]  < pos_initial[0] and piece.position[1]  < pos_initial[1]:
                    if piece.position[0]  > pos_final_rounded[0] and piece.position[1]  > pos_final_rounded[1]:
                        return None
                if piece.position[0]  < pos_initial[0] and piece.position[1]  > pos_initial[1]:
                    if piece.position[0]  > pos_final_rounded[0] and piece.position[1]  < pos_final_rounded[1]:
                        return None
            return (pos_final_rounded[0] , pos_final_rounded[1] )
        else:
            return (pos_final_rounded[0] , pos_final_rounded[1] )


def dame_is_mouvement_correct(list_pieces, pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)
    
    dx = abs(pos_final_rounded[0] - pos_initial[0])
    dy = abs(pos_final_rounded[1] - pos_initial[1])

    if dx == 0 or dy == 0 or dx == dy:

        if pos_initial[0] == pos_final_rounded[0]:
            list_piece_same_x = list(filter(lambda piece: piece.position[0]  == pos_initial[0] and piece.position[1]  != pos_initial[1], list_pieces))
            if list_piece_same_x:
                for piece in list_piece_same_x:
                    if piece.position[1]  > pos_initial[1]:
                        if pos_final_rounded[1] > piece.position[1] :
                            return None
                    elif piece.position[1]  < pos_initial[1]:
                        if pos_final_rounded[1] < piece.position[1] :
                            return None
                return (pos_final_rounded[0] , pos_final_rounded[1] )
            else: 
                return (pos_final_rounded[0] , pos_final_rounded[1] )
        
        if pos_initial[1] == pos_final_rounded[1]:
            list_piece_same_y = list(filter(lambda piece: piece.position[1]  == pos_initial[1] and piece.position[0]  != pos_initial[0], list_pieces))
            if list_piece_same_y:
                for piece in list_piece_same_y:
                    if piece.position[0]  > pos_initial[0]:
                        if pos_final_rounded[0] > piece.position[0] :
                            return None
                    elif piece.position[0]  < pos_initial[0]:
                        if pos_final_rounded[0] < piece.position[0] :
                            return None
                return (pos_final_rounded[0] , pos_final_rounded[1] )
            else: 
                return (pos_final_rounded[0] , pos_final_rounded[1] )
            
        if abs(pos_final_rounded[0] - pos_initial[0]) == abs(pos_final_rounded[1] - pos_initial[1]):
            pieces_same_diagonale = list(filter(lambda piece: abs(pos_initial[0] - piece.position[0] ) == abs(pos_initial[1] - piece.position[1] ), list_pieces))
            if pieces_same_diagonale:
                for piece in pieces_same_diagonale: 
                    if piece.position[0]  > pos_initial[0] and piece.position[1]  < pos_initial[1]:
                        if piece.position[0]  < pos_final_rounded[0] and piece.position[1]  > pos_final_rounded[1]:
                            return None
                    if piece.position[0]  > pos_initial[0] and piece.position[1]  > pos_initial[1]:
                        if piece.position[0]  < pos_final_rounded[0] and piece.position[1]  < pos_final_rounded[1]:
                            return None
                    if piece.position[0]  < pos_initial[0] and piece.position[1]  < pos_initial[1]:
                        if piece.position[0]  > pos_final_rounded[0] and piece.position[1]  > pos_final_rounded[1]:
                            return None
                    if piece.position[0]  < pos_initial[0] and piece.position[1]  > pos_initial[1]:
                        if piece.position[0]  > pos_final_rounded[0] and piece.position[1]  < pos_final_rounded[1]:
                            return None
                return (pos_final_rounded[0] , pos_final_rounded[1] )
            else:
                return (pos_final_rounded[0] , pos_final_rounded[1] )
            
        
def roi_is_mouvement_correct(pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)

    dx = abs(pos_final_rounded[0] - pos_initial[0])
    dy = abs(pos_final_rounded[1] - pos_initial[1])
    if dx <= 100 and dy <= 100:
        return (pos_final_rounded[0], pos_final_rounded[1])
    

def pion_is_mouvement_correct(list_pieces, piece_clicked, pos_initial, pos_final):
    pos_final_rounded = (math.floor(pos_final[0] / 100) * 100, math.floor(pos_final[1] / 100) * 100)

    if pos_initial[0] == pos_final_rounded[0]:
        if piece_clicked.color == "blanc":
            if pos_initial[1] - pos_final_rounded[1] == 200:
                if pos_initial[1] == 600:
                    return (pos_final_rounded[0], pos_final_rounded[1])
            elif pos_initial[1] - pos_final_rounded[1] == 100:
                return (pos_final_rounded[0], pos_final_rounded[1])
        elif piece_clicked.color == "noir":
            if pos_final_rounded[1] - pos_initial[1] == 200:
                if pos_initial[1] == 100:
                    return (pos_final_rounded[0], pos_final_rounded[1])
            elif pos_final_rounded[1] - pos_initial[1] == 100:
                return (pos_final_rounded[0], pos_final_rounded[1])
    
    dx = abs(pos_initial[0] - pos_final_rounded[0])
    dy = pos_initial[1] - pos_final_rounded[1]

    if piece_clicked.color == "blanc":
        if dx == dy and dx == 100:
            piece_collision = is_collision(list_pieces, piece_clicked, pos_initial, pos_final_rounded)
            if piece_clicked.color != piece_collision[0].color:
                return (pos_final_rounded[0], pos_final_rounded[1])
    elif piece_clicked.color == "noir":
        if dx == -dy and dx == 100:
            piece_collision = is_collision(list_pieces, piece_clicked, pos_initial, pos_final_rounded)
            if piece_collision:
                if piece_clicked.color != piece_collision[0].color:
                    return (pos_final_rounded[0], pos_final_rounded[1])




def is_collision(list_pieces, piece_clicked, pos_initial, pos_final):
    for piece in list_pieces:
        if piece.position == pos_final and pos_initial != piece.position:
            if piece.color != piece_clicked.color:
                return [piece]
            return [piece, pos_initial]


def a_qui_de_jouer(white_black):
    if white_black % 2 == 0:
        return "noir"
    elif white_black % 2 != 0:
        return "blanc"