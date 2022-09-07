# bitboard functions exist here.

def chararr_to_bitarr(arr:list)->list:
    r = []
    if(len(arr) != 64):
            print('Length specified is not equal to a chess bitboard array.')
            return
    for x in arr:
        if(x == 'e'):
            r.append(0)
        else:
            r.append(1)

    return r