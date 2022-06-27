import ipaddress


def int32_to_ip(int32):
    """Returns a string representation of a number as an IPv4 address"""
    return str(ipaddress.IPv4Address(int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(2) == "0.0.0.2"
