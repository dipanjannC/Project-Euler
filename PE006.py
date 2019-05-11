def sum_of_squares_first_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i*i
    return sum


def square_of_sum_first_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum*sum


def sum_square_difference(n):
    sum_of_squares = (n*(n+1)*(2*n+1))/6
    sum_of_n_numbers = (n*(n+1))/2
    square_of_sum = sum_of_n_numbers**2
    difference = square_of_sum - sum_of_squares
    return difference


def main():
    n = int(input("Enter value of n: "))
    print('Brute Force Method :')
    print(square_of_sum_first_n_numbers(n)-sum_of_squares_first_n_numbers(n))
    print('Faster Algorithm: ')
    print(sum_square_difference(n))


if __name__ == "__main__":
    main()