import driver

string_pattern = '''
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTZZZZZZTTTTTTTTTT
TTTTZZZZZZTTTTTTTTTT
TTTTZZZXXXBBBTTTTTTT
TTTTZZZXXXBBBTTTTTTT
TTTTTTTBBBBBBTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
TTTTTTTTTTTTTTTTTTTT
'''


# Determines the appropriate letter for the intended pattern based
# on the row (top to bottom) and column (left to right) positions
# within that pattern.
#
# input: row as int
# input: column as int
# result: single character as str
def compute_letter(row: int, column: int) -> str:

    if (row >= 2  and row <= 3 and column >= 4 and column <= 9):
        return 'Z'
    elif (row >= 4 and row <= 5 and column >= 4 and column <= 6):
        return 'Z'
    elif (row >= 4 and row <= 5 and column >= 7 and column <= 9):
        return 'X'
    elif (row >= 4 and row <= 5 and column >= 10 and column <= 12):
        return 'B'
    elif (row == 6 and column >= 7 and column <= 12):
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    driver.compare_patterns(string_pattern, compute_letter)
