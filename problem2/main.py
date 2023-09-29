def primeX(x):
    if x == 1:
        return 2
    prima = []
    bil = 3
    while len(prima) < x:
        if (bil == 3):
            prima.append(bil)
            bil += 2
        else:
            cek_prima = True
            for el in prima:
                if bil % el == 0:
                    cek_prima = False
                    break
            if cek_prima:
                prima.append(bil)
            bil += 2
    return prima[x - 2]

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29
