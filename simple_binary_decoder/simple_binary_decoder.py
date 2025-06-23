# binary list for input
binary = [1,0,0,1,1,0,0,1] 
# checking the length of input(important for loop and decoding)
binary_len = len(binary)
# list of numbers 
decode = [] 
# use it for check but it did not work properly i chose different 
# approach
check = [0,1] 
# loop where im checking if input is valid, that the input includes only 1 and 0
for num in binary:
    if num != 0 and num != 1:
        print("Invalid input")
# here im making equivalent of binary number
for num in range(0,binary_len):
    n = 2 ** num
    decode.append(n)
# need revers binary is red from right to left
binary.reverse()
# This one is a bit complicated:
# Here I'm comparing two lists — one is binary, one is decode (which holds powers of 2)
# They have the same length and same order.
# So, if a binary bit is 1, it will pass its decimal value from decode.
# Then all those values are added together to get the final result.
result = sum([n for b,n in zip(binary,decode) if b == 1])
print(result)