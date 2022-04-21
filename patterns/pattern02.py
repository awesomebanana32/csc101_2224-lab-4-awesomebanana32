import driver

string_pattern = '''
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRR
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
QQQQQQQQQQQQQQQQQQQQ
'''


# Determines the appropriate letter for the intended pattern based
# on the row (top to bottom) and column (left to right) positions
# within that pattern.
#
# input: row as int
# input: column as int
# result: single character as str
def compute_letter(row: int, column: int) -> str:
    if (row < 10):
        return 'R'
    else:
    # complete this function
        return 'Q'


if __name__ == '__main__':
    driver.compare_patterns(string_pattern, compute_letter)
