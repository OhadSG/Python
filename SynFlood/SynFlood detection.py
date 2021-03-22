from scapy.all import *

LOG = 'SynFloodSample.pcap'
SAVE = 'IPs.txt'
SERVER_IP = '69.90.200.90'

SUS_LIST = []
SA = []
A = []

SYN = 0x02
ACK = 0x10


def clear(ip, seq, ack):
    exists = False  # true if there is an ACK response to the given SYN-ACk packet
    sus = False  # true if the ACK response's SEQ and ACK values don't match the given ones

    for packet in A:  # go over all the ack responses
        if packet[IP].src == ip:  # check if they are related to the given SYN-ACK packet
            exists = True
            A.remove(packet)
            if not (packet[TCP].seq == ack and packet[TCP].ack == seq + 1):  # check if the SEQ and ACK values match - this is similar to the SYN cookies solution
                sus = True
    return (not exists) or sus


def check():
    packet = SA.pop(0)  # get the packet
    ip = packet[IP].dst
    if ip != SERVER_IP:  # make sure this is a packet sent by the server
        if clear(ip, packet[TCP].seq, packet[TCP].ack):  # check if the packet is related to the SYN-FLOOD attack
            SUS_LIST.append(ip)  # add the ip of the attacker to the list


def main():
    file = rdpcap(LOG)  # open the log file
    for packet in file:  # go over each packet
        packet.show()
        if packet[TCP].flags & ACK:  # if the packet is ACK
            if packet[TCP].flags & SYN:  # if the packet is SYN-ACK
                SA.append(packet)
            else:  # if the packet is ACK
                A.append(packet)

    while len(SA) > 0:  # while there are still packets to check
        check()

    with open(SAVE, 'w') as file:
        for i in SUS_LIST:
            file.write(i + '\n')


if __name__ == '__main__':
    main()
