from pcapfile import savefile
import gzip

subject_ip = '159.237.13.37'
mix_ip = '94.147.150.188'
nbr_of_partners = int(input("Input the number of partners: "))


def read_pcap():
    testcap = open(r'cia.log.1337.pcap', 'rb')
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
    testcap = gzip.open(r'cia.log.1339.pcap.gz', 'rb')
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



def find_partners(packet_list):
    outgoing_sets = []
    collect_out_set = False
    i = 0
    size = len(packet_list) - 1
    disjoint_sets = []
    # Finding all sets when subject sent message
    while i < size:
        while packet_list[i]['ip_src'] != mix_ip:
            if packet_list[i]['ip_src'] == subject_ip:
                collect_out_set = True
            i += 1
        if collect_out_set:
            outgoing_sets.append([])
        while packet_list[i]['ip_src'] == mix_ip and i < size:
            if collect_out_set:
                outgoing_sets[-1].append(packet_list[i]['ip_dst'])
            i += 1
        if len(outgoing_sets) > 0:
            outgoing_sets[-1] = set(outgoing_sets[-1])

        # Checking if the last set is a disjoint set
        if len(disjoint_sets) != nbr_of_partners and len(outgoing_sets) > 0 and collect_out_set:
            disjoint = True
            j = 0
            while j < len(outgoing_sets) - 1 and disjoint:
                # print(outgoing_sets[j] in outgoing_sets[-1]
                #      or outgoing_sets[j] == outgoing_sets[-1])
                if outgoing_sets[j] in outgoing_sets[-1] or outgoing_sets[j] == outgoing_sets[-1]:
                    disjoint = False
                j += 1
            if disjoint:
                #print(outgoing_sets[-1])
                disjoint_sets.append(outgoing_sets[-1])
            # print('------------')
        # When m disjoint sets are found, start reducing
        elif len(disjoint_sets) == nbr_of_partners:
            for item in disjoint_sets:
                # print(item)
                # print(outgoing_sets[-1])
                new_set = item & outgoing_sets[-1]
                # print(new_set)
                if len(new_set) == 1:
                    item.clear()
                    item.update(new_set)

        collect_out_set = False

    if len(disjoint_sets) == nbr_of_partners and all(len(item) == 1 for item in disjoint_sets):
        return disjoint_sets

    # print(disjoint_sets)
    #return disjoint_sets


packet_list = read_pcap()
partners = find_partners(packet_list)
str_partners = [partner.pop() for partner in partners]

ip_sum = 0
for partner in str_partners:
    string_partner = str(partner).split(".")
    # Code from https://stackoverflow.com/questions/20948393/convert-a-ip-to-hex-by-python
    hex = "{:02X}{:02X}{:02X}{:02X}".format(*map(int, string_partner))
    result = int(hex, 16)
    ip_sum += result
print(ip_sum)
# Svaret ska vara: 6100595791
