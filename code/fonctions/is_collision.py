def is_collision(list_pieces, pos_initial, pos_final):
    for piece in list_pieces:
        if piece.position == pos_final and pos_initial != piece.position:
            return piece