'''Arnab has given me a challenge. I have to calculate the number of numbers which are less than a certain value n, 
and have exactly k set bits in its binary form. As you are a Prepster like me, help me write a code that will take input for n 
and k and give the expected output.'''


def count_numbers_with_k_bits(n, k):
    def count_set_bits(num):
        count = 0 
        while num:
            count += num & 1
            num >>= 1
        return count
    result = 0
    for num in range(n):
        if count_set_bits(num)==k:
            result += 1 
    return result

n, k = map(int, input("Enter value of n and k: ").split())

output = count_numbers_with_k_bits(n, k)
print(output)