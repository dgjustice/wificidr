import asyncio
import socket
from time import time
import struct
import logging
import shlex
import subprocess
import re

async def icmp_recv(expected=3):
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Listen for ICMP packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.bind(('', 1))

    for i in range(expected):
        # Wait for data
        data = await loop.sock_recv(sock, 1024)

        # ip header is the first 20 bytes
        ip_header = data[:20]

        type_ = struct.unpack("!B", data[20:21])[0]
        code = struct.unpack("!B", data[21:22])[0]
        checksum = data[22:24]
        nh_mtu = None
        # TODO: Check if type 3, 11 MUST be 56 bytes
        if type_ == 3:
            nh_mtu = struct.unpack("!H", data[26:28])[0]
            logging.error(f"Next-hop MTU: {nh_mtu}")
        if type_ == 11:
            icmp_ip_recv_header = data[28:48]
            icmp_udp_src_port = data[48:50]
            icmp_udp_dst_port = data[50:52]
            icmp_udp_len = struct.unpack("!H", data[52:54])[0]
            icmp_udp_checksum = data[54:56]
            icmp_udp_data_len = icmp_udp_len - 8
            # icmp_recv_data = struct.unpack("!Q", data[48:56])[0]
            icmp_udp_data = data[56:56 + icmp_udp_data_len]
            logging.error(f"ICMP payload: {icmp_udp_data}")
        ip_src = socket.inet_ntop(socket.AF_INET, ip_header[12:16])
        logging.error(f"Reply from: {ip_src}, ICMP type: {type_}")

def sendto(sock, data, addr, ttl, fut=None, registed=False):
    loop = asyncio.get_running_loop()
    fd = sock.fileno()
    if fut is None:
        fut = loop.create_future()
    if registed:
        loop.remove_writer(fd)
    if not data:
        return
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)

    try:
        n = sock.sendto(data, addr)
        logging.error(f"Sent {n} bytes with TTL {ttl}.")
    except (BlockingIOError, InterruptedError):
        loop.add_writer(fd, sendto, loop, sock, data, addr, fut, True)
    else:
        fut.set_result(n)
    return fut

def udp_server(sock):
    pass
    # max_ttl = sock.getsockopt(socket.IPPROTO_IP, socket.IP_TTL)
    # data = b"f" * 50
    # addr = ("neteng.wal-mart.com", 22)
    # for ttl in range(1, max_ttl + 1):
    #     n_bytes = await sendto(loop, sock, data, addr, ttl)


async def main():
    # Wait for at most 1 second
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    for i in range(1, 4):
        await sendto(sock, b"Hello World", ("192.168.100.1", 22), i)
    try:
        await asyncio.wait_for(icmp_recv(), timeout=3.0)
    except asyncio.TimeoutError:
        print('timeout!')

def get_mtu():
    """OSX, and let's dangerously assume everything.
    
    Routing tables

    Internet:
    Destination        Gateway            Flags        Refs      Use    Mtu   Netif Expire
    default            192.168.1.1        UGSc           58        0   1500     en0
    127                127.0.0.1          UCS             0        0  16384     lo0"""
    cmd = "netstat -nlrf inet"
    args = shlex.split(cmd)
    with subprocess.Popen(args, stdout=subprocess.PIPE) as p:
        data = p.stdout.read()
    match = re.findall(r"^default.*", (data.decode("utf-8")), re.MULTILINE)
    mtu = match[0].split()[5]
    return mtu

if __name__ == "__main__":
    get_mtu()
    # asyncio.run(main())
