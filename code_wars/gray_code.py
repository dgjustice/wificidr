def bin2gray(bits):
    out_bits = []
    out_bits.append(bits[0])
    index = 1
    for bit in bits[:-1]:
        out_bits.append(bits[index]^bits[index - 1])
        index += 1
    return out_bits

def gray2bin(bits):
    out_bits = []
    out_bits.append(bits[0])
    index = 1
    for bit in bits[:-1]:
        out_bits.append(bits[index]^out_bits[index - 1])
        index += 1
    return out_bits
