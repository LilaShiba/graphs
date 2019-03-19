# https://www.youtube.com/watch?v=L5Dsxtl4iIo
def encode_rail_fence_cipher(string, n):
    count = 0
    down = True
    ans = []

    # create 2d list to hold rail lvl chars
    for x in range(n):
        ans.append('')

    for x in string:
        if down:
            ans[count]= ans[count] + x
            count +=1
            if count == n-1:
                down = False
        else:
            ans[count] = ans[count] + x
            count -= 1
            if count == 0:
                down = True
    print(ans)
    ans = ''.join(ans)
    print(ans)

def decode_rail_fence_cipher(string, n):
    result = ''
    matrix = [['' for x in range(len(string))]for u in range(n)]
    idx = 0
    increment = 1

    for selectedRow in range(0,len(matrix)):
        row = 0
        for col in range(0,len(matrix[row])):
            # if outside bounds swith increment
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1

            if row == selectedRow:
                matrix[row][col] += string[idx]
                idx += 1

            row += increment
    matrix = transpose(matrix)
    for row in matrix:
        result += ''.join(row)
    print(result)
    return result


def transpose(m):
    result = [[ 0 for y in range(len(m))]for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result




#encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)
# "WECRLTEERDSOEEFEAOCAIVDEN"
#  WECRLTEERDSOEEFEAOCAIVDEN
#encode_rail_fence_cipher("Hello, World!", 3)
# "Hoo!el,Wrdl l"
#  Hoo!el,Wrdl l

#encode_rail_fence_cipher("Hello, World!", 4)
# "H !e,Wdloollr"
#  H !e,Wdloollr

#encode_rail_fence_cipher("", 3)
#""



decode_rail_fence_cipher("H !e,Wdloollr", 4)
#  H !e,Wdloollr
# decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3)
# # "WEAREDISCOVEREDFLEEATONCE")
# decode_rail_fence_cipher("", 3)
#""
