from scapy.all import *

DEFAULT_DNS = '198.41.0.4'
#DEFAULT_DNS = '8.8.8.8'
#DEFAULT_DNS = '192.33.4.12'

QUERY = 0
A = 1
NS = 2
PORT = 53
NORECURSE = 0
TIMEOUT = 10


def main():
    while (url := input()).upper() != 'EXIT':
        try:
            print(nslookup(url))
        except Exception as e:
            print(e)
            print("Didn't work?\nConsider removing the 'www' from the beginning of the domain or using another DNS")
            print("Or maybe just try again :P")


def nslookup(url, qtype=A, destination=DEFAULT_DNS):
    p = IP(dst=destination) / UDP(dport=PORT) / DNS(opcode=QUERY, rd=NORECURSE, qdcount=1) / DNSQR(qtype=qtype,
                                                                                                   qname=url)
    r = sr1(p, timeout=TIMEOUT)

    answer = r[DNS].an
    if answer is not None:
        if type(answer[0].rdata) is not bytes:
            return '\n'.join([answer[x].rdata for x in range(r[DNS].ancount)])
        else:
            return nslookup(answer[0].rdata.decode())

    is_a, ip = extract_ip(r)

    if is_a:
        return nslookup(url, A, ip)
    else:
        return nslookup(url=ip, qtype=NS)


def extract_ip(p):
    for x in range(p[DNS].arcount):
        i = p[DNS].ar[x]
        if i.type == A:
            return True, i.rdata
    return False, p[DNS].ns[0].rdata.decode()


if __name__ == "__main__":
    main()
