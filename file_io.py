
def get_file_columns(file_name, col_nums):
    print('Nothing')
    cols = []

    for l in open(file_name, encoding = "ISO-8859-1"):
        A = l.rstrip().split()
        col = []
        for i in col_nums:
            col.append(A[i])
        cols.append(col)
    return cols
