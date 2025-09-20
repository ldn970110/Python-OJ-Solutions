try:
    while True:
        r, c = map(int, input().split())

        matrix_input = []
        for _ in range(r):
            matrix_input.append(list(map(int, input().split())))

        matrix_output = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(r):
            for j in range(c):
                matrix_output[j][i] = matrix_input[i][j]

        for row in matrix_output:
            print(*row)

except EOFError:
    pass