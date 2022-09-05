# individual sets of pieces are stored in these bitboards 

board = [

    'R','N','B','Q','K','B','N','R', # black is represented by upper case
    'P','P','P','P','P','P','P','P',
    'e','e','e','e','e','e','e','e',
    'e','e','e','e','e','e','e','e',
    'e','e','e','e','e','e','e','e',
    'e','e','e','e','e','e','e','e',
    'p','p','p','p','p','p','p','p',
    'r','n','b','q','k','b','n','r', # white is represented by lower case

]

piece_index = {

    'p' : 0,
    'r' : 1,
    'n' : 2,
    'b' : 3,
    'q' : 4,
    'k' : 5,
    'P' : 6,
    'R' : 7,
    'N' : 8,
    'B' : 9,
    'Q' : 10,
    'K' : 11,

}

print(piece_index.keys())

def generate_bitboard(piece)->list:

    arr = []

    for x in board:
        if (x == piece):
            for p in range(len(piece_index)):
                if(piece == piece_index.items()[p]):
                    arr.append(piece_index.keys()[p])
        else:
            arr.append(0)

    return arr

w_pawn = generate_bitboard('p')

w_rook = generate_bitboard('r')

w_knight = generate_bitboard('n')

w_bishop = generate_bitboard('b')

w_queen = generate_bitboard('q')

w_king = generate_bitboard('k')

b_pawn = generate_bitboard('P')

b_rook = generate_bitboard('R')

b_knight = generate_bitboard('N')

b_bishop = generate_bitboard('B')

b_queen = generate_bitboard('Q')

b_king = generate_bitboard('K')

# mask is used for avoiding irregular placement of the pawns

mask = [

    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,
    0,0,0,0,0,0,0,1,

]

print(w_pawn)

# bit boards without mask

barray_wo_mask = [w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook]

# bit boards without mask

barray_w_mask = [w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_bishop,b_king,b_knight,b_pawn,b_queen,b_rook,mask]