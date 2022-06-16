a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

prod_ac= a * c
step = int(prod_ac / abs(prod_ac))
factors = []

for i in range(0, int(prod_ac / 2) + step, step):
    if not(i) or (prod_ac % i): continue
    factors.append([i, int(prod_ac / i)])
print(factors)

def search(i, j):
    if (i + j) == b: return ([i, j])
    if (i - j) == b and (i * -j) == prod_ac: return ([i, -j])
    if (-i - j) == b: return ([-i, -j])
    if (-i + j) == b and (-i * j) == prod_ac: return ([-i, j])
    return None;
        
two_factors = []
for [i, j] in factors:
    two_factors = search(i, j)
    if two_factors: break
        
print(two_factors)