


def find_error(bits):
    error_idx = 0
    for i in range(len(bin(len(bits) - 3))):
        xor = 0   
        for idx, val in enumerate(bits):
            if idx >> i & 1:
                xor = xor ^ val
        if xor:
            error_idx = error_idx + (2 ** i)

    return error_idx



 
'''
def elements_with_bit_set(lst, bit_position):
    return [elem for elem in lst if (elem >> bit_position) & 1]

# Example list
my_list = [5, 3, 9, 6, 10, 12]

# Bit position (e.g., the 2nd bit from the right)
bit_position = 1

result = elements_with_bit_set(my_list, bit_position)

print(f"Elements in the list with '1' at bit position {bit_position}: {result}")'''


message = '10101111001000110100100110000101111000000100000011101000111100000110010101101110001000000110100101110101011101000110111001010110100101111011110010110110000101110011101000010111100101111001110100111001101110000011101000111010001101000'

bits = [int(i) for i in message]

print(bits)
print(len(bits))
print(len(bin(len(bits))))

error_idx = find_error(bits)
print(error_idx)

bits_fix = bits
bits_fix[error_idx] = 1 - bits_fix[error_idx] 

print(bits_fix)
print(find_error(bits_fix))

new_bits = [val for idx, val in enumerate(bits_fix) if not (idx & (idx - 1) == 0)]

print(new_bits)

new_bits = [str(i) for i in new_bits]

new_message = ''

print(new_bits)
print(len(new_bits))

for idx, val in enumerate(new_bits[::8]):

    print(new_bits[idx * 8 : idx * 8 + 8])
    print(chr(int(''.join(new_bits[idx * 8 : idx * 8 + 8]), 2)))

    new_message = new_message + chr(int(''.join(new_bits[idx * 8 : idx * 8 + 8]), 2))

print(new_message)

def text_from_bits(bits, encoding='ascii'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "little").decode(encoding) or "\0"

new_str_bits = ''.join(new_bits)

print(text_from_bits(new_str_bits))