def pascal_triangle(n):
    '''
    Function for the triangle
    '''
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        res = [[1]]
        for i in range(n - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

a = pascal_triangle(5)
print(a)