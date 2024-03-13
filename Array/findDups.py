# find dups from 1D array
# find dups from 2d array
# find dups in row in 1D
# Find dups in row in 2D
import collections


def dupsInRow(array):
    # Initialize a dictionary to keep sets for each row
    row_sets = {}


    for i in range(len(array)):
        row_sets[i] = set()  # Initialize a new set for each row

        for j in range(len(array[i])):  # Ensure it works for non-uniform row lengths
            if array[i][j] in row_sets[i]:
                return [array[i][j], True]  # Return the duplicate value and True
            else:
                row_sets[i].add(array[i][j])
    return False  # No duplicates found

def dupsInColumn(array):
    if not array or not array[0]:
        return False  # Return False if the array is empty or the first row is empty

    column_sets = {}  # Dictionary to keep track of sets for each column
    numRows = len(array)
    numColumns = len(array[0])

    for i in range(numColumns):
        column_sets[i] = set()  # Correctly initialize a new set for each column outside the inner loop

        for j in range(numRows):
            if array[j][i] in column_sets[i]:
                return [array[j][i], True]  # Return the duplicate value and True if found
            else:
                column_sets[i].add(array[j][i])
    return False  # No duplicates found


def checkDupsInRowsAndColumns(array):

    row_sets = collections.defaultdict(set)
    column_sets = collections.defaultdict(set)
    result = []  # Use a list to store details about duplicates

    for i in range(len(array)):
        for j in range(len(array[0])):
            # Check for duplicates in the current row
            if array[i][j] in row_sets[i]:
                result.append(('row',array[i][j]))  # Append details as a tuple
            else:
                row_sets[i].add(array[i][j])

            # Check for duplicates in the current column
            if array[i][j] in column_sets[j]:
                result.append(('column', array[i][j]))  # Append details as a tuple
            else:
                column_sets[j].add(array[i][j])

    if result:
        return True, result  # Return True and the list of duplicates if found
    else:
        return False, []  # Return False with an empty list if no duplicates are found



def checkDupsIn2Darray(array):
    #     array = [[1,2],
    #             [2,3],
    #             [3,2]]
    #
    #     list = set()
    #                                             list = 1, 2
    # is 1 in the list? No -- add to the list
    # is 2 in the lilst? No -- add 2 to the list
    # is 2 in the list? Yes    return False
    list = set()

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] in list:
                return [array[i][j], True]
            else:
                list.add(array[i][j])
    return False





if __name__ == '__main__':
    array = [[1,2],
            [6,2],
            [3,3]]

    result = checkDupsIn2Darray(array)
    if result:
        message = 'Duplicate found: {}. There are duplicates.'.format(result[0])
    else:
        message = 'No duplicates found.'
    print(message)

    result = dupsInRow(array)
    if result:
        message = 'Duplicate row found: {}. There are duplicates.'.format(result[0])
    else:
        message = 'No duplicates row found.'
    print(message)




    result = dupsInColumn(array)
    if result:
        message = 'Duplicate column found: {}. There are duplicates.'.format(result[0])
    else:
        message = 'No duplicates cols found.'
    print(message)


    result = checkDupsInRowsAndColumns(array)
    if result:
        message = 'Duplicate rows and column found: {}. There are duplicates.'.format(result)
    else:
        message = 'No duplicates rows and cols found.'
    print(message)


