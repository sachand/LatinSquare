def _is_valid_line(l, N):
    return sorted(l) == [i+1 for i in range(N)]

'''
Checks if given `square` is a completed latin square of size `N`
'''
def is_latin_square(square, N):
    # Check all cells are valid:
    for i in range(N):
        for j in range(N):
            if square[i][j] < 1 or square[i][j] > N:
                print('f1')
                return False

    # Check rows are fine
    for i in range(N):
        if not _is_valid_line(square[i], N):
            print('f2' + str(i))
            return False

    # Check cols are fine
    for j in range(N):
        if not _is_valid_line([square[i][j] for i in range(N)], N):
            print('f3' + str(j))
            return False

    return True

'''
Checks if given complete latin square `csquare` of size `N` is derivable from partial
latin square `psquare`
'''
def is_latin_square_completion(psquare, csquare, N):
    for i in range(N):
        for j in range(N):
            if psquare[i][j] > 0 and csquare[i][j] != psquare[i][j]:
                print('Mismatch at ' + str((i, j)))
                return False
    return True
