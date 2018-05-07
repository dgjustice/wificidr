from ipaddress import ip_address, ip_network
from math import ceil, floor, log

class IPv6Gen:
    """Sparse provides methods to allocat IPv6 networks per RFC3531"""

    def __init__(self, subnet, new_prefix):
        """
        Keyword arguments:
        new_prefix -- The new (longer) prefix desired from the parent block
        subnet -- The parent block to be allocated from

        The generator returned from each method is an IPv6Network class
        """
        self.new_prefix = new_prefix
        self.subnet = ip_network(subnet)
        diff = self.new_prefix - self.subnet.prefixlen
        if diff <= 0:
            raise ValueError
    
    def right(self):
        """Allocates networks starting with right-hand bits (regular binary counting)"""
        # Trivial, just passing along the ip_network generator
        return self.subnet.subnets(new_prefix=self.new_prefix)


    def left(self):
        """Allocates networks starting with left-hand bits (inverse binary counting)"""
        base = int(self.subnet.network_address)
        diff = self.new_prefix - self.subnet.prefixlen
        # iterate through the range
        for i in range(0, pow(2, diff)):
            # reverse bits, pad and return
            rev_bits = (bin(i)[2::][::-1] + '0' * (128 - self.subnet.prefixlen - i.bit_length()))
            # add rev_bits to base address, slap on the prefix, and return
            yield ip_network(str(ip_address(base + int(rev_bits, 2))) + "/" + str(self.new_prefix))

    def center(self):
        """Allocates networks starting with center bits"""
        base = int(self.subnet.network_address)
        diff = self.new_prefix - self.subnet.prefixlen
        mid_bit = diff >> 1 
        # print("mid_bit", mid_bit)

        # Fill the array of bit positions in the correct order per the center algorithm
        # described in RFC3531.  This section does steps 1 and 3 at once.  Sort of.
        sel_bits = [mid_bit]
        for i in range(2, diff):
            # odd
            if i & 1 != 0:
                # print("odd", i, "mod", (i >> 1) + (i % 2) - 1)
                cur_bit = mid_bit + (i >> 1) + (i % 2) - 1
                sel_bits.append(cur_bit)
            # even
            else:
                # print("even", i, "shift", mid_bit - (i >> 1))
                cur_bit = mid_bit - (i >> 1)
                sel_bits.append(cur_bit)
        sel_bits.append(0)

        yield ip_network(str(ip_address(base)) + "/" + str(self.new_prefix))
        # Per step 2 of the algorithm
        # These bits are left-padded, but it makes t-shooting much easier to read
        combos = []
        for i in range(0, len(sel_bits)):
            cur_bit = sel_bits[i]
            # print("cur", cur_bit)
            base_str = list("".zfill(diff))
            if i == 0:
                combos.append(base_str)
            for c in range(0, len(combos)):
                out_str = list(combos[c])
                out_str[cur_bit] = "1"
                out = "".join(out_str)
                # print(out)
                combos.append(out)
                offset = base + (int(out, 2) << (128 - self.subnet.prefixlen - diff))
                yield ip_network(str(ip_address(offset)) + "/" + str(self.new_prefix))
