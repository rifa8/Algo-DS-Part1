def fibonacci(number):
    fibo_num = [0, 1]
    idx = 2
    nxt_num = 0
    while len(fibo_num) < number + 1:
        nxt_num += fibo_num[idx-1] + fibo_num[idx-2]
        fibo_num.append(nxt_num)
        nxt_num = 0
        idx += 1
    return fibo_num[number]

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144
