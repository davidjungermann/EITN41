from pcapfile import savefile
import gzip


def main():
    subject_ip = input("Input the subjects IP: ")
    mix_ip = input('Input the IP of the mix: ')
    nbr_of_partners = int(input("Input the number of partners: "))
    packet_list = zipped_read_pcap()
    partners = find_partners(packet_list, mix_ip, subject_ip, nbr_of_partners)

    str_partners = [partner.pop() for partner in partners]

    ip_sum = 0
    for partner in str_partners:
        string_partner = str(partner).split(".")
        # Code from https://stackoverflow.com/questions/20948393/convert-a-ip-to-hex-by-python
        hex = "{:02X}{:02X}{:02X}{:02X}".format(*map(int, string_partner))
        result = int(hex, 16)
        ip_sum += result
    print(ip_sum)


def read_pcap():
    testcap = open(
        r'cia.log.1337.pcap', 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    # print the packets
    print('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
    packet_list = []
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        # all data is ASCII encoded (byte arrays). If we want to compare with strings
        # we need to decode the byte arrays into UTF8 coded strings
        packet_list.append({'ip_src': pkt.packet.payload.src.decode('UTF8'),
                            'ip_dst': pkt.packet.payload.dst.decode('UTF8')})
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        print('{}\t\t{}\t{}\t{}\t{}'.format(
            timestamp, eth_src, eth_dst, ip_src, ip_dst))
    return(packet_list)


def zipped_read_pcap():
    testcap = gzip.open(
        r'cia.log.5.pcap.gz', 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    # print the packets
    print('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
    packet_list = []
    for pkt in capfile.packets:
        packet_list.append({'ip_src': pkt.packet.payload.src.decode('UTF8'),
                            'ip_dst': pkt.packet.payload.dst.decode('UTF8')})
    return(packet_list)


def find_partners(packet_list, mix_ip, subject_ip, nbr_of_partners):
    sub_sent_msg = False
    i = 0
    size = len(packet_list) - 1
    disjoint_sets = []

    while i < size:
        # Finding if subject sent a message when subject sent message
        while packet_list[i]['ip_src'] != mix_ip:
            if packet_list[i]['ip_src'] == subject_ip:
                sub_sent_msg = True
            i += 1
        # Adding item to new set if subject sent a message
        if sub_sent_msg:
            outgoing_set = set()
        while packet_list[i]['ip_src'] == mix_ip and i < size:
            if sub_sent_msg:
                outgoing_set.add(packet_list[i]['ip_dst'])
            i += 1

        # Checking if the last set is a disjoint set
        if len(disjoint_sets) != nbr_of_partners and sub_sent_msg:
            disjoint = True
            j = 0
            while j < len(disjoint_sets) and disjoint:

                if len(disjoint_sets[j].intersection(outgoing_set)) != 0 or disjoint_sets[j] == outgoing_set:
                    disjoint = False
                j += 1
            if disjoint:
                disjoint_sets.append(outgoing_set)
        # When m disjoint sets are found, start reducing by intersection
        elif len(disjoint_sets) == nbr_of_partners:
            new_sets = []
            count = 0
            for item in disjoint_sets:
                if(len(item.intersection(outgoing_set)) != 0):
                    count += 1
            if(count == 1):
                for item in disjoint_sets:
                    new_set = item.intersection(outgoing_set)
                    if len(new_set) != 0:
                        item.clear()
                        item.update(new_set)
        sub_sent_msg = False
    # If sets are equal to one, return
    if len(disjoint_sets) == nbr_of_partners and all(len(item) == 1 for item in disjoint_sets):
        return disjoint_sets
    return disjoint_sets


main()
