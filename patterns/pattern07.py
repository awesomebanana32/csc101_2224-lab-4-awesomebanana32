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
    # complete this function
    # ** tip ** Think of this as rectangles overlapping (such as cloth stacked)
    # and work from the "top" to the "bottom"
    return 'X'


if __name__ == '__main__':
    driver.compare_patterns(string_pattern, compute_letter)
