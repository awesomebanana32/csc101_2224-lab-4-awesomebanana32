import driver

string_pattern = '''
SSSSSSSSSS
SSSSSSSSSS
SSSMMMMSSS
SSSMMMMSSS
SSSMMMMSSS
SSSSSSSSSS
SSSSSSSSSS
'''


# Determines the appropriate letter for the intended pattern based
# on the row (top to bottom) and column (left to right) positions
# within that pattern.
#
# input: row as int
# input: column as int
# result: single character as str
def compute_letter(row: int, column: int) -> str:
    if (row > 1 and row < 5 and column > 2 and column < 7):
        return 'M'
    else:
        # complete this function
        return 'S'

if __name__ == '__main__':
    driver.compare_patterns(string_pattern, compute_letter)
