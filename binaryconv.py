number = 42
binary_representation = bin(number)
print(f"Binary representation of {number}: {binary_representation}")

num_bits = number.bit_length() + 1
binary_with_sign = bin(number & ((1 << num_bits) - 1))[2:]
inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_with_sign)

inverted_number = int(inverted_bits, 2)
negative_representation = inverted_number + 1
negative_binary = bin(negative_representation)[2:].zfill(num_bits)

original_negative = -number
original_negative_binary = bin(original_negative & ((1 << num_bits) - 1))
print(f"Original negative number in binary: {original_negative_binary}")
print(f"Negative binary representation of {number}: {negative_binary}")