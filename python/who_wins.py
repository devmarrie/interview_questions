def wins(n, k):
    start = 1
    sam = []
    alex = []
    for i in n:
        print(f'before {i}')
        if i > k:
            i -= k
        else:
            i = k
        while i:
            print(f'after {i}')
            if start % 2 == 0:
               alex.append(k)
               start += 1
               break
            else:
               sam.append(k)
               start += 1
    print(f'sam - {sam}, alex - {alex}')
    if len(sam) > len(alex):
        print ("Sam wins")
    else:
        print ("Alex wins")
if __name__ == "__main__":
    wins([3,5,7], 2)
