
def get_file_columns(file_name, col_nums):
    cols = []

    for l in open(file_name):
        A = l.rstrip().split()
        col = []
        for i in col_nums:
            col.append(A[i])
        cols.append(col)
    return cols
