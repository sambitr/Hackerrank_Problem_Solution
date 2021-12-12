#converting tdecimal to binary
# this code is generalized for both positive and negetive decimal numbers to get their binary numbers

n = int(input("Enter the number:"))
i,ans = 0, 0

# getting the absolute value of the number entered to first get the binary one
abs_n = abs(n)
while( abs_n != 0):
    digit = abs_n & 1
    ans  = (digit * (10**i)) + ans
    abs_n = abs_n >> 1
    i+=1


if n > 0:
    print(ans)
else:
    # for negetive ones, the way forward is:
    # calculate the one's complement of the number
    # and add 1 to it, to get the result
    ans = ~ ans
    ans = ans + 1
    print(ans)
