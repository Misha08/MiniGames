from math import sqrt


def create_field(count_of_numbers: int):
    '''

    The function of constructing a visual playing field,
    creates it according to the following algorithm:

    1) An empty list is created, which will later be converted to a matrix
    2) Dimension parameter of the initial matrix, equal to the integer root of the number of numbers,
    and start and end pointers
    3) Start and end pointers
    4) Start of filling the field matrix with dimension (square_of_count x square_of_count),
    at each iteration, after filling the string with numbers from beginning to end,
    the beginning and end are increased on square_of_count
    5) The number of numbers and lines required to be added is calculated
    6) if there is no need to add a new line, then the last extra one is filled with missing numbers,
    the remaining elements of the line remain empty, otherwise, the necessary rows are added by forming them,
    filling them in and adding them to the matrix,
    start and end pointers are equal to the square of the integer root of 'square_of_count'
    and the sum of the numerical value of the start pointer with 'square_of_count', respectively,
    at the end, the missing line is added, which is not completely filled,
    but only up to the very end number
    7) At this stage, the elements are transformed by adding spaces to them,
    to bring them to a common scale in accordance with the size of the largest number
    the number of spaces from the beginning is equal
    to the difference between the length of the largest number and the element
    8) The field is output and its matrix is obtained

    '''

    # Numerical number of field elements
    count = count_of_numbers

    # Measuring parameter, for forming the scale of the field
    square_of_count = int(sqrt(count))

    # Creating the field itself as a matrix
    matrix_with_counts = [list() for _ in range(square_of_count)]

    # Start and end options
    begin = 0
    end = square_of_count

    # Filling in the field
    for row in range(square_of_count):
        matrix_with_counts[row] = [column + 1 for column in range(begin, end)]
        begin += square_of_count
        end += square_of_count

    # Calculation of the value of the remainder of the numbers and
    # the required number of rows in the matrix required to add
    rest = count - square_of_count ** 2
    count_add = rest // square_of_count

    # Checking necessity if Rows Are Added to a Matrix
    if count_add == 0:
        # Adding numbers to the last empty row in a matrix
        matrix_with_counts.append([number for number in range(count - square_of_count + 2, count + 1)])
    else:
        # Start and end options
        begin = square_of_count ** 2 + 1
        end = begin + square_of_count

        # Adding "full" rows to a matrix
        for _ in range(count_add):
            matrix_with_counts.append([row for row in range(begin, end)])

        # Adding an "incomplete" row to a matrix
        matrix_with_counts.append([k for k in range(matrix_with_counts[-1][-1] + 1, count + 1)])

    # "Decoration of Numbers"
    for row in range(len(matrix_with_counts)):
        for column in range(len(matrix_with_counts[row])):
            matrix_with_counts[row][column] = (len(str(count)) - len(str(matrix_with_counts[row][column])))\
                                       * " " + str(matrix_with_counts[row][column])

    # Output of the playing field
    print("/*---Your play field :)---*/")
    for i in matrix_with_counts:
        print(*i)

    return matrix_with_counts


def get_beautiful_field(max_number: int, field: list, set_of_guess_numbers: set, result_turn: set):
    '''

    This function returns the results of matching random result numbers
    and numbers received from the player and a field with filled in guessed numbers
    according to the following algorithm:

    1) Taking the value of the main generated field,
    the results of random generation and numbers from the player
    2) The results are calculated by forming a set from the combined sets
    of random generation and numbers from the player
    3) And an empty list to form a matrix with hidden numbers crossed out
    4) There is a replacement of numbers with spaces for scales
    and the formation of a matrix of "pure numbers"
    5) Matrix search, if a matched number was found, then it is replaced by "x"
    6) At this stage, the elements are transformed by adding spaces to them,
    to bring them to a common scale in accordance with the size of the largest number
    the number of spaces from the beginning is equal
    to the difference between the length of the largest number and the element
    7) Returns a completed field with strikethrough numbers and the result of matches

    '''

    # A copy of the field, for its further modification
    field_for_beauty = field

    # Copying sets of player numbers and generated RNGs
    sample_numbers = set(set_of_guess_numbers)
    matching_numbers = set(result_turn)

    # Set of matched numbers
    set_of_matched_numbers = sample_numbers.intersection(matching_numbers)
    beautiful_field = list()

    # Adding numbers without leading gaps to new field sets
    for row in field_for_beauty:
        beautiful_field.append([number.replace(" ", "") for number in row])

    # Adding numbers, in case of guessing a number, it is replaced by "x"
    for number_to_match in set_of_matched_numbers:
        for row in range(len(beautiful_field)):
            for column in range(len(beautiful_field[row])):
                if str(number_to_match) == beautiful_field[row][column]:
                    beautiful_field[row][column] = "x" * len(beautiful_field[row][column])

    # "Decoration of Numbers"
    for row in range(len(beautiful_field)):
        for column in range(len(beautiful_field[row])):
            beautiful_field[row][column] = (len(str(max_number)) - len(str(beautiful_field[row][column]))) * " "\
                                    + str(beautiful_field[row][column])

    # returning the results, and the field itself
    return beautiful_field, set_of_matched_numbers


# The function for get rows from the matrix of field
def get_field(field: list):
    for row in field:
        print(*row)
