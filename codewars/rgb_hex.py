def rgb(r, g, b):
    ans = []
    hex = [r,g,b]
    rgb_hex = {10:'A', 11:'B', 12:'C', 13:'D', 14: 'E', 15:'F'}
    convert = []

    for x in hex:
        if x >= 0:
            if x > 255:
                x = 255
            first = x//16
            second = (x%16)
            ans.append(first)
            ans.append(second)
        elif x < 0:
            ans.append(0)
            ans.append(0)

    for x in range(len(ans)):
        if ans[x] in rgb_hex:
            hex = ans[x]
            convert.append(rgb_hex[hex])
        else:
            convert.append(str(ans[x]))
    convert = ''.join(convert)
    return convert


rgb(0,0,0),
# "000000", "testing zero values")
rgb(1,2,3)
#"010203", "testing near zero values")
rgb(255,255,255)
# "FFFFFF", "testing max values")
rgb(254,253,252)
#, "FEFDFC", "testing near max values")
rgb(-20,275,125)
#"00FF7D", "testing out of range values")
