def add_matrices_version_1(m1, m2):
    result = []
    for row_i in range(len(m1)):
        row = []
        for col_i in range(len(m1[row_i])):
            element = m1[row_i][col_i] + m2[row_i][col_i]
            row.append(element)
        result.append(row)
    return result


def add_matrices_version_2(m1, m2):
    result = []
    for row_m1, row_m2 in zip(m1, m2):
        row = []
        for ele_m1, ele_m2 in zip(row_m1, row_m2):
            row.append(ele_m1 + ele_m2)
        result.append(row)
    return result


def add_matrices(m1, m2):
    return [[ele_m1 + ele_m2 for ele_m1, ele_m2 in zip(row_m1, row_m2)] for row_m1, row_m2 in zip(m1, m2)]
