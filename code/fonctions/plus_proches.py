def tour_pieces_plus_proches(list, key):
    piece_valeur_min = min(list, key=key)
    return [piece for piece in list if key(piece) == key(piece_valeur_min)]


def fou_pieces_plus_proches(list, key):
    piece_valeur_min = min(list, key=key)
    return [piece for piece in list if key(piece) == key(piece_valeur_min)]