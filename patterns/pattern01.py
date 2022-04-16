import driver

string_pattern = '''
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGZGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGGGG
'''


# Determines the appropriate letter for the intended pattern based
# on the row (top to bottom) and column (left to right) positions
# within that pattern.
#
# input: row as int
# input: column as int
# result: single character as str
def compute_letter(row: int, column: int) -> str:
    # complete this function
    return 'X'


if __name__ == '__main__':
    driver.compare_patterns(string_pattern, compute_letter)
