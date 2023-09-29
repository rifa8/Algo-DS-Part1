def max_sequence(arr):
    list_jml = []
    for i in range(2, len(arr) + 1):
        for j in range(len(arr) - i + 1):
            jml = sum(arr[j:j + i])
            list_jml.append(jml)
    return max(list_jml)

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12
