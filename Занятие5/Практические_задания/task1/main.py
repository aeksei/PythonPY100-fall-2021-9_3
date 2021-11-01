

if __name__ == "__main__":
    matrix = [
        [i * j for j in range(1, 11)]
        for i in range(1, 11)
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value_ceil = matrix[row][col]
            print(f"{value_ceil:3}", end="\t")
        print()
