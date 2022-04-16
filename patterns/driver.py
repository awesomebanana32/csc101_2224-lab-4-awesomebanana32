from typing import Callable
from typing import List


# Takes a desired pattern, computes a corresponding pattern using
# the provided function, and displays results of comparison between
# patterns.
#
# input: string_pattern as str
# input: compute_letter function to compute a letter as Callable[[int,int], str]
# result: None
def compare_patterns(string_pattern: str,
                     compute_letter: Callable[[int, int], str]):
    desired_pattern = list(map(list, string_pattern.split()))
    cols_list = [len(row) for row in desired_pattern]
    computed_pattern = build_pattern(len(desired_pattern), cols_list, compute_letter)
    display_results(desired_pattern, computed_pattern)


# Builds a pattern by calling the provided function for each row and column
# populating the two-dimensional list with the resulting letter.
#
# input: rows - the number of rows as an int
# input: cols_list - a list of the number of columns in each corresponding row
# input: compute_letter function to compute a letter as Callable[[int,int], str]
# result: List[List[int]] containing the computed pattern
def build_pattern(rows: int, cols_list: List[int],
                  compute_letter: Callable[[int, int], str]):
    pattern = []

    for r in range(rows):
        pattern_row = []
        for c in range(cols_list[r]):
            pattern_row.append(compute_letter(r, c))
        pattern.append(pattern_row)

    return pattern


# Compares the expected pattern with the computed pattern.
#
# input: desired_pattern as List[List[str]]
# input: computed_pattern as List[List[str]]
# result: None
#
# Special Notes:
#
#   If the computed patterns matches the expected pattern, this function
#   displays a 'success' message. Otherwise, this function displays the
#   computed pattern with all incorrect letters replaced with the lower-case
#   equivalent. Any non A-Z characters will show as a '?'.
#
#   When there are errors, the function displays a key to how to interpret any
#   lower-case letters or '?' characters.
def display_results(expected: List[List[str]], computed: List[List[str]]):
    if expected == computed:
        print(
            '\nWell done - your logic produced the specified pattern!\n')
    else:
        # Doesn't match :-(
        print('\nNot done yet - ',
              'your logic did not produce the specified pattern.\n')
        print(
            'Below you see the expected pattern on the left and the computed pattern')
        print(
            'on the right. Any \'?\' characters indicate that compute_letter returned')
        print(
            'an unexpected character. Any lower case letters indicate that')
        print(
            'compute_letter returned the upper-case equivalent but it did not match')
        print(
            'the specified pattern.\n')
        print(
            'Check the logic in the compute_letter function and run again.\n')

        widest = max(map(len, expected))
        out_string = '{0:' + str(widest) + '}'

        for row in range(len(expected)):
            # row of expected pattern
            print(out_string.format(''.join(expected[row])), end='')

            # separation
            print('   ', end='')

            # row of computed pattern
            for col, ch in enumerate(computed[row]):
                if not ch.isupper():
                    print('?', end='')
                elif expected[row][col] != ch:
                    print(computed[row][col].lower(), end='')
                else:
                    print(ch, end='')

            print()

        print()
