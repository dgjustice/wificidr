import pypureomapi
import sys
import struct
import argparse
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

keyname = "mykey"
secret = "NOTSECRET"
server = "127.0.0.1"
port = 7911

def loadyml(fname):
    return load(open(fname, 'r'), Loader=Loader)

def host_exists(oma, hwaddr):
    try:
        oma.lookup_ip_host(hwaddr)
    except pypureomapi.OmapiErrorNotFound:
        return False
    return True

def add_host_w_args(omapi, ip, hwaddr, host, state_list):
    msg = pypureomapi.OmapiMessage.open(b'host')
    msg.message.append(('create', struct.pack('!I', 1)))
    msg.message.append(('exclusive', struct.pack('!I', 1)))
    msg.obj.append(('hardware-address', pypureomapi.pack_mac(hwaddr)))
    msg.obj.append(("hardware-type", struct.pack("!I", 1)))
    msg.obj.append(('ip-address', pypureomapi.pack_ip(ip)))
    msg.obj.append(("name", host))
    statements = ""
    for s in state_list:
        statements += s
    statements += 'supersede host-name "%s";' % host
    msg.obj.append(('statements', statements))
    resp = omapi.query_server(msg)
    print(resp.message)

def main(fname):
    vars = loadyml(fname)
    try:
      oma = pypureomapi.Omapi(server, port, keyname, secret)
    except pypureomapi.OmapiError, err:
      print "OMAPI error: %s" % (err, )
      sys.exit(1)
    for hname, host in vars['HOSTS'].items():
        # Big hammer, will try more stateful tomorrow
        if host_exists(oma, host['HWADDR']):
            print("Blowing up %s" % hname)
            oma.del_host(host['HWADDR'])
        if host['STATUS'] == "present" and not host_exists(oma, host['HWADDR']):
            print("adding %s" % hname)
            statements = ""
            statements += 'filename "{0}"; '.format("nxos.cfg")
            statements += 'next-server = "{0}"; '.format("172.16.0.200")
            add_host_w_args(oma, host['INET'], host['HWADDR'], hname, statements)
            # oma.add_host_supersede_name(host['INET'], host['HWADDR'], hname)
        elif host['STATUS'] == "absent" and host_exists(oma, host['HWADDR']):
            print("deleting %s" % hname)
            oma.del_host(host['HWADDR'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update DHCP leases")
    parser.add_argument("fname", type=str, help="YAML file with lease info")

    cli_args = parser.parse_args()
    main(cli_args.fname)
