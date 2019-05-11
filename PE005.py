# def min(x, y):
#     min = x if x < y else y
#     return min


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

#
# Function to return LCM of two numbers
# def lcm(a,b):
#     return (a*b) / gcd(a,b)


# least common factor / least number divisible by first n numbers
def lcm_1(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i)/gcd(result, i)
    return result


#  as , a x b = gcd(a,b) X lcm(a,b)
def lcm_2(x, y):
    result = x  # initializing result to lower limit
    for i in range(x, y+1):  # looping from lower limit -> upper limit
        result = (result * i)/gcd(result, i)
    return result


def main():
    print("1.Find the least number divisible by first n numbers ")
    print("2. least number divisible from any start and end points")
    option = int(input("Enter Option: "))
    if option == 1:
        n = int(input("Enter First n numbers: "))
        print(lcm_1(n))
    elif option == 2:
        x = int(input("Enter lower limit: "))
        y = int(input("Enter upper limit: "))
        print(lcm_2(x, y))


if __name__ == "__main__":
    main()
