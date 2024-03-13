import collections as collection
def sudoku(array):
    rows = collection.defaultdict(set)
    cols = collection.defaultdict(set)
    sub = collection.defaultdict(set)

    for i in range(len(array)):
        for j in range(len(array[0])):
            num = array[i][j]
            if num == None:
                continue
            if num in rows[i] or num in cols[j] or num in sub[i//3,j//3]:
                return False
            rows[i].add(num)
            cols[j].add(num)
            sub[i//3,j//3].add(num)
    return True

if __name__ == '__main__':
    array = [
        [1,2],
        [3,4],
        [5,6],
        [7,8]]
    print(sudoku(array))
