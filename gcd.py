def gcd(a, b):
	if a == 0:
		return b

	return gcd(b % a, a)

# Driver code
if __name__ == "__main__":
    a = int(input())
    b = int(input())
print("gcd(", a, ",", b, ") = ", gcd(a, b))
