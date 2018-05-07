## Synopsis

Python module that allocates IPv6 networks per the techniques listed in RFC3531
<https://tools.ietf.org/html/rfc3531>

## Requires
Python3 since it uses the ipaddress module
It should work with the netaddr module in Python2, but I'll have to backport all the
str to unicode.

## Code Example
```
>>> from ipv6gen import IPv6Gen
>>>
>>> # The first argument is the block, second argument is the new prefix length
... sp = IPv6Gen("2000:beef:face::/48", 52)
>>>
>>> for i in sp.left():
...     print(i)
...
2000:beef:face::/52
2000:beef:face:8000::/52
2000:beef:face:4000::/52
2000:beef:face:c000::/52
2000:beef:face:2000::/52
2000:beef:face:a000::/52
2000:beef:face:6000::/52
2000:beef:face:e000::/52
2000:beef:face:1000::/52
2000:beef:face:9000::/52
2000:beef:face:5000::/52
2000:beef:face:d000::/52
2000:beef:face:3000::/52
2000:beef:face:b000::/52
2000:beef:face:7000::/52
2000:beef:face:f000::/52
>>>
```

## Tests

Tests are straightforward.

```
python sparse_test.py
```
