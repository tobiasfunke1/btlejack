"""
Helpers.
"""


def bytes_to_bd_addr(bd_addr):
    """
    Convert 6-byte values to BD address
    """
    return ':'.join(['%02x' % c for c in bd_addr[::-1]])


def bd_address_to_int(bd_address):
    """
    Helper function converting a BD address to the corresponding integer value.
    """
    addr_bytes = [int(v, 16) for v in bd_address.lower().split(':')]
    if len(addr_bytes) != 6:
        return None
    else:
        addr_value = addr_bytes[0] << (8 * 5)
        addr_value |= addr_bytes[1] << (8 * 4)
        addr_value |= addr_bytes[2] << (8 * 3)
        addr_value |= addr_bytes[3] << (8 * 2)
        addr_value |= addr_bytes[4] << (8 * 1)
        addr_value |= addr_bytes[5] << (8 * 0)
        return addr_value
