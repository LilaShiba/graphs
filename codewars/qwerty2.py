def encrypt(s, shift):
    shift = str(shift)
    shift_lvl = len(shift)
    # get correct shift levels
    if shift_lvl == 2:
        shift = '0'+shift
    elif shift_lvl < 2:
        shift = '00'+shift
    # 2D array
    d = [list('qwertyuiop'),list("asdfghjkl"),list("zxcvbnm,."), list('qwertyuiop'.upper()), list("asdfghjkl".upper()),list("zxcvbnm,.".upper())]
    ans = []

    count = 0
    while s:
        if x in d[count]:
            new_letter = d[count].index(x) + int(shift[count])
            
