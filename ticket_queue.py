

T = [5, 2, 7, 8, 3, 9, 4, 2]
S = [6, 3, 10, 12, 8, 8, 6]

def recursive(i):
    if i == 0: 
        return T[0];
    if i == 1:
        return min(T[0] + T[1], S[0])
    
    return min(recursive(i - 1) + T[i], recursive(i - 2) + S[i - 1])


print(recursive(len(T) - 1))


def dynamic():
    x, y = 0, T[0]
    for i in range(1, len(T)):
        x, y = y, min(y + T[i], x + S[i - 1])
    
    return y
    
print(dynamic())
