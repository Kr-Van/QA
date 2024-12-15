def transpose(Matrix):
    rows, columns = len(Matrix), len(Matrix[0])
    Res = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(rows):
        for j in range(columns):
            Res[j][i] = Matrix[i][j]
    return Res

File = open("input.txt")
A = File.readlines()
for i in range(len(A)):
    A[i] = A[i][:-1].split()

A_trans = transpose(A)
for a in A_trans:
    print(*a)
