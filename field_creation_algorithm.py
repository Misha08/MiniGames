from math import sqrt


def create_field(count_of_numbers: int):

    count = count_of_numbers
    square_of_count = int(sqrt(count))
    matrix_with_counts = [list() for _ in range(square_of_count)]
    begin = 0
    end = square_of_count

    for i in range(square_of_count):
        matrix_with_counts[i] = [j + 1 for j in range(begin, end)]
        begin += square_of_count
        end += square_of_count

    rest = count - square_of_count ** 2
    count_add = rest // square_of_count

    if count_add == 0:
        matrix_with_counts.append([i for i in range(count - square_of_count + 2, count + 1)])
    else:
        begin = square_of_count ** 2 + 1
        end = begin + square_of_count
        for i in range(count_add):
            matrix_with_counts.append([j for j in range(begin, end)])

        matrix_with_counts.append([k for k in range(matrix_with_counts[-1][-1] + 1, count + 1)])

    for i in range(len(matrix_with_counts)):
        for j in range(len(matrix_with_counts[i])):
            matrix_with_counts[i][j] = (len(str(count)) - len(str(matrix_with_counts[i][j])))\
                                       * " " + str(matrix_with_counts[i][j])

    print("/*---Your play field :)---*/")
    for i in matrix_with_counts:
        print(*i)

    return matrix_with_counts


def get_beautiful_field(max_number, field, set_of_guess_numbers, result_turn):
    field_for_beauty = field
    sample_numbers = set(set_of_guess_numbers)
    matching_numbers = set(result_turn)
    set_of_matched_numbers = sample_numbers.intersection(matching_numbers)
    beautiful_field = list()

    for i in field_for_beauty:
        beautiful_field.append([j.replace(" ", "") for j in i])

    for k in set_of_matched_numbers:
        for i in range(len(beautiful_field)):
            for j in range(len(beautiful_field[i])):
                if str(k) == beautiful_field[i][j]:
                    beautiful_field[i][j] = "x" * len(beautiful_field[i][j])

    for i in range(len(beautiful_field)):
        for j in range(len(beautiful_field[i])):
            beautiful_field[i][j] = (len(str(max_number)) - len(str(beautiful_field[i][j]))) * " "\
                                    + str(beautiful_field[i][j])

    return beautiful_field, set_of_matched_numbers


def get_field(field):
    for row in field:
        print(*row)