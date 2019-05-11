import time
start_time = time.time()


def largestPalindrome(digits):
	upper_limit = 0  # for 2-digit, Upper Limit is 99
	for i in range(1, digits+1):
		upper_limit = upper_limit*10
		upper_limit = upper_limit+9
	lower_limit = upper_limit//10 + 1  # Lower limit is 10
	max_product = 0  # maximum value of the product of two numbers is 0 initially
	# iterate from upper limit to lower limit in reverse order
	# n1 X n2 = product , i = n1
	for i in range(upper_limit, lower_limit-1, -1):
		# j=n2
		for j in range(i, lower_limit-1, -1):
			product = i*j
			if product < max_product:
				break
			# storing the product to check it palindrome or not
			number = product
			reverse = 0
			while number != 0:
				reverse = reverse * 10 + number % 10
				number = number//10

			if product == reverse and product > max_product:
				max_product = product
	return max_product


def main():
	digits = int(input("Enter the number of digits: "))
	result = largestPalindrome(digits)
	print(result)


if __name__ == "__main__":
	main()
