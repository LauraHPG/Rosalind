def  rabbitsRecurrence(n,k):
    if n == 1: 
        return 0, 1
    else:
        adults, children = rabbitsRecurrence(n - 1, k)
        return adults + children, adults*k

n_input = input("n: ")
k_input = input("k: ")
res_adults, res_children = rabbitsRecurrence(int(n_input), int(k_input))
print(res_adults + res_children)

