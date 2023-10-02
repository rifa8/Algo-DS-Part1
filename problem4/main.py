def generate_primes_grid(width, height, start):
    prima = []
    grid = []
    bil = 1
    while len(grid) < width * height:
        if bil == 1:
            bil += 1
        elif bil == 2:
            prima.append(bil)
            bil +=1
        else:
            cek_prima = True
            for el in prima:
                if bil % el == 0:
                    cek_prima = False
                    break
            if cek_prima:
                prima.append(bil)
            bil += 2
        for el in prima:
            if el > start and el not in grid:
                grid.append(el)

    output = ''
    for idx, num in enumerate(grid):
        if num < 10 and idx > 0:
            output += ' '
        output += str(num)
        if (idx + 1) % width != 0:
            output += ' '
        if (idx + 1) % width == 0:
            output += '\n'  
    return output
    

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """
