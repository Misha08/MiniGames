from math import sqrt


def create_field(count_of_numbers: int):

    count = count_of_numbers
    square_of_count = int(sqrt(count))
    tech_arr = [i for i in range(1, count + 1)]
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
        c1 = square_of_count ** 2 + 1
        c2 = c1 + square_of_count
        for i in range(count_add):
            matrix_with_counts.append([j for j in range(c1, c2)])

        matrix_with_counts.append([k for k in range(matrix_with_counts[-1][-1] + 1, count + 1)])

    for i in range(len(matrix_with_counts)):
        for j in range(len(matrix_with_counts[i])):
            matrix_with_counts[i][j] = (len(str(count)) - len(str(matrix_with_counts[i][j])))\
                                       * " " + str(matrix_with_counts[i][j])

    print("/*---Your play field :)---*/")
    for i in matrix_with_counts:
        print(*i)

    return tech_arr, matrix_with_counts
