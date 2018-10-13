def square_of_sum(count):
    return (count * (count+1)/2)**2


def sum_of_squares(count):
    return (count * (count + 1) * (2*count + 1)) / 6


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
