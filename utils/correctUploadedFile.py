

def isCorrectUploadedFile(matrix):
    try:
        row = len(matrix)
        if (row < 2):
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] != matrix[j][i]):
                    return False
                if ((i == j) and (matrix[i][j] != 0)):
                    return False
        return True
    except:
        return False