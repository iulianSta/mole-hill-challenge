S = 16
answer = 0
L = ' '* S

for i in range(S):
    L, L0 = input(), L
    inside = False
    for j,c in enumerate(L):
        if c =='|' or (c =='+' and L0[j] in '|+'): inside = not inside
        elif c =='o' and inside: answer += 1
print(answer)