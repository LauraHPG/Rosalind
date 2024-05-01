n_in = int(input("n: "))
m_in = int(input("m: "))

small = [-1]*n_in
adult = [-1]*n_in


adult[0] = 0
small[0] = 1

def mortalRabbits(n):
    if n < 0:
        return 0,0
    
    if small[n] == -1:

        a1, s1 = mortalRabbits(n-1)
        _, sm = mortalRabbits(n-m_in)

        small[n] = a1
        adult[n] = s1 + a1 - sm
        
    
    return adult[n], small[n]

adults, children = mortalRabbits(n_in-1)
print(adults + children)
    