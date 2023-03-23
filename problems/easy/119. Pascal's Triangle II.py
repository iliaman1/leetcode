from typing import List


def generate(rowIndex: int) -> List[int]:
    current_row = [1]
    for _ in range(rowIndex):
        tmp_row = [1]
        for i in range(len(current_row)-1):
            tmp_row.append(current_row[i] + current_row[i+1])
        tmp_row.append(1)
        current_row = tmp_row[:]
    return current_row


#recursion
# def generate(rowIndex: int) -> List[int]:
#     if rowIndex == 0:
#         return [1]
#     prevRow = getRow(rowIndex - 1)
#     currentRow = [1]
#     for i in range(len(prevRow) - 1):
#         currentRow.append(prevRow[i] + prevRow[i + 1])
#     currentRow.append(1)
#     return currentRow
